# Multi-stage Dockerfile for Django/Wagtail with PostgreSQL
FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Set work directory
WORKDIR /app

# ==============================================================================
# Frontend builder stage - use Node.js with Tailwind CSS v4
# ==============================================================================
FROM node:18-alpine as frontend-builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Verify package.json exists and ensure fresh timestamps
RUN ls -la package*.json && touch package.json package-lock.json

# Install dependencies
RUN npm install

# Copy source files
RUN mkdir -p ./static/css/
COPY src/ ./src/
COPY tailwind.config.js ./
COPY postcss.config.js ./
COPY templates/ ./templates/
COPY apps/ ./apps/

# Build CSS using npm script
RUN npm run build-css-prod

# ==============================================================================
# Builder stage - install Python dependencies
# ==============================================================================
FROM base as builder

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# ==============================================================================
# Production stage - runtime environment
# ==============================================================================
FROM base as production

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/app/.local

# Copy built CSS from frontend builder
COPY --from=frontend-builder /app/static/css/site.css /app/static/css/site.css

# Make sure scripts in .local are usable
ENV PATH=/home/app/.local/bin:$PATH

# Copy project files (excluding source CSS files that would overwrite built CSS)
COPY --chown=app:app . .
RUN rm -f /app/static/css/input.css

# Copy entrypoint script
COPY --chown=app:app docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories for static/media/logs files
RUN mkdir -p /app/staticfiles /app/media /app/logs && \
    chown -R app:app /app/staticfiles /app/media /app/logs

# Switch to non-root user
USER app

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Health check - use more appropriate readiness endpoint
HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health/ready/ || exit 1

# Expose port
EXPOSE 8000

# Use entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Default command with optimized Gunicorn settings
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-2} --timeout ${GUNICORN_TIMEOUT:-60} --max-requests ${GUNICORN_MAX_REQUESTS:-1000} --max-requests-jitter ${GUNICORN_MAX_REQUESTS_JITTER:-100} --worker-class ${GUNICORN_WORKER_CLASS:-sync} --keep-alive ${GUNICORN_KEEP_ALIVE:-5} --access-logfile - --error-logfile - --access-logformat '%(h)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\" %(D)s' project.wsgi:application"]