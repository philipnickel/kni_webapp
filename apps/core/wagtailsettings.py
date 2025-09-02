from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel


@register_setting
class SiteSettings(BaseSiteSetting):
    # Logo
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Upload dit firmalogo"
    )
    
    # Company information
    company_name = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Firmanavn',
        help_text='Dit officielle firmanavn'
    )
    cvr = models.CharField(
        max_length=64, 
        blank=True,
        verbose_name='CVR-nummer',
        help_text='Dit CVR-nummer (valgfrit)'
    )
    phone = models.CharField(
        max_length=64, 
        blank=True,
        verbose_name='Telefonnummer',
        help_text='Hovedtelefonnummer til dit firma'
    )
    email = models.EmailField(
        blank=True,
        verbose_name='Email',
        help_text='Kontakt email-adresse'
    )
    address = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Adresse',
        help_text='Firmaets adresse'
    )

    panels = [
        FieldPanel("logo"),
        FieldPanel("company_name"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("cvr"),
    ]

    class Meta:
        verbose_name = 'Website Indstillinger'
        verbose_name_plural = 'Website Indstillinger'
