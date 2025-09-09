# KNI Webapp Deployment Guide

## Domain Setup
You have two domains: **jcleemannbyg.dk** and **kni.dk**

### Configuration:
- **jcleemannbyg.dk** → Johann's main site and Wagtail admin
- **kni.dk** → Available for additional tenant or redirect

## Deployment Steps

### 1. DNS Configuration (Hostinger)
Point these domains to your VPS IP (**72.60.81.210**):
```
A    jcleemannbyg.dk        → 72.60.81.210
A    www.jcleemannbyg.dk    → 72.60.81.210  
A    kni.dk                 → 72.60.81.210
A    www.kni.dk             → 72.60.81.210
```

### 2. VPS Setup Commands
```bash
# SSH into your VPS  
ssh root@72.60.81.210

# Run deployment script
sudo bash deploy.sh

# Edit environment variables
nano .env
# Update:
# - DJANGO_SECRET_KEY (generate a long random string)
# - Database password  
# - Other settings as needed

# Set up nginx
sudo cp nginx.conf /etc/nginx/sites-available/kni_webapp
sudo ln -s /etc/nginx/sites-available/kni_webapp /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl reload nginx

# Set up systemd service
sudo cp kni_webapp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable kni_webapp
sudo systemctl start kni_webapp

# Get SSL certificates (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d jcleemannbyg.dk -d www.jcleemannbyg.dk -d kni.dk -d www.kni.dk
```

### 3. Access Points After Deployment:
- **Johann's Site**: https://jcleemannbyg.dk/
- **Wagtail Admin**: https://jcleemannbyg.dk/admin/ (User: JCleemannByg, Pass: admin123)  
- **Super Admin**: https://jcleemannbyg.dk/django-admin/
- **KNI Domain**: https://kni.dk/ (available for future use)

### 4. Post-Deployment
1. Change default admin password
2. Configure Johann's site content in Wagtail admin
3. Set up regular backups
4. Monitor logs: `sudo journalctl -u kni_webapp -f`

## Troubleshooting
- Check service status: `sudo systemctl status kni_webapp`
- View logs: `sudo journalctl -u kni_webapp -n 50`
- Test database: `sudo -u postgres psql kni_webapp`
- Check nginx: `sudo nginx -t && sudo systemctl status nginx`