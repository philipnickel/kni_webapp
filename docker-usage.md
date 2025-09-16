# Docker Compose Usage Guide

This project uses a unified `docker-compose.yml` configuration that works for both development and production environments through environment variables.

## Quick Start

### Development Mode (Default)
```bash
# Start all development services (includes Node.js and Mailhog)
docker-compose --profile dev up -d

# Start only core services (no Node.js/Mailhog)
docker-compose up -d web db redis
```

### Production Mode
```bash
# Set production environment
export ENV_FILE=.env.prod

# Start production services
docker-compose up -d

# Or directly specify environment file
docker-compose --env-file .env.prod up -d
```

### Dokploy Deployment
```bash
# Dokploy will automatically use the unified compose with .env.prod
# No manual commands needed - handled by the platform
```

## Environment Files

### `.env.dev` - Development Configuration
- Uses development Docker target with hot reload
- Includes Node.js service for CSS building
- Includes Mailhog for email testing
- Debug mode enabled
- Ports configured to avoid conflicts (8001, 5433, 6380)

### `.env.prod` - Production Configuration
- Uses production Docker target with optimized builds
- Production-hardened security settings
- Standard ports (80, 5432, 6379)
- Minimal resource usage
- Health checks optimized for monitoring

## Service Profiles

### Development Profile (`--profile dev`)
Includes development-only services:
- `node`: Node.js for Tailwind CSS building
- `mailhog`: Email testing interface

### Production Profile (default)
Core services only:
- `web`: Django application with Caddy
- `db`: PostgreSQL database
- `redis`: Redis cache

## Port Mappings

### Development (.env.dev)
- Web: `8001:8000` (Django dev server)
- Database: `5433:5432` (avoid PostgreSQL conflicts)
- Redis: `6380:6379` (avoid Redis conflicts)
- Node: `3000:3000` (Tailwind watcher)
- Mailhog UI: `8025:8025`
- Mailhog SMTP: `1025:1025`

### Production (.env.prod)
- Web: `80:80` (Caddy + Gunicorn)
- Database: `5432:5432` (standard PostgreSQL)
- Redis: `6379:6379` (standard Redis)

## Common Commands

### Development Workflow
```bash
# Full development stack with hot reload
docker-compose --profile dev up -d

# View logs
docker-compose logs -f web

# Run Django commands
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic

# Rebuild after code changes
docker-compose build web
docker-compose up -d web
```

### Production Testing
```bash
# Test production build locally
ENV_FILE=.env.prod docker-compose build web
ENV_FILE=.env.prod docker-compose up -d

# Health checks
curl http://localhost/health/ready/
```

### Database Operations
```bash
# Database migrations
docker-compose exec web python manage.py migrate

# Create database backup
docker-compose exec db pg_dump -U wagtail wagtail_dev > backup.sql

# Restore database backup
cat backup.sql | docker-compose exec -T db psql -U wagtail wagtail_dev
```

### Cleanup
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (⚠️  destroys data)
docker-compose down -v

# Remove unused images
docker image prune -f
```

## Environment Variable Override

You can override any environment variable:

```bash
# Override single variables
WEB_PORT=9000 docker-compose up -d

# Use different environment file
docker-compose --env-file .env.staging up -d

# Mix environment files
ENV_FILE=.env.prod WEB_PORT=8080 docker-compose up -d
```

## Troubleshooting

### Port Conflicts
If you get port binding errors:
```bash
# Check what's using the port
lsof -i :8001

# Use different ports
WEB_PORT=8002 docker-compose up -d
```

### Permission Issues
```bash
# Fix volume permissions
docker-compose exec web chown -R app:app /app/media /app/logs
```

### Database Connection Issues
```bash
# Verify database is healthy
docker-compose exec db pg_isready -U wagtail

# Reset database
docker-compose down db
docker volume rm kni_webapp_dev_db_data
docker-compose up -d db
```

### Container Not Starting
```bash
# Check container logs
docker-compose logs web

# Debug container interactively
docker-compose run --rm web bash
```

## Integration with CI/CD

### GitHub Actions Example
```yaml
- name: Test Docker Build
  run: |
    ENV_FILE=.env.prod docker-compose build
    docker-compose run --rm web python manage.py test
```

### Dokploy Deployment
The `dokploy-template.yml` automatically:
- References the unified `docker-compose.yml`
- Uses `.env.prod` configuration
- Handles secret generation
- Manages persistent volumes
- Sets up health monitoring