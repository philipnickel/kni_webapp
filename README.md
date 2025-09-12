# KNI Webapp 🏗️

Modern multi-tenant construction business platform built with Django, Wagtail CMS, and Docker.

## 🚀 Quick Start

**Docker Development:**
```bash
make docker-up            # Start application on http://localhost:8002
make docker-logs          # View logs  
make docker-down          # Stop
make force-clean          # Force cleanup (kills port conflicts)
```

**Deploy to Coolify:** See [DEPLOY_COOLIFY.md](DEPLOY_COOLIFY.md)

## Access Points

### **Wagtail Admin**  
- **URL:** http://localhost:8002/admin/
- **Login:** admin / admin123 (from baseline data)
- **Purpose:** Manage content, projects, and site settings

### **Public Website**
- **URL:** http://localhost:8002/ 
- **Purpose:** Public-facing construction business site

## Project Management

Projects are managed as **snippets** in Wagtail admin (not individual pages):

- **Admin:** http://localhost:8002/admin/snippets/projects/project/
- **Gallery:** http://localhost:8002/galleri/ (shows all projects with modal popups)
- **No individual project pages** - cleaner structure and easier management

### Initial Setup (One-time only)
See [IMPORT_PROCESS.md](IMPORT_PROCESS.md) for importing stock projects.

## Baseline Data System

The application uses a baseline data system for clean deployments:

### **Commands:**
```bash
make docker-up              # Normal startup (preserves existing data)
make docker-up-baseline     # Start with baseline data (wipes existing data)
make clean-data             # Reset to clean baseline state
make update-baseline        # Update baseline from current state
```

### **Baseline Structure:**
```
baselineData/
├── baseline.sql           # Complete database dump
└── media/
    ├── original_images/   # Clean original images (7 files)
    └── images/           # Rendered images (auto-generated)
```

### **How it works:**
- **Normal startup**: Uses existing data, no baseline loading
- **Baseline startup**: Only loads baseline when `LOAD_BASELINE=true` and database is empty
- **Clean data**: Removes all volumes and data, ready for fresh baseline
- **Update baseline**: Captures current state as new baseline

## Login Troubleshooting

If you can't access admin areas:

1. **Make sure the application is running:** `make docker-up`
2. **Use the correct URLs:**
   - Super admin: http://localhost:8001/django-admin/
   - Tenant admin: http://johann.localhost:8001/admin/
3. **Clear browser cache** (Ctrl+F5 or Cmd+Shift+R)
4. **Check Docker logs:** `make docker-logs`
5. **If admin access is needed, shell into container:**
   ```bash
   make docker-shell
   # Then inside container:
   python manage.py createsuperuser
   ```

## Features

- **Multi-tenant Architecture** - Isolated tenant schemas
- **Project Gallery** - Construction work showcase with image galleries
- **Wagtail CMS** - User-friendly content management
- **Contact Forms** - Quote requests and inquiries
- **Responsive Design** - Mobile-friendly interface
- **Danish Language** - Localized for Danish market
- **PostgreSQL Database** - Production-ready database

## Development Commands

```bash
make help           # Show all available commands
make docker-up      # Start application with baseline data
make docker-down    # Stop application  
make docker-logs    # View application logs
make docker-shell   # Shell into web container
make create-baseline # Update baseline data
make clean          # Remove generated files
```

## Architecture

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
└── requirements.txt        # Python dependencies
```

## Database

- **Type:** PostgreSQL (required for multi-tenancy)
- **Schemas:** 
  - `public` - Super admin and tenant management
  - `johann` - JCleemannByg tenant data
- **Multi-tenancy:** Schema-based isolation using django-tenants

## Admin Features

- **Custom Branding** - Construction business theme
- **Project Management** - Image galleries and project showcases
- **Content Management** - Easy page editing with Wagtail
- **User Management** - Separate admin for each tenant
- **Media Library** - Image and document management

## 🐳 Docker & Production

**Development & Deployment:**
- **Local Development**: `make docker-up` (with baseline data)
- **Production Deployment**: Coolify with auto-SSL

### Database bootstrap strategy

- `baselineData/baseline.sql` is a full PostgreSQL dump used to quickly bootstrap an empty database. When the web container starts, `docker/entrypoint.sh` checks if the database has zero tables and, if `LOAD_BASELINE=true`, restores this dump automatically.
- The previous `docker/init-db.sql` helper (extensions/timezone) has been removed to avoid confusion. If you ever need DB init scripts on first boot, mount them under `/docker-entrypoint-initdb.d/` in the `db` service.

To force a fresh bootstrap from the baseline dump:

```bash
make clean
LOAD_BASELINE=true make docker-up
```

**Production Features:**
- ✅ Multi-stage Docker builds (optimized for size & security)
- ✅ PostgreSQL + Redis for performance & caching  
- ✅ Health checks & auto-restart capabilities
- ✅ GitHub Actions CI/CD with security scanning
- ✅ Multi-tenant isolation with separate schemas
- ✅ Auto-SSL certificates via Let's Encrypt (Coolify)
- ✅ Baseline data loading for consistent environments

**Scaling:**
- **1-10 tenants**: Single VPS with Coolify (€4-12/month total)
- **10+ tenants**: Multi-VPS with load balancer
- **Enterprise**: Kubernetes cluster with auto-scaling

---

**Stack:** Django 4.2 • Wagtail 7.1 • PostgreSQL • Multi-tenant  
**Language:** Danish (da-DK)  
**Database:** PostgreSQL with schema-based tenancy
