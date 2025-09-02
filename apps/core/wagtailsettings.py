from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    primary_color = models.CharField(max_length=7, default="#0ea5e9")
    secondary_color = models.CharField(max_length=7, default="#111827")
    font_choice = models.CharField(
        max_length=32,
        choices=[("sans", "Sans"), ("serif", "Serif"), ("display", "Display")],
        default="sans",
    )

    company_name = models.CharField(max_length=255, blank=True)
    cvr = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("logo"),
            FieldPanel("primary_color"),
            FieldPanel("secondary_color"),
            FieldPanel("font_choice"),
        ], heading="Brand Kit"),
        MultiFieldPanel([
            FieldPanel("company_name"),
            FieldPanel("cvr"),
            FieldPanel("phone"),
            FieldPanel("email"),
            FieldPanel("address"),
        ], heading="Footer / NAP / CVR"),
    ]
