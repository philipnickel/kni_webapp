from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from wagtail.models import Page
from apps.pages.models import HomePage, GalleryPage, ContactPage


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
        root_page = Page.objects.get(id=1)
        
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
            
            # Create HomePage
            home_page = HomePage(
                title=f'Velkommen til {company_name}',
                slug=slug,
                intro=f'<p>Velkommen til {company_name} - din lokale byggeentreprenør.</p>',
            )
            root_page.add_child(instance=home_page)
            home_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created HomePage: {home_page.title} (slug: {slug})')
            )

        # Update site root page to point to our homepage
        site.root_page = home_page
        site.save()
        
        # Create Gallery Page
        existing_gallery = GalleryPage.objects.filter(slug='galleri').first()
        if not existing_gallery:
            gallery_page = GalleryPage(
                title='Projekt Galleri',
                slug='galleri',
                intro=f'<p>Se vores tidligere projekter og få inspiration til dit næste byggeprojekt.</p>',
            )
            home_page.add_child(instance=gallery_page)
            gallery_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created GalleryPage: {gallery_page.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Gallery page already exists')
            )

        # Create Contact Page
        existing_contact = ContactPage.objects.filter(slug='kontakt').first()
        if not existing_contact:
            contact_page = ContactPage(
                title='Kontakt Os',
                slug='kontakt',
                intro=f'<p>Kontakt {company_name} i dag for et uforpligtende tilbud på dit næste byggeprojekt.</p>',
                contact_form_title='Send os en besked',
                contact_form_intro='<p>Udfyld formularen nedenfor, så vender vi tilbage hurtigst muligt.</p>',
            )
            home_page.add_child(instance=contact_page)
            contact_page.save_revision().publish()
            self.stdout.write(
                self.style.SUCCESS(f'Created ContactPage: {contact_page.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Contact page already exists')
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Default pages setup complete for {company_name}!\n'
                f'Site root page updated to: {home_page.title}'
            )
        )