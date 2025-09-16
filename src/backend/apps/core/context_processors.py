from wagtail.models import Site


def settings(request):
    """
    Custom settings context processor that provides company_settings, design_settings, header_settings, footer_settings, and navigation_links.
    """
    try:
        # Import here to avoid circular imports
        from apps.pages.models import CompanySettings, DesignPage, HeaderSettings, FooterSettings, NavigationLink
        
        # Get the site using Wagtail's site detection
        site = Site.find_for_request(request)
        
        # Get the settings for the site
        try:
            company_settings = CompanySettings.for_site(site) if site else CompanySettings.objects.first()
        except:
            company_settings = None
            
        try:
            design_settings = DesignPage.objects.live().first()
        except:
            design_settings = None
            
        try:
            header_settings = HeaderSettings.objects.first()
        except:
            header_settings = None
            
        try:
            footer_settings = FooterSettings.objects.first()
        except:
            footer_settings = None
            
        try:
            navigation_links = NavigationLink.objects.all().order_by('order', 'name')
        except:
            navigation_links = []
        
        return {
            'company_settings': company_settings,
            'design_settings': design_settings,
            'header_settings': header_settings,
            'footer_settings': footer_settings,
            'navigation_links': navigation_links,
        }
    except Exception:
        # If we can't get any site, return empty settings
        return {
            'company_settings': None,
            'design_settings': None,
            'header_settings': None,
            'footer_settings': None,
            'navigation_links': [],
        }