"""
Management command to seed a tenant with lorem ipsum content for demo purposes
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from django.db import transaction

from apps.tenants.models import Client


class Command(BaseCommand):
    help = 'Seed a tenant schema with lorem ipsum content for demo purposes'

    def add_arguments(self, parser):
        parser.add_argument('schema_name', type=str, help='The tenant schema name to seed')
        parser.add_argument(
            '--admin-user',
            type=str,
            default='admin',
            help='Username for tenant admin user (default: admin)'
        )
        parser.add_argument(
            '--admin-password',
            type=str,
            default='admin123',
            help='Password for tenant admin user (default: admin123)'
        )
        parser.add_argument(
            '--admin-email',
            type=str,
            default='admin@example.com',
            help='Email for tenant admin user (default: admin@example.com)'
        )

    def handle(self, *args, **options):
        schema_name = options['schema_name']
        admin_user = options['admin_user']
        admin_password = options['admin_password']
        admin_email = options['admin_email']

        try:
            # Get the tenant
            client = Client.objects.get(schema_name=schema_name)
        except Client.DoesNotExist:
            raise CommandError(f'Tenant with schema "{schema_name}" does not exist')

        self.stdout.write(f'Seeding tenant: {client.name} (schema: {schema_name})')

        # Work within the tenant schema
        with schema_context(schema_name):
            try:
                with transaction.atomic():
                    self._create_admin_user(admin_user, admin_password, admin_email)
                    self._seed_wagtail_content(client)
                    
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully seeded tenant "{client.name}" with demo content'
                    )
                )
                self.stdout.write(f'Admin user created: {admin_user}/{admin_password}')
                
            except Exception as e:
                raise CommandError(f'Error seeding tenant: {e}')

    def _create_admin_user(self, username, password, email):
        """Create admin user for the tenant"""
        from django.contrib.auth.models import User
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Admin user "{username}" already exists, skipping...')
            return
        
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(f'Created admin user: {username}')

    def _seed_wagtail_content(self, client):
        """Seed Wagtail content for the tenant"""
        from wagtail.models import Site
        from apps.pages.models import HomePage, GalleryPage
        from apps.projects.models import Project
        
        # Check if root page exists, create if not
        from wagtail.models import Page
        
        try:
            root_page = Page.objects.get(depth=1)
        except Page.DoesNotExist:
            # Create root page if it doesn't exist
            root_page = Page.add_root(
                title="Root",
                slug="root"
            )
            
        # Create homepage if it doesn't exist
        try:
            homepage = HomePage.objects.get(slug='home')
            self.stdout.write('Homepage already exists, updating...')
        except HomePage.DoesNotExist:
            homepage = HomePage(
                title=f"{client.name} - Professional Construction",
                slug='home',
                intro=f"<p>Welcome to {client.name}! We provide high-quality construction, renovation, and carpentry services for residential and commercial projects throughout Denmark.</p>"
            )
            root_page.add_child(instance=homepage)
            self.stdout.write('Created homepage')

        # Create Site record
        site, created = Site.objects.get_or_create(
            is_default_site=True,
            defaults={
                'hostname': client.primary_domain.domain if client.primary_domain else 'localhost',
                'port': 80,
                'site_name': client.name,
                'root_page': homepage,
            }
        )
        if created:
            self.stdout.write('Created Wagtail site')
        else:
            # Update existing site
            site.site_name = client.name
            site.root_page = homepage
            if client.primary_domain:
                site.hostname = client.primary_domain.domain
            site.save()
            self.stdout.write('Updated Wagtail site')

        # Create Gallery page
        try:
            gallery_page = GalleryPage.objects.get(slug='projects')
            self.stdout.write('Gallery page already exists, skipping...')
        except GalleryPage.DoesNotExist:
            gallery_page = GalleryPage(
                title="Our Projects",
                slug='projects',
                intro="<p>Take a look at some of our completed construction projects. We're proud of the quality work we deliver for our clients.</p>"
            )
            homepage.add_child(instance=gallery_page)
            self.stdout.write('Created gallery page')

        # Create sample projects
        from datetime import date
        from wagtail.models import Site
        
        # Get the current site for projects
        current_site = Site.objects.get(is_default_site=True)
        
        sample_projects = [
            {
                'title': 'Villa renovering i København',
                'description': '<p>Komplet renovering af historisk villa inkluderet nyt køkken, badeværelser og energieffektive vinduer. Projektet tog 6 måneder at færdiggøre.</p>',
                'client_name': 'Familie Hansen',
                'location': 'København, Danmark',
                'date': date(2024, 6, 15),
                'project_type': 'renovation',
                'materials': 'Eg træ, keramiske fliser, energiglas',
                'featured': True,
            },
            {
                'title': 'Moderne kontorbygning',
                'description': '<p>Opførelse af moderne 3-etagers kontorbygning med bæredygtige materialer og smart bygningsteknologi.</p>',
                'client_name': 'TechCorp A/S',
                'location': 'Aarhus, Danmark', 
                'date': date(2023, 9, 30),
                'project_type': 'nybyggeri',
                'materials': 'Beton, stål, glas',
                'featured': True,
            },
            {
                'title': 'Skræddersyet køkken installation',
                'description': '<p>Design og installation af skræddersyet køkken med håndlavede skabe og premium apparater.</p>',
                'client_name': 'Nielsen Bolig',
                'location': 'Odense, Danmark',
                'date': date(2024, 3, 20),
                'project_type': 'haandvaerk',
                'materials': 'Jatoba træ, granit bordplade',
                'featured': False,
            },
            {
                'title': 'Badeværelse renovering',
                'description': '<p>Komplet badeværelse renovering med moderne armaturer, gulvvarme og vandtætte membraner.</p>',
                'client_name': 'Andersen Lejlighed',
                'location': 'Aalborg, Danmark',
                'date': date(2023, 11, 10),
                'project_type': 'renovation',
                'materials': 'Porcelænsgulv, kromo armaturer',
                'featured': False,
            }
        ]

        created_projects = 0
        for project_data in sample_projects:
            # Check if project already exists
            if not Project.objects.filter(title=project_data['title']).exists():
                project = Project.objects.create(
                    site=current_site,
                    title=project_data['title'],
                    description=project_data['description'],
                    client_name=project_data['client_name'],
                    location=project_data['location'],
                    date=project_data['date'],
                    project_type=project_data['project_type'],
                    materials=project_data['materials'],
                    featured=project_data['featured'],
                    published=True,
                )
                created_projects += 1
                self.stdout.write(f'Created project: {project_data["title"]}')

        if created_projects:
            self.stdout.write(f'Seeded {created_projects} sample projects')
        else:
            self.stdout.write('All sample projects already exist, skipping...')