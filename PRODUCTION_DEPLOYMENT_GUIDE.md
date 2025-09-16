# Production Deployment Guide for KNI Webapp

## Overview
This guide implements Dokploy's recommended production deployment pattern using CI/CD pipelines and pre-built Docker images.

## ✅ What's Already Done

1. **Production-Optimized Dockerfile**: Enhanced with security updates, proper Gunicorn settings, and health checks
2. **CI/CD Pipeline**: GitHub Actions workflow that builds and pushes Docker images to GHCR
3. **Health Check Endpoints**: Comprehensive health monitoring at `/health/ready/`

## 🚀 Production Deployment Steps

### Step 1: Wait for Docker Image Build
Your CI/CD pipeline is currently building the production Docker image. Check the status:
- Go to: https://github.com/philipnickel/kni_webapp/actions
- Wait for "Build and Deploy KNI Webapp" workflow to complete successfully
- The image will be available at: `ghcr.io/philipnickel/kni_webapp:latest`

### Step 2: Create New Dokploy Application (Recommended)

1. **Access Dokploy**: https://72.60.81.210:3000/
2. **Create New Application**:
   - Name: `kni-webapp-production`
   - Description: `Production KNI Webapp using Docker deployment`

3. **Configure Docker Source**:
   - **Source Type**: Select "Docker"
   - **Docker Image**: `ghcr.io/philipnickel/kni_webapp:latest`
   - **Registry URL**: `ghcr.io`
   - **Username**: `philipnickel` (your GitHub username)
   - **Password**: [Create GitHub Personal Access Token with `packages:read` scope]

### Step 3: Environment Variables
Copy these from your current application to the new one:
```
DJANGO_SECRET_KEY=${{project.DJANGO_SECRET_KEY}}
DATABASE_URL=postgresql://wagtail:${{project.DATABASE_PASSWORD}}@kni-webapp-db-mwzipf:5432/wagtail?sslmode=disable
REDIS_URL=redis://:${{project.REDIS_PASSWORD}}@kni-webapp-redis-cae73e:6379/0
DJANGO_SETTINGS_MODULE=project.settings
```

### Step 4: Configure Health Checks
In **Advanced → Swarm Settings**:
- **Health Check**: `curl --fail http://localhost:8000/health/ready/ || exit 1`
- **Interval**: 30s
- **Timeout**: 10s
- **Start Period**: 60s
- **Retries**: 3

### Step 5: Update Domain Configuration
- **Domain**: `jcleemannbyg.dk`
- **Path**: `/`
- **Container Port**: `8000` ⭐ **This fixes the 502 error!**
- **HTTPS**: Enabled
- **Certificate**: Let's Encrypt

### Step 6: Deploy and Test
1. Click **Deploy**
2. Monitor logs for successful startup
3. Test health endpoints:
   - `https://jcleemannbyg.dk/health/ready/`
   - `https://jcleemannbyg.dk/health/`

### Step 7: Set Up Automatic Deployments (Optional)
1. In Dokploy → Deployments tab, copy the **Webhook URL**
2. Add to GitHub repository:
   - Go to: https://github.com/philipnickel/kni_webapp/settings/hooks
   - Add webhook with the Dokploy URL
   - Events: "Just the push event"

## 🔧 Alternative: Update Existing Application

If you prefer to update your current application instead:

1. **Change Build Type**:
   - Go to your current application
   - **Source Type** → Change from "Git Provider" to "Docker"
   - **Docker Image**: `ghcr.io/philipnickel/kni_webapp:latest`

2. **Update Domain Port**:
   - **Domains** tab → Edit `jcleemannbyg.dk`
   - **Container Port**: Change from `80` to `8000`

## 🎯 Benefits of This Setup

✅ **Zero-downtime deployments** with health checks
✅ **Automatic rollbacks** if deployment fails
✅ **Build caching** reduces deployment time
✅ **Security scanning** with GitHub Actions
✅ **Resource optimization** - builds off-server
✅ **Consistency** - same image everywhere

## 🐛 Troubleshooting

### 502 Bad Gateway
- **Cause**: Domain port mismatch
- **Fix**: Ensure Container Port is set to `8000`

### Health Check Failures
- **Check**: Application logs for startup errors
- **Verify**: Database and Redis connectivity
- **Test**: Direct health endpoint: `curl http://localhost:8000/health/ready/`

### Docker Image Pull Errors
- **Verify**: GitHub Personal Access Token has `packages:read` scope
- **Check**: Image exists at `ghcr.io/philipnickel/kni_webapp:latest`
- **Test**: `docker pull ghcr.io/philipnickel/kni_webapp:latest`

## 📊 Monitoring

Your application includes comprehensive health monitoring:
- **Basic Health**: `/health/`
- **Readiness Check**: `/health/ready/` (for Dokploy health checks)
- **Detailed Health**: `/health/detailed/` (includes DB, Redis, cache status)
- **Liveness Check**: `/health/live/` (minimal check)

## 🔄 Next Steps

1. Monitor the first deployment carefully
2. Set up log aggregation if needed
3. Consider implementing blue-green deployments for even safer releases
4. Add performance monitoring (APM) for production insights

## 📞 Support

If you encounter issues:
1. Check Dokploy application logs
2. Verify health endpoints are responding
3. Test database and Redis connectivity
4. Review GitHub Actions build logs

---
*Generated with production best practices from Dokploy documentation*