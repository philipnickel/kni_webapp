from wagtail.models import Site


def settings(request):
    """
    Custom settings context processor that provides company_settings and design_settings.
    """
    try:
        # Try to get the site from the request first
        if hasattr(request, 'site'):
            site = request.site
        else:
            # Fall back to the default site
            site = None  # Let SafeSettingsProxy handle this
        
        # Import here to avoid circular imports
        from apps.pages.models import CompanySettings, DesignSettings
        
        # Get the new separate settings
        try:
            company_settings = CompanySettings.for_site(site) if site else CompanySettings.objects.first()
        except:
            company_settings = None
            
        try:
            design_settings = DesignSettings.for_site(site) if site else DesignSettings.objects.first()
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