"""
Django management command to load baseline data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from wagtail.models import Site, Page
from wagtail.rich_text import RichText
import os


class Command(BaseCommand):
    help = 'Load baseline data for new deployments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-existing',
            action='store_true',
            help='Skip if baseline data already exists',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force creation even if content exists',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🎯 Loading baseline data...'))

        try:
            # Check if we already have content (unless forced)
            if options.get('skip_existing') and not options.get('force'):
                pages_count = Page.objects.count()
                if pages_count > 2:  # More than root + home page
                    self.stdout.write(
                        self.style.WARNING(f'⏭️ Skipping - {pages_count} pages already exist')
                    )
                    return

            # Configure default site
            self._configure_site()

            # Create basic page structure
            self._create_basic_pages()

            self.stdout.write(
                self.style.SUCCESS('🎉 Baseline data loaded successfully!')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error loading baseline data: {e}')
            )
            raise

    def _configure_site(self):
        """Configure the default Wagtail site with proper domain"""
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

    def _create_basic_pages(self):
        """Create basic page structure for the website"""
        from wagtail.models import Page

        # Get or create home page
        try:
            # Try to get the root page
            root_page = Page.objects.filter(depth=1).first()
            if not root_page:
                self.stdout.write(self.style.WARNING('⚠️ No root page found'))
                return

            # Check if we already have a home page
            existing_home = root_page.get_children().filter(slug='home').first()
            if existing_home:
                self.stdout.write(self.style.SUCCESS('✅ Home page already exists'))
                return

            # Import here to avoid circular imports
            from apps.core.models import HomePage

            # Create a new home page
            home_page = HomePage(
                title='Welcome to KNI Webapp',
                slug='home',
                intro='Welcome to the KNI construction management system.',
            )

            # Add it as a child of root
            root_page.add_child(instance=home_page)

            # Set it as the default page for the site
            site = Site.objects.filter(is_default_site=True).first()
            if site:
                site.root_page = home_page
                site.save()

            self.stdout.write(
                self.style.SUCCESS('✅ Created home page')
            )

        except ImportError:
            # If HomePage model doesn't exist, just configure the existing structure
            self.stdout.write(
                self.style.WARNING('⚠️ HomePage model not found - using default structure')
            )
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'⚠️ Could not create pages: {e}')
            )