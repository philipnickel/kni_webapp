#!/bin/bash
set -e

# =============================================================================
# KNI Webapp SaaS - Zero Configuration Deployment
# =============================================================================
# This script handles container initialization with automatic configuration
# for SaaS deployments with zero manual setup required.
#
# SaaS Features:
#   - Auto-generates Django secret keys
#   - Auto-configures database passwords
#   - Auto-sets up Redis passwords
#   - Auto-configures domains and ports
#   - Creates admin users automatically
#   - Handles preview deployment isolation
#
# Environment Variables:
#   DOMAIN=client-domain.com          - Customer domain (optional)
#   ADMIN_EMAIL=admin@client.com      - Admin email (optional)
#   PREVIEW_MODE=true                 - Preview deployment mode
#   PREVIEW_ID=pr123                  - Preview deployment ID
#   SAAS_MODE=true                    - Enable SaaS auto-configuration
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
# SaaS Auto-Configuration
# =============================================================================

# Check if we're in SaaS mode (auto-configure everything)
SAAS_MODE=${SAAS_MODE:-false}
if [ "$SAAS_MODE" = "true" ] || [ "$SAAS_MODE" = "1" ]; then
    echo -e "${BLUE}🎯 SaaS Mode: Auto-configuring deployment...${NC}"
    
    # Auto-generate Django secret key if not provided
    if [ -z "$DJANGO_SECRET_KEY" ] || [ "$DJANGO_SECRET_KEY" = "{{AUTO_GENERATE}}" ]; then
        echo -e "${YELLOW}🔐 Auto-generating Django secret key...${NC}"
        export DJANGO_SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
        echo -e "${GREEN}✅ Django secret key generated${NC}"
    fi
    
    # Auto-generate database password if not provided
    if [ -z "$DATABASE_PASSWORD" ] || [ "$DATABASE_PASSWORD" = "{{AUTO_GENERATE}}" ]; then
        echo -e "${YELLOW}🔐 Auto-generating database password...${NC}"
        export DATABASE_PASSWORD=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)
        echo -e "${GREEN}✅ Database password generated${NC}"
    fi
    
    # Auto-generate Redis password if not provided
    if [ -z "$REDIS_PASSWORD" ] || [ "$REDIS_PASSWORD" = "{{AUTO_GENERATE}}" ]; then
        echo -e "${YELLOW}🔐 Auto-generating Redis password...${NC}"
        export REDIS_PASSWORD=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)
        echo -e "${GREEN}✅ Redis password generated${NC}"
    fi
    
    # Auto-configure database URL
    if [ -z "$DATABASE_URL" ]; then
        export DATABASE_URL="postgresql://kni_user:${DATABASE_PASSWORD}@postgres:5432/kni_webapp"
        echo -e "${GREEN}✅ Database URL auto-configured${NC}"
    fi
    
    # Auto-configure Redis URL
    if [ -z "$REDIS_URL" ]; then
        export REDIS_URL="redis://:${REDIS_PASSWORD}@redis:6379/0"
        echo -e "${GREEN}✅ Redis URL auto-configured${NC}"
    fi
    
    # Auto-configure domain settings
    if [ -n "$DOMAIN" ]; then
        export PRIMARY_DOMAIN="$DOMAIN"
        export ALLOWED_HOSTS="$DOMAIN,www.$DOMAIN,localhost,127.0.0.1"
        export CSRF_TRUSTED_ORIGINS="https://$DOMAIN,https://www.$DOMAIN"
        echo -e "${GREEN}✅ Domain auto-configured: $DOMAIN${NC}"
    fi
    
    # Preview deployment configuration
    if [ "$PREVIEW_MODE" = "true" ] || [ "$PREVIEW_MODE" = "1" ]; then
        echo -e "${BLUE}🎭 Preview deployment detected${NC}"
        
        # Configure preview-specific settings
        if [ -n "$PREVIEW_ID" ]; then
            export PREVIEW_DATABASE_NAME="kni_webapp_${PREVIEW_ID}"
            export PREVIEW_REDIS_DB="1"
            echo -e "${GREEN}✅ Preview ID configured: $PREVIEW_ID${NC}"
        fi
        
        # Use minimal resources for previews
        export GUNICORN_WORKERS=1
        export GUNICORN_TIMEOUT=30
        export GUNICORN_MAX_REQUESTS=100
        echo -e "${GREEN}✅ Preview resource limits configured${NC}"
    fi
    
    echo -e "${GREEN}🎉 SaaS auto-configuration complete!${NC}"
fi

# Legacy: Generate Django secret key if not provided (for backward compatibility)
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

# Ensure logs directory has proper permissions (fix for Docker volume mounts)
echo -e "${YELLOW}📁 Ensuring logs directory permissions...${NC}"
mkdir -p /app/logs
chmod 755 /app/logs
echo -e "${GREEN}✅ Logs directory is ready!${NC}"

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

# SaaS: Auto-create admin user if in SaaS mode
if [ "$SAAS_MODE" = "true" ] || [ "$SAAS_MODE" = "1" ]; then
    if [ "$ROLE" = "web" ]; then
        # Auto-generate admin credentials if not provided
        if [ -z "$ADMIN_EMAIL" ]; then
            export ADMIN_EMAIL="admin@${DOMAIN:-localhost}"
            echo -e "${YELLOW}📧 Auto-generated admin email: $ADMIN_EMAIL${NC}"
        fi
        
        if [ -z "$ADMIN_PASSWORD" ]; then
            export ADMIN_PASSWORD=$(openssl rand -base64 16 | tr -d "=+/" | cut -c1-12)
            echo -e "${YELLOW}🔑 Auto-generated admin password: $ADMIN_PASSWORD${NC}"
        fi
        
        echo -e "${YELLOW}👤 Creating SaaS admin user...${NC}"
        python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='$ADMIN_EMAIL').exists():
    user = User.objects.create_superuser('$ADMIN_EMAIL', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')
    print(f'✅ SaaS admin user created: $ADMIN_EMAIL')
    print(f'🔑 Admin password: $ADMIN_PASSWORD')
    print(f'🌐 Admin URL: https://${DOMAIN:-localhost}/admin/')
else:
    print('Admin user already exists')
"
        
        # Display deployment information
        echo -e "${GREEN}🎉 SaaS Deployment Ready!${NC}"
        echo -e "${BLUE}📋 Deployment Information:${NC}"
        echo -e "   🌐 URL: https://${DOMAIN:-localhost}"
        echo -e "   👤 Admin: $ADMIN_EMAIL"
        echo -e "   🔑 Password: $ADMIN_PASSWORD"
        echo -e "   🛠️  Admin Panel: https://${DOMAIN:-localhost}/admin/"
        if [ "$PREVIEW_MODE" = "true" ]; then
            echo -e "   🎭 Preview ID: ${PREVIEW_ID:-unknown}"
        fi
    fi
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

# Add startup delay for Dokploy compatibility
if [ "${DOKPLOY_DEPLOYMENT:-false}" = "true" ]; then
    echo -e "${BLUE}⏳ Dokploy deployment detected - waiting 10s for services to stabilize...${NC}"
    sleep 10
fi

echo -e "${GREEN}🌐 Starting web server...${NC}"

# Execute the main command
exec "$@"
