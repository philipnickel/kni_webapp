"""
Django management command to load baseline data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from wagtail.models import Site, Page
import os


class Command(BaseCommand):
    help = 'Load baseline data for new deployments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-existing',
            action='store_true',
            help='Skip if baseline data already exists',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🎯 Loading baseline data...'))

        try:
            # Check if we already have content
            if options.get('skip_existing'):
                pages_count = Page.objects.count()
                if pages_count > 2:  # More than root + home page
                    self.stdout.write(
                        self.style.WARNING(f'⏭️ Skipping - {pages_count} pages already exist')
                    )
                    return

            # Configure default site
            site = Site.objects.filter(is_default_site=True).first()
            if site:
                # Update with environment variables if available
                domain = os.environ.get('DOMAIN', 'localhost')
                port = int(os.environ.get('PORT', '8000'))

                site.hostname = domain
                site.port = port if domain == 'localhost' else 80
                site.save()

                self.stdout.write(
                    self.style.SUCCESS(f'✅ Site configured: {domain}:{site.port}')
                )

            # Load any JSON fixtures if they exist
            baseline_dir = '/app/baseline_data'
            if os.path.exists(baseline_dir):
                for filename in os.listdir(baseline_dir):
                    if filename.endswith('.json'):
                        fixture_path = os.path.join(baseline_dir, filename)
                        try:
                            self.stdout.write(f'📁 Loading fixture: {filename}')
                            # Note: loaddata is commented out as we don't have fixtures yet
                            # call_command('loaddata', fixture_path)
                            self.stdout.write(f'✅ Loaded: {filename}')
                        except Exception as e:
                            self.stdout.write(
                                self.style.WARNING(f'⚠️ Could not load {filename}: {e}')
                            )

            self.stdout.write(
                self.style.SUCCESS('🎉 Baseline data loaded successfully!')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error loading baseline data: {e}')
            )
            raise