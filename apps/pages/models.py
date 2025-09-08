from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from . import blocks as site_blocks


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    subheading = blocks.TextBlock(required=False)
    cta_text = blocks.CharBlock(required=False, help_text="Button text")
    cta_anchor = blocks.CharBlock(required=False, help_text="Anchor id to scroll to")

    class Meta:
        icon = "placeholder"
        label = "Hero"
        template = "blocks/hero.html"


class TrustBadge(blocks.StructBlock):
    label = blocks.CharBlock()
    description = blocks.CharBlock(required=False)


class FeaturedProject(blocks.StructBlock):
    project_slug = blocks.CharBlock(help_text="Slug of a Project to feature")


THEME_CHOICES = [
    ('forest', 'Forest'),
    ('wood', 'Wood'),
    ('slate', 'Slate'),
]


class HomePage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst")
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("cta", site_blocks.CTABlock()),
        ("features", site_blocks.FeaturesBlock()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("testimonials_snippets", site_blocks.TestimonialsBlock()),
        ("logo_cloud", site_blocks.LogoCloudBlock()),
        ("services_grid", site_blocks.ServicesGridBlock()),
        ("services_grid_inline", site_blocks.ServicesGridInlineBlock()),
        ("faq", site_blocks.FAQBlock()),
        ("image_gallery", site_blocks.ImageGalleryBlock()),
    ], use_json_field=True, blank=True, verbose_name="Indhold")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Hjemmeside"
        verbose_name_plural = "Hjemmesider"

    def get_context(self, request):
        context = super().get_context(request)
        # Featured projects for homepage
        try:
            from apps.projects.models import Project
            current_site = getattr(request, 'site', None)
            qs = Project.objects.filter(published=True, featured=True)
            if current_site is not None:
                qs = qs.filter(site=current_site)
            context['featured_projects'] = qs.order_by('-date', 'title')[:6]
        except Exception:
            context['featured_projects'] = []
        return context


class GalleryPage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst", help_text="Beskriv dine projekter og arbejde")
    
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Galleri Side"
        verbose_name_plural = "Galleri Sider"

    def get_context(self, request):
        context = super().get_context(request)
        # Get all projects to display in gallery
        from apps.projects.models import Project
        context['projects'] = Project.objects.filter(published=True).order_by('-date', 'title')
        return context


class ContactPage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst")
    show_contact_form = models.BooleanField(
        default=True, 
        verbose_name="Vis kontakt formular",
        help_text="Vis kontakt formularen på siden"
    )
    contact_form_title = models.CharField(
        max_length=255, 
        default="Kontakt os",
        verbose_name="Formular titel"
    )
    contact_form_intro = RichTextField(
        blank=True,
        verbose_name="Formular intro tekst",
        help_text="Tekst der vises over kontakt formularen"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("show_contact_form"),
        FieldPanel("contact_form_title"),
        FieldPanel("contact_form_intro"),
    ]

    class Meta:
        verbose_name = "Kontakt Side"
        verbose_name_plural = "Kontakt Sider"


class ModularPage(Page):
    template = "pages/modular_page.html"
    intro = RichTextField(blank=True, verbose_name="Intro tekst", help_text="Valgfrit indhold før sektioner")
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("cta", site_blocks.CTABlock()),
        ("features", site_blocks.FeaturesBlock()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("testimonials_snippets", site_blocks.TestimonialsBlock()),
        ("logo_cloud", site_blocks.LogoCloudBlock()),
        ("services_grid", site_blocks.ServicesGridBlock()),
        ("services_grid_inline", site_blocks.ServicesGridInlineBlock()),
        ("faq", site_blocks.FAQBlock()),
        ("image_gallery", site_blocks.ImageGalleryBlock()),
    ], use_json_field=True, blank=True, verbose_name="Indhold")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Modul side"
        verbose_name_plural = "Modul sider"


@register_setting
class SiteSettings(BaseSiteSetting):
    # Company Information
    company_name = models.CharField(
        max_length=255, default="JCleemann Byg",
        verbose_name="Firmanavn", help_text="Navn der vises på websitet"
    )
    logo = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Logo", help_text="Firmalogo der vises i headeren"
    )
    
    # Contact Information
    phone = models.CharField(
        max_length=50, blank=True,
        verbose_name="Telefonnummer"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="Email adresse"
    )
    cvr = models.CharField(
        max_length=20, blank=True,
        verbose_name="CVR nummer"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Adresse"
    )
    
    # Theme Settings
    default_theme = models.CharField(
        max_length=20, choices=THEME_CHOICES, default='forest',
        verbose_name="Standard tema", help_text="Tema for hele websitet"
    )

    panels = [
        FieldPanel("company_name"),
        FieldPanel("logo"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("cvr"),
        FieldPanel("address"),
        FieldPanel("default_theme"),
    ]

    class Meta:
        verbose_name = "Generelle indstillinger"
        verbose_name_plural = "Generelle indstillinger"


# Reusable snippets for modular components
@register_snippet
class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    quote = models.TextField()
    role = models.CharField(max_length=120, blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("role"),
        FieldPanel("quote"),
    ]

    class Meta:
        verbose_name = "Udtalelse"
        verbose_name_plural = "Udtalelser"

    def __str__(self):
        return f"{self.name} — {self.quote[:40]}…"


@register_snippet
class Logo(models.Model):
    title = models.CharField(max_length=120)
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    url = models.URLField(blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel("url"),
    ]

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logoer"

    def __str__(self):
        return self.title


@register_snippet
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
    ]

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
