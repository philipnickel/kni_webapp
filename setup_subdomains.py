#!/usr/bin/env python
"""
Script to set up subdomain routing for tenants.
Each tenant will be available at tenantname.kni.dk
"""

import os
import django
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django_tenants.utils import get_tenant_model
from apps.tenants.models import Domain

def setup_subdomains():
    """Set up subdomain routing for existing tenants"""
    Tenant = get_tenant_model()
    
    print("=== Current Tenant Configuration ===")
    for tenant in Tenant.objects.all():
        print(f"Schema: {tenant.schema_name}")
        domains = Domain.objects.filter(tenant=tenant)
        for domain in domains:
            print(f"  - Domain: {domain.domain} (primary: {domain.is_primary})")
        if not domains.exists():
            print("  - No domains configured")
    
    print("\n=== Setting up subdomain routing ===")
    
    # Get all tenants except public
    tenants = Tenant.objects.exclude(schema_name='public')
    
    for tenant in tenants:
        # Create subdomain: tenantname.kni.dk
        subdomain = f"{tenant.schema_name}.kni.dk"
        
        # Check if domain already exists
        existing_domain = Domain.objects.filter(domain=subdomain).first()
        if existing_domain:
            print(f"Domain {subdomain} already exists for tenant {existing_domain.tenant.schema_name}")
            continue
            
        # Create new domain
        domain = Domain.objects.create(
            domain=subdomain,
            tenant=tenant,
            is_primary=True
        )
        print(f"Created domain {subdomain} for tenant {tenant.schema_name}")
        
        # Remove old domain mappings if they exist
        old_domains = Domain.objects.filter(tenant=tenant).exclude(domain=subdomain)
        for old_domain in old_domains:
            print(f"Removing old domain {old_domain.domain} for tenant {tenant.schema_name}")
            old_domain.delete()
    
    print("\n=== Final Configuration ===")
    for tenant in Tenant.objects.all():
        print(f"Schema: {tenant.schema_name}")
        domains = Domain.objects.filter(tenant=tenant)
        for domain in domains:
            print(f"  - Domain: {domain.domain} (primary: {domain.is_primary})")

if __name__ == "__main__":
    setup_subdomains()