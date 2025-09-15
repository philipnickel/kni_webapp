# Multi-stage Dockerfile for Django/Wagtail with PostgreSQL
FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    UV_LINK_MODE=copy

# Install system dependencies including supervisor and caddy
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    postgresql-client \
    supervisor \
    debian-keyring \
    debian-archive-keyring \
    apt-transport-https \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update \
    && apt-get install -y caddy \
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
FROM node:18-alpine as node-builder

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy source files for CSS building
COPY tailwind.config.js postcss.config.js ./
COPY templates/ ./templates/
COPY apps/ ./apps/
COPY static/css/input.css ./static/css/input.css

# Build CSS
RUN npm run build-css-prod

# Copy node_modules for JavaScript libraries
RUN cp -r node_modules ./static/ && ls -la ./static/node_modules/

# ==============================================================================
# Builder stage - install Python dependencies
# ==============================================================================
FROM base as builder

# Install Python dependencies using UV
COPY requirements.txt .
RUN uv venv /opt/venv && \
    uv pip install --python /opt/venv/bin/python --no-cache -r requirements.txt

# ==============================================================================
# Production stage - runtime environment
# ==============================================================================
FROM base as production

# ARG declarations for build-time environment variables (optional migrations)
ARG RUN_MIGRATIONS=false
ARG DATABASE_URL=""
ARG DJANGO_SECRET_KEY=""
ARG DJANGO_SETTINGS_MODULE="project.settings"

# Copy Python dependencies from builder (UV virtual environment)
COPY --from=builder /opt/venv /opt/venv

# Copy built CSS from node builder
COPY --from=node-builder /app/static/css/site.css /app/static/css/site.css

# Make sure UV virtual environment is usable
ENV PATH=/opt/venv/bin:$PATH

# Copy project files (excluding source CSS files that would overwrite built CSS)
COPY --chown=app:app . .
RUN rm -f /app/static/css/input.css

# JavaScript libraries are loaded via CDN in templates

# Ensure backup files are available
COPY --chown=app:app backups/ /app/backups/

# Ensure .config directory is properly copied and has correct permissions
COPY --chown=app:app .config/ /app/.config/

# Copy entrypoint script
COPY --chown=app:app docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories for static/media/logs files and ensure baseline data permissions
RUN mkdir -p /app/staticfiles /app/media /app/logs && \
    chown -R app:app /app/staticfiles /app/media /app/logs
    # baselineData no longer used - Django-native backups in /app/backups

# Switch to non-root user
USER app

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Optional build-time migrations (with caution)
# Only run if RUN_MIGRATIONS=true and database is accessible
RUN if [ "$RUN_MIGRATIONS" = "true" ] && [ -n "$DATABASE_URL" ] && [ -n "$DJANGO_SECRET_KEY" ]; then \
        echo "Build-time migrations enabled, checking database connectivity..."; \
        export DJANGO_SECRET_KEY="$DJANGO_SECRET_KEY"; \
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
        echo "DJANGO_SECRET_KEY is $([ -n \"$DJANGO_SECRET_KEY\" ] && echo 'set' || echo 'not set')"; \
    fi

# Health check - now using Caddy on port 80
HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:80/health/ready/ || exit 1

# Expose port 80 instead of 8000 (Caddy will serve everything)
EXPOSE 80

# Use entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Default command using supervisor to manage Caddy and Gunicorn
CMD ["/usr/bin/supervisord", "-c", "/app/.config/supervisord.conf", "-n"]

# ==============================================================================
# Development stage - extends production with development tools
# ==============================================================================
FROM production as development

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

# Development health check (less strict) - still use port 8000 for dev server
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Development command with Django's development server (can be overridden)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]