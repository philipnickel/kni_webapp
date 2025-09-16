# Multi-stage Dockerfile for Django/Wagtail with PostgreSQL
FROM python:3.12-slim AS base

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

# Ensure Python can find the project module
ENV PYTHONPATH=/app

# JavaScript libraries are loaded via CDN in templates

# Ensure backup files are available
# Backup files will be created at runtime

# Ensure .config directory is properly copied and has correct permissions
COPY --chown=app:app .config/ /app/.config/

# Copy entrypoint script
COPY --chown=app:app deployment/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories for static/media/logs files and ensure baseline data permissions
RUN mkdir -p /app/staticfiles /app/media /app/logs && \
    chown -R app:app /app/staticfiles /app/media /app/logs && \
    chmod -R 755 /app/logs
    # baselineData no longer used - Django-native backups in /app/backups

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

# Health check disabled for Dokploy compatibility
# Dokploy handles health monitoring externally via its reverse proxy
# HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
#     CMD curl -f http://localhost:80/health/ready/ || exit 1

# Expose port 80 instead of 8000 (Caddy will serve everything)
EXPOSE 80

# Use entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Default command using supervisor to manage Caddy and Gunicorn
CMD ["/usr/bin/supervisord", "-c", "/app/.config/supervisord.conf", "-n"]

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