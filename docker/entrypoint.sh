#!/bin/bash
set -e

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

# Check if we need to load baseline data first
SHOULD_LOAD_BASELINE=false
if [ "$ROLE" = "web" ] && [ "$LOAD_BASELINE" = "true" ] && [ -f "/app/baselineData/baseline.sql" ]; then
    # Check if database has any tables
    TABLE_COUNT=$(python -c "
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
    cursor = conn.cursor()
    cursor.execute(\"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public'\")
    count = cursor.fetchone()[0]
    conn.close()
    print(count)
except Exception as e:
    print(0)
")
    
    if [ "$TABLE_COUNT" -eq 0 ]; then
        SHOULD_LOAD_BASELINE=true
        echo -e "${YELLOW}Empty database detected, will load baseline data${NC}"
    fi
fi

if [ "$ROLE" = "web" ] && [ "$SHOULD_LOAD_BASELINE" = "false" ]; then
  # Run database migrations only if not loading baseline
  echo -e "${YELLOW}🔄 Running database migrations...${NC}"
  python manage.py migrate --noinput
fi

# Create superuser if it doesn't exist (for development)
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

# Load baseline data if needed
if [ "$ROLE" = "web" ] && [ "$SHOULD_LOAD_BASELINE" = "true" ]; then
    echo -e "${YELLOW}📦 Loading baseline data from /app/baselineData/baseline.sql...${NC}"
    echo -e "${YELLOW}Database appears empty, loading baseline...${NC}"
    
    # Copy baseline media files to media directory
    if [ -d "/app/baselineData/media" ]; then
        echo -e "${YELLOW}📁 Copying baseline media files...${NC}"
        cp -r /app/baselineData/media/* /app/media/ 2>/dev/null || true
    fi
    
    # Now restore the baseline which includes CREATE statements  
    psql "$DATABASE_URL" < /app/baselineData/baseline.sql
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Baseline data loaded successfully!${NC}"
    else
        echo -e "${RED}❌ Failed to load baseline data${NC}"
        exit 1
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

# Collect static files if not already done
if [ "$ROLE" = "web" ]; then
  echo -e "${YELLOW}📦 Collecting static files...${NC}"
  python manage.py collectstatic --noinput --clear || true
fi

# Create health check endpoint
echo -e "${YELLOW}🏥 Setting up health check...${NC}"

echo -e "${GREEN}🎉 Deployment setup complete!${NC}"
echo -e "${GREEN}🌐 Starting web server...${NC}"

# Execute the main command
exec "$@"
