# Dokploy Deployment Guide

This guide explains how to deploy the KNI Webapp to production using Dokploy with baseline data loading.

## Quick Start

### 1. Initial Deployment (With Baseline Data)

In Dokploy, set these environment variables:

```env
# Required
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@hostname:5432/database

# Domain
DOMAIN=yourdomain.com

# Baseline Loading (for first deployment)
LOAD_BASELINE_ON_START=true
BASELINE_BACKUP_FILE=baseline.json

# Optional
ADMIN_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=secure-password-here
```

### 2. Subsequent Deployments (Preserve Data)

Update the environment variable:

```env
# Disable baseline loading to preserve existing data
LOAD_BASELINE_ON_START=false
```

## Environment Variables Reference

### Required Variables
- `DJANGO_SECRET_KEY` - Django secret key for security
- `DATABASE_URL` - PostgreSQL connection string
- `DOMAIN` - Your domain name

### Baseline Loading Variables
- `LOAD_BASELINE_ON_START` - Set to `true` for initial deployment, `false` afterwards
- `BASELINE_BACKUP_FILE` - Baseline file name (default: `baseline.json`)

### Optional Variables
- `ADMIN_EMAIL` - Admin user email
- `DJANGO_SUPERUSER_EMAIL` - Superuser email
- `DJANGO_SUPERUSER_PASSWORD` - Superuser password
- `DEBUG` - Set to `false` for production (default)

## Deployment Workflow

### First Deployment
1. Create new Dokploy application
2. Set `LOAD_BASELINE_ON_START=true`
3. Configure other required environment variables
4. Deploy from GitHub
5. Verify baseline data loaded (check logs)
6. Update `LOAD_BASELINE_ON_START=false` for future deployments

### Updates
1. Update `LOAD_BASELINE_ON_START=false` (if not already)
2. Deploy from GitHub
3. Existing data preserved, only migrations run

## Verification

After deployment, check:

1. **Application Health**: Visit `https://yourdomain.com/health/ready/`
2. **Homepage**: Should show "JCleemann Byg" content (not generic Wagtail)
3. **Admin Panel**: `https://yourdomain.com/admin/`
4. **Logs**: Look for "✅ Baseline restored successfully" message

## Troubleshooting

### Deployment Fails
- Check Dokploy logs for error messages
- Verify all required environment variables are set
- Ensure database is accessible

### Baseline Not Loading
- Verify `LOAD_BASELINE_ON_START=true`
- Check container logs for baseline-related messages
- Ensure database is empty for initial deployment

### Generic Wagtail Content Shows
- Indicates baseline data wasn't loaded
- Check `LOAD_BASELINE_ON_START` setting
- Review container logs for errors

## Docker Configuration

The Dockerfile automatically:
- Includes baseline data at `/app/backups/`
- Configures entrypoint script for baseline loading
- Sets up proper health checks for Dokploy
- Optimizes for production performance

## Security Notes

- Never commit secrets to the repository
- Use Dokploy's environment variable system
- Generate strong `DJANGO_SECRET_KEY`
- Use secure database passwords
- Enable HTTPS in production (Dokploy handles this)

## Support

For issues or questions:
1. Check the container logs in Dokploy
2. Review the baseline loading documentation
3. Verify environment variable configuration
4. Test locally with `test_production_baseline.sh`