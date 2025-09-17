# Dokploy Deployment Guide

This project is configured for direct deployment with Dokploy using just the Dockerfile - no complex JSON configurations needed!

## Quick Start

1. **Import Repository** in Dokploy
2. **Point to Dockerfile**: `deployment/Dockerfile`
3. **Set Environment Variables** (see below)
4. **Deploy!**

## Required Environment Variables

Set these in your Dokploy application:

### Production (Required)
```bash
DJANGO_SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

### Optional
```bash
DOMAIN=yourdomain.com
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=your-admin-password
REDIS_URL=redis://localhost:6379/0
DEBUG=False
LOAD_BASELINE_ON_START=false  # Enable to restore bundled baseline (native_restore) on boot
BASELINE_BACKUP_FILE=baseline.json  # (Optional) Override which fixture to restore from /app/backups
```

## Configuration

- **Dockerfile**: `deployment/Dockerfile`
- **Port**: 8000 (auto-detected by Dokploy labels)
- **Health Check**: `/health/ready/` (auto-detected)
- **Build Target**: `production`

## Auto-Configuration

The deployment automatically:
- Generates Django secret key if missing (dev only)
- Configures domain settings
- Creates admin user if credentials provided
- Loads baseline Wagtail data
- Sets up health checks

## Database Setup

For PostgreSQL, use a connection string like:
```bash
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

Dokploy can provide managed PostgreSQL or you can use external services.

## Preview Deployments

Dokploy automatically creates preview deployments for branches. The application will work with any branch - just push and deploy!

## Baseline Data Workflow

The Docker image now ships with the contents of `deployment/baseline/` baked into `/app/backups/`. That package is produced with Django's native backup/restore commands, so it includes Wagtail pages, snippets, and media.

### Automatic Restore
- Set `LOAD_BASELINE_ON_START=true` (default `false`) to run `python manage.py native_restore --backup baseline.json --include-media --flush` during container start-up.
- Leave the flag `false` once a site has real data; toggling it back on will wipe the database and restore the bundled snapshot.
- Override `BASELINE_BACKUP_FILE` if you package multiple fixtures under `/app/backups/` and want a different default name.

### Updating the Bundled Baseline
1. Run `python manage.py native_backup --name baseline --include-media` locally (or in staging) to refresh the backup under `backups/`.
2. Execute `./deployment/scripts/update-baseline.sh` to copy the latest baseline JSON + media into `deployment/baseline/`.
3. Commit the updated files and trigger a new Dokploy build.

### Manual Restore Commands
```bash
# Restore bundled baseline (full reset)
python manage.py native_restore --backup baseline.json --include-media --flush --force

# Export current site state
python manage.py native_backup --name baseline --include-media

# Quick bootstrap helper
python manage.py setup_baseline
```

## Troubleshooting

- Check logs in Dokploy dashboard
- Health check available at `/health/ready/`
- Admin panel at `/admin/` (if admin user created)
- Static files served from `/static/`
