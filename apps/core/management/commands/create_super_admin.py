from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
import getpass


class Command(BaseCommand):
    help = 'Create a super admin account with full system access'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for super admin')
        parser.add_argument('--email', type=str, help='Email for super admin')
        parser.add_argument('--password', type=str, help='Password for super admin')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating super admin account...'))
        
        # Get super admin group
        super_admin_group, created = Group.objects.get_or_create(name='Super Admins')
        
        # Get user details
        username = options.get('username') or input('Enter username for super admin: ')
        email = options.get('email') or input('Enter email for super admin: ')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.ERROR(f'User {username} already exists!')
            )
            return
        
        # Get password
        password = options.get('password')
        if not password:
            password = getpass.getpass('Enter password for super admin: ')
            confirm_password = getpass.getpass('Confirm password: ')
            if password != confirm_password:
                self.stdout.write(self.style.ERROR('Passwords do not match!'))
                return
        
        # Create super admin user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        
        # Add to super admin group
        user.groups.add(super_admin_group)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Super admin account created successfully!\n'
                f'Username: {username}\n'
                f'Email: {email}\n'
                f'Access: Full system access (all features, all sites)\n'
                f'Group: Super Admins'
            )
        )
        
        # Show final status
        self.stdout.write('\n' + '='*60)
        self.stdout.write('CURRENT ADMIN USERS:')
        for admin_user in User.objects.filter(is_superuser=True):
            groups = list(admin_user.groups.values_list('name', flat=True))
            self.stdout.write(
                f'  {admin_user.username} ({admin_user.email}): groups={groups}'
            )
        
        self.stdout.write('\nCUSTOMER USERS:')
        customer_group = Group.objects.get(name='Customer Editors')
        for customer_user in customer_group.user_set.all():
            self.stdout.write(
                f'  {customer_user.username} ({customer_user.email}): limited access'
            )
        self.stdout.write('='*60)