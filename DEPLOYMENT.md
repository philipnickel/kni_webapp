# Dokploy Deployment Guide

## Prerequisites

1. **Dokploy Server**: Running instance
2. **GitHub Repository**: This project pushed to GitHub

## Simple Setup Steps

### 1. Create Dokploy Application

**In Dokploy Dashboard:**
1. Click "Create Application"
2. Choose `Git Provider` as Source Type
3. Configure:
   - **Repository**: `https://github.com/your-username/kni_alt`
   - **Branch**: `main`
   - **Build Path**: `/kni_webapp`
   - **Dockerfile**: `Dockerfile`
   - **Port**: `80`
4. **Enable Auto Deploy** ✅

### 2. Set Environment Variables

Copy required values from `.env.dokploy`:
```
DJANGO_SECRET_KEY=your-super-secret-key-here-make-it-long-and-random-50-chars
DATABASE_PASSWORD=your_secure_production_password
REDIS_PASSWORD=your_secure_redis_password
PRIMARY_DOMAIN=jcleemannbyg.dk
DEBUG=False
ALLOWED_HOSTS=jcleemannbyg.dk,www.jcleemannbyg.dk,kni.dk,www.kni.dk
# ... add other required variables from .env.dokploy
```

### 3. Create Database & Redis Services

**PostgreSQL Database:**
1. Create new PostgreSQL service in Dokploy
2. Set database name, user, password (matching your env vars)
3. Note the service name for DATABASE_URL

**Redis Service:**
1. Create new Redis service in Dokploy
2. Set password (matching REDIS_PASSWORD)
3. Note the service name for REDIS_URL

### 4. Configure Domain & SSL

1. Add domain: `jcleemannbyg.dk`
2. Enable SSL certificate
3. Set application port to `80`

### 5. Deploy! 🚀

**That's it!** Now every push to main branch automatically deploys:
1. Push changes to GitHub
2. Dokploy detects changes
3. Builds Docker image
4. Deploys new version
5. Health checks verify success

## How It Works

```
git push origin main
     ↓
Dokploy detects changes
     ↓
Git clone → Docker build → Deploy → Health check
     ↓
✅ Live at jcleemannbyg.dk
```

## Loading Baseline Data

After successful deployment, you may need to load baseline/demo data into your production database.

### Method 1: Via Dokploy Terminal (Recommended)

1. **Access Dokploy Dashboard**
   - Navigate to: `http://your-dokploy-server:3000/dashboard/projects`
   - Find your project and click on the DjangoWebapp service

2. **Open Container Terminal**
   - Click "Open Terminal" button
   - Select the running container
   - Choose "Bash" tab

3. **Navigate and Execute**
   ```bash
   cd /app
   python manage.py native_restore --name baseline --include-media --flush
   ```

4. **Expected Output**
   ```
   📥 Django Native Restore System
   ========================================
   📁 Found backup: backups/baseline_20250915_141323.json
   🗑️  Flushing database for fresh start...
   ✅ Database flushed successfully
   🔧 Running migrations to recreate schema...
   ✅ Migrations completed
   📥 Restoring Django data from: backups/baseline_20250915_141323.json
   Installed 116 object(s) from 1 fixture(s)
   ✅ Django data restored successfully
   📁 Restoring media files...
   ✅ Media files restored successfully
   ✅ Django native restore completed successfully!
   ```

### Method 2: Via Makefile (Local Development)

If running locally with Docker Compose:
```bash
make load-baseline
```

### What Gets Loaded

The baseline data includes:
- **Wagtail Pages**: Homepage and site structure
- **Site Configuration**: Site name, domain settings
- **Admin Users**: Pre-configured admin accounts
- **Content**: Sample pages, images, and media files
- **Settings**: Theme and site preferences

### Notes

- **⚠️ Warning**: The `--flush` flag completely clears the database first
- **Backup Files**: Located in `backups/` directory in the container
- **Media Files**: Restored to `/app/media/` with `--include-media` flag
- **Docker Requirements**: The baseline backup files must be included in the Docker image via `.dockerignore` configuration

### Troubleshooting

**"No backup file found" Error:**
- Verify backup files are in the container: `ls -la /app/backups/`
- Check `.dockerignore` allows `!backups/baseline_*`
- Ensure Docker rebuild included the fixed `.dockerignore`

**Permission Errors:**
- Commands run as `app` user inside container
- Media directory should be writable: `/app/media/`

**Database Connection Issues:**
- Verify DATABASE_URL environment variable
- Check PostgreSQL service is running
- Test connection: `python manage.py check --database default`

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

## Quick Checklist

- [ ] Dokploy application created with Git Provider
- [ ] Auto-deploy enabled ✅
- [ ] Environment variables set
- [ ] PostgreSQL service created
- [ ] Redis service created
- [ ] Domain configured with SSL
- [ ] First deployment successful
- [ ] Baseline data loaded via Dokploy terminal
- [ ] Website functional with admin access

## Commands

### Test Locally
```bash
# Test production build
docker build --target production -t kni-webapp .
docker run -p 8000:80 kni-webapp
```

### Force Deploy
```bash
# Empty commit triggers auto-deploy
git commit --allow-empty -m "Deploy"
git push origin main
```

---
**That's it!** Simple, automatic deployments with just `git push`. 🎉