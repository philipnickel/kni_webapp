# KNI Webapp 🏗️

Modern multi-tenant construction business platform built with Django, Wagtail CMS, and Docker.

## 🚀 Quick Start

**Local Development:**
```bash
make dev-up            # Start development environment on http://localhost:8000
make dev-logs          # View development logs
make dev-shell         # Access container shell
make dev-status        # Check service health
make dev-reset         # Reset to baseline state
make dev-clean         # Clean development environment
```

**Legacy Commands (still supported):**
```bash
make up                # Alias for dev-up
make reset             # Alias for dev-reset
make clean             # Alias for dev-clean
```

**Production Deployment (Dokploy):**
- Copy `.env.dokploy` to `.env` and configure values
- Set `PRIMARY_DOMAIN`, `DJANGO_SECRET_KEY`, `DATABASE_PASSWORD`, `REDIS_PASSWORD`
- Deploy automatically with Traefik SSL
- Use `make dokploy-up` for Dokploy-optimized deployment

## 🏗️ Architecture

- **Framework**: Django 4.2 + Wagtail 7.1 CMS
- **Database**: PostgreSQL with schema-based multi-tenancy
- **Cache**: Redis for sessions and page caching
- **Frontend**: Tailwind CSS v4 with responsive design
- **Language**: Danish (da-DK) localization

```
├── apps/                    # Django applications
│   ├── core/               # Wagtail customization & themes
│   ├── pages/              # Homepage, gallery, contact pages
│   ├── projects/           # Project management & galleries
│   ├── contacts/           # Contact forms & submissions
│   └── tenants/            # Multi-tenant management
├── static/                 # CSS, JS, images
├── templates/              # HTML templates
├── media/                  # User uploads (images, documents)
├── project/                # Django settings & configuration
# Baseline data is now stored in backups/ using Django-native format
```

## 🎯 Access Points

### **Development Environment**
- **URL**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/
- **Login**: admin / admin123 (baseline data)
- **Gallery**: http://localhost:8000/galleri/ (project showcase with modals)

### **Health & Monitoring**
- **Health Check**: http://localhost:8000/health/
- **Detailed Health**: http://localhost:8000/health/detailed/
- **Readiness**: http://localhost:8000/health/ready/
- **Liveness**: http://localhost:8000/health/live/

## 🗄️ Database & Multi-tenancy

- **Type**: PostgreSQL (required for multi-tenancy)
- **Schemas**:
  - `public` - Super admin and tenant management
  - `johann` - JCleemannByg tenant data
- **Multi-tenancy**: Schema-based isolation using django-tenants

### Project Management
Projects are managed as **snippets** in Wagtail admin:
- **Admin**: http://localhost:8003/admin/snippets/projects/project/
- **No individual project pages** - cleaner structure and easier management

## 📦 Baseline Data System

The application uses a baseline data system for consistent deployments:

### Development Commands
```bash
make dev-up          # Start development environment
make dev-reset       # Reset to baseline data (wipes existing data)
make dev-baseline    # Update baseline from current state
make dev-clean       # Remove development containers and volumes
make dev-logs        # View development logs
make dev-shell       # Access container shell
make dev-status      # Check service health
```

### Production Commands
```bash
make prod-build      # Build production images
make prod-deploy     # Deploy production stack
make prod-logs       # View production logs
make prod-status     # Check production health
make prod-clean      # Clean production environment
```

### How it Works
- **Normal startup**: Uses existing data, no baseline loading
- **Reset**: Only loads baseline when database is empty
- **Baseline update**: Captures current state as new baseline
- **Production**: Automatic baseline loading on fresh deployments

### Structure
```
# baselineData/ - REMOVED: Now using Django-native backups in backups/
├── baseline.sql           # Complete database dump
└── media/
    ├── original_images/   # Clean original images
    └── images/           # Rendered images (auto-generated)
```

## 🚀 Production Features

### Performance Optimizations
- **Redis Caching**: Page, session, and query caching with configurable TTL
- **Static Files**: WhiteNoise compression with long-term caching
- **Database**: Connection pooling and SSL enforcement
- **Gunicorn**: Optimized worker configuration with health checks

### Security Enhancements
- **HTTPS**: Forced redirect with HSTS headers
- **Security Headers**: CSP, XSS protection, frame options
- **Sessions**: Redis-backed with secure cookies
- **Secret Management**: Auto-generation with environment fallbacks

### Monitoring & Health Checks
- `/health/` - Basic health check
- `/health/detailed/` - Comprehensive service health
- `/health/ready/` - Kubernetes readiness probe
- `/health/live/` - Kubernetes liveness probe

## 🐳 Docker & Development

### Unified Development Workflow
```bash
make help           # Show all available commands

# Development workflow
make dev-up         # Start development environment (http://localhost:8000)

# Production workflow
make prod-up        # Start production environment
make dokploy-up     # Start Dokploy-optimized production environment

# Data management
make load-baseline  # Load baseline backup (Django native restore)
make backup         # Create database backup (Django native JSON)
make baseline       # Create named 'baseline' backup

# Maintenance
make clean          # Clean up everything (preserves backups)
```

### Docker Architecture

**Development Setup (`docker-compose.dev.yml`)**:
- Live code reloading with volume mounting
- Django development server with auto-reload
- Exposed ports for database/Redis access
- Development debugging tools included

**Production Setup (`docker-compose.yml`)**:
- Multi-stage optimized builds
- Gunicorn WSGI server with performance tuning
- Security hardening and resource limits
- Dokploy/Traefik-compatible reverse proxy configuration
- External dokploy-network support

### Environment Variables

**Development** (`.env.local` - auto-configured):
```bash
WEB_EXPOSE_PORT=8000              # Standardized development port
DEBUG=True
DATABASE_NAME=kni_webapp_dev      # Separate dev database
WAGTAILADMIN_BASE_URL=http://localhost:8000
LOAD_BASELINE=false               # Preserve development data
```

**Production** (`.env` from `.env.dokploy` template):
```bash
PRIMARY_DOMAIN=your-domain.com         # Required: Your domain
DJANGO_SECRET_KEY=your-secret-key      # Required: Secure secret key
DATABASE_PASSWORD=secure-password     # Required: Database password
REDIS_PASSWORD=secure-redis-password   # Required: Redis password
LOAD_BASELINE=false                    # Load baseline on fresh deployment
```

**Legacy Coolify** (`.env` from `.env.production` template):
```bash
PRIMARY_DOMAIN=your-domain.com         # Required: Your domain
DJANGO_SECRET_KEY=your-secret-key      # Required: Secure secret key
DATABASE_PASSWORD=secure-password     # Required: Database password
REDIS_PASSWORD=secure-redis-password   # Required: Redis password
```

## 🌐 Deployment

### Dokploy (Recommended)
1. **Create Service**: Use docker-compose.yml
2. **Set Environment**: Copy `.env.dokploy` to `.env` and configure
3. **Configure Domain**: Set `PRIMARY_DOMAIN` in environment
4. **Deploy**: Complete stack with automatic SSL via Traefik
5. **Use Command**: `make dokploy-up` for optimized deployment

### Legacy Coolify Support
Legacy support available via `.env.production` configuration.

### Manual Deployment
1. **Build**: Multi-stage Docker build with optimizations
2. **Database**: PostgreSQL with SSL and connection pooling
3. **Cache**: Redis with persistence and authentication
4. **Health**: Built-in monitoring and readiness checks

### Post-Deploy Commands
```bash
# Docker Compose
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput --clear

# Dockerfile
sh docker/post_deploy.sh
```

## 🔧 Development Workflow

### Making Changes
1. Edit code locally
2. Test with `make up`
3. Check health with `make logs`
4. Reset data with `make reset` if needed

### Creating Baseline
1. Set up data in admin interface
2. Run `make baseline` to capture state
3. Baseline includes database + media files
4. New deployments use this baseline automatically

### Troubleshooting
```bash
make dev-logs       # View development logs (real-time)
make dev-shell      # Access development container shell
make dev-status     # Check all service health
make dev-clean      # Force cleanup and restart

# For production
make prod-logs      # View production logs
make prod-status    # Check production health
```

## 📊 Performance Targets

With production optimizations:
- **Page Load**: < 2 seconds
- **Database Response**: < 100ms
- **Cache Hit Ratio**: > 80%
- **Uptime**: > 99.5%
- **Security Score**: A+ headers rating

## 🔒 Security

### Built-in Security Features
- Multi-tenant schema isolation
- Automatic HTTPS redirect
- Secure session handling
- CSRF protection
- XSS protection headers
- Content Security Policy

### Environment Security
- Secret auto-generation in production
- Environment variable validation
- Database SSL enforcement
- Redis authentication

## 📱 Mobile & Accessibility

### Mobile Optimization
- Touch-friendly navigation (44px minimum)
- Responsive image loading
- Mobile-optimized forms
- Fast mobile page load times

### Accessibility Features
- Color contrast compliance (4.5:1 ratio)
- Keyboard navigation support
- Alt text for images
- Semantic HTML structure

## 🛠️ Scaling Recommendations

### Higher Traffic (10+ tenants)
- Increase Gunicorn workers: `GUNICORN_WORKERS=8`
- Add Redis clustering
- Implement CDN for static assets
- Consider database read replicas

### Better Performance
- Elasticsearch for Wagtail search
- Image optimization and WebP support
- API caching for dynamic content
- Async task processing with Celery

---

**Stack**: Django 4.2 • Wagtail 7.1 • PostgreSQL • Redis • Multi-tenant
**Language**: Danish (da-DK)
**Deployment**: Docker + Coolify with auto-SSL