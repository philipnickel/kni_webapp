#!/bin/bash

# KNI Webapp Dokploy Deployment Script
# This script deploys the KNI webapp to Dokploy using CLI and API

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 KNI Webapp Dokploy Deployment Script${NC}"
echo "=============================================="

# Configuration - Updated with your details
DOKPLOY_URL="http://72.60.81.210:3000"
DOKPLOY_TOKEN="KNIuaQHeqKVMZkbPDJASmYDHcsxYrwYoTIXccuermrDZuOvkrLTNPYMLViUwbHpuqrh"
PROJECT_NAME="kni-webapp"
PROJECT_DESCRIPTION="KNI Webapp - Django/Wagtail application"
COMPOSE_NAME="kni-webapp-compose"
GITHUB_REPO="https://github.com/philipnickel/kni_webapp"
DOMAIN="jcleemannbyg.dk"

# Check if required variables are set
if [ -z "$DOKPLOY_TOKEN" ]; then
    echo -e "${RED}❌ Error: DOKPLOY_TOKEN is not set${NC}"
    echo "Please get your API token from your Dokploy server at: $DOKPLOY_URL/settings/profile"
    exit 1
fi

# URL is configured correctly

# Step 1: Authenticate with Dokploy
echo -e "${YELLOW}🔐 Authenticating with Dokploy...${NC}"
dokploy authenticate --url="$DOKPLOY_URL" --token="$DOKPLOY_TOKEN"

# Step 2: Verify authentication
echo -e "${YELLOW}✅ Verifying authentication...${NC}"
dokploy verify

# Step 3: Create project
echo -e "${YELLOW}📁 Creating project: $PROJECT_NAME${NC}"
PROJECT_ID=$(dokploy project:create --name="$PROJECT_NAME" --description="$PROJECT_DESCRIPTION" --skipConfirm | grep -o '"projectId":"[^"]*"' | cut -d'"' -f4)

if [ -z "$PROJECT_ID" ]; then
    echo -e "${RED}❌ Failed to create project or extract project ID${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Project created with ID: $PROJECT_ID${NC}"

# Step 4: Create Docker Compose service using API
echo -e "${YELLOW}🐳 Creating Docker Compose service...${NC}"
COMPOSE_RESPONSE=$(curl -s -X POST "$DOKPLOY_URL/api/compose.create" \
  -H "Authorization: Bearer $DOKPLOY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"$COMPOSE_NAME\",
    \"description\": \"KNI Webapp Docker Compose deployment\",
    \"projectId\": \"$PROJECT_ID\",
    \"composeType\": \"docker-compose\"
  }")

COMPOSE_ID=$(echo $COMPOSE_RESPONSE | grep -o '"composeId":"[^"]*"' | cut -d'"' -f4)

if [ -z "$COMPOSE_ID" ]; then
    echo -e "${RED}❌ Failed to create Docker Compose service${NC}"
    echo "Response: $COMPOSE_RESPONSE"
    exit 1
fi

echo -e "${GREEN}✅ Docker Compose service created with ID: $COMPOSE_ID${NC}"

# Step 5: Update Docker Compose service with repository and settings
echo -e "${YELLOW}⚙️ Configuring Docker Compose service...${NC}"
UPDATE_RESPONSE=$(curl -s -X POST "$DOKPLOY_URL/api/compose.update" \
  -H "Authorization: Bearer $DOKPLOY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"composeId\": \"$COMPOSE_ID\",
    \"sourceType\": \"github\",
    \"repository\": \"$(basename $GITHUB_REPO)\",
    \"owner\": \"$(dirname $GITHUB_REPO | xargs basename)\",
    \"branch\": \"main\",
    \"composeFile\": \"./docker-compose.yml\",
    \"env\": \"# Production Environment Variables\nDJANGO_SECRET_KEY=\${DJANGO_SECRET_KEY}\nDATABASE_PASSWORD=\${DATABASE_PASSWORD}\nREDIS_PASSWORD=\${REDIS_PASSWORD}\nDOMAIN=$DOMAIN\nADMIN_EMAIL=admin@$DOMAIN\",
    \"autoDeploy\": true
  }")

echo -e "${GREEN}✅ Docker Compose service configured${NC}"

# Step 6: Set up project-level environment variables
echo -e "${YELLOW}🔧 Setting up environment variables...${NC}"

# Create environment variables (this would need to be done via API calls to the environment endpoints)
cat << EOF > /tmp/dokploy-env-setup.md
## Environment Variables to Set in Dokploy UI

Please go to your Dokploy dashboard and set these **PROJECT-LEVEL** environment variables:

### Required Secrets:
- DJANGO_SECRET_KEY=your-secure-django-secret-key-here
- DATABASE_PASSWORD=your-secure-database-password
- REDIS_PASSWORD=your-secure-redis-password

### Domain Configuration:
- DOMAIN=$DOMAIN
- ADMIN_EMAIL=admin@$DOMAIN

### Optional Email Configuration:
- EMAIL_HOST=smtp.$DOMAIN
- EMAIL_PORT=587
- EMAIL_USE_TLS=True
- EMAIL_HOST_USER=noreply@$DOMAIN
- EMAIL_HOST_PASSWORD=your-email-password

Then reference them in your service using: \${{project.VARIABLE_NAME}}
EOF

echo -e "${GREEN}✅ Environment variables template created at /tmp/dokploy-env-setup.md${NC}"

# Step 7: Display next steps
echo ""
echo -e "${GREEN}🎉 Deployment Setup Complete!${NC}"
echo "=============================================="
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Go to your Dokploy dashboard: $DOKPLOY_URL"
echo "2. Navigate to project '$PROJECT_NAME'"
echo "3. Set up the environment variables listed in /tmp/dokploy-env-setup.md"
echo "4. Configure your GitHub repository access if needed"
echo "5. Add domain: $DOMAIN in the Domains section"
echo "6. Deploy your application!"
echo ""
echo -e "${GREEN}Project ID: $PROJECT_ID${NC}"
echo -e "${GREEN}Compose ID: $COMPOSE_ID${NC}"
echo ""
echo -e "${YELLOW}Remember to:${NC}"
echo "- Point your domain's A record to your Dokploy server's IP"
echo "- Generate secure secrets for production"
echo "- Configure your GitHub repository access"

# Display the environment setup instructions
echo ""
echo -e "${YELLOW}📋 Environment Variables Setup:${NC}"
cat /tmp/dokploy-env-setup.md