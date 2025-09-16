from django import template
from django.utils import timezone
import hashlib

register = template.Library()


@register.simple_tag(takes_context=True)
def theme_cache_bust(context):
    """
    Generate a cache-busting parameter that changes when the theme changes.
    Uses theme name + current hour to ensure cache busting when theme changes
    but doesn't change too frequently.
    """
    design_settings = context.get('design_settings')
    if design_settings and hasattr(design_settings, 'theme'):
        theme = design_settings.theme
    else:
        theme = 'tailwind'
    
    # Use current hour to create a cache-busting parameter that changes periodically
    current_hour = timezone.now().strftime('%Y%m%d%H')
    
    # Create a hash of theme + hour for a stable but changing cache-bust parameter
    cache_string = f"{theme}-{current_hour}"
    cache_hash = hashlib.md5(cache_string.encode()).hexdigest()[:8]
    
    return f"{theme}-{cache_hash}"


@register.simple_tag(takes_context=True)
def theme_timestamp(context):
    """
    Generate a timestamp-based cache-busting parameter for immediate cache invalidation.
    Use this for development or when you need immediate cache busting.
    """
    design_settings = context.get('design_settings')
    if design_settings and hasattr(design_settings, 'theme'):
        theme = design_settings.theme
    else:
        theme = 'tailwind'
    
    # Use current timestamp for immediate cache busting
    timestamp = int(timezone.now().timestamp())
    
    return f"{theme}-{timestamp}"
