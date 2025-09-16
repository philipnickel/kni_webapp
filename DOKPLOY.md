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

## Management Commands

Available Django commands:
```bash
# Load baseline Wagtail data
python manage.py load_baseline_data

# Export baseline data
python manage.py export_baseline_data

# Create superuser
python manage.py createsuperuser
```

## Troubleshooting

- Check logs in Dokploy dashboard
- Health check available at `/health/ready/`
- Admin panel at `/admin/` (if admin user created)
- Static files served from `/static/`