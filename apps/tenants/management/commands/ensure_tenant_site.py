from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context

class Command(BaseCommand):
    help = "Ensure a tenant Site has the expected hostname/port and a valid HomePage as root."

    def add_arguments(self, parser):
        parser.add_argument('--schema', default='johann', help='Tenant schema name (default: johann)')
        parser.add_argument('--hostname', default='johann.localhost', help='Hostname for the tenant site')
        parser.add_argument('--port', type=int, default=8000, help='Port for the tenant site (default: 8000)')

    def handle(self, *args, **options):
        schema = options['schema']
        hostname = options['hostname']
        port = options['port']

        from wagtail.models import Site, Page

        # Work inside tenant schema
        with schema_context(schema):
            # Ensure a Site exists
            site = Site.objects.filter(is_default_site=True).first() or Site.objects.first()
            if not site:
                # Create minimal site if none exists
                root = Page.get_first_root_node()
                site = Site.objects.create(
                    hostname=hostname,
                    port=port,
                    site_name=schema,
                    root_page=root,
                    is_default_site=True,
                )

            # Ensure a HomePage exists and is set as root when possible
            try:
                from apps.pages.models import HomePage
                home = HomePage.objects.order_by('-id').first()
                if not home:
                    # Create a simple homepage under the root
                    root = Page.get_first_root_node()
                    home = HomePage(title='JCleemannByg – Byggeri & Renovering', slug='forside')
                    root.add_child(instance=home)
                if site.root_page_id != home.id:
                    site.root_page = home
            except Exception:
                # If pages app is unavailable, keep existing root
                pass

            # Update host/port
            site.hostname = hostname
            site.port = port
            site.is_default_site = True
            site.save()

            self.stdout.write(self.style.SUCCESS(
                f"Ensured tenant site -> host: {site.hostname}, port: {site.port}, root: {site.root_page}"
            ))

