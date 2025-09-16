#!/bin/bash

# Setup GitHub Secrets for Dokploy Deployment
# Run this script to configure the required secrets for GitHub Actions

echo "🔧 Setting up GitHub repository secrets for Dokploy deployment..."

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Please install it: https://cli.github.com/"
    exit 1
fi

# Repository information
REPO="philipnickel/kni_webapp"
DOKPLOY_URL="http://72.60.81.210:3000"
DOKPLOY_API_KEY="KNIuaQHeqKVMZkbPDJASmYDHcsxYrwYoTIXccuermrDZuOvkrLTNPYMLViUwbHpuqrh"
DOKPLOY_COMPOSE_ID="YzNI_IDhPM40FRlR5su98"

echo "Setting up secrets for repository: $REPO"

# Set GitHub repository secrets
gh secret set DOKPLOY_URL --body "$DOKPLOY_URL" --repo "$REPO"
echo "✅ DOKPLOY_URL secret set"

gh secret set DOKPLOY_API_KEY --body "$DOKPLOY_API_KEY" --repo "$REPO"
echo "✅ DOKPLOY_API_KEY secret set"

gh secret set DOKPLOY_COMPOSE_ID --body "$DOKPLOY_COMPOSE_ID" --repo "$REPO"
echo "✅ DOKPLOY_COMPOSE_ID secret set"

echo ""
echo "🎉 GitHub secrets configured successfully!"
echo ""
echo "Next steps:"
echo "1. Commit and push the GitHub Actions workflow"
echo "2. The workflow will automatically build and push Docker images"
echo "3. Update Dokploy to use the built image"
echo ""
echo "Repository: https://github.com/$REPO"
echo "Actions: https://github.com/$REPO/actions"