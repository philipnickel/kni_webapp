# Django Multi-Tenant System Management

## Current System Overview

**Server:** 72.60.81.210 (Hostinger VPS)  
**Web Server:** LiteSpeed with native Django integration  
**Database:** PostgreSQL  
**Django Location:** `/usr/local/lsws/Example/html/`  
**SSL Certificate:** Let's Encrypt (expires Dec 9, 2025)  

## Current Configuration

### Tenants
- **johann** (schema: `johann`, name: "JCleemannByg")

### Domain Mappings
- `jcleemannbyg.dk` → johann tenant
- `kni.dk` → johann tenant  
- `72.60.81.210` → johann tenant
- `localhost` → johann tenant
- `127.0.0.1` → johann tenant

### Current Users
**johann tenant:**
- **Username:** admin
- **Email:** admin@jcleemannbyg.dk
- **Password:** admin123
- **Superuser:** Yes
- **Staff:** Yes

### SSL/TLS Configuration
- **Certificate covers:** jcleemannbyg.dk, kni.dk, www.jcleemannbyg.dk, www.kni.dk
- **Provider:** Let's Encrypt
- **Auto-renewal:** Configured via `/etc/cron.d/certbot` (runs twice daily)
- **Location:** `/etc/letsencrypt/live/jcleemannbyg.dk/`

## Admin Access

### For Tenants (Regular Users)
- **Wagtail CMS Admin:** `https://jcleemannbyg.dk/admin/` or `https://kni.dk/admin/`
- **Credentials:** admin / admin123
- **Purpose:** Content management, pages, images, etc.

### For Super-Admin (Tenant Management)  
- **Django Admin:** `https://jcleemannbyg.dk/django-admin/` or `https://kni.dk/django-admin/`
- **Credentials:** admin / admin123
- **Purpose:** Create/manage tenants, domains, users, themes
- **Features:**
  - ✅ Add/edit/delete tenants with full GUI
  - ✅ Manage domains and assign them to tenants  
  - ✅ Create/manage users across all tenants
  - ✅ Theme management with live color previews
  - ✅ Tenant schema creation and management
  - ✅ Bulk actions for tenant activation/deactivation

### LiteSpeed WebAdmin
- **URL:** `https://72.60.81.210:7080/`
- **Credentials:** admin / newpassword123
- **Purpose:** Server and web server configuration

## Management Commands

### Accessing the Django Environment
```bash
ssh hostinger
cd /usr/local/lsws/Example/html
source bin/activate
```

### Check Current Tenants
```bash
python manage.py shell -c "
from apps.tenants.models import Client, Domain
print('Tenants:')
for c in Client.objects.all():
    print(f'  - {c.schema_name}: {c.name}')
print('Domain mappings:')
for d in Domain.objects.all():
    print(f'  - {d.domain} -> {d.tenant.schema_name}')
"
```

## Creating New Tenants

### 1. Create a New Tenant
```bash
python manage.py shell << EOF
from apps.tenants.models import Client, Domain

# Create new tenant
new_tenant = Client(
    schema_name='newcompany',
    name='New Company Name'
)
new_tenant.save()
print(f"Created tenant: {new_tenant.schema_name}")

# Create domain mapping
domain = Domain(
    domain='newcompany.com',
    tenant=new_tenant,
    is_primary=True
)
domain.save()
print(f"Created domain mapping: {domain.domain} -> {new_tenant.schema_name}")
EOF
```

### 2. Run Migrations for New Tenant
```bash
python manage.py migrate_schemas --tenant
```

### 3. Create Superuser for New Tenant
```bash
python manage.py shell << EOF
from django.contrib.auth.models import User
from django_tenants.utils import schema_context

with schema_context('newcompany'):
    User.objects.create_superuser(
        username='admin',
        email='admin@newcompany.com', 
        password='secure_password'
    )
    print("Superuser created for newcompany tenant")
EOF
```

## Adding Additional Domains to Existing Tenants

### Add Domain to Existing Tenant
```bash
python manage.py shell << EOF
from apps.tenants.models import Client, Domain

# Get existing tenant
tenant = Client.objects.get(schema_name='johann')

# Add new domain
new_domain = Domain(
    domain='anotherdomain.com',
    tenant=tenant,
    is_primary=False
)
new_domain.save()
print(f"Added domain: {new_domain.domain} -> {tenant.schema_name}")
EOF
```

## SSL Certificate Management

### Adding New Domain to SSL Certificate
```bash
# Stop LiteSpeed
sudo systemctl stop lsws

# Add new domain to existing certificate
sudo certbot certonly --webroot \
  -w /usr/local/lsws/Example/html/ \
  -d jcleemannbyg.dk \
  -d kni.dk \
  -d www.jcleemannbyg.dk \
  -d www.kni.dk \
  -d newdomain.com \
  -d www.newdomain.com

# Update LiteSpeed SSL configuration if needed
# (Usually auto-updated if certificate path stays the same)

# Start LiteSpeed
sudo systemctl start lsws
```

### Create Separate SSL Certificate
```bash
sudo certbot certonly --webroot \
  -w /usr/local/lsws/Example/html/ \
  -d newdomain.com \
  -d www.newdomain.com
```

## User Management

### Create Regular User in Tenant
```bash
python manage.py shell << EOF
from django.contrib.auth.models import User
from django_tenants.utils import schema_context

with schema_context('johann'):  # or your tenant name
    user = User.objects.create_user(
        username='newuser',
        email='user@company.com',
        password='user_password'
    )
    user.is_staff = True  # if needed for admin access
    user.save()
    print(f"Created user: {user.username}")
EOF
```

### List All Users in Tenant
```bash
python manage.py shell << EOF
from django.contrib.auth.models import User
from django_tenants.utils import schema_context

with schema_context('johann'):  # or your tenant name
    users = User.objects.all()
    print(f"Users in tenant:")
    for user in users:
        print(f"  - {user.username} ({user.email}) - Superuser: {user.is_superuser}")
EOF
```

### Change User Password
```bash
python manage.py shell << EOF
from django.contrib.auth.models import User
from django_tenants.utils import schema_context

with schema_context('johann'):
    user = User.objects.get(username='admin')
    user.set_password('new_secure_password')
    user.save()
    print("Password updated successfully")
EOF
```

## Database Operations

### Backup Specific Tenant Data
```bash
# Backup only tenant schema
pg_dump -h localhost -U your_db_user -n johann kni_webapp > johann_tenant_backup.sql

# Backup entire database
pg_dump -h localhost -U your_db_user kni_webapp > full_database_backup.sql
```

### Remove Tenant (DANGEROUS)
```bash
python manage.py shell << EOF
from apps.tenants.models import Client

# WARNING: This will delete all tenant data!
tenant = Client.objects.get(schema_name='tenant_to_delete')
tenant.delete()  # This also drops the database schema
print("Tenant deleted")
EOF
```

## LiteSpeed Configuration

### Django Context Configuration
Location: `/usr/local/lsws/conf/vhosts/Example/vhconf.conf`

Key settings:
```
context / {
  type                    appserver
  location                /usr/local/lsws/Example/html/
  binPath                 /usr/local/lsws/fcgi-bin/lswsgi
  appType                 wsgi
  startupFile             project/wsgi.py
  env                     PYTHONPATH=/usr/local/lsws/Example/html/lib/python3.12:/usr/local/lsws/Example/html
  env                     LS_PYTHONBIN=/usr/local/lsws/Example/html/bin/python
}
```

### Restart LiteSpeed Services
```bash
# Graceful restart
sudo systemctl restart lsws

# Kill Python processes if needed
sudo killall lswsgi

# Test configuration
sudo /usr/local/lsws/bin/lshttpd -t
```

## Troubleshooting

### Django Not Loading
1. Check LiteSpeed error logs: `sudo tail -f /usr/local/lsws/logs/error.log`
2. Check virtual host logs: `sudo tail -f /usr/local/lsws/Example/logs/error.log`
3. Test Django manually: `cd /usr/local/lsws/Example/html && source bin/activate && python manage.py check`

### Database Connection Issues
1. Check database credentials in `.env` file
2. Test connection: `python manage.py shell -c "from django.db import connection; connection.ensure_connection(); print('DB OK')"`

### SSL Certificate Issues
1. Check certificate status: `sudo certbot certificates`
2. Test renewal: `sudo certbot renew --dry-run`
3. Check LiteSpeed SSL config in WebAdmin

## Security Notes

- Change default admin passwords immediately after setup
- Use strong passwords for all accounts
- Keep SSL certificates updated (auto-renewal should handle this)
- Regular database backups are recommended
- Monitor server logs for unusual activity

## File Locations

- **Django Application:** `/usr/local/lsws/Example/html/`
- **Virtual Environment:** `/usr/local/lsws/Example/html/bin/activate`
- **LiteSpeed Config:** `/usr/local/lsws/conf/`
- **SSL Certificates:** `/etc/letsencrypt/live/`
- **Environment Variables:** `/usr/local/lsws/Example/html/.env`
- **Static Files:** `/usr/local/lsws/Example/html/staticfiles/`

---

*Last updated: September 10, 2025*
*Server: 72.60.81.210 (Hostinger VPS)*