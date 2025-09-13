"""
Management command to populate the site with realistic content for mobile UX testing.
This creates a proper site structure for JCleemannByg construction company.
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from wagtail.models import Site, Page
from apps.pages.models import HomePage, ContactPage, GalleryPage, CompanySettings, DesignSettings
from apps.projects.models import Project
from model_bakery import baker


class Command(BaseCommand):
    help = 'Populate the site with realistic content for mobile UX testing'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write('Setting up JCleemannByg mobile test content...')

            # Get the root page
            root_page = Page.objects.get(depth=1)

            # Delete existing welcome page if it exists
            welcome_pages = Page.objects.filter(title__icontains='Welcome to your new Wagtail')
            for page in welcome_pages:
                if page.depth > 1:  # Don't delete the root
                    page.delete()

            # Create and set up the main site
            site = Site.objects.get(pk=1)

            # Create HomePage
            home_page = HomePage(
                title='JCleemann Byg - Byggeentreprenør i København',
                slug='home',
                seo_title='JCleemann Byg - Professionel byggeentreprenør i København og omegn',
                search_description='Erfaren byggeentreprenør i København. Vi tilbyder nybyggeri, renovering, tilbygninger og håndværkertjenester. Få et uforpligtende tilbud.',
                intro='<p>Velkommen til JCleemann Byg - din pålidelige partner til byggeprojekter i København og omegn.</p>',
                body='[]'  # Empty streamfield initially
            )
            root_page.add_child(instance=home_page)

            # Set as site root
            site.root_page = home_page
            site.save()

            # Create Contact Page
            contact_page = ContactPage(
                title='Kontakt os',
                slug='kontakt',
                seo_title='Kontakt JCleemann Byg - Få et uforpligtende tilbud',
                search_description='Kontakt JCleemann Byg for et uforpligtende tilbud. Ring på tlf: +45 12 34 56 78 eller send en besked.',
                intro='<p>Har du et byggeprojekt? Vi er klar til at hjælpe dig med alt fra små reparationer til store byggeprojekter.</p>',
                show_contact_form=True,
                contact_form_title='Få et uforpligtende tilbud',
                contact_form_intro='<p>Fortæl os om dit projekt, så vender vi tilbage hurtigst muligt med et tilbud.</p>'
            )
            home_page.add_child(instance=contact_page)

            # Create Gallery/Projects Page
            gallery_page = GalleryPage(
                title='Vores projekter',
                slug='projekter',
                seo_title='Se vores gennemførte byggeprojekter - JCleemann Byg',
                search_description='Se eksempler på vores gennemførte byggeprojekter. Nybyggeri, renovering, tilbygninger og meget mere.',
                intro='<p>Se eksempler på vores gennemførte projekter og lad dig inspirere til dit næste byggeprojekt.</p>'
            )
            home_page.add_child(instance=gallery_page)

            # Create sample projects
            project_data = [
                {
                    'title': 'Moderne køkkenrenovering, Østerbro',
                    'description': 'Komplet renovering af køkken i 1930er-villa. Nye skabe, bordplade i granit og integrerede hvidevarer.',
                    'location': 'Østerbro, København',
                    'published': True,
                    'featured': True,
                },
                {
                    'title': 'Tilbygning med terrasse, Frederiksberg',
                    'description': 'Tilbygning af stue og soveværelse med stor terrasse. Glasparti mod haven skaber lyse rum.',
                    'location': 'Frederiksberg',
                    'published': True,
                    'featured': True,
                },
                {
                    'title': 'Badeværelse renovering, Nørrebro',
                    'description': 'Moderne badeværelse med fliser, indbygget douche og undervarme i gulvet.',
                    'location': 'Nørrebro, København',
                    'published': True,
                    'featured': False,
                },
                {
                    'title': 'Nyt tag og tagrender, Vanløse',
                    'description': 'Udskiftning af gammelt eternittag til moderne tegl. Nye tagrender og nedløb.',
                    'location': 'Vanløse',
                    'published': True,
                    'featured': True,
                },
                {
                    'title': 'Komplet hus renovering, Valby',
                    'description': 'Totalrenovering af ældre hus. Nyt køkken, bad, gulve og maling gennem hele huset.',
                    'location': 'Valby',
                    'published': True,
                    'featured': False,
                },
            ]

            for project_info in project_data:
                Project.objects.create(**project_info)

            # Set up Company Settings
            company_settings, created = CompanySettings.objects.get_or_create(
                site=site,
                defaults={
                    'company_name': 'JCleemann Byg',
                    'phone': '+45 12 34 56 78',
                    'email': 'kontakt@jcleemannbyg.dk',
                    'cvr': '12345678',
                    'address': 'Byggevej 123\n2100 København Ø',
                    'footer_description': '<p>JCleemann Byg er din pålidelige byggeentreprenør i København. Vi har over 15 års erfaring med byggeprojekter af alle størrelser.</p>',
                    'copyright_text': '© 2025 JCleemann Byg. Alle rettigheder forbeholdes.',
                }
            )

            # Set up Design Settings with mobile-friendly theme
            design_settings, created = DesignSettings.objects.get_or_create(
                site=site,
                defaults={
                    'theme': 'business',  # Professional theme good for construction
                    'font_choice': 'inter-playfair',
                    'navigation_style': 'horizontal',
                    'show_navigation': True,
                    'header_style': 'standard',
                    'navigation_cta_text': 'Få tilbud',
                }
            )

            # Set navigation CTA to contact page
            design_settings.navigation_cta_page = contact_page
            design_settings.save()

            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully created mobile test content for JCleemannByg!\n'
                    f'- Home page: {home_page.get_url()}\n'
                    f'- Contact page: {contact_page.get_url()}\n'
                    f'- Projects page: {gallery_page.get_url()}\n'
                    f'- Created {len(project_data)} sample projects\n'
                    'Site is ready for mobile UX testing.'
                )
            )