#!/bin/bash
set -e

# =============================================================================
# KNI Webapp SaaS - Deployment Script
# =============================================================================
# This script helps deploy the KNI Webapp as a SaaS solution
# =============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_FILE="$PROJECT_DIR/config/environments/env.saas.template"
ENV_FILE="$PROJECT_DIR/.env.saas"

echo -e "${GREEN}🚀 KNI Webapp SaaS Deployment Script${NC}"
echo -e "${BLUE}=====================================${NC}"

# Function to display help
show_help() {
    echo -e "${YELLOW}Usage: $0 [OPTIONS]${NC}"
    echo ""
    echo -e "${YELLOW}Options:${NC}"
    echo "  -d, --domain DOMAIN        Customer domain (required)"
    echo "  -e, --email EMAIL          Admin email address (optional)"
    echo "  -p, --preview              Deploy as preview environment"
    echo "  -i, --preview-id ID        Preview deployment ID (required for preview)"
    echo "  -h, --help                 Show this help message"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 --domain client-domain.com --email admin@client.com"
    echo "  $0 --domain client-domain.com --preview --preview-id pr123"
    echo ""
    echo -e "${YELLOW}What this script does:${NC}"
    echo "  1. Creates SaaS environment configuration"
    echo "  2. Sets up auto-generated secrets"
    echo "  3. Configures domain and admin settings"
    echo "  4. Prepares for Dokploy deployment"
}

# Function to validate domain
validate_domain() {
    local domain=$1
    if [[ ! $domain =~ ^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$ ]]; then
        echo -e "${RED}❌ Invalid domain format: $domain${NC}"
        echo -e "${YELLOW}Please provide a valid domain (e.g., example.com)${NC}"
        exit 1
    fi
}

# Function to validate email
validate_email() {
    local email=$1
    if [[ ! $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo -e "${RED}❌ Invalid email format: $email${NC}"
        echo -e "${YELLOW}Please provide a valid email address${NC}"
        exit 1
    fi
}

# Function to generate random password
generate_password() {
    openssl rand -base64 32 | tr -d "=+/" | cut -c1-25
}

# Function to create SaaS environment file
create_saas_env() {
    local domain=$1
    local email=$2
    local preview_mode=$3
    local preview_id=$4
    
    echo -e "${YELLOW}📝 Creating SaaS environment configuration...${NC}"
    
    # Copy template
    cp "$TEMPLATE_FILE" "$ENV_FILE"
    
    # Replace placeholders
    sed -i.bak "s/your-domain.com/$domain/g" "$ENV_FILE"
    sed -i.bak "s/admin@your-domain.com/$email/g" "$ENV_FILE"
    
    # Configure preview mode if specified
    if [ "$preview_mode" = "true" ]; then
        echo -e "${BLUE}🎭 Configuring preview deployment...${NC}"
        sed -i.bak "s/# PREVIEW_MODE=false/PREVIEW_MODE=true/g" "$ENV_FILE"
        sed -i.bak "s/# PREVIEW_ID=/PREVIEW_ID=$preview_id/g" "$ENV_FILE"
        sed -i.bak "s/# PREVIEW_DATABASE_NAME=/PREVIEW_DATABASE_NAME=kni_webapp_$preview_id/g" "$ENV_FILE"
        sed -i.bak "s/# PREVIEW_REDIS_DB=1/PREVIEW_REDIS_DB=1/g" "$ENV_FILE"
        
        # Preview-specific settings
        sed -i.bak "s/DEBUG=False/DEBUG=True/g" "$ENV_FILE"
        sed -i.bak "s/GUNICORN_WORKERS=2/GUNICORN_WORKERS=1/g" "$ENV_FILE"
        sed -i.bak "s/GUNICORN_TIMEOUT=60/GUNICORN_TIMEOUT=30/g" "$ENV_FILE"
        sed -i.bak "s/GUNICORN_MAX_REQUESTS=1000/GUNICORN_MAX_REQUESTS=100/g" "$ENV_FILE"
    fi
    
    # Clean up backup file
    rm -f "$ENV_FILE.bak"
    
    echo -e "${GREEN}✅ SaaS environment file created: $ENV_FILE${NC}"
}

# Function to display deployment information
show_deployment_info() {
    local domain=$1
    local email=$2
    local preview_mode=$3
    local preview_id=$4
    
    echo -e "${GREEN}🎉 SaaS Deployment Configuration Complete!${NC}"
    echo -e "${BLUE}===========================================${NC}"
    echo -e "${YELLOW}📋 Deployment Information:${NC}"
    echo -e "   🌐 Domain: $domain"
    echo -e "   👤 Admin Email: $email"
    echo -e "   📁 Environment File: $ENV_FILE"
    
    if [ "$preview_mode" = "true" ]; then
        echo -e "   🎭 Preview Mode: Enabled"
        echo -e "   🆔 Preview ID: $preview_id"
        echo -e "   🔗 Preview URL: https://$preview_id-$domain"
    else
        echo -e "   🏭 Production Mode: Enabled"
        echo -e "   🔗 Production URL: https://$domain"
    fi
    
    echo ""
    echo -e "${YELLOW}🚀 Next Steps:${NC}"
    echo "   1. Review the environment file: $ENV_FILE"
    echo "   2. Deploy using Dokploy with the template: dokploy-template.yml"
    echo "   3. Monitor deployment logs for auto-generated credentials"
    echo "   4. Access your application at the URL above"
    echo ""
    echo -e "${YELLOW}📚 Documentation:${NC}"
    echo "   - Template: dokploy-template.yml"
    echo "   - Preview Template: dokploy-preview.yml"
    echo "   - Environment Template: env.saas.template"
}

# Parse command line arguments
DOMAIN=""
EMAIL=""
PREVIEW_MODE="false"
PREVIEW_ID=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--domain)
            DOMAIN="$2"
            shift 2
            ;;
        -e|--email)
            EMAIL="$2"
            shift 2
            ;;
        -p|--preview)
            PREVIEW_MODE="true"
            shift
            ;;
        -i|--preview-id)
            PREVIEW_ID="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# Validate required parameters
if [ -z "$DOMAIN" ]; then
    echo -e "${RED}❌ Domain is required${NC}"
    show_help
    exit 1
fi

if [ "$PREVIEW_MODE" = "true" ] && [ -z "$PREVIEW_ID" ]; then
    echo -e "${RED}❌ Preview ID is required for preview deployments${NC}"
    show_help
    exit 1
fi

# Set default email if not provided
if [ -z "$EMAIL" ]; then
    EMAIL="admin@$DOMAIN"
    echo -e "${YELLOW}📧 Using default admin email: $EMAIL${NC}"
fi

# Validate inputs
validate_domain "$DOMAIN"
validate_email "$EMAIL"

# Create SaaS environment configuration
create_saas_env "$DOMAIN" "$EMAIL" "$PREVIEW_MODE" "$PREVIEW_ID"

# Display deployment information
show_deployment_info "$DOMAIN" "$EMAIL" "$PREVIEW_MODE" "$PREVIEW_ID"

echo -e "${GREEN}🎉 SaaS deployment setup complete!${NC}"

