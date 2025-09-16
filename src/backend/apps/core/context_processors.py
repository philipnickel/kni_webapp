from wagtail.models import Site


def settings(request):
    """
    Custom settings context processor that provides company_settings and design_settings.
    """
    try:
        # Import here to avoid circular imports
        from apps.pages.models import CompanySettings, DesignPage
        
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
        
        return {
            'company_settings': company_settings,
            'design_settings': design_settings,
        }
    except Exception:
        # If we can't get any site, return empty settings
        return {
            'company_settings': None,
            'design_settings': None,
        }