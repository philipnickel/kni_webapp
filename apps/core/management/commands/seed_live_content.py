from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from wagtail.models import Page
from apps.pages.models import HomePage, SiteSettings
from apps.projects.models import Project, ProjectImage
from wagtail.images.models import Image
from django.core.files.images import ImageFile
import io
from PIL import Image as PILImage
from datetime import date
import random


class Command(BaseCommand):
    help = 'Seed content to match the live JCleemannByg site'

    def handle(self, *args, **options):
        # First, clear existing projects and update homepage
        self.clear_existing_content()
        self.update_homepage()
        self.create_live_projects()
        self.update_site_settings()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded content to match live site!')
        )

    def clear_existing_content(self):
        """Clear existing sample content"""
        Project.objects.all().delete()
        self.stdout.write('Cleared existing projects')

    def update_homepage(self):
        """Update homepage content to match live site"""
        try:
            # Find the homepage
            homepage = HomePage.objects.filter(title__icontains='JCleemannByg').first()
            if not homepage:
                homepage = HomePage.objects.first()
            if homepage:
                homepage.title = 'Velkommen til JCleemannByg'
                homepage.intro = '<p>Professionelle bygge- og renoveringsløsninger med fokus på kvalitet og håndværk</p>'
                homepage.save()
                
                revision = homepage.save_revision()
                revision.publish()
                
                self.stdout.write(self.style.SUCCESS('Updated homepage content'))
            else:
                self.stdout.write(self.style.WARNING('Homepage not found'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating homepage: {e}'))

    def create_live_projects(self):
        """Create projects that match the live site"""
        projects_data = [
            {
                'title': 'Træ terrasse og udendørs køkken',
                'description': '''<h3>Smukt udendørs køkken og terrasse</h3>
                <p>Vi har bygget en fantastisk træterrasse med integreret udendørs køkken. Projektet omfatter:</p>
                <ul>
                    <li>Lærketræ terrasse på 45m²</li>
                    <li>Indbygget grill og kogezone</li>
                    <li>Opbevaringsløsninger i vejrbestandigt træ</li>
                    <li>LED-belysning til aftentimer</li>
                </ul>
                <p>Materialer brugt: Lærketræ, rustfrit stål, natursten. Projektet blev færdiggjort til tiden og within budget.</p>''',
                'materials': 'Lærketræ, rustfrit stål, natursten',
                'location': 'Privat villa, Nordsjælland',
                'date': date(2024, 8, 15),
                'featured': True,
                'published': True,
                'client_name': 'Familie Hansen',
                'width': 800,
                'height': 600,
                'color': '#8B4513'  # Brown for wood
            },
            {
                'title': 'Villa renovering i København',
                'description': '''<h3>Totalrenovering af historisk villa</h3>
                <p>Komplet renovering af villa fra 1920'erne med respekt for den oprindelige arkitektur:</p>
                <ul>
                    <li>Restaurering af originale trægulve</li>
                    <li>Modernisering af køkken og badeværelser</li>
                    <li>Energioptimering med nye vinduer</li>
                    <li>Tilbygning af moderne familierum</li>
                </ul>
                <p>Et smukt eksempel på hvordan historie og moderne komfort kan forenes harmonisk.</p>''',
                'materials': 'Eg, marmor, glas, tegl',
                'location': 'Indre København',
                'date': date(2024, 6, 20),
                'featured': True,
                'published': True,
                'client_name': 'Privat kunde',
                'width': 800,
                'height': 600,
                'color': '#D2691E'  # Saddle brown for villa
            },
            {
                'title': 'Skræddersyet køkken installation',
                'description': '''<h3>Håndlavet køkken efter mål</h3>
                <p>Designet og bygget et unikt køkken der passer perfekt til kundens behov:</p>
                <ul>
                    <li>Massiv eg køkkenø med Corian bordplade</li>
                    <li>Skræddersyede skabe i alle højder</li>
                    <li>Integrerede hvidevarer af højeste kvalitet</li>
                    <li>Skjult LED-belysning under skabe</li>
                </ul>
                <p>Køkkenet er både funktionelt og æstetisk smukt.</p>''',
                'materials': 'Massiv eg, Corian, rustfrit stål',
                'location': 'Frederiksberg',
                'date': date(2024, 3, 10),
                'featured': False,
                'published': True,
                'client_name': '',
                'width': 800,
                'height': 600,
                'color': '#CD853F'  # Peru for kitchen
            },
            {
                'title': 'Badeværelse renovering',
                'description': '''<h3>Luksuriøst badeværelse</h3>
                <p>Fuldstændig renovering af master badeværelse:</p>
                <ul>
                    <li>Italienske marmor fliser</li>
                    <li>Fritstående badekar</li>
                    <li>Regnbruser med termostat</li>
                    <li>Skræddersyet vask møbel</li>
                </ul>
                <p>Et spa-lignende badeværelse der oser af luksus og komfort.</p>''',
                'materials': 'Marmor, messing, glas',
                'location': 'Gentofte',
                'date': date(2023, 11, 5),
                'featured': False,
                'published': True,
                'client_name': '',
                'width': 800,
                'height': 600,
                'color': '#F5F5DC'  # Beige for bathroom
            },
            {
                'title': 'Moderne kontorbygning',
                'description': '''<h3>Erhvervsprojekt med fokus på bæredygtighed</h3>
                <p>Opførelse af moderne kontorbygning for mindre virksomhed:</p>
                <ul>
                    <li>Bæredygtige materialer i hele byggeriet</li>
                    <li>Store glaspartier for naturligt lys</li>
                    <li>Energieffektiv varme- og ventilationsystem</li>
                    <li>Fleksible kontorrum der kan tilpasses</li>
                </ul>
                <p>Et moderne og miljøvenligt arbejdsmiljø.</p>''',
                'materials': 'Træ, glas, beton, stål',
                'location': 'Erhvervsområde, Glostrup',
                'date': date(2023, 9, 15),
                'featured': False,
                'published': True,
                'client_name': 'TechStart ApS',
                'width': 800,
                'height': 600,
                'color': '#708090'  # Slate gray for office
            }
        ]
        
        for i, project_data in enumerate(projects_data, 1):
            # Create a stock image
            stock_image = self.create_stock_image(
                project_data['width'],
                project_data['height'],
                project_data['color'],
                f"live-project-{i}",
                project_data['title']
            )
            
            # Create project
            project = Project.objects.create(
                title=project_data['title'],
                description=project_data['description'],
                materials=project_data['materials'],
                location=project_data['location'],
                date=project_data['date'],
                featured=project_data['featured'],
                published=project_data['published'],
                client_name=project_data['client_name']
            )
            
            # Add image to project
            if stock_image:
                ProjectImage.objects.create(
                    project=project,
                    image=stock_image,
                    caption=f'Billede af {project.title}',
                    alt_text=f'Professionelt håndværk: {project.title}'
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created live project: {project.title}')
            )

    def update_site_settings(self):
        """Update site settings to match live site"""
        try:
            site_settings, created = SiteSettings.objects.get_or_create(
                site_id=1,
                defaults={
                    'company_name': 'JCleemannByg',
                    'phone': '+45 12 34 56 78',
                    'email': 'info@jcleemannbyg.dk',
                    'address': 'Eksempel Vej 123, 1234 København',
                    'cvr': '12345678',
                    'opening_hours': '''Mandag - Fredag: 08:00 - 16:00
Lørdag: 08:00 - 12:00
Søndag: Lukket''',
                    'footer_cta_title': 'Klar til at starte?',
                    'footer_cta_text': 'Kontakt JCleemannByg i dag for et uforpligtende tilbud på dit næste projekt.',
                    'footer_cta_button_text': 'Få et tilbud',
                    'copyright_text': '© 2025 JCleemannByg. Alle rettigheder forbeholdes.',
                }
            )
            
            # Update existing settings if not created
            if not created:
                site_settings.company_name = 'JCleemannByg'
                site_settings.phone = '+45 12 34 56 78'
                site_settings.email = 'info@jcleemannbyg.dk'
                site_settings.address = 'Eksempel Vej 123, 1234 København'
                site_settings.cvr = '12345678'
                site_settings.opening_hours = '''Mandag - Fredag: 08:00 - 16:00
Lørdag: 08:00 - 12:00
Søndag: Lukket'''
                site_settings.footer_cta_title = 'Klar til at starte?'
                site_settings.footer_cta_text = 'Kontakt JCleemannByg i dag for et uforpligtende tilbud på dit næste projekt.'
                site_settings.footer_cta_button_text = 'Få et tilbud'
                site_settings.copyright_text = '© 2025 JCleemannByg. Alle rettigheder forbeholdes.'
                site_settings.save()
            
            self.stdout.write(self.style.SUCCESS('Updated site settings'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating site settings: {e}'))

    def create_stock_image(self, width, height, color, name, title):
        """Create a stock image with project title overlay"""
        try:
            # Create PIL image with solid color
            pil_image = PILImage.new('RGB', (width, height), color)
            
            # Convert to file-like object
            image_io = io.BytesIO()
            pil_image.save(image_io, format='JPEG', quality=85)
            image_io.seek(0)
            
            # Create Wagtail Image
            image_file = ImageFile(image_io, name=f'{name}.jpg')
            wagtail_image = Image.objects.create(
                title=f'{title} - Projekt billede',
                file=image_file
            )
            
            return wagtail_image
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to create stock image {name}: {e}')
            )
            return None