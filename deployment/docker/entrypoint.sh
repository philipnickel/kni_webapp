#!/bin/bash
set -e

# =============================================================================
# KNI Webapp - Dokploy Deployment Entrypoint
# =============================================================================
# This script handles container initialization for Dokploy deployments.
#
# Required Environment Variables:
#   DJANGO_SECRET_KEY                 - Django secret key
#   DATABASE_URL                      - PostgreSQL connection string
#
# Optional Environment Variables:
#   REDIS_URL                         - Redis connection string
#   DOMAIN                           - Your domain name
#   ADMIN_EMAIL                      - Admin user email
#   ADMIN_PASSWORD                   - Admin user password
#   DEBUG                            - Set to True for development
# =============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 KNI Webapp SaaS - Auto-configuring deployment...${NC}"

# Default role is 'web' (others: 'worker', 'beat')
ROLE=${ROLE:-web}

# =============================================================================
# Basic Auto-Configuration for Dokploy
# =============================================================================

echo -e "${BLUE}🎯 Configuring deployment for Dokploy...${NC}"

# Generate Django secret key if not provided (for development/testing only)
if [ -z "$DJANGO_SECRET_KEY" ]; then
    echo -e "${YELLOW}⚠️ DJANGO_SECRET_KEY not set - generating temporary key${NC}"
    echo -e "${YELLOW}   For production, set DJANGO_SECRET_KEY environment variable${NC}"
    export DJANGO_SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
fi

# Configure domain settings if provided
if [ -n "$DOMAIN" ]; then
    export ALLOWED_HOSTS="$DOMAIN,www.$DOMAIN,localhost,127.0.0.1"
    export CSRF_TRUSTED_ORIGINS="https://$DOMAIN,https://www.$DOMAIN"
    echo -e "${GREEN}✅ Domain configured: $DOMAIN${NC}"
else
    export ALLOWED_HOSTS="localhost,127.0.0.1"
    echo -e "${YELLOW}⚠️ No DOMAIN set - using localhost only${NC}"
fi

echo -e "${GREEN}✅ Configuration complete!${NC}"


# Wait for database to be ready
echo -e "${YELLOW}⏳ Waiting for database...${NC}"
while ! python -c "
import os
import psycopg2
from urllib.parse import urlparse

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/kni_webapp')
parsed = urlparse(DATABASE_URL)

try:
    conn = psycopg2.connect(
        host=parsed.hostname or 'localhost',
        port=parsed.port or 5432,
        user=parsed.username or '',
        password=parsed.password or '',
        database=parsed.path.lstrip('/') if parsed.path else 'kni_webapp'
    )
    conn.close()
    print('Database connection successful!')
    exit(0)
except Exception as e:
    print(f'Database not ready: {e}')
    exit(1)
"; do
  echo -e "${YELLOW}Database is unavailable - sleeping...${NC}"
  sleep 2
done

echo -e "${GREEN}✅ Database is ready!${NC}"

# Ensure logs and backups directories have proper permissions (fix for Docker volume mounts)
echo -e "${YELLOW}📁 Ensuring logs and backups directory permissions...${NC}"
mkdir -p /app/logs /app/backups
chmod 755 /app/logs /app/backups
echo -e "${GREEN}✅ Logs and backups directories are ready!${NC}"

# Run database migrations (unless run at build time)
if [ "$ROLE" = "web" ]; then
  # Check if migrations were run at build time
  if [ "$RUN_MIGRATIONS" = "true" ]; then
    echo -e "${YELLOW}⏭️ Migrations were run at build time, checking if new migrations needed...${NC}"
    # Check for pending migrations
    PENDING_MIGRATIONS=$(python manage.py showmigrations --plan | grep -c "\[ \]" || true)
    if [ "$PENDING_MIGRATIONS" -gt 0 ]; then
      echo -e "${YELLOW}🔄 Found $PENDING_MIGRATIONS pending migrations, running them...${NC}"
      python manage.py migrate --noinput
    else
      echo -e "${GREEN}✅ No pending migrations found${NC}"
    fi
  else
    echo -e "${YELLOW}🔄 Running database migrations...${NC}"
    python manage.py migrate --noinput
  fi

  # Load baseline data for new deployments
  echo -e "${YELLOW}📦 Loading baseline data...${NC}"
  python manage.py load_baseline_data --skip-existing || true
fi

# Create superuser if it doesn't exist
if [ "$ROLE" = "web" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo -e "${YELLOW}👤 Creating superuser...${NC}"
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='$DJANGO_SUPERUSER_EMAIL').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
fi

# Create admin user if credentials provided
if [ "$ROLE" = "web" ] && [ -n "$ADMIN_EMAIL" ] && [ -n "$ADMIN_PASSWORD" ]; then
    echo -e "${YELLOW}👤 Creating admin user...${NC}"
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='$ADMIN_EMAIL').exists():
    user = User.objects.create_superuser('$ADMIN_EMAIL', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')
    print(f'✅ Admin user created: $ADMIN_EMAIL')
else:
    print('Admin user already exists')
"

    echo -e "${GREEN}🎉 Admin user ready!${NC}"
    echo -e "${BLUE}👤 Admin: $ADMIN_EMAIL${NC}"
    echo -e "${BLUE}🛠️  Admin Panel: https://${DOMAIN:-localhost}/admin/${NC}"
fi


# Collect static files if not already done (skip in development)
if [ "$ROLE" = "web" ] && [ "$DEBUG" != "True" ]; then
  echo -e "${YELLOW}📦 Collecting static files...${NC}"
  python manage.py collectstatic --noinput --clear || true
else
  echo -e "${YELLOW}📦 Skipping static file collection in development mode...${NC}"
fi

# Create health check endpoint
echo -e "${YELLOW}🏥 Setting up health check...${NC}"

echo -e "${GREEN}🎉 Deployment setup complete!${NC}"

# Brief startup delay for service stability
echo -e "${BLUE}⏳ Starting services...${NC}"
sleep 3

echo -e "${GREEN}🌐 Starting web server...${NC}"

# Execute the main command
exec "$@"
