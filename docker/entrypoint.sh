#!/bin/bash
set -e

# =============================================================================
# KNI Webapp Docker Entrypoint
# =============================================================================
# This script handles container initialization including backup restoration
#
# Environment Variables for Backup/Restore:
#   (LOAD_BASELINE removed - use 'make load-baseline' manually instead)
#   (Note: Backup restoration removed - use Django management commands manually)
#   SEED_TENANT_DATA=true           - Seed tenant-specific data
#   TENANT_SCHEMA=schema_name       - Target tenant schema
#   TENANT_HOSTNAME=hostname        - Tenant hostname
#   TENANT_PORT=port                - Tenant port (default: 80)
#   TENANT_ADMIN_USER=username      - Tenant admin username
#   TENANT_ADMIN_PASSWORD=password  - Tenant admin password
#   TENANT_ADMIN_EMAIL=email        - Tenant admin email
# =============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting KNI Webapp deployment...${NC}"

# Default role is 'web' (others: 'worker', 'beat')
ROLE=${ROLE:-web}

# Generate Django secret key if not provided
if [ "$ROLE" = "web" ] && [ -z "$DJANGO_SECRET_KEY" ]; then
    echo -e "${YELLOW}🔐 No DJANGO_SECRET_KEY found, generating one...${NC}"
    export DJANGO_SECRET_KEY=$(python manage.py generate_secret_key --print-only)
    echo -e "${GREEN}✅ Generated secure Django secret key${NC}"
fi

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

# Seed tenant data if specified
if [ "$ROLE" = "web" ] && [ "$SEED_TENANT_DATA" = "true" ]; then
    echo -e "${YELLOW}🌱 Seeding tenant data...${NC}"
    if [ "$TENANT_SCHEMA" ] && [ "$TENANT_HOSTNAME" ]; then
        python manage.py seed_tenant "$TENANT_SCHEMA" \
            --admin-user "${TENANT_ADMIN_USER:-admin}" \
            --admin-password "${TENANT_ADMIN_PASSWORD:-admin123}" \
            --admin-email "${TENANT_ADMIN_EMAIL:-admin@example.com}" || true
        
        python manage.py ensure_tenant_site \
            --schema="$TENANT_SCHEMA" \
            --hostname="$TENANT_HOSTNAME" \
            --port="${TENANT_PORT:-80}" || true
    fi
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
echo -e "${GREEN}🌐 Starting web server...${NC}"

# Execute the main command
exec "$@"
