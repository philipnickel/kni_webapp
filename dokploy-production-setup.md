# Official Dokploy Production Deployment

Following the exact process from: https://docs.dokploy.com/docs/core/applications/going-production

## Problem with Current Setup
- Building on server with "Git Provider" consumes high server resources
- Can cause server timeouts and application downtime
- Not recommended for production

## Official Solution: CI/CD Pipeline + Docker Registry

### Step 1: CI/CD is Already Set Up ✅

Your GitHub Actions workflow is already configured correctly:
- Builds Docker image in CI/CD pipeline (off-server)
- Pushes to GitHub Container Registry (ghcr.io)
- Available at: `ghcr.io/philipnickel/kni_webapp:latest`

### Step 2: Switch Dokploy to Docker Mode

1. **Access Dokploy**: https://72.60.81.210:3000/
2. **Go to your application** (kni-webapp)
3. **Change Source Type**:
   - Current: "Git Provider"
   - New: **"Docker"** (as per official guide)

### Step 3: Configure Docker Settings

In the Docker configuration:
- **Docker Image**: `ghcr.io/philipnickel/kni_webapp:latest`
- **Docker Registry URL**: `ghcr.io`
- **Username**: `philipnickel`
- **Password**: [GitHub Personal Access Token with `packages:read` scope]

### Step 4: Deploy Following Official Process

1. Click **"Save"** (as mentioned in guide)
2. Click **"Deploy"** (as mentioned in guide)
3. Navigate to **"Domains"** tab
4. Set the port to match your application (8000 for Django)

### Step 5: Configure Production Features (Official Guide)

#### Health Checks (Advanced → Swarm Settings):
```bash
curl --fail http://localhost:8000/health/ready/ || exit 1
```

#### Auto-Deploy Webhook:
1. Go to **Deployments** tab in Dokploy
2. Copy the **Webhook URL**
3. Add to GitHub repository webhooks

### Step 6: Test Production Deployment

The official guide recommends testing:
1. Domain accessibility
2. Application functionality
3. Health check endpoints

## Benefits (Per Official Guide)
- ✅ Reduced server resource consumption
- ✅ Faster deployments
- ✅ Eliminates server timeout issues
- ✅ Professional CI/CD workflow
- ✅ Better application availability

## Why This Follows Official Best Practices

1. **"Build & Publish in CI/CD"**: ✅ Done with GitHub Actions
2. **"Use Docker source type"**: ✅ Switching from Git Provider
3. **"Push to registry"**: ✅ Using ghcr.io registry
4. **"Configure Dokploy to pull"**: ✅ Setting up Docker source

This is the **exact workflow** recommended by Dokploy documentation for production deployments.