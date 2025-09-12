# KNI Webapp 🏗️

Modern multi-tenant construction business platform built with Django, Wagtail CMS, and Docker.

## 🚀 Quick Start

**Docker Development:**
```bash
make docker-up            # Start application on http://localhost:8001
make docker-logs          # View logs  
make docker-down          # Stop
```

**Deploy to Coolify:** See [DEPLOY_COOLIFY.md](DEPLOY_COOLIFY.md)

## Access Points

### **Super Admin (Public Schema)**  
- **URL:** http://localhost:8001/django-admin/
- **Login:** From baseline data
- **Purpose:** Manage tenants and global settings

### **Tenant Admin (JCleemannByg)**
- **URL:** http://johann.localhost:8001/admin/  
- **Login:** From baseline data
- **Purpose:** Manage construction business content

### **Public Website**
- **URL:** http://localhost:8001/ 
- **Purpose:** Public-facing JCleemannByg construction business site

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
