#!/bin/bash

# =============================================================================
# Coolify Customer Onboarding Script
# =============================================================================
#
# This script loads baseline data for new customer onboarding in Coolify.
#
# Usage in Coolify:
#   1. Go to your service in Coolify
#   2. Navigate to "Execute Command"
#   3. Run: bash scripts/load_baseline_coolify.sh
#
# Or run directly in container:
#   docker exec -it <container_name> bash scripts/load_baseline_coolify.sh
#
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 KNI Webapp - Customer Onboarding${NC}"
echo -e "${BLUE}====================================${NC}"
echo ""

# Check if we're running as the app user
if [ "$(id -u)" -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Running as root, switching to app user...${NC}"
    exec su app -c "$0 $*"
fi

# Ensure we're in the right directory
cd /app

# Check database connection
echo -e "${YELLOW}🔍 Checking database connection...${NC}"
if ! python manage.py check --database default >/dev/null 2>&1; then
    echo -e "${RED}❌ Database connection failed!${NC}"
    echo -e "${RED}   Please ensure the database is running and accessible.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Database connection successful${NC}"

# Show what will be loaded
echo -e "${YELLOW}📋 Checking baseline data...${NC}"
python manage.py load_baseline --dry-run

echo ""
echo -e "${YELLOW}⚠️  This will load demo content and create an admin user.${NC}"
echo -e "${YELLOW}   Admin login: admin@customer.com / admin123${NC}"
echo ""

# Confirmation prompt
read -p "🤔 Load baseline data for customer onboarding? (y/N): " -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}❌ Baseline loading cancelled${NC}"
    exit 0
fi

# Load baseline data
echo -e "${GREEN}🎯 Loading baseline data...${NC}"
python manage.py load_baseline --include-media --create-admin

echo ""
echo -e "${GREEN}✅ Customer onboarding completed successfully!${NC}"
echo -e "${GREEN}🌐 Your customer's site is ready with demo content${NC}"
echo ""
echo -e "${BLUE}📊 Next steps:${NC}"
echo -e "${BLUE}   1. Customer can login at: /admin/${NC}"
echo -e "${BLUE}   2. Default login: admin@customer.com / admin123${NC}"
echo -e "${BLUE}   3. Customer should change password immediately${NC}"
echo -e "${BLUE}   4. Customer can replace demo content with their own${NC}"
echo ""
echo -e "${GREEN}🎉 Customer onboarding complete!${NC}"