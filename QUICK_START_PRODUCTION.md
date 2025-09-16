# 🚀 Quick Start: Production Deployment

## ✅ What's Ready
- ✅ **CI/CD Pipeline**: GitHub Actions building Docker images
- ✅ **Production Dockerfile**: Optimized with health checks
- ✅ **Docker Image**: Available at `ghcr.io/philipnickel/kni_webapp:latest`
- ✅ **Health Endpoints**: `/health/ready/` for Dokploy monitoring

## 🎯 Quick Fix for 502 Error

**The main issue is a port mismatch. Here's the instant fix:**

1. **Go to Dokploy**: https://72.60.81.210:3000/
2. **Edit Domain**: `jcleemannbyg.dk`
3. **Change Port**: `80` → `8000` ⭐
4. **Save & Deploy**

**That's it!** The 502 error should be fixed immediately.

## 🔧 Full Production Setup (5 minutes)

### 1. Create GitHub Personal Access Token
```bash
# Go to: https://github.com/settings/tokens/new
# Name: "Dokploy Production"
# Scope: ✅ packages:read
# Copy the generated token
```

### 2. Update Dokploy Application
1. **Source Type**: Git Provider → **Docker**
2. **Docker Image**: `ghcr.io/philipnickel/kni_webapp:latest`
3. **Registry**: `ghcr.io`
4. **Username**: `philipnickel`
5. **Password**: [Paste your GitHub token]

### 3. Configure Domain (Critical!)
- **Container Port**: `8000` (not 80!)
- **HTTPS**: Enabled
- **Certificate**: Let's Encrypt

### 4. Set Health Check
**Advanced → Swarm Settings:**
```bash
curl --fail http://localhost:8000/health/ready/ || exit 1
```

### 5. Deploy & Test
```bash
# Deploy in Dokploy UI, then test:
curl https://jcleemannbyg.dk/health/ready/
```

## 🎉 Benefits
- **Zero-downtime deployments**
- **Automatic rollbacks**
- **Optimized builds**
- **Production security**

## 🚨 Troubleshooting
- **502 Error**: Check Container Port is `8000`
- **Image Pull Failed**: Verify GitHub token has `packages:read`
- **Health Check Failed**: Check database/Redis connectivity

## 📞 Need Help?
Run the detailed setup script:
```bash
./setup-production-dokploy.sh
```

---
*Your CI/CD pipeline is building the production image now!*