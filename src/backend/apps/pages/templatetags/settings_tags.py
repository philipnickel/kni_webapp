from django import template
from django.core.cache import cache
from ..models import HeaderSettings, FooterSettings, DesignPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_header_settings(context):
    """Get the first available header settings or create default"""
    cache_key = 'header_settings'
    header_settings = cache.get(cache_key)
    
    if header_settings is None:
        try:
            header_settings = HeaderSettings.objects.first()
            if not header_settings:
                # Create default header settings
                header_settings = HeaderSettings.objects.create(
                    name="Default Header",
                    header_style="standard",
                    primary_color="#4d7a3a",
                    secondary_color="#6b7280",
                    background_color="#ffffff",
                    text_color="#111827",
                    show_search=True,
                    show_theme_toggle=True,
                    show_cta_button=False,
                    cta_button_text="Kontakt os",
                    cta_button_url="/kontakt/",
                    mobile_menu_style="slide",
                    sticky_header=True,
                    header_height="h-16"
                )
            cache.set(cache_key, header_settings, 300)  # Cache for 5 minutes
        except Exception:
            # Fallback to a mock object with default values
            class MockHeaderSettings:
                def __init__(self):
                    self.name = "Default Header"
                    self.header_style = "standard"
                    self.primary_color = "#4d7a3a"
                    self.secondary_color = "#6b7280"
                    self.background_color = "#ffffff"
                    self.text_color = "#111827"
                    self.surface_color = "#f9fafb"
                    self.show_search = True
                    self.show_theme_toggle = True
                    self.show_cta_button = False
                    self.cta_button_text = "Kontakt os"
                    self.cta_button_url = "/kontakt/"
                    self.mobile_menu_style = "slide"
                    self.sticky_header = True
                    self.header_height = "h-16"
            
            header_settings = MockHeaderSettings()
    
    return header_settings


@register.simple_tag(takes_context=True)
def get_footer_settings(context):
    """Get the first available footer settings or create default"""
    cache_key = 'footer_settings'
    footer_settings = cache.get(cache_key)
    
    if footer_settings is None:
        try:
            footer_settings = FooterSettings.objects.first()
            if not footer_settings:
                # Create default footer settings
                footer_settings = FooterSettings.objects.create(
                    name="Default Footer",
                    footer_style="standard",
                    background_color="#111827",
                    text_color="#9ca3af",
                    heading_color="#ffffff",
                    link_color="#d1d5db",
                    show_company_info=True,
                    show_social_links=True,
                    show_quick_links=True,
                    show_newsletter_signup=False,
                    newsletter_title="Tilmeld dig vores nyhedsbrev",
                    newsletter_description="Få de seneste nyheder og tilbud direkte i din indbakke.",
                    copyright_text="© 2025 JCleemann Byg. Alle rettigheder forbeholdes.",
                    footer_height="auto"
                )
            cache.set(cache_key, footer_settings, 300)  # Cache for 5 minutes
        except Exception:
            # Fallback to a mock object with default values
            class MockFooterSettings:
                def __init__(self):
                    self.name = "Default Footer"
                    self.footer_style = "standard"
                    self.background_color = "#111827"
                    self.text_color = "#9ca3af"
                    self.heading_color = "#ffffff"
                    self.link_color = "#d1d5db"
                    self.show_company_info = True
                    self.show_social_links = True
                    self.show_quick_links = True
                    self.show_newsletter_signup = False
                    self.newsletter_title = "Tilmeld dig vores nyhedsbrev"
                    self.newsletter_description = "Få de seneste nyheder og tilbud direkte i din indbakke."
                    self.copyright_text = "© 2025 JCleemann Byg. Alle rettigheder forbeholdes."
                    self.footer_height = "auto"
            
            footer_settings = MockFooterSettings()
    
    return footer_settings


@register.simple_tag(takes_context=True)
def get_design_settings(context):
    """Get the first available design settings page or return default"""
    cache_key = 'design_settings'
    design_settings = cache.get(cache_key)
    
    if design_settings is None:
        try:
            # Get the first live DesignPage
            design_settings = DesignPage.objects.live().first()
            if design_settings:
                cache.set(cache_key, design_settings, 300)  # Cache for 5 minutes
            else:
                # Fallback to a mock object with default values
                class MockDesignSettings:
                    def __init__(self):
                        self.title = "Default Design"
                        self.primary_color = "#4d7a3a"
                        self.secondary_color = "#6b7280"
                        self.accent_color = "#f59e0b"
                        self.success_color = "#10b981"
                        self.warning_color = "#f59e0b"
                        self.error_color = "#ef4444"
                        self.background_color = "#ffffff"
                        self.surface_color = "#f9fafb"
                        self.text_primary = "#111827"
                        self.text_secondary = "#6b7280"
                        self.enable_color_preview = True
                
                design_settings = MockDesignSettings()
        except Exception:
            # Fallback to a mock object with default values
            class MockDesignSettings:
                def __init__(self):
                    self.title = "Default Design"
                    self.primary_color = "#4d7a3a"
                    self.secondary_color = "#6b7280"
                    self.accent_color = "#f59e0b"
                    self.success_color = "#10b981"
                    self.warning_color = "#f59e0b"
                    self.error_color = "#ef4444"
                    self.background_color = "#ffffff"
                    self.surface_color = "#f9fafb"
                    self.text_primary = "#111827"
                    self.text_secondary = "#6b7280"
                    self.enable_color_preview = True
            
            design_settings = MockDesignSettings()
    
    return design_settings
