#!/bin/bash

# =============================================================================
# Production Dokploy Setup Script
# =============================================================================
# This script configures your Dokploy application for production CI/CD deployment
# =============================================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
DOKPLOY_SERVER="72.60.81.210:3000"
APP_ID="H0uYjwFkGyFXgbAXjam-i"
DOMAIN_ID="kQB5-JasS0VojwAh0U7N1"
DOCKER_IMAGE="ghcr.io/philipnickel/kni_webapp:latest"
GITHUB_USERNAME="philipnickel"

echo -e "${GREEN}🚀 Setting up Production Dokploy Deployment${NC}"
echo -e "${BLUE}=======================================${NC}"
echo ""

echo -e "${YELLOW}📦 Docker Image Available:${NC} $DOCKER_IMAGE"
echo -e "${YELLOW}🌐 Server:${NC} $DOKPLOY_SERVER"
echo -e "${YELLOW}🎯 Application:${NC} $APP_ID"
echo ""

echo -e "${BLUE}Step 1: Update Application to use Docker deployment${NC}"
echo "Please manually update your application in Dokploy UI:"
echo ""
echo -e "${YELLOW}1. Access Dokploy:${NC} https://$DOKPLOY_SERVER/"
echo -e "${YELLOW}2. Go to your application (kni-webapp)${NC}"
echo -e "${YELLOW}3. Change Source Type:${NC}"
echo "   - From: Git Provider"
echo "   - To: Docker"
echo ""
echo -e "${YELLOW}4. Configure Docker Settings:${NC}"
echo "   - Docker Image: $DOCKER_IMAGE"
echo "   - Registry URL: ghcr.io"
echo "   - Username: $GITHUB_USERNAME"
echo "   - Password: [GitHub Personal Access Token - see Step 6 below]"
echo ""

echo -e "${BLUE}Step 2: Update Domain Port Configuration${NC}"
echo -e "${YELLOW}🔧 Critical Fix for 502 Error:${NC}"
echo "1. Go to Domains tab in your application"
echo "2. Edit domain: jcleemannbyg.dk"
echo "3. Change Container Port: 80 → 8000"
echo "4. Save changes"
echo ""

echo -e "${BLUE}Step 3: Configure Health Checks${NC}"
echo "1. Go to Advanced → Swarm Settings"
echo "2. Set Health Check Command:"
echo "   curl --fail http://localhost:8000/health/ready/ || exit 1"
echo "3. Configure intervals:"
echo "   - Interval: 30s"
echo "   - Timeout: 10s"
echo "   - Start Period: 60s"
echo "   - Retries: 3"
echo ""

echo -e "${BLUE}Step 4: Environment Variables${NC}"
echo "Ensure these are set (should already be configured):"
cat << 'EOF'
DJANGO_SECRET_KEY=${{project.DJANGO_SECRET_KEY}}
DATABASE_URL=postgresql://wagtail:${{project.DATABASE_PASSWORD}}@kni-webapp-db-mwzipf:5432/wagtail?sslmode=disable
REDIS_URL=redis://:${{project.REDIS_PASSWORD}}@kni-webapp-redis-cae73e:6379/0
DJANGO_SETTINGS_MODULE=project.settings
EOF
echo ""

echo -e "${BLUE}Step 5: Deploy and Test${NC}"
echo "1. Click Deploy in Dokploy"
echo "2. Monitor deployment logs"
echo "3. Test endpoints:"
echo "   - https://jcleemannbyg.dk/"
echo "   - https://jcleemannbyg.dk/health/ready/"
echo "   - https://jcleemannbyg.dk/health/"
echo ""

echo -e "${BLUE}Step 6: Create GitHub Personal Access Token${NC}"
echo "1. Go to: https://github.com/settings/tokens/new"
echo "2. Name: 'Dokploy Production Access'"
echo "3. Scopes: Select 'packages:read'"
echo "4. Copy the generated token"
echo "5. Use it as the Docker Registry Password in Dokploy"
echo ""

echo -e "${BLUE}Step 7: Test Production Deployment${NC}"
echo "Run these tests after deployment:"
echo ""

cat << 'EOF'
# Test basic connectivity
curl -I https://jcleemannbyg.dk/

# Test health endpoints
curl https://jcleemannbyg.dk/health/ready/
curl https://jcleemannbyg.dk/health/

# Test admin access
curl -I https://jcleemannbyg.dk/admin/

EOF

echo -e "${GREEN}🎉 Production Setup Benefits:${NC}"
echo "✅ Zero-downtime deployments with health checks"
echo "✅ Automatic rollbacks if deployment fails"
echo "✅ Build caching reduces deployment time"
echo "✅ Security scanning with GitHub Actions"
echo "✅ Resource optimization - builds off-server"
echo "✅ Consistency - same image everywhere"
echo ""

echo -e "${BLUE}🔄 Automatic CI/CD Flow:${NC}"
echo "1. Push to main branch → GitHub Actions builds Docker image"
echo "2. Image pushed to ghcr.io/philipnickel/kni_webapp:latest"
echo "3. Dokploy can pull latest image for deployments"
echo "4. Health checks ensure safe deployments"
echo ""

echo -e "${YELLOW}⚠️  Important Notes:${NC}"
echo "• The Container Port change (80 → 8000) is critical to fix the 502 error"
echo "• GitHub Personal Access Token needs 'packages:read' scope"
echo "• Health checks will prevent bad deployments from going live"
echo "• This setup follows Dokploy's recommended production practices"
echo ""

echo -e "${GREEN}📚 Documentation:${NC}"
echo "• Full guide: PRODUCTION_DEPLOYMENT_GUIDE.md"
echo "• Troubleshooting: debug-dokploy-502.sh"
echo "• Health endpoints: /health/ready/, /health/, /health/detailed/"
echo ""

echo -e "${GREEN}✨ Setup script completed!${NC}"
echo -e "${YELLOW}Next: Follow the manual steps above in Dokploy UI${NC}"