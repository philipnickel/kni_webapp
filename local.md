# Local Verification Needed

## Issue
ProgrammingError: `column projects_project.unsplash_image_id does not exist` when accessing `/projekter/` page.

## What Was Done
1. ✅ Downloaded 5 construction stock images to `/usr/local/lsws/Example/html/media/project_images/`
2. ✅ Removed `unsplash_image_id` field from Project model
3. ✅ Created and applied migration 0005 to remove the field
4. ✅ Updated seed script to use local images with Wagtail Image objects
5. ✅ Enhanced gallery and contact page templates
6. ✅ Restarted OpenLiteSpeed web server
7. ✅ Cleared Python cache files

## Still Need to Verify/Fix

### 1. Database Schema Verification
```bash
# Check if migration was actually applied to jcleemannbyg schema
ssh hostinger "cd /usr/local/lsws/Example/html && source venv/bin/activate && python manage.py shell -c \"
from django_tenants.utils import schema_context
from django.db import connection

with schema_context('jcleemannbyg'):
    with connection.cursor() as cursor:
        cursor.execute('SELECT column_name FROM information_schema.columns WHERE table_name = \'projects_project\' AND column_name = \'unsplash_image_id\';')
        result = cursor.fetchall()
        if result:
            print('ERROR: unsplash_image_id column still exists!')
        else:
            print('OK: unsplash_image_id column removed')
\""
```

### 2. Check for Cached Queries or Views
```bash
# Look for any custom views that might be selecting specific fields
ssh hostinger "grep -r 'unsplash_image_id' /usr/local/lsws/Example/html/apps/projects/views.py || echo 'No references in views'"

# Check admin.py for field references
ssh hostinger "grep -r 'unsplash_image_id' /usr/local/lsws/Example/html/apps/projects/admin.py || echo 'No references in admin'"

# Check for any queryset annotations or custom SQL
ssh hostinger "grep -rn 'SELECT.*unsplash_image_id' /usr/local/lsws/Example/html/ || echo 'No custom SQL found'"
```

### 3. Restart Application Process
```bash
# Force restart all Python processes
ssh hostinger "pkill -f python"
ssh hostinger "systemctl restart lsws"

# Or check if there's a specific app process to restart
ssh hostinger "ps aux | grep python"
```

### 4. Check Migration Status
```bash
# Verify migration was applied to all schemas
ssh hostinger "cd /usr/local/lsws/Example/html && source venv/bin/activate && python manage.py showmigrations projects"
```

### 5. Check if Field is Referenced in Gallery Template
```bash
# Ensure gallery template doesn't reference the field
ssh hostinger "grep -n 'unsplash_image_id' /usr/local/lsws/Example/html/templates/pages/gallery_page.html || echo 'Template is clean'"
```

### 6. Test Direct Model Access
```bash
# Test if the error occurs in model access or template rendering
ssh hostinger "cd /usr/local/lsws/Example/html && source venv/bin/activate && python manage.py shell -c \"
from django_tenants.utils import schema_context
from apps.projects.models import Project

with schema_context('jcleemannbyg'):
    try:
        projects = Project.objects.values()  # Get raw dict values
        print('Model access works')
        print('First project fields:', list(projects[0].keys()) if projects else 'No projects')
    except Exception as e:
        print('ERROR in model access:', str(e))
\""
```

## Likely Solutions

1. **Migration not applied to tenant schema**: Re-run tenant migrations
2. **Cached QuerySet in view**: Check `/apps/projects/views.py` for hardcoded field lists
3. **Python process not restarted**: Kill all Python processes and restart web server
4. **Django model cache**: Clear Django's model cache by restarting the application

## Files Changed
- `/usr/local/lsws/Example/html/apps/projects/models.py` - Removed unsplash_image_id field
- `/usr/local/lsws/Example/html/templates/pages/gallery_page.html` - Removed unsplash references
- `/usr/local/lsws/Example/html/apps/tenants/management/commands/seed_tenant.py` - Updated to use local images
- Added stock images to `/usr/local/lsws/Example/html/media/project_images/`