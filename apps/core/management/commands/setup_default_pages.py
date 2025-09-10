from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from wagtail.models import Page
from apps.pages.models import HomePage, GalleryPage, ContactPage
from apps.projects.models import Project
from wagtail.images.models import Image
from django.core.files.images import ImageFile
import io
from PIL import Image as PILImage
from datetime import date
import random


class Command(BaseCommand):
    help = 'Setup default pages (Home, Gallery, Contact) for a construction business site'

    def add_arguments(self, parser):
        parser.add_argument(
            '--site-id',
            type=int,
            default=1,
            help='Site ID to setup pages for (default: 1)'
        )
        parser.add_argument(
            '--company-name',
            type=str,
            default='JCleemannByg',
            help='Company name to use in default content'
        )

    def handle(self, *args, **options):
        site_id = options['site_id']
        company_name = options['company_name']
        
        try:
            site = Site.objects.get(id=site_id)
        except Site.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Site with ID {site_id} does not exist')
            )
            return

        # Get the root page
        root_page = Page.objects.get(depth=1)
        
        # Check if we already have a HomePage
        existing_home = HomePage.objects.filter(title__icontains=company_name).first()
        if existing_home:
            self.stdout.write(
                self.style.WARNING(f'HomePage for {company_name} already exists')
            )
            home_page = existing_home
        else:
            # Create HomePage with unique slug if needed
            slug = 'home'
            counter = 0
            while Page.objects.filter(slug=slug).exists():
                counter += 1
                slug = f'home-{counter}'
            
            # Create HomePage with Lorem Ipsum content
            home_page = HomePage(
                title=f'Velkommen til {company_name}',
                slug=slug,
                intro='<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>',
            )
            root_page.add_child(instance=home_page)
            home_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created HomePage: {home_page.title} (slug: {slug})')
            )

        # Update site root page to point to our homepage  
        site.root_page = home_page
        site.save()
        
        # Create Gallery Page as sibling (child of root, not homepage)
        existing_gallery = GalleryPage.objects.filter(slug='galleri').first()
        if not existing_gallery:
            gallery_page = GalleryPage(
                title='Projekt Galleri',
                slug='galleri',
                intro='<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
            )
            root_page.add_child(instance=gallery_page)
            gallery_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created GalleryPage: {gallery_page.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Gallery page already exists')
            )
            gallery_page = existing_gallery

        # Create Contact Page as sibling (child of root, not homepage)  
        existing_contact = ContactPage.objects.filter(slug='kontakt').first()
        if not existing_contact:
            contact_page = ContactPage(
                title='Kontakt Os',
                slug='kontakt',
                intro='<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>',
                contact_form_title='Send os en besked',
                contact_form_intro='<p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>',
            )
            root_page.add_child(instance=contact_page)
            contact_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created ContactPage: {contact_page.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Contact page already exists')
            )
            contact_page = existing_contact
            
        # Create sample projects with stock images
        self.create_sample_projects(site)

        self.stdout.write(
            self.style.SUCCESS(
                f'Default pages setup complete for {company_name}!\n'
                f'Site root page updated to: {home_page.title}'
            )
        )
    
    def create_sample_projects(self, site):
        """Create 4 sample projects with stock images"""
        if Project.objects.filter(site=site).exists():
            self.stdout.write(self.style.WARNING('Sample projects already exist'))
            return
            
        # Sample project data with Lorem Ipsum
        projects_data = [
            {
                'title': 'Villa Moderna',
                'description': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.</p>',
                'materials': 'Træ, Glas, Sten',
                'location': 'København',
                'width': 800,
                'height': 600,
                'color': '#4A90E2'
            },
            {
                'title': 'Traditionelt Hus',
                'description': '<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.</p>',
                'materials': 'Træ, Tegl, Skifer',
                'location': 'Aarhus',
                'width': 600,
                'height': 800,
                'color': '#7ED321'
            },
            {
                'title': 'Moderne Tilbygning',
                'description': '<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.</p>',
                'materials': 'Stål, Glas, Beton',
                'location': 'Odense',
                'width': 1200,
                'height': 400,
                'color': '#F5A623'
            },
            {
                'title': 'Træ Terrasse',
                'description': '<p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores.</p>',
                'materials': 'Lærketræ, Rustfrit stål',
                'location': 'Aalborg',
                'width': 900,
                'height': 600,
                'color': '#BD10E0'
            }
        ]
        
        for i, project_data in enumerate(projects_data, 1):
            # Create a simple colored stock image
            stock_image = self.create_stock_image(
                project_data['width'],
                project_data['height'], 
                project_data['color'],
                f"stock-image-{i}"
            )
            
            # Create project
            project = Project.objects.create(
                site=site,
                title=project_data['title'],
                description=project_data['description'],
                materials=project_data['materials'],
                location=project_data['location'],
                date=date(2024, random.randint(1, 12), random.randint(1, 28)),
                featured=i <= 2,  # First 2 projects are featured
                published=True
            )
            
            # Add image to project
            if stock_image:
                from apps.projects.models import ProjectImage
                ProjectImage.objects.create(
                    project=project,
                    image=stock_image,
                    caption=f'Billede af {project.title}',
                    alt_text=f'Arkitekturbillede af {project.title}'
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created sample project: {project.title}')
            )
    
    def create_stock_image(self, width, height, color, name):
        """Create a simple colored stock image"""
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
                title=f'Stock billede {name}',
                file=image_file
            )
            
            return wagtail_image
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to create stock image {name}: {e}')
            )
            return None