from wagtail.contrib.settings.context_processors import SettingsProxy
from wagtail.models import Site


class SafeSettingsProxy(SettingsProxy):
    """
    A SettingsProxy that always tries to use the default site if no site is provided
    or if there's no request context available.
    """
    
    def __init__(self, site=None, use_default_site=True):
        if site is None and use_default_site:
            try:
                site = Site.objects.get(is_default_site=True)
            except Site.DoesNotExist:
                site = Site.objects.first()
        super().__init__(site, use_default_site=use_default_site)

    def get_setting(self, model_name):
        """Override get_setting to always use default site if needed."""
        try:
            return super().get_setting(model_name)
        except RuntimeError as e:
            if "request is not available" in str(e):
                # If we can't get the site from request, use the default site
                try:
                    site = Site.objects.get(is_default_site=True)
                except Site.DoesNotExist:
                    site = Site.objects.first()
                
                # Create a new proxy with the default site
                safe_proxy = SafeSettingsProxy(site, use_default_site=True)
                return safe_proxy.get_setting(model_name)
            raise


def settings(request):
    """
    Custom settings context processor that uses SafeSettingsProxy.
    """
    try:
        # Try to get the site from the request first
        if hasattr(request, 'site'):
            site = request.site
        else:
            # Fall back to the default site
            site = None  # Let SafeSettingsProxy handle this
        
        return {
            'settings': SafeSettingsProxy(site),
        }
    except Exception:
        # If we can't get any site, return empty settings
        return {
            'settings': {},
        }