#!/bin/bash
# Dokploy Deployment Script
# Handles Git clone conflicts and ensures clean deployments

set -e

echo "🚀 Starting Dokploy deployment for KNI Webapp..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to handle Git clone conflicts
handle_git_cleanup() {
    echo -e "${YELLOW}🧹 Cleaning up any existing Git directories...${NC}"

    # Remove any existing .git directories that might cause conflicts
    if [ -d ".git" ]; then
        echo -e "${YELLOW}Found existing .git directory, removing...${NC}"
        rm -rf .git
    fi

    # Remove any temporary clone directories
    if [ -d "/tmp/dokploy-clone" ]; then
        echo -e "${YELLOW}Removing temporary clone directory...${NC}"
        rm -rf /tmp/dokploy-clone
    fi

    echo -e "${GREEN}✅ Git cleanup completed${NC}"
}

# Function to validate Docker Compose configuration
validate_compose() {
    echo -e "${YELLOW}🔍 Validating Docker Compose configuration...${NC}"

    # Use Dokploy-specific compose file if it exists
    if [ -f ".dokploy/docker-compose.yml" ]; then
        echo -e "${YELLOW}Using Dokploy-specific compose file...${NC}"
        docker-compose -f .dokploy/docker-compose.yml config > /dev/null
        echo -e "${GREEN}✅ Dokploy compose configuration is valid${NC}"
    else
        echo -e "${YELLOW}Using main compose file...${NC}"
        docker-compose config > /dev/null
        echo -e "${GREEN}✅ Main compose configuration is valid${NC}"
    fi
}

# Function to check port availability
check_ports() {
    echo -e "${YELLOW}🔍 Checking port availability...${NC}"

    # Check if port 8000 is available or if we can use it
    if netstat -tuln 2>/dev/null | grep -q ":8000 "; then
        echo -e "${YELLOW}⚠️  Port 8000 is already in use, this might be from a previous deployment${NC}"
    else
        echo -e "${GREEN}✅ Port 8000 is available${NC}"
    fi
}

# Function to ensure environment variables are set
setup_environment() {
    echo -e "${YELLOW}🔧 Setting up environment variables...${NC}"

    # Load Dokploy-specific environment if available
    if [ -f ".dokploy/.env" ]; then
        echo -e "${YELLOW}Loading Dokploy environment variables...${NC}"
        export $(cat .dokploy/.env | grep -v '^#' | xargs)
    fi

    # Set required defaults for Dokploy
    export DOCKER_TARGET=${DOCKER_TARGET:-production}
    export DEBUG=${DEBUG:-false}
    export WEB_EXPOSE_PORT=${WEB_EXPOSE_PORT:-8000}
    export ALLOWED_HOSTS=${ALLOWED_HOSTS:-localhost,127.0.0.1,0.0.0.0,72.60.81.210}

    echo -e "${GREEN}✅ Environment setup completed${NC}"
    echo -e "${GREEN}   - DOCKER_TARGET: $DOCKER_TARGET${NC}"
    echo -e "${GREEN}   - DEBUG: $DEBUG${NC}"
    echo -e "${GREEN}   - WEB_EXPOSE_PORT: $WEB_EXPOSE_PORT${NC}"
}

# Main deployment process
main() {
    echo -e "${GREEN}🎯 KNI Webapp Dokploy Deployment${NC}"
    echo -e "${GREEN}================================${NC}"

    # Run deployment steps
    handle_git_cleanup
    setup_environment
    validate_compose
    check_ports

    echo -e "${GREEN}🎉 Pre-deployment checks completed successfully!${NC}"
    echo -e "${GREEN}📦 Ready for Docker Compose deployment...${NC}"

    # Note: The actual docker-compose up will be handled by Dokploy
    echo -e "${YELLOW}ℹ️  Dokploy will now handle the container orchestration${NC}"
}

# Run main function
main "$@"