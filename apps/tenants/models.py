from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Theme(models.Model):
    """
    Database-stored theme system for easy admin management
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Theme Name",
        help_text="e.g. 'Forest Green', 'Wood Brown'"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Theme Slug",
        help_text="e.g. 'forest', 'wood' - used in CSS"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Description of this theme"
    )
    
    # CSS Variables
    primary_color = models.CharField(
        max_length=7,
        default="#4d7a3a",
        verbose_name="Primary Color",
        help_text="Hex color code (e.g. #4d7a3a)"
    )
    primary_hover_color = models.CharField(
        max_length=7,
        default="#3a5e2c", 
        verbose_name="Primary Hover Color",
        help_text="Hex color code for hover state"
    )
    hero_start_color = models.CharField(
        max_length=7,
        default="#3a5e2c",
        verbose_name="Hero Gradient Start",
        help_text="Hero section gradient start color"
    )
    hero_end_color = models.CharField(
        max_length=7,
        default="#654e33",
        verbose_name="Hero Gradient End", 
        help_text="Hero section gradient end color"
    )
    footer_bg_color = models.CharField(
        max_length=7,
        default="#3d251b",
        verbose_name="Footer Background",
        help_text="Footer background color"
    )
    footer_text_color = models.CharField(
        max_length=7,
        default="#e9e3d9",
        verbose_name="Footer Text",
        help_text="Footer text color"
    )
    
    # System fields
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this theme is available for selection"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def to_css_vars(self):
        """Convert theme to CSS variables dict"""
        return {
            '--color-primary': self.primary_color,
            '--color-primary-hover': self.primary_hover_color,
            '--color-hero-start': self.hero_start_color, 
            '--color-hero-end': self.hero_end_color,
            '--color-footer-bg': self.footer_bg_color,
            '--color-footer-text': self.footer_text_color,
        }


class Client(TenantMixin):
    """
    Tenant model for each construction business client
    """
    name = models.CharField(
        max_length=255,
        verbose_name="Business Name",
        help_text="e.g. 'JCleemann Byg', 'Peters Construction'"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Business Description",
        help_text="Brief description of the construction business"
    )
    contact_email = models.EmailField(
        blank=True,
        verbose_name="Contact Email",
        help_text="Primary contact email for this business"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone Number",
        help_text="Primary contact phone number"
    )
    
    # Theme and branding
    theme = models.ForeignKey(
        Theme,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Website Theme",
        help_text="Visual theme for this tenant's website"
    )
    
    # Business details
    cvr_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="CVR Number",
        help_text="Danish CVR business registration number"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Business Address",
        help_text="Physical business address"
    )
    
    # System fields
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this tenant is active and accessible"
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created On"
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated On"
    )
    
    # Disable automatic schema creation to avoid migration conflicts
    auto_create_schema = False

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    @property
    def primary_domain(self):
        """Get the primary domain for this tenant"""
        return self.domains.filter(is_primary=True).first()


class Domain(DomainMixin):
    """
    Domain model to map domains to tenants
    """
    pass
    
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
    
    def __str__(self):
        return f"{self.domain} ({'primary' if self.is_primary else 'secondary'})"