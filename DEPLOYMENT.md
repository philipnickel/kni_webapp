# Dokploy Deployment Guide (Git Provider)

## Prerequisites

1. **Dokploy Server**: Running instance with API access
2. **GitHub Repository**: This project pushed to GitHub

## Setup Steps

### 1. GitHub Secrets Configuration (Optional)
Add these secrets in GitHub: Settings → Secrets and variables → Actions → New repository secret

```
DOKPLOY_URL=https://your-dokploy-domain.com
DOKPLOY_API_KEY=your-dokploy-api-key
DOKPLOY_APPLICATION_ID=your-application-id
```

*Note: GitHub Action is optional - Dokploy can auto-deploy on git pushes*

#### Getting Dokploy API Key:
1. In Dokploy dashboard → Settings → API Keys
2. Generate new API key
3. Copy the key

### 2. Dokploy Application Setup

1. **Create Application** in Dokploy:
   - Source Type: `Git Provider`
   - Repository: `https://github.com/your-username/kni_alt`
   - Branch: `main`
   - Build Path: `/kni_webapp`
   - Dockerfile: `Dockerfile`
   - Port: `80`

2. **Environment Variables** (copy from `.env.dokploy`):
   ```
   DJANGO_SECRET_KEY=your-super-secret-key-here-make-it-long-and-random-50-chars
   DATABASE_PASSWORD=your_secure_production_password
   REDIS_PASSWORD=your_secure_redis_password
   PRIMARY_DOMAIN=jcleemannbyg.dk
   DEBUG=False
   ALLOWED_HOSTS=jcleemannbyg.dk,www.jcleemannbyg.dk,kni.dk,www.kni.dk
   # ... add other required variables from .env.dokploy
   ```

3. **Domain Configuration**:
   - Add domain: `jcleemannbyg.dk`
   - Configure SSL certificate
   - Set port to `80`

### 3. Database & Redis Setup

Create companion services in Dokploy:

1. **PostgreSQL Database**:
   - Create new PostgreSQL service
   - Set database name, user, password (matching your env vars)
   - Note the internal service name for DATABASE_URL

2. **Redis Service**:
   - Create new Redis service
   - Set password (matching REDIS_PASSWORD)
   - Note the internal service name for REDIS_URL

### 4. Deployment Options

#### Option A: Auto-Deploy (Recommended)
1. Enable "Auto Deploy" in Dokploy application settings
2. Push to main branch → Dokploy automatically rebuilds and deploys

#### Option B: Manual Deploy
1. Push changes to GitHub
2. Go to Dokploy application → Click "Deploy"

#### Option C: GitHub Action Deploy (Optional)
1. Configure GitHub secrets (see step 1)
2. Push to main → GitHub Action triggers Dokploy API

## Workflow Overview

1. **Push to main** → Dokploy detects changes
2. **Git clone** → Dokploy pulls latest code
3. **Docker build** → Uses your Dockerfile (production target)
4. **Deploy** → New container replaces old one
5. **Health check** → Verifies deployment success

## Health Checks

The application includes:
- **Health endpoint**: `/health/ready/`
- **Docker health check**: Built into container
- **Dokploy monitoring**: Automatic rollback on failure

## Troubleshooting

### Build Issues
- Check Dokploy build logs
- Verify Dockerfile builds locally: `docker build --target production .`
- Check build path is correct (`/kni_webapp`)

### Deployment Issues
- Check Dokploy deployment logs
- Verify environment variables are set
- Test database/Redis connectivity
- Check domain/SSL configuration

### Application Issues
- Monitor application logs in Dokploy
- Check health endpoint: `curl https://yourdomain.com/health/ready/`
- Verify static files serving
- Test database migrations

## Production Checklist

- [ ] GitHub repository accessible
- [ ] Dokploy application created (Git Provider)
- [ ] Environment variables set
- [ ] PostgreSQL service created and connected
- [ ] Redis service created and connected
- [ ] Domain configured with SSL
- [ ] First deployment successful
- [ ] Health checks passing
- [ ] Auto-deploy enabled

## Commands

### Local Testing
```bash
# Test production build locally
docker build --target production -t kni-webapp .
docker run -p 8000:80 kni-webapp

# Test with environment file
docker run --env-file .env.dokploy -p 8000:80 kni-webapp
```

### Force Redeploy
```bash
# Option 1: Empty commit
git commit --allow-empty -m "Trigger deployment"
git push origin main

# Option 2: Manual deploy in Dokploy dashboard
# Go to application → Deploy button
```