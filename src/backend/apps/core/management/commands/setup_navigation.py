from django.core.management.base import BaseCommand
from apps.pages.models import NavigationLink, HeaderSettings, FooterSettings


class Command(BaseCommand):
    help = 'Set up default navigation links and header/footer settings'

    def handle(self, *args, **options):
        self.stdout.write('Setting up default navigation...')
        
        # Create default navigation links
        default_links = [
            {'name': 'Galleri', 'url': '/galleri/', 'order': 1, 'show_in_header': True, 'show_in_footer': True},
            {'name': 'Om Os', 'url': '/om-os/', 'order': 2, 'show_in_header': True, 'show_in_footer': True},
            {'name': 'FAQ', 'url': '/faq/', 'order': 3, 'show_in_header': True, 'show_in_footer': True},
            {'name': 'Kontakt', 'url': '/kontakt/', 'order': 4, 'show_in_header': True, 'show_in_footer': True},
        ]
        
        for link_data in default_links:
            link, created = NavigationLink.objects.get_or_create(
                name=link_data['name'],
                defaults=link_data
            )
            if created:
                self.stdout.write(f'Created navigation link: {link.name}')
            else:
                self.stdout.write(f'Navigation link already exists: {link.name}')
        
        # Create default header settings
        header_settings, created = HeaderSettings.objects.get_or_create(
            name='Standard Header',
            defaults={
                'header_style': 'standard',
                'show_search': True,
                'show_theme_toggle': True,
                'show_cta_button': False,
                'cta_button_text': 'Kontakt os',
                'cta_button_url': '/kontakt/',
                'mobile_menu_style': 'slide',
                'sticky_header': True,
                'header_height': 'h-16',
            }
        )
        if created:
            self.stdout.write('Created default header settings')
        else:
            self.stdout.write('Header settings already exist')
        
        # Create default footer settings
        footer_settings, created = FooterSettings.objects.get_or_create(
            name='Standard Footer',
            defaults={
                'footer_style': 'standard',
                'show_company_info': True,
                'show_social_links': True,
                'show_quick_links': True,
                'show_newsletter_signup': False,
                'newsletter_title': 'Tilmeld dig vores nyhedsbrev',
                'newsletter_description': 'Få de seneste nyheder og tilbud direkte i din indbakke.',
                'copyright_text': '© 2025 JCleemann Byg. Alle rettigheder forbeholdes.',
                'footer_height': 'auto',
            }
        )
        if created:
            self.stdout.write('Created default footer settings')
        else:
            self.stdout.write('Footer settings already exist')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully set up default navigation!')
        )
