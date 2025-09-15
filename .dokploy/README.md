# Dokploy Deployment Configuration

This directory contains Dokploy-specific configuration files for deploying the KNI Webapp.

## Files

- `docker-compose.yml` - Dokploy-optimized Docker Compose configuration
- `.env` - Environment variables for Dokploy deployment
- `deploy.sh` - Pre-deployment script to handle common issues
- `README.md` - This documentation

## Deployment Configuration

### Port Mapping
- **External Port**: 8000 (Dokploy access)
- **Internal Port**: 80 (Caddy web server)
- **Mapping**: `8000:80`

### Services
- **Web**: Django/Wagtail application with Caddy reverse proxy
- **Database**: PostgreSQL 15
- **Cache**: Redis 7

### Environment
- **Mode**: Production
- **Debug**: Disabled
- **Target**: production (uses Caddy + Gunicorn via supervisor)

## Dokploy Setup Instructions

1. **Repository Configuration**
   - Repository: `github.com/philipnickel/kni_webapp`
   - Branch: `main`
   - Compose Path: `.dokploy/docker-compose.yml`

2. **Environment Variables** (Set in Dokploy UI)
   ```
   DJANGO_SECRET_KEY=your-secret-key-here
   DATABASE_PASSWORD=secure-password
   ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,72.60.81.210
   ```

3. **Domain Configuration**
   - External URL: `http://72.60.81.210:8000`
   - Health Check: `http://72.60.81.210:8000/health/ready/`

## Troubleshooting

### Git Clone Issues
- The `deploy.sh` script handles Git directory conflicts
- Dokploy sometimes fails when destination directories exist

### Port Issues
- Ensure port 8000 is mapped to container port 80
- Production uses Caddy on port 80, not Django dev server on 8000

### Service Health
- Database health check: `pg_isready`
- Redis health check: `redis-cli ping`
- Web health check: `curl http://localhost:80/health/ready/`

### Volume Mounts
- Only essential volumes are mounted in production
- No source code volumes (code is baked into the image)
- Media, logs, and backups volumes only

## Verification Steps

After deployment:

1. Check service status:
   ```bash
   docker-compose -f .dokploy/docker-compose.yml ps
   ```

2. Check logs:
   ```bash
   docker-compose -f .dokploy/docker-compose.yml logs web
   ```

3. Test health endpoint:
   ```bash
   curl http://72.60.81.210:8000/health/ready/
   ```

4. Test main application:
   ```bash
   curl http://72.60.81.210:8000/
   ```

## Common Issues

### Connection Refused
- Check port mapping (8000:80)
- Verify Caddy is running inside container
- Check supervisor logs

### 404 Errors
- Verify ALLOWED_HOSTS includes `72.60.81.210`
- Check Django URL configuration
- Verify static files are collected

### Database Errors
- Check PostgreSQL container health
- Verify DATABASE_URL environment variable
- Check migration status