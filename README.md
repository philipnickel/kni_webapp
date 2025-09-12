# KNI Webapp 🏗️

Modern multi-tenant construction business platform built with Django, Wagtail CMS, and Docker.

## 🚀 Quick Start

**Local Development:**
```bash
make setup    # Install dependencies & setup database  
make run      # Start development server
```

**Docker Production:**
```bash
cp .env.example .env      # Configure environment
docker-compose up -d      # Start all services
```

**Deploy to Coolify:** See [DEPLOY_COOLIFY.md](DEPLOY_COOLIFY.md)

## Access Points

### **Super Admin (Public Schema)**
- **URL:** http://localhost:8000/django-admin/
- **Login:** `admin` / `admin123`
- **Purpose:** Manage tenants and global settings

### **Tenant Admin (JCleemannByg)**
- **URL:** http://johann.localhost:8000/admin/
- **Login:** `JCleemannByg` / `admin123`
- **Purpose:** Manage construction business content

### **Public Website**
- **URL:** http://johann.localhost:8000/
- **Purpose:** Public-facing construction business site

## Login Troubleshooting

If you can't log in:

1. **Make sure the server is running:** `make run`
2. **Use the correct URLs:**
   - Super admin: http://localhost:8000/django-admin/
   - Tenant admin: http://johann.localhost:8000/admin/
3. **Clear browser cache** (Ctrl+F5 or Cmd+Shift+R)
4. **Check you're using the right credentials:**
   - Super admin: `admin` / `admin123`
   - Tenant admin: `JCleemannByg` / `admin123`
5. **If still having issues, reset the admin user:**
   ```bash
   python manage.py shell -c "
   from django.contrib.auth.models import User
   from django_tenants.utils import schema_context
   
   # Reset super admin
   admin = User.objects.get(username='admin')
   admin.set_password('admin123')
   admin.save()
   
   # Reset tenant admin
   with schema_context('johann'):
       tenant_admin = User.objects.get(username='JCleemannByg')
       tenant_admin.set_password('admin123')
       tenant_admin.save()
   
   print('Passwords reset to admin123')
   "
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
make setup          # One-time setup (install deps, migrate)
make run            # Start development server on port 8000
make run PORT=3000  # Start server on custom port
make admin          # Create new admin user
make reset-db       # Reset database completely
make clean          # Remove generated files
make migrate-public # Run public schema migrations
make migrate-tenants # Run tenant schema migrations
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

**Multi-stack deployment options:**
- **Docker Compose**: Full-stack local development & testing
- **Coolify**: One-click production deployment with auto-SSL
- **Kubernetes**: Enterprise-scale with Helm charts (coming soon)

**Production Features:**
- ✅ Multi-stage Docker builds (optimized for size & security)
- ✅ PostgreSQL + Redis for performance & caching  
- ✅ Health checks & auto-restart capabilities
- ✅ GitHub Actions CI/CD with security scanning
- ✅ Multi-tenant isolation with separate schemas
- ✅ Auto-SSL certificates via Let's Encrypt (Coolify)

**Scaling:**
- **1-10 tenants**: Single VPS with Coolify (€4-12/month total)
- **10+ tenants**: Multi-VPS with load balancer
- **Enterprise**: Kubernetes cluster with auto-scaling

---

**Stack:** Django 4.2 • Wagtail 7.1 • PostgreSQL • Multi-tenant  
**Language:** Danish (da-DK)  
**Database:** PostgreSQL with schema-based tenancy