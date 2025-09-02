from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from wagtail.models import Page, Site


class Command(BaseCommand):
    help = 'Set up user groups and permissions for multi-tenant admin'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up user groups and permissions...'))
        
        # Create Customer Editors group with limited permissions
        customer_group, created = Group.objects.get_or_create(name='Customer Editors')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Customer Editors group'))
        
        # Get required permissions for customer editors
        permissions_needed = [
            # Basic admin access
            ('wagtailadmin', 'admin', 'access_admin'),
            
            # Page management
            ('wagtailcore', 'page', 'add_page'),
            ('wagtailcore', 'page', 'change_page'),
            ('wagtailcore', 'page', 'publish_page'),
            ('wagtailcore', 'page', 'view_page'),
            
            # Site settings
            ('wagtailcore', 'site', 'view_site'),
            
            # Image management (basic)
            ('wagtailimages', 'image', 'add_image'),
            ('wagtailimages', 'image', 'change_image'),
            ('wagtailimages', 'image', 'view_image'),
            
            # Document management (basic)
            ('wagtaildocs', 'document', 'add_document'),
            ('wagtaildocs', 'document', 'change_document'),
            ('wagtaildocs', 'document', 'view_document'),
        ]
        
        # Add permissions to customer group
        for app_label, model_name, codename in permissions_needed:
            try:
                content_type = ContentType.objects.get(app_label=app_label, model=model_name)
                permission = Permission.objects.get(content_type=content_type, codename=codename)
                customer_group.permissions.add(permission)
                self.stdout.write(f'Added permission: {app_label}.{codename}')
            except (ContentType.DoesNotExist, Permission.DoesNotExist):
                self.stdout.write(
                    self.style.WARNING(f'Permission not found: {app_label}.{model_name}.{codename}')
                )
        
        # Create Super Admin group with all permissions
        super_admin_group, created = Group.objects.get_or_create(name='Super Admins')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Super Admins group'))
            # Super admins get all permissions (handled by is_superuser status)
        
        # Update existing users
        customer_users = User.objects.filter(is_superuser=False, is_staff=True)
        for user in customer_users:
            if not user.groups.filter(name='Customer Editors').exists():
                user.groups.add(customer_group)
                self.stdout.write(f'Added {user.username} to Customer Editors group')
        
        super_users = User.objects.filter(is_superuser=True)
        for user in super_users:
            if not user.groups.filter(name='Super Admins').exists():
                user.groups.add(super_admin_group)
                self.stdout.write(f'Added {user.username} to Super Admins group')
        
        self.stdout.write(self.style.SUCCESS('User groups setup completed!'))
        
        # Show summary
        self.stdout.write('\n' + '='*50)
        self.stdout.write('SUMMARY:')
        self.stdout.write(f'Customer Editors: {customer_group.user_set.count()} users')
        self.stdout.write(f'Super Admins: {super_admin_group.user_set.count()} users')
        self.stdout.write('='*50)