# Production-optimized Django/Wagtail Dockerfile for Dokploy
FROM python:3.12-slim AS base

# Labels for Dokploy
LABEL org.opencontainers.image.title="KNI Webapp"
LABEL org.opencontainers.image.description="Django/Wagtail CMS application"
LABEL org.opencontainers.image.vendor="KNI"
LABEL dokploy.port="8000"
LABEL dokploy.healthcheck="/health/ready/"

# Set production environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    UV_LINK_MODE=copy \
    DJANGO_SETTINGS_MODULE=project.settings \
    PYTHONPATH=/app

# Install system dependencies and security updates
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install UV package manager
RUN pip install --no-cache-dir uv

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Set work directory
WORKDIR /app

# ==============================================================================
# Node.js stage for CSS building
# ==============================================================================
FROM node:18-alpine AS node-builder

WORKDIR /app

# Copy package files and install dependencies
COPY src/frontend/package.json src/frontend/package-lock.json ./
RUN npm install

# Copy source files for CSS building
COPY src/frontend/tailwind.config.js src/frontend/postcss.config.js ./
COPY src/frontend/templates/ ./templates/
COPY src/backend/apps/ ./apps/
COPY src/frontend/static/css/input.css ./static/css/input.css

# Build CSS
RUN npm run build-css-prod

# Copy node_modules for JavaScript libraries
RUN cp -r node_modules ./static/ && ls -la ./static/node_modules/

# ==============================================================================
# Builder stage - install Python dependencies
# ==============================================================================
FROM base AS builder

# Install Python dependencies using UV
COPY requirements.txt .
RUN uv venv /opt/venv && \
    uv pip install --python /opt/venv/bin/python --no-cache -r requirements.txt

# ==============================================================================
# Production stage - runtime environment
# ==============================================================================
FROM base AS production

# ARG declarations for build-time environment variables (optional migrations)
ARG RUN_MIGRATIONS=false
ARG DATABASE_URL=""
# ARG DJANGO_SECRET_KEY=""  # Removed for security - use environment variables instead
ARG DJANGO_SETTINGS_MODULE="project.settings"

# Copy Python dependencies from builder (UV virtual environment)
COPY --from=builder /opt/venv /opt/venv

# Copy built CSS from node builder
COPY --from=node-builder /app/static/css/site.css /app/static/css/site.css

# Make sure UV virtual environment is usable
ENV PATH=/opt/venv/bin:$PATH

# Copy project files (excluding source CSS files that would overwrite built CSS)
COPY --chown=app:app src/backend/ ./
COPY --chown=app:app manage.py ./
COPY --chown=app:app requirements.txt ./
RUN rm -f /app/static/css/input.css

# JavaScript libraries are loaded via CDN in templates

# Create empty baseline data directory (files can be added later via management commands)
RUN mkdir -p /app/baseline_data && chown app:app /app/baseline_data

# Ensure .config directory is properly copied and has correct permissions
COPY --chown=app:app .config/ /app/.config/

# Copy entrypoint script
COPY --chown=app:app deployment/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories for static/media/logs/backups files and ensure proper permissions
RUN mkdir -p /app/staticfiles /app/media /app/logs /app/backups /app/frontend_static && \
    chown -R app:app /app/staticfiles /app/media /app/logs /app/backups /app/frontend_static && \
    chmod -R 755 /app/logs /app/backups /app/frontend_static

# Switch to non-root user
USER app

# Static files will be collected at runtime in entrypoint

# Optional build-time migrations (with caution)
# Only run if RUN_MIGRATIONS=true and database is accessible
# Note: DJANGO_SECRET_KEY must be provided via environment at runtime, not build-time
RUN if [ "$RUN_MIGRATIONS" = "true" ] && [ -n "$DATABASE_URL" ]; then \
        echo "Build-time migrations enabled, checking database connectivity..."; \
        export DJANGO_SETTINGS_MODULE="$DJANGO_SETTINGS_MODULE"; \
        export DATABASE_URL="$DATABASE_URL"; \
        python -c "import os,sys,psycopg2; from urllib.parse import urlparse; db_url=os.environ.get('DATABASE_URL',''); sys.exit(0) if not db_url else None; parsed=urlparse(db_url); conn=psycopg2.connect(host=parsed.hostname,port=parsed.port or 5432,user=parsed.username,password=parsed.password,database=parsed.path.lstrip('/'),connect_timeout=10); conn.close(); print('Database connectivity verified')" && \
        echo "Running migrations at build time..." && \
        python manage.py migrate --noinput && \
        echo "Build-time migrations completed successfully"; \
    else \
        echo "Build-time migrations disabled or missing required variables"; \
        echo "RUN_MIGRATIONS=$RUN_MIGRATIONS"; \
        echo "DATABASE_URL is $([ -n \"$DATABASE_URL\" ] && echo 'set' || echo 'not set')"; \
        echo "Note: DJANGO_SECRET_KEY should be provided at runtime for security"; \
    fi

# Health check for Dokploy compatibility
# Health check disabled for Dokploy compatibility - Dokploy/Traefik handles health monitoring
# HEALTHCHECK --interval=30s --timeout=10s --start-period=90s --retries=3 \
#     CMD curl -f http://localhost:8000/health/ready/ || exit 1

# Expose port 8000 (standard Django/Gunicorn port)
EXPOSE 8000

# Use entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Production Gunicorn command optimized for Dokploy
CMD ["bash", "-c", "\
    echo 'Starting production Django application...' && \
    python manage.py collectstatic --noinput --clear && \
    python manage.py migrate --noinput && \
    echo 'Starting Gunicorn server...' && \
    gunicorn \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --worker-class gthread \
        --threads 2 \
        --timeout 120 \
        --max-requests 1000 \
        --max-requests-jitter 100 \
        --preload \
        --access-logfile - \
        --error-logfile - \
        project.wsgi:application"]

# ==============================================================================
# Development stage - extends production with development tools
# ==============================================================================
FROM production AS development

# Switch back to root for package installation
USER root

# Install additional development packages
RUN apt-get update && apt-get install -y \
    git \
    vim \
    htop \
    jq \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install development-specific Python packages using UV
RUN uv pip install --no-cache \
    ipdb \
    django-debug-toolbar \
    django-extensions \
    watchdog

# Switch back to app user
USER app

# Override ENTRYPOINT and CMD for development - use Django runserver directly
ENTRYPOINT []
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]