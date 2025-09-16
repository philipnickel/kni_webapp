#!/bin/bash

# =============================================================================
# Dokploy 502 Error Debugging Script
# =============================================================================
# Run this script to diagnose common 502 Bad Gateway issues in Dokploy
# =============================================================================

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

APP_ID="${1:-H0uYjwFkGyFXgbAXjam-i}"
DOMAIN="${2:-jcleemannbyg.dk}"

echo -e "${GREEN}🔍 Dokploy 502 Error Diagnostic Tool${NC}"
echo -e "${BLUE}====================================${NC}"
echo ""
echo -e "${YELLOW}Application ID:${NC} $APP_ID"
echo -e "${YELLOW}Domain:${NC} $DOMAIN"
echo ""

echo -e "${BLUE}1. DNS Resolution Check${NC}"
echo -n "Checking DNS resolution for $DOMAIN... "
if dig +short $DOMAIN > /dev/null 2>&1; then
    IP=$(dig +short $DOMAIN | tail -n1)
    echo -e "${GREEN}✅ Resolved to: $IP${NC}"
else
    echo -e "${RED}❌ DNS resolution failed${NC}"
fi

echo ""
echo -e "${BLUE}2. SSL Certificate Check${NC}"
echo -n "Checking SSL certificate for https://$DOMAIN... "
if openssl s_client -connect $DOMAIN:443 -servername $DOMAIN < /dev/null > /dev/null 2>&1; then
    echo -e "${GREEN}✅ SSL handshake successful${NC}"

    # Get certificate details
    CERT_INFO=$(openssl s_client -connect $DOMAIN:443 -servername $DOMAIN < /dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates 2>/dev/null)
    if [ ! -z "$CERT_INFO" ]; then
        echo -e "${BLUE}Certificate details:${NC}"
        echo "$CERT_INFO" | sed 's/^/  /'
    fi
else
    echo -e "${RED}❌ SSL handshake failed${NC}"
fi

echo ""
echo -e "${BLUE}3. HTTP Response Check${NC}"
echo -n "Testing HTTP response from https://$DOMAIN... "
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 https://$DOMAIN 2>/dev/null || echo "000")
if [ "$HTTP_STATUS" = "502" ]; then
    echo -e "${RED}❌ 502 Bad Gateway (confirmed)${NC}"
elif [ "$HTTP_STATUS" = "200" ]; then
    echo -e "${GREEN}✅ 200 OK (site is working!)${NC}"
else
    echo -e "${YELLOW}⚠️  HTTP $HTTP_STATUS${NC}"
fi

echo ""
echo -e "${BLUE}4. Health Check Endpoint Test${NC}"
for endpoint in "/ready" "/ready/" "/health/ready" "/health/ready/"; do
    echo -n "Testing https://$DOMAIN$endpoint... "
    HEALTH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 https://$DOMAIN$endpoint 2>/dev/null || echo "000")
    if [ "$HEALTH_STATUS" = "200" ]; then
        echo -e "${GREEN}✅ $HEALTH_STATUS${NC}"
    elif [ "$HEALTH_STATUS" = "502" ]; then
        echo -e "${RED}❌ $HEALTH_STATUS${NC}"
    else
        echo -e "${YELLOW}⚠️  $HEALTH_STATUS${NC}"
    fi
done

echo ""
echo -e "${BLUE}5. Docker Services Check (if running locally)${NC}"
if command -v docker > /dev/null 2>&1; then
    echo "Checking for local Docker services..."

    # Check if any containers are running with our app name
    CONTAINERS=$(docker ps --filter "name=$APP_ID" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || echo "No containers found")
    if [ "$CONTAINERS" != "No containers found" ]; then
        echo -e "${BLUE}Running containers:${NC}"
        echo "$CONTAINERS"
    else
        echo -e "${YELLOW}⚠️  No local containers found for app ID $APP_ID${NC}"
    fi

    # Check Docker Swarm services
    SWARM_SERVICES=$(docker service ls --filter "name=$APP_ID" --format "table {{.NAME}}\t{{.REPLICAS}}\t{{.IMAGE}}" 2>/dev/null || echo "Not in swarm mode or no services")
    if [ "$SWARM_SERVICES" != "Not in swarm mode or no services" ]; then
        echo -e "${BLUE}Docker Swarm services:${NC}"
        echo "$SWARM_SERVICES"
    fi
else
    echo -e "${YELLOW}⚠️  Docker not available for local inspection${NC}"
fi

echo ""
echo -e "${BLUE}6. Common 502 Causes & Solutions${NC}"
echo -e "${YELLOW}Cause 1: Container not responding on port 80${NC}"
echo "  ✅ Solution: Verify Dockerfile exposes port 80"
echo "  ✅ Solution: Check that Caddy is running and bound to :80"
echo "  ✅ Solution: Ensure supervisord starts both Caddy and Gunicorn"
echo ""
echo -e "${YELLOW}Cause 2: Gunicorn not responding on 127.0.0.1:8000${NC}"
echo "  ✅ Solution: Check Gunicorn bind address in supervisord.conf"
echo "  ✅ Solution: Verify Django app loads without errors"
echo "  ✅ Solution: Check database connectivity"
echo ""
echo -e "${YELLOW}Cause 3: Deployment mode mismatch${NC}"
echo "  ✅ Solution: Use Application mode, not Compose mode"
echo "  ✅ Solution: Don't use docker-compose.dokploy.yml with Application mode"
echo "  ✅ Solution: Let Dockerfile handle the complete stack"
echo ""
echo -e "${YELLOW}Cause 4: Environment variables not set${NC}"
echo "  ✅ Solution: Set DJANGO_SECRET_KEY, DATABASE_URL, REDIS_URL"
echo "  ✅ Solution: Use Dokploy template syntax: \${{project.VARIABLE}}"
echo ""
echo -e "${YELLOW}Cause 5: Service dependencies not ready${NC}"
echo "  ✅ Solution: Ensure PostgreSQL and Redis services are healthy"
echo "  ✅ Solution: Check service discovery (postgres:5432, redis:6379)"
echo "  ✅ Solution: Wait for entrypoint script to complete database setup"
echo ""

echo -e "${BLUE}7. Recommended Next Steps${NC}"
if [ "$HTTP_STATUS" = "502" ]; then
    echo -e "${RED}🚨 502 Error Confirmed - Follow these steps:${NC}"
    echo ""
    echo -e "${YELLOW}STEP 1:${NC} Check Dokploy application logs"
    echo "  - Look for container startup errors"
    echo "  - Verify supervisor starts Caddy and Gunicorn"
    echo "  - Check for Django/database errors"
    echo ""
    echo -e "${YELLOW}STEP 2:${NC} Verify deployment configuration"
    echo "  - Ensure using Application mode (not Compose)"
    echo "  - Check Dockerfile path: deployment/Dockerfile"
    echo "  - Verify port 80 is exposed and mapped"
    echo ""
    echo -e "${YELLOW}STEP 3:${NC} Check service dependencies"
    echo "  - PostgreSQL service health"
    echo "  - Redis service health"
    echo "  - Network connectivity between services"
    echo ""
    echo -e "${YELLOW}STEP 4:${NC} Review environment variables"
    echo "  - DATABASE_URL format and credentials"
    echo "  - REDIS_URL format and password"
    echo "  - DJANGO_SECRET_KEY presence"
    echo ""
    echo -e "${YELLOW}STEP 5:${NC} Test health endpoints directly"
    echo "  - SSH into container if possible"
    echo "  - Test: curl http://localhost:80/ready"
    echo "  - Test: curl http://localhost:8000/admin/ (Gunicorn direct)"
    echo ""
elif [ "$HTTP_STATUS" = "200" ]; then
    echo -e "${GREEN}🎉 Site appears to be working! No 502 error detected.${NC}"
else
    echo -e "${YELLOW}⚠️  Site returning HTTP $HTTP_STATUS - investigate further${NC}"
fi

echo ""
echo -e "${GREEN}🔧 Quick Fix Commands:${NC}"
echo "Run the deployment script:"
echo "  ./deploy-dokploy-app.sh"
echo ""
echo "Check this diagnostic again:"
echo "  ./debug-dokploy-502.sh $APP_ID $DOMAIN"
echo ""
echo -e "${BLUE}💡 For more help, check the deployment logs in Dokploy UI${NC}"