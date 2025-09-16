# KNI Webapp - JCleemann Byg

Django/Wagtail CMS webapp for construction company with SaaS deployment capabilities.

## Quick Start

### Development
```bash
# Setup development environment
make dev-setup

# Daily development
make dev

# View logs
make dev-logs

# Access shell
make dev-shell
```

**Access:**
- App: http://localhost:8000
- Admin: http://localhost:8000/admin (admin/admin123)
- Mailhog: http://localhost:8025

### Production Deployment

**SaaS Deployment (Zero-config):**
```bash
# Deploy to Dokploy with auto-configuration
make saas-deploy DOMAIN=yourdomain.com ADMIN_EMAIL=admin@yourdomain.com
```

**Preview Deployment:**
```bash
# Create isolated preview environment
make saas-preview PREVIEW_ID=feature-branch
```

## Tech Stack

- **Backend:** Django 5.0 + Wagtail CMS
- **Frontend:** Tailwind CSS + Preline UI
- **Database:** PostgreSQL
- **Cache:** Redis
- **Deployment:** Dokploy (Docker Compose)
- **Email:** SMTP (Mailhog for dev)

## Key Features

- ✅ **SaaS Ready:** Zero-configuration deployment
- ✅ **Preview Deployments:** Isolated environments for testing
- ✅ **Auto-setup:** Automatic secret generation and configuration
- ✅ **Project Gallery:** Showcase construction projects
- ✅ **Contact Forms:** Lead generation with email notifications
- ✅ **Admin Panel:** Full Wagtail CMS for content management
- ✅ **Responsive Design:** Mobile-first with Tailwind CSS

## Project Structure

```
├── src/                 # Source code
│   ├── backend/         # Django backend
│   │   ├── apps/        # Django apps (core, pages, projects, contacts)
│   │   └── project/     # Django project settings
│   ├── frontend/        # Frontend assets
│   │   ├── templates/   # HTML templates
│   │   ├── static/      # Static files (CSS/JS)
│   │   ├── package.json # Node.js dependencies
│   │   └── tailwind.config.js # Tailwind configuration
│   └── docs/           # Documentation
├── deployment/          # Deployment configuration
│   ├── Dockerfile      # Multi-stage Docker build
│   ├── compose.dev.yml # Development Docker Compose
│   ├── dokploy-template.yml # Production deployment template
│   ├── environments/   # Environment templates
│   └── scripts/        # Deployment scripts
├── Makefile            # Project commands
├── manage.py           # Django management
└── requirements.txt    # Python dependencies
```

## Environment Variables

**Required for SaaS:**
- `DOMAIN` - Your domain (optional, auto-generates if not provided)
- `ADMIN_EMAIL` - Admin user email

**Auto-generated if not provided:**
- `DJANGO_SECRET_KEY`
- `DATABASE_PASSWORD`
- `REDIS_PASSWORD`

## Commands

```bash
# Development
make dev-setup          # Full development setup
make dev                # Start development services
make dev-logs           # View logs
make dev-shell          # Access container shell
make dev-stop           # Stop services
make dev-clean          # Clean up

# Production
make saas-deploy        # Deploy to Dokploy
make saas-preview       # Create preview deployment
make build              # Build production image
make deploy             # Deploy to production

# Data management
make backup             # Create backup
make restore            # Restore from backup
make migrate            # Run migrations
make collectstatic      # Collect static files
```

## License

Private - JCleemann Byg