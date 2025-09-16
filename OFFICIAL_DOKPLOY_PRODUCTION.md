# Official Dokploy Production Deployment

**Exactly following**: https://docs.dokploy.com/docs/core/applications/going-production

## The Problem (From Official Guide)

Building with "nixpacks" or "heroku buildpacks" on the server:
- Consumes high server resources
- Can cause server timeouts
- Leads to application downtime
- Not suitable for production

## The Solution (Official Recommendation)

**"Build & Publish the application in a CI/CD pipeline"**

## Step 1: CI/CD Pipeline ✅ Done

The GitHub Actions workflow is now configured exactly as per Dokploy documentation:
- Builds Docker image off-server (saves resources)
- Pushes to GitHub Container Registry
- Available at: `ghcr.io/philipnickel/kni_webapp:latest`

## Step 2: Configure Dokploy (Official Process)

### 2.1 Switch Source Type
1. Go to your Dokploy application
2. **Source Type**: Change from "Git Provider" to **"Docker"**

### 2.2 Configure Docker Settings
Following the official guide configuration:
- **Docker Image**: `ghcr.io/philipnickel/kni_webapp:latest`
- **Registry URL**: `ghcr.io`
- **Username**: `philipnickel`
- **Password**: [GitHub Personal Access Token]

### 2.3 Deploy (Official Steps)
1. Click **"Save"** (as stated in guide)
2. Click **"Deploy"** (as stated in guide)
3. Navigate to **"Domains"** tab
4. Set the port to **8000**

## Step 3: Create GitHub Personal Access Token

Required for accessing GitHub Container Registry:

1. Go to: https://github.com/settings/tokens/new
2. Name: "Dokploy Production Registry Access"
3. Permissions: ✅ `packages:read`
4. Copy the generated token
5. Use as Docker Registry Password in Dokploy

## Step 4: Verify Production Setup

After deployment, test these endpoints:
- `https://jcleemannbyg.dk/` - Main application
- `https://jcleemannbyg.dk/health/ready/` - Health check
- `https://jcleemannbyg.dk/admin/` - Admin interface

## Step 5: Configure Auto-Deploy (Optional)

Following the official webhook setup:
1. In Dokploy → **Deployments** tab
2. Copy the **Webhook URL**
3. Add to GitHub repository:
   - Go to: https://github.com/philipnickel/kni_webapp/settings/hooks
   - Add webhook with Dokploy URL
   - Events: "Just the push event"

## Benefits (Official Guide)

✅ **Reduced server resource consumption**
✅ **Faster, more reliable deployments**
✅ **Eliminates server timeout issues**
✅ **Professional production workflow**
✅ **Better application availability**

## Why This is the Official Approach

1. **Problem Identified**: Official docs state building on server "consumes high server resources"
2. **Solution Provided**: "Build & Publish the application in a CI/CD pipeline"
3. **Process Defined**: Use Docker source type with pre-built images
4. **Benefits Listed**: Reduced resource consumption, faster deployments

This follows the **exact workflow** and reasoning from the official Dokploy production documentation.

## Next Steps

1. **Create GitHub Token**: Follow Step 3 above
2. **Switch Dokploy to Docker**: Follow Step 2 above
3. **Deploy**: Click Save → Deploy
4. **Test**: Verify all endpoints work
5. **Set up Auto-Deploy**: Optional webhook configuration

Your application will now follow Dokploy's official production best practices!