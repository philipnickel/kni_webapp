#!/usr/bin/env python
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django_tenants.utils import schema_context
from django.contrib.auth.models import User

def create_johann_user():
    with schema_context('johann'):
        # Check if admin user exists
        if User.objects.filter(username='admin').exists():
            print("✅ Admin user already exists in Johann schema")
        else:
            # Create the admin user
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ Created admin user in Johann schema")
            print("   Username: admin")
            print("   Password: admin123")

if __name__ == '__main__':
    create_johann_user()