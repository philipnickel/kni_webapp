"""
Management command to seed a tenant with complete editable content using StreamFields
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from django.db import transaction
from datetime import date
import json

from apps.tenants.models import Client


class Command(BaseCommand):
    help = 'Seed a tenant schema with complete editable content using StreamFields'

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
                    self._seed_site_settings(client)
                    
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully seeded tenant "{client.name}" with complete editable content'
                    )
                )
                self.stdout.write(f'Admin user: {admin_user}/{admin_password}')
                
            except Exception as e:
                import traceback
                traceback.print_exc()
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

    def _seed_site_settings(self, client):
        """Seed site settings with proper configuration"""
        from apps.pages.models import SiteSettings
        from wagtail.models import Site
        
        # Get the actual site ID
        site = Site.objects.get(is_default_site=True)
        
        # Create or update site settings
        site_settings, created = SiteSettings.objects.get_or_create(
            site_id=site.id,
            defaults={
                'company_name': client.name,
                'phone': '+45 12 34 56 78',
                'email': 'info@example.com',
                'cvr': '12345678',
                'address': 'Eksempel Vej 123, 1234 København',
                'opening_hours': 'Mandag - Fredag: 08:00 - 16:00\nLørdag: 08:00 - 12:00\nSøndag: Lukket',
                'default_theme': 'forest',
                'show_navigation': True,
                'navigation_cta_text': 'Få et tilbud',
                'footer_description': f'<p>{client.name} leverer professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk. Vi har mange års erfaring og tilbyder altid faste priser uden skjulte omkostninger.</p>',
                'footer_contact_title': 'Kontakt',
                'footer_cta_title': 'Klar til at starte?',
                'footer_cta_text': f'Kontakt {client.name} i dag for et uforpligtende tilbud på dit næste projekt.',
                'footer_cta_button_text': 'Få et tilbud',
                'facebook_url': '',
                'instagram_url': '',
                'linkedin_url': '',
                'copyright_text': f'© 2025 {client.name}. Alle rettigheder forbeholdes.',
            }
        )
        
        if not created:
            # Update existing settings
            site_settings.company_name = client.name
            site_settings.footer_description = f'<p>{client.name} leverer professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk. Vi har mange års erfaring og tilbyder altid faste priser uden skjulte omkostninger.</p>'
            site_settings.footer_cta_text = f'Kontakt {client.name} i dag for et uforpligtende tilbud på dit næste projekt.'
            site_settings.copyright_text = f'© 2025 {client.name}. Alle rettigheder forbeholdes.'
            if not site_settings.opening_hours:
                site_settings.opening_hours = 'Mandag - Fredag: 08:00 - 16:00\nLørdag: 08:00 - 12:00\nSøndag: Lukket'
            site_settings.save()
            self.stdout.write('Updated site settings')
        else:
            self.stdout.write('Created site settings')
            
        # Create homepage if it doesn't exist
        try:
            homepage = HomePage.objects.get(slug='home')
            self.stdout.write('Homepage already exists, updating...')
        except HomePage.DoesNotExist:
            homepage = HomePage(
                title=f"Professionel bygge- og renoveringsvirksomhed",
                slug='home',
                intro=f"<p>Velkommen til {client.name}! Vi leverer professionelle bygge-, renoverings- og snedkerløsninger med fokus på kvalitet og håndværk. Med mange års erfaring og altid faste priser uden skjulte omkostninger.</p>"
            )
            root_page.add_child(instance=homepage)
            self.stdout.write('Created homepage')
>>>>>>> 6d787a0 (Improve typography and fonts throughout website)

    def _seed_wagtail_content(self, client):
        """Seed Wagtail content with complete StreamField blocks"""
        from wagtail.models import Site, Page
        from apps.pages.models import HomePage, GalleryPage, ContactPage
        from apps.projects.models import Project
        from django.db import connection
        
        # Build the homepage StreamField content
        homepage_content = [
            {
                "type": "hero_v2",
                "value": {
                    "heading": f"Velkommen til {client.name}",
                    "subheading": "Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk",
                    "primary_text": "Få et tilbud",
                    "primary_page": None,  
                    "secondary_text": "Se vores projekter",
                    "secondary_page": None,  
                    "image": None,
                    "style": {
                        "background": "hero",
                        "spacing": "lg",
                        "container": "normal",
                        "divider": False
                    }
                }
            },
            {
                "type": "trust_badges",
                "value": {
                    "heading": "",
                    "items": [
                        {
                            "title": "20+ års erfaring",
                            "description": "Specialister i kvalitets træbyggeri",
                            "icon": "clock"
                        },
                        {
                            "title": "Fuld forsikring", 
                            "description": "Garantier på alt håndværk",
                            "icon": "shield"
                        },
                        {
                            "title": "Faste priser",
                            "description": "Ingen skjulte omkostninger", 
                            "icon": "dollar"
                        },
                        {
                            "title": "Lokal snedker",
                            "description": "Altid tæt på vores kunder",
                            "icon": "heart"
                        }
                    ],
                    "columns": "4",
                    "style": {
                        "background": "surface-soft",
                        "spacing": "md", 
                        "container": "normal",
                        "divider": False
                    }
                }
            },
            {
                "type": "featured_projects",
                "value": {
                    "heading": "Fremhævede projekter",
                    "subheading": "Et udpluk af vores seneste håndværk",
                    "show_all_link": True,
                    "all_projects_page": None,
                    "columns": "3",
                    "style": {
                        "background": "surface",
                        "spacing": "lg", 
                        "container": "normal",
                        "divider": False
                    }
                }
            },
            {
                "type": "services_grid_inline",
                "value": {
                    "heading": "Vores tjenester",
                    "items": [
                        {
                            "title": "Byggeprojekter",
                            "description": "Professionelle byggeprojekter fra start til slut. Vi leverer kvalitetsarbejde med fokus på detaljer og håndværk.",
                            "icon": "building"
                        },
                        {
                            "title": "Renovering", 
                            "description": "Totalrenovering og restaurering af bygninger. Vi hjælper med at modernisere og forbedre eksisterende strukturer.",
                            "icon": "wrench"
                        },
                        {
                            "title": "Tilbygninger",
                            "description": "Udvidelse af eksisterende boliger med tilbygninger, der harmonerer perfekt med den oprindelige arkitektur.",
                            "icon": "home"
                        }
                    ],
                    "columns": "3",
                    "style": {
                        "background": "surface",
                        "spacing": "lg",
                        "container": "normal",
                        "divider": False
                    }
                }
            }
        ]
        
        # Get root page
        root_page = Page.objects.get(depth=1)
        
        # Remove existing homepage if it exists
        existing_homepage = Page.objects.filter(slug='home').first()
        if existing_homepage:
            existing_homepage.delete()
            self.stdout.write('Removed existing homepage')
            
        # Fix root page tree structure
        root_page.numchild = root_page.get_children().count()
        root_page.save()
        
        # Create new HomePage
        homepage = HomePage(
            title=client.name,
            slug='home',
            intro=f"<p>Velkommen til {client.name} - din lokale byggeentreprenør med mange års erfaring i kvalitetsbyggeri.</p>",
            body=json.dumps(homepage_content)
        )
        homepage = root_page.add_child(instance=homepage)
        self.stdout.write('Created new HomePage with StreamField content')

        # Update Site record
        site, created = Site.objects.get_or_create(
            is_default_site=True,
            defaults={
                'hostname': client.primary_domain.domain if client.primary_domain else 'localhost',
                'port': 80,
                'site_name': client.name,
                'root_page': homepage,
            }
        )
        if not created:
            # Update existing site
            site.site_name = client.name
            site.root_page = homepage
            if client.primary_domain:
                site.hostname = client.primary_domain.domain
            site.save()

        # Create sample projects
        current_site = Site.objects.get(is_default_site=True)
        
        sample_projects = [
            {
                'title': 'Totalrenovering af historisk villa',
                'description': '<h3>Omfattende renovering med respekt for den oprindelige arkitektur</h3><p>Komplet renovering af historisk villa fra 1920\'erne inkluderet nyt køkken, tre badeværelser og energieffektive træ-alu vinduer. Projektet blev udført over 8 måneder med fokus på at bevare husets originale charme samtidig med moderne komfort.</p><p><strong>Særlige udfordringer:</strong> Bevarelse af originale stuk-lofter og genopførelse af historiske døre og karme.</p>',
                'client_name': 'Familie Hansen-Møller',
                'location': 'Hellerup, København',
                'date': date(2024, 6, 15),
                'project_type': 'renovation',
                'materials': 'Eg gulve, keramiske fliser, træ-alu vinduer, natursten',
                'featured': True,
            },
            {
                'title': 'Moderne kontorbygning med DGNB-certificering',
                'description': '<h3>Bæredygtig nybyggeri i tre etager</h3><p>Opførelse af moderne 3-etagers kontorbygning med fokus på bæredygtige materialer og smart bygningsteknologi. Bygningen opnåede DGNB-guld certificering gennem innovative løsninger som geotermisk opvarmning og regnvandsopsamling.</p><p><strong>Byggeperiode:</strong> 14 måneder fra første spadestik til indflytning.</p>',
                'client_name': 'TechCorp A/S',
                'location': 'Aarhus C, Danmark', 
                'date': date(2023, 9, 30),
                'project_type': 'nybyggeri',
                'materials': 'Armeret beton, FSC-certificeret træ, tripleglas, sedum-tag',
                'featured': True,
            },
            {
                'title': 'Skræddersyet køkkendesign og installation',
                'description': '<h3>Håndlavet køkken i dansk design</h3><p>Design og installation af skræddersyet køkken med håndlavede skabe i massiv eg og italienske natursten bordplader. Alle detaljer blev tilpasset kundens specifikke ønsker og husstandens behov.</p><p><strong>Specialfunktioner:</strong> Integreret vin-køleskab, skjult opbevaring og ergonomisk arbejdshøjder.</p>',
                'client_name': 'Nielsen Familie',
                'location': 'Odense M, Danmark',
                'date': date(2024, 3, 20),
                'project_type': 'haandvaerk',
                'materials': 'Massiv eg, Carrara marmor, rustfrit stål, keramisk bagvæg',
                'featured': False,
            },
            {
                'title': 'Luksuriøs badeværelse med wellnessfaciliteter',
                'description': '<h3>Spa-oplevelse i eget hjem</h3><p>Komplet transformation af stort badeværelse med moderne wellness-faciliteter inkluderet regnbruser, fristående badekar og gulvvarme. Hele projektet blev udført med vandtætte membraner og førsteklasses materialer.</p><p><strong>Særlige features:</strong> LED-lys integreret i fliser, smart spejl med berøringsfunktion.</p>',
                'client_name': 'Andersen Penthouse',
                'location': 'Aalborg Centrum',
                'date': date(2023, 11, 10),
                'project_type': 'renovation',
                'materials': 'Store naturstensfliser, messing armaturer, Corian-bordplade',
                'featured': False,
            },
            {
                'title': 'Moderne tilbygning med glasparti',
                'description': '<h3>Udvidelse der forbinder have og hjem</h3><p>Opførelse af 40m² tilbygning med store glaspartier og direkte adgang til haven. Tilbygningen integrerer sømløst med det eksisterende hus gennem matchende materialer og gennemtænkt design.</p><p><strong>Arkitektonisk fokus:</strong> Maksimering af naturligt lys og skabelse af indendørs-udendørs flow.</p>',
                'client_name': 'Larsen Familie',
                'location': 'Rungsted, Danmark',
                'date': date(2024, 1, 12),
                'project_type': 'tilbygning',
                'materials': 'Tegl facade, egetræs gulve, aluminium vinduer, skifertag',
                'featured': True,
            }
        ]

        created_projects = 0
        for project_data in sample_projects:
            if not Project.objects.filter(title=project_data['title']).exists():
                project = Project.objects.create(
                    site=current_site,
                    title=project_data['title'],
                    description=project_data['description'],
                    client_name=project_data['client_name'],
                    location=project_data['location'],
                    date=project_data['date'],
                    project_type=project_data.get('project_type', 'renovation'),
                    materials=project_data['materials'],
                    featured=project_data['featured'],
                    published=True,
                )
                
                # Add stock image if available
                if 'stock_image' in project_data:
                    try:
                        from wagtail.images.models import Image
                        from django.core.files import File
                        import os
                        
                        # Path to stock image
                        stock_image_path = f'/usr/local/lsws/Example/html/media/project_images/{project_data["stock_image"]}'
                        
                        # Check if image file exists
                        if os.path.exists(stock_image_path):
                            # Create Wagtail image from file
                            with open(stock_image_path, 'rb') as f:
                                django_file = File(f)
                                image = Image(
                                    title=f'{project_data["title"]} - hovedbillede',
                                )
                                image.file.save(project_data["stock_image"], django_file, save=True)
                                
                                # Add image to project
                                from apps.projects.models import ProjectImage
                                ProjectImage.objects.create(
                                    project=project,
                                    image=image,
                                    sort_order=0
                                )
                                self.stdout.write(f'Added stock image to: {project_data["title"]}')
                    except Exception as e:
                        self.stdout.write(f'Failed to add image to {project_data["title"]}: {e}')
                
                created_projects += 1
                self.stdout.write(f'Created project: {project_data["title"]}')

        # Create Contact Page
        try:
            if not ContactPage.objects.filter(slug='kontakt').exists():
                contact_page = ContactPage(
                    title="Kontakt Os",
                    slug='kontakt',
                    intro=f"<p>Har du brug for et tilbud eller har spørgsmål til vores tjenester? Kontakt {client.name} i dag.</p>",
                    show_contact_form=True,
                    contact_form_title="Send os en besked",
                    contact_form_intro="<p>Udfyld formularen nedenfor, så vender vi tilbage til dig hurtigst muligt.</p>"
                )
                homepage.add_child(instance=contact_page)
                self.stdout.write('Created contact page')
        except Exception as e:
            self.stdout.write(f'Contact page creation failed: {e}')

        # Create Gallery Page  
        try:
            if not GalleryPage.objects.filter(slug='projekter').exists():
                gallery_page = GalleryPage(
                    title="Vores Projekter", 
                    slug='projekter',
                    intro=f"<p>Se nogle af vores færdige byggeprojekter. Vi er stolte af det kvalitetsarbejde, vi leverer for vores kunder.</p>"
                )
                homepage.add_child(instance=gallery_page)
                self.stdout.write('Created gallery page')
        except Exception as e:
            self.stdout.write(f'Gallery page creation failed: {e}')

        self.stdout.write(f'\\n🎉 Tenant seeding completed!')
        self.stdout.write(f'📝 Homepage: Fully editable with StreamFields') 
        self.stdout.write(f'📁 Gallery page: /projekter/')
        self.stdout.write(f'📞 Contact page: /kontakt/')
        self.stdout.write(f'🏗️  Sample projects: {created_projects} created')
        self.stdout.write(f'⚙️  Site settings: Fully configured and editable')
        self.stdout.write(f'\\n✨ Everything is now editable through Wagtail admin!')