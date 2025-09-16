"""
Complete baseline setup command - runs all initialization tasks
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Complete baseline setup for new deployments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--admin-email',
            type=str,
            help='Email for admin user (falls back to ADMIN_EMAIL env var)',
        )
        parser.add_argument(
            '--admin-password',
            type=str,
            help='Password for admin user (falls back to ADMIN_PASSWORD env var)',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Setting up KNI Webapp baseline...'))

        # 1. Load baseline data
        self.stdout.write('📦 Loading baseline Wagtail data...')
        call_command('load_baseline_data', '--skip-existing')

        # 2. Create admin user if credentials provided
        admin_email = options.get('admin_email') or os.environ.get('ADMIN_EMAIL')
        admin_password = options.get('admin_password') or os.environ.get('ADMIN_PASSWORD')

        if admin_email and admin_password:
            self.stdout.write(f'👤 Creating admin user: {admin_email}')

            User = get_user_model()
            if not User.objects.filter(email=admin_email).exists():
                try:
                    User.objects.create_superuser(admin_email, admin_email, admin_password)
                    self.stdout.write(self.style.SUCCESS(f'✅ Admin user created: {admin_email}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'❌ Failed to create admin user: {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ Admin user already exists: {admin_email}'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ No admin credentials provided - skipping admin user creation'))

        # 3. Collect static files (if in production)
        if not os.environ.get('DEBUG') == 'True':
            self.stdout.write('📦 Collecting static files...')
            try:
                call_command('collectstatic', '--noinput', '--clear')
                self.stdout.write(self.style.SUCCESS('✅ Static files collected'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Static files collection failed: {e}'))

        # 4. Show setup summary
        domain = os.environ.get('DOMAIN', 'localhost')
        port = ':8000' if domain == 'localhost' else ''

        self.stdout.write(self.style.SUCCESS('\n🎉 KNI Webapp setup complete!'))
        self.stdout.write(self.style.SUCCESS('📋 Summary:'))
        self.stdout.write(f'   🌐 Website: https://{domain}{port}')
        if admin_email:
            self.stdout.write(f'   👤 Admin: {admin_email}')
            self.stdout.write(f'   🛠️  Admin Panel: https://{domain}{port}/admin/')
        self.stdout.write(f'   🏥 Health Check: https://{domain}{port}/health/ready/')
        self.stdout.write('')
        self.stdout.write('🚀 Your KNI Webapp is ready to use!')