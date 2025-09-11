from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_tenants.utils import get_public_schema_name
from django.db import connection


class TenantAdminSite(AdminSite):
    """
    Custom admin site for tenant management
    This forces operations to happen in the public schema
    """
    site_header = _("Tenant Management")
    site_title = _("Tenant Admin")
    index_title = _("Tenant Administration")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure we're using public schema for all operations
        
    def admin_view(self, view, cacheable=False):
        """Wrap admin views to ensure they run in public schema"""
        def wrapper(request, *args, **kwargs):
            # Force public schema
            connection.set_schema_to_public()
            return view(request, *args, **kwargs)
        
        return super().admin_view(wrapper, cacheable)


# Create the tenant admin site instance
tenant_admin = TenantAdminSite(name='tenant_admin')

# Import models and register them with tenant admin
from .models import Client, Domain, Theme
from .admin import ClientAdmin, DomainAdmin, ThemeAdmin

# Register models with the custom admin site
tenant_admin.register(Client, ClientAdmin)
tenant_admin.register(Domain, DomainAdmin)
tenant_admin.register(Theme, ThemeAdmin)

# Also register User model for user management
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

tenant_admin.register(User, UserAdmin)