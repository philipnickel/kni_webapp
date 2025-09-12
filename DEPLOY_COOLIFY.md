# 🚀 KNI Webapp - Coolify Deployment Guide

Complete guide for deploying the KNI Webapp to multiple tenants using Docker + Coolify.

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [VPS Setup](#vps-setup) 
3. [Coolify Installation](#coolify-installation)
4. [First Tenant Deployment](#first-tenant-deployment)
5. [Adding New Tenants](#adding-new-tenants)
6. [Mass Updates](#mass-updates)
7. [Troubleshooting](#troubleshooting)

## 🏁 Quick Start

**For experienced users:**

1. **VPS**: Ubuntu 22.04 LTS with 2GB+ RAM
2. **Install Coolify**: `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`
3. **Deploy**: Add Git repo → Set domain → Deploy
4. **Configure**: Set env vars from `.env.example` → Redeploy

---

## 🖥️ VPS Setup

### Minimum Requirements
- **OS**: Ubuntu 22.04 LTS (recommended) 
- **RAM**: 2GB minimum, 4GB+ for production
- **Storage**: 20GB minimum, 40GB+ recommended
- **Network**: Public IP with ports 80, 443, 22 open

### Recommended Providers
- **Hostinger VPS**: €3.99/month, good for EU traffic
- **DigitalOcean**: $12/month for 2GB droplet
- **Hetzner**: €4.15/month for CX22 (EU-based)
- **Linode**: $12/month for 2GB Nanode

### Initial VPS Setup

```bash
# SSH into your VPS
ssh root@YOUR_VPS_IP

# Update system
apt update && apt upgrade -y

# Install essential tools
apt install -y curl wget git htop ufw

# Setup firewall (Coolify will manage Docker ports)
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

# Create non-root user (optional but recommended)
adduser deploy
usermod -aG sudo deploy
```

---

## 🐳 Coolify Installation

Coolify is a self-hostable alternative to Heroku/Netlify that makes Docker deployments effortless.

### One-Command Install

```bash
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
```

This installs:
- Docker & Docker Compose
- Coolify dashboard
- Traefik reverse proxy (for SSL & routing)

### Access Coolify Dashboard

1. **Open browser**: `http://YOUR_VPS_IP:8000`
2. **Create admin account** (first user becomes admin)
3. **Complete setup wizard**

### Coolify Dashboard Overview

- **Applications**: Your deployed apps
- **Databases**: PostgreSQL, Redis, etc.
- **Domains**: SSL certificates, routing
- **Settings**: Git connections, notifications

---

## 🎯 First Tenant Deployment

Let's deploy your first tenant (e.g., `jcleemannbyg.dk`):

### Step 1: Create Application

1. **Dashboard** → **Applications** → **+ New Application**
2. **Source**: GitHub (connect your account)
3. **Repository**: Select `philipnickel/kni_webapp`
4. **Branch**: `main`
5. **Application Name**: `jcleemann-byg`

### Step 2: Configure Build

1. **Build Settings**:
   - **Build Command**: `docker build --target production .`
   - **Dockerfile Path**: `/Dockerfile`
   - **Port**: `8000`

2. **Environment Variables** (click **+ Environment**):

```bash
# Core Django Settings
DJANGO_SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=jcleemannbyg.dk,www.jcleemannbyg.dk

# Database (Coolify will provide these)
DATABASE_NAME=kni_webapp
DATABASE_USER=kni_user  
DATABASE_PASSWORD=auto-generated-by-coolify

# Site Configuration
WAGTAILADMIN_BASE_URL=https://jcleemannbyg.dk
SECURE_SSL_REDIRECT=True

# Tenant Seeding (for first deployment)
SEED_TENANT_DATA=true
TENANT_SCHEMA=johann
TENANT_HOSTNAME=jcleemannbyg.dk
TENANT_ADMIN_USER=JCleemannByg
TENANT_ADMIN_PASSWORD=secure-admin-password
TENANT_ADMIN_EMAIL=admin@jcleemannbyg.dk
```

### Step 3: Add Database

1. **Applications** → Your app → **Resources** → **+ Add Resource**
2. **PostgreSQL 15**
3. **Database Name**: `kni_webapp`
4. **User**: `kni_user`
5. **Password**: Auto-generated (copy to env vars)

### Step 4: Add Domain & SSL

1. **Applications** → Your app → **Domains**
2. **+ Add Domain**: `jcleemannbyg.dk`
3. **SSL**: Automatic (Let's Encrypt)
4. **Add www redirect**: `www.jcleemannbyg.dk` → `jcleemannbyg.dk`

### Step 5: Deploy

1. **Deploy** button (builds Docker image & starts container)
2. **Monitor logs** during deployment
3. **Test site**: `https://jcleemannbyg.dk`
4. **Admin access**: `https://jcleemannbyg.dk/admin/`

---

## 🔄 Adding New Tenants

For each new customer, you'll replicate the setup:

### Quick Tenant Setup (15 minutes per tenant)

1. **New VPS** (or use existing with different ports)
2. **Install Coolify** (if new VPS)
3. **Clone application settings** from first tenant
4. **Update environment variables**:
   ```bash
   ALLOWED_HOSTS=newclient.dk,www.newclient.dk
   WAGTAILADMIN_BASE_URL=https://newclient.dk
   TENANT_SCHEMA=newclient
   TENANT_HOSTNAME=newclient.dk
   TENANT_ADMIN_EMAIL=admin@newclient.dk
   ```
5. **Add domain**: `newclient.dk`
6. **Deploy**

### Scaling Options

**Option A: One VPS per tenant** (simplest)
- Complete isolation
- Easy backup/restore per client
- €4-12/month per tenant

**Option B: Multiple tenants per VPS** (cost-effective)
- Use different ports: 8000, 8001, 8002...
- Shared database server
- €1-3/month per tenant

---

## 📦 Mass Updates

The beauty of this setup: **one git push updates all tenants**.

### Automatic Updates (Recommended)

1. **Enable Auto-Deploy** in each Coolify app:
   - **Applications** → App → **Settings** → **Auto Deploy**: ON
   - **Branch**: `main`
   - **Webhook**: Automatically created

2. **Push to main branch**:
   ```bash
   git add .
   git commit -m "Update feature X"
   git push origin main
   ```

3. **All tenants rebuild & deploy automatically** (5-10 minutes)

### Manual Updates

If you prefer control:

1. **Dashboard** → **Applications**
2. **Deploy** button on each app
3. Or use Coolify CLI for batch operations

### Rolling Updates with Zero Downtime

Coolify automatically handles:
- Health checks during deployment
- Rolling updates (old container runs until new one is healthy)
- Rollback if deployment fails

---

## 🛠️ Advanced Configuration

### Custom Nginx (Optional)

If you need custom routing/caching:

```bash
# docker/nginx.conf
server {
    listen 80;
    server_name _;
    
    location /static/ {
        alias /app/staticfiles/;
        expires 1y;
    }
    
    location /media/ {
        alias /app/media/;
        expires 30d;
    }
    
    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
    }
}
```

Then update `docker-compose.yml` to use `--profile nginx`.

### Background Tasks (Celery)

Enable worker & beat services:

```bash
# In Coolify app settings, add:
ENABLE_WORKER=true
ENABLE_BEAT=true
```

Coolify will start additional containers for background processing.

### External Database

For high-traffic tenants, use managed databases:

```bash
# Environment variables
DATABASE_URL=postgresql://user:pass@external-db.com:5432/dbname
REDIS_URL=redis://:pass@external-redis.com:6379/0
```

---

## 🔍 Monitoring & Backups

### Built-in Monitoring

Coolify provides:
- **Application metrics**: CPU, RAM, disk usage
- **Deployment history**: Previous versions, rollback options
- **Health checks**: Automatic restart if app crashes
- **Log aggregation**: Centralized logging

### Database Backups

```bash
# Automatic daily backups (in Coolify dashboard)
Databases → Your DB → Backups → Schedule
```

### External Monitoring (Optional)

- **Uptime monitoring**: UptimeRobot, Pingdom
- **Error tracking**: Sentry (add `SENTRY_DSN` to env vars)
- **Performance**: New Relic, DataDog

---

## 🚨 Troubleshooting

### Common Issues

**1. Build fails with "out of space"**
```bash
# SSH into VPS, clean Docker
docker system prune -af
docker volume prune -f
```

**2. Database connection errors**
```bash
# Check database container logs
docker logs kni_webapp_db_1

# Test connection
docker exec -it kni_webapp_db_1 psql -U kni_user -d kni_webapp
```

**3. SSL certificate issues**
```bash
# Force SSL renewal in Coolify dashboard
Domains → Your domain → Renew Certificate
```

**4. Site shows "502 Bad Gateway"**
- Check application logs in Coolify
- Verify health check endpoint: `/health/`
- Ensure port 8000 is exposed in Dockerfile

### Logs & Debugging

```bash
# Application logs
docker logs container_name

# Database logs  
docker logs kni_webapp_db_1

# System resources
htop
df -h
```

### Performance Optimization

**For high-traffic sites:**

1. **Increase resources**:
   ```yaml
   # docker-compose.yml
   services:
     web:
       deploy:
         resources:
           limits:
             memory: 1G
             cpus: '1.0'
   ```

2. **Enable Redis caching** in Django settings
3. **Use CDN** for static files (Cloudflare)
4. **Database optimization** (connection pooling, read replicas)

---

## 🎉 Success Metrics

After deployment, you should have:

- ✅ **Sub-5 minute deployments** for updates
- ✅ **Automatic SSL certificates** for all domains  
- ✅ **Zero-downtime updates** with rollback capability
- ✅ **Isolated tenant data** (no cross-contamination)
- ✅ **Scalable architecture** (add tenants in 15 minutes)
- ✅ **Cost-effective hosting** (€3-12/month per tenant)

---

## 📞 Support

**Coolify Documentation**: https://coolify.io/docs  
**Django Issues**: Check application logs  
**Database Issues**: PostgreSQL container logs  
**DNS/SSL Issues**: Cloudflare or domain registrar settings

---

**🚢 Happy Deploying!**

This setup scales from 1 to 100+ tenants with the same simple workflow. Push code → all tenants update. Perfect for multi-tenant SaaS!