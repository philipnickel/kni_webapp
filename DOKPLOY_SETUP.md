# Dokploy Deployment Setup Instructions

## Critical Configuration for Dokploy

### 1. Dokploy Project Settings

**Repository Configuration:**
- Repository URL: `https://github.com/philipnickel/kni_webapp`
- Branch: `main`
- Compose Path: `.dokploy/docker-compose.yml` ⚠️ **IMPORTANT: Use the Dokploy-specific compose file**

### 2. Environment Variables (Set in Dokploy UI)

**Required Environment Variables:**
```bash
DJANGO_SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DATABASE_PASSWORD=secure_database_password_here
REDIS_PASSWORD=optional_redis_password
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,72.60.81.210
```

**Database Configuration:**
```bash
DATABASE_NAME=kni_webapp
DATABASE_USER=kni_user
```

### 3. Port Configuration

**Critical Port Mapping:**
- **External Port**: 8000 (What you access via browser)
- **Container Port**: 80 (What the app serves on internally)
- **Mapping**: `8000:80` ⚠️ **This is configured in the Dokploy compose file**

### 4. Domain/Network Settings

**Access URL:** `http://72.60.81.210:8000`

**Health Check Endpoint:** `http://72.60.81.210:8000/health/ready/`

### 5. Key Differences from Main Compose File

The `.dokploy/docker-compose.yml` file has these critical differences:

1. **Port Mapping**: `8000:80` (not `8000:8000`)
2. **Target**: `production` (not `development`)
3. **Debug**: `false` (not `true`)
4. **Minimal Volumes**: Only essential volumes, no source code mounts
5. **Optimized Health Checks**: Tuned for production deployment

## Troubleshooting Previous Issues

### ✅ Fixed: Git Clone Directory Issue
- The deployment script handles directory cleanup
- Dokploy-specific configuration prevents conflicts

### ✅ Fixed: Port Mapping Issue
- Correct mapping: `8000:80`
- Production container serves on port 80 (Caddy)
- External access on port 8000

### ✅ Fixed: Target Environment Issue
- Uses `production` target (Caddy + Gunicorn + Supervisor)
- Not `development` target (Django dev server)

### ✅ Fixed: ALLOWED_HOSTS Issue
- Includes `72.60.81.210` in allowed hosts
- Proper domain configuration

## Deployment Steps

1. **Configure Dokploy Project:**
   - Set repository to `https://github.com/philipnickel/kni_webapp`
   - Set branch to `main`
   - **IMPORTANT**: Set compose path to `.dokploy/docker-compose.yml`

2. **Set Environment Variables:**
   - Add all required environment variables listed above
   - Generate a strong `DJANGO_SECRET_KEY` (50+ characters)

3. **Deploy:**
   - Click deploy in Dokploy
   - Monitor logs for any issues
   - Verify health check passes

4. **Verify Deployment:**
   ```bash
   # Should return "OK"
   curl http://72.60.81.210:8000/health/ready/

   # Should show the Django application
   curl http://72.60.81.210:8000/
   ```

## What Should Work Now

After following this setup:

1. **No more Git clone errors** - Handled by deployment configuration
2. **No more connection refused** - Correct port mapping (8000:80)
3. **No more 404 errors** - Proper ALLOWED_HOSTS configuration
4. **Successful health checks** - Optimized health check endpoints
5. **Accessible application** - Should be reachable at `http://72.60.81.210:8000`

## If Deployment Still Fails

Check these in order:

1. **Verify compose file path**: Must be `.dokploy/docker-compose.yml`
2. **Check environment variables**: All required vars must be set
3. **Monitor deployment logs**: Look for specific error messages
4. **Test health endpoint**: `curl http://72.60.81.210:8000/health/ready/`
5. **Check container logs**: `docker logs [container_name]`

## Emergency Rollback

If deployment fails:

1. Switch compose path back to `docker-compose.yml` (main file)
2. Set `DOCKER_TARGET=development`
3. Set `DEBUG=true`
4. This will use the development server on port 8000 directly