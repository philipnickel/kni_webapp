def site_settings(request):
    """
    Add site settings to template context.
    This makes company information and logo available in all templates.
    """
    try:
        from django.contrib.sites.shortcuts import get_current_site
        from .wagtailsettings import SiteSettings
        
        current_site = get_current_site(request)
        settings = SiteSettings.for_site(current_site)
        
        return {
            'site_settings': settings,
        }
    except Exception:
        # Return default values if there's any issue
        return {
            'site_settings': None,
        }