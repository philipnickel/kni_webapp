# 🚀 Coolify Deployment Guide

**Fast, reliable Django + Wagtail deployment with zero-config setup**

This repo is optimized for **one-click Coolify deployment** with complete PostgreSQL + Redis stack and automatic baseline data loading.

## ✨ What's Automated

- 🔧 **Smart Configuration**: `PRIMARY_DOMAIN` auto-configures `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and `WAGTAILADMIN_BASE_URL`
- 🔒 **Production Security**: HTTPS redirect, HSTS headers, secure cookies, proxy SSL handling
- 💾 **Baseline Data**: Automatic database seeding with sample content and images
- 🏥 **Health Monitoring**: Built-in health checks for web, database, and Redis services  
- 📦 **Complete Stack**: PostgreSQL 15 + Redis 7 + Django app in one deployment

## 📋 Prerequisites

- ✅ Coolify instance running with domain access
- ✅ This GitHub repo connected to Coolify  
- ✅ DNS A/AAAA record pointing to your VPS IP

## ⚡ Quick Deploy (2 minutes)

### 1️⃣ Create Service
Coolify → **New Service** → Select this repo → **Use Docker Compose**

### 2️⃣ Configure Environment
Set only these **3 variables** (Coolify generates the secrets):

```bash
PRIMARY_DOMAIN=yourdomain.com
DJANGO_SECRET_KEY=          # Click "Generate" in Coolify UI  
DATABASE_PASSWORD=          # Click "Generate" in Coolify UI
REDIS_PASSWORD=             # Click "Generate" in Coolify UI
```

### 3️⃣ Attach Domain
Coolify → **Domains** → Add `yourdomain.com` → Enable **SSL (Let's Encrypt)**

### 4️⃣ Deploy & Access
- **Deploy**: Coolify builds and starts your complete stack automatically
- **Access**: `https://yourdomain.com/admin/` (login: `admin` / `admin123`)
- **Done!** Your site is live with sample content and images

## 🔧 Alternative: Dockerfile-only Deployment

**Advanced option** requiring external database services:

1. **Create App**: Coolify → New App → Deploy from Git Repository → select this repo (Dockerfile)
2. **Add Volumes**:
   - `/app/staticfiles`
   - `/app/media`
3. **Environment Variables**:
   ```bash
   DJANGO_SETTINGS_MODULE=project.settings
   DEBUG=false
   DJANGO_SECRET_KEY=          # Use Coolify's "Generate" button
   PRIMARY_DOMAIN=yourdomain.com
   DATABASE_URL=postgresql://user:pass@db-host:5432/dbname?sslmode=require
   REDIS_URL=redis://:password@redis-host:6379/0
   ```
4. **Domain Setup**: Attach domain and enable SSL
5. **Deploy**: Run migrations using post-deploy commands

## 📦 Stack Information

**Docker Compose deployment includes:**

- 🗄️ **PostgreSQL 15**: Internal access at `db:5432`
- ⚡ **Redis 7**: Internal access at `redis:6379`  
- 🌐 **Django App**: Exposed on port 8000 with health checks
- 💾 **Persistent Volumes**: 
  - `postgres_data` - Database storage
  - `redis_data` - Redis persistence  
  - `media_volume` - User uploads
  - `static_volume` - CSS/JS/Images

🔒 **Security**: Database and Redis are isolated on Docker's internal network

## 🤖 Post-Deploy Automation

**For Docker Compose**: Add to Coolify → Service → Post Deploy Command:
```bash
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput --clear
```

**For Dockerfile**: Use the included script:
```bash
sh docker/post_deploy.sh
```

✅ Enable "Run after deployment" to auto-apply migrations and collect static files

## 🚀 Production Features

- 📁 **Static Files**: Served by WhiteNoise, auto-collected during build
- 🖼️ **Media Files**: Persisted in Docker volumes with Coolify backup
- 🔐 **SSL**: Automatic Let's Encrypt certificates
- 🏥 **Health Checks**: Built-in monitoring at `/health/` endpoint  
- 📈 **Scaling**: Horizontal scaling available in Coolify UI
- 🔒 **Security**: All services on isolated internal network

## 💡 Best Practices

Based on production deployments, consider these improvements:

### **Security Configuration**
✅ **Already configured** - Your app includes production-ready security:
- HTTPS proxy headers for Coolify/Traefik integration
- HSTS headers with 1-year max-age and subdomain inclusion
- Content security and XSS protection
- Secure cookie configuration (SameSite, Secure flags)

### **Backup Strategy**
- **Automatic**: Coolify backs up Docker volumes daily
- **Manual**: Use `pg_dump` for database exports  
- **Media**: Consider external storage (S3) for production scaling

### **Environment Security**
- ✅ Use Coolify's built-in secret generation
- ✅ Never commit secrets to Git
- ✅ Rotate passwords periodically

## 🧪 Local Testing

**Test before deploying** with the dev stack:
```bash
make docker-up              # Start with baseline data
make docker-logs            # View logs
make docker-shell           # Access container shell  
make docker-down            # Stop stack
open http://localhost:8002  # View locally
```

## 🛠️ Troubleshooting

### **Service Issues**
- 🔴 **Won't start**: Check Coolify logs for each service (web, db, redis)
- 🔌 **Database failed**: Verify `DATABASE_PASSWORD` is set and containers communicate
- ⚡ **Redis failed**: Ensure `REDIS_PASSWORD` matches between services

### **Common Problems**
- 🌐 **502/Bad Gateway**: Check container health; ensure `/health/` responds 200
- 🔒 **CSRF failures**: Confirm `PRIMARY_DOMAIN` is correct (no http/https prefix)
- 👤 **Admin unavailable**: Ensure migrations ran and database is reachable
- 📁 **Static not loading**: Check volume mounting and build success

### **Quick Fixes**
- 🔄 **Reset database**: Delete `postgres_data` volume in Coolify and redeploy
- 📋 **View logs**: Coolify → Service → Logs (select container)
- 💾 **Access database**: Use Coolify's Execute Command for `psql`
- 🏥 **Health check**: Visit `https://yourdomain.com/health/` to test
