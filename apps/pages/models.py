from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.search import index

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

FONT_CHOICES = [
    ('inter-playfair', 'Inter + Playfair Display (Professionel)'),
    ('inter-georgia', 'Inter + Georgia (Klassisk)'),
    ('system-fonts', 'System skrifttyper (Hurtig)'),
    ('roboto-lora', 'Roboto + Lora (Moderne)'),
    ('open-sans-merriweather', 'Open Sans + Merriweather (Læsbar)'),
]


class HomePage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst")
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("trust_badges", site_blocks.TrustBadgesBlock()),
        ("featured_projects", site_blocks.FeaturedProjectsBlock()),
        ("services_grid_inline", site_blocks.ServicesGridInlineBlock()),
        ("cta", site_blocks.CTABlock()),
        ("features", site_blocks.FeaturesBlock()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("testimonials_snippets", site_blocks.TestimonialsBlock()),
        ("logo_cloud", site_blocks.LogoCloudBlock()),
        ("services_grid", site_blocks.ServicesGridBlock()),
        ("faq", site_blocks.FAQBlock()),
        ("image_gallery", site_blocks.ImageGalleryBlock()),
    ], use_json_field=True, blank=True, verbose_name="Indhold")

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.AutocompleteField('title'),
        index.AutocompleteField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
    
    # Enable PromoteTab functionality
    promote_panels = Page.promote_panels

    class Meta:
        verbose_name = "Hjemmeside"
        verbose_name_plural = "Hjemmesider"

    def get_context(self, request):
        context = super().get_context(request)
        
        # Featured projects for homepage - prefer new ProjectPage model
        featured_project_pages = []
        try:
            # Try to get projects from GalleryPage children (new page-based approach)
            from apps.pages.models import GalleryPage
            gallery_pages = GalleryPage.objects.live().public()
            
            for gallery_page in gallery_pages:
                project_pages = (
                    gallery_page.get_children()
                    .live()
                    .public()
                    .specific()
                    .filter(featured=True)
                    .order_by('-project_date', 'title')
                )
                featured_project_pages.extend(list(project_pages[:6]))
            
            # If we have page-based projects, use them
            if featured_project_pages:
                context['featured_projects'] = featured_project_pages[:6]
            else:
                # Fallback to old Project model during transition
                from apps.projects.models import Project
                qs = Project.objects.filter(published=True, featured=True)
                context['featured_projects'] = qs.order_by('-date', 'title')[:6]
                
        except Exception as e:
            # Final fallback - empty list
            context['featured_projects'] = []
            
        return context


class GalleryPage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst", help_text="Beskriv dine projekter og arbejde")
    
    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.AutocompleteField('title'),
        index.AutocompleteField('intro'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]
    
    # Enable PromoteTab functionality
    promote_panels = Page.promote_panels

    # Define what page types can be children of this page
    subpage_types = ['projects.ProjectPage']

    class Meta:
        verbose_name = "Galleri Side"
        verbose_name_plural = "Galleri Sider"

    def get_context(self, request):
        context = super().get_context(request)
        
        # Get child ProjectPage instances using Wagtail's page tree
        project_pages = list(
            self.get_children()
            .live()
            .public()
            .specific()
        )
        
        # Apply filters on the specific instances
        featured_filter = request.GET.get('featured')
        tag_filter = request.GET.get('tag')
        
        if featured_filter == 'true':
            project_pages = [p for p in project_pages if hasattr(p, 'featured') and p.featured]
        
        if tag_filter:
            project_pages = [p for p in project_pages if hasattr(p, 'tags') and p.tags.filter(name=tag_filter).exists()]
        
        # Sort by project_date (newest first), then by title
        project_pages.sort(key=lambda p: (
            p.project_date if hasattr(p, 'project_date') and p.project_date else '1900-01-01',
            p.title
        ), reverse=True)
        
        context['project_pages'] = project_pages
        context['tag_filter'] = tag_filter
        context['featured_filter'] = featured_filter
        
        # Also provide backwards compatibility with old Project model for transition
        try:
            from apps.projects.models import Project
            old_projects = Project.objects.filter(published=True).order_by('-date', 'title')
            context['old_projects'] = old_projects
        except Exception:
            context['old_projects'] = []
        
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

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('contact_form_title'),
        index.SearchField('contact_form_intro'),
        index.AutocompleteField('title'),
        index.AutocompleteField('contact_form_title'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("show_contact_form"),
        FieldPanel("contact_form_title"),
        FieldPanel("contact_form_intro"),
    ]
    
    # Enable PromoteTab functionality
    promote_panels = Page.promote_panels

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

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.AutocompleteField('title'),
        index.AutocompleteField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
    
    # Enable PromoteTab functionality
    promote_panels = Page.promote_panels

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
    font_choice = models.CharField(
        max_length=30, choices=FONT_CHOICES, default='inter-playfair',
        verbose_name="Skrifttype", help_text="Skrifttype kombination for websitet"
    )
    
    # Preview Settings
    enable_preview = models.BooleanField(
        default=True,
        verbose_name="Aktivér forhåndsvisning",
        help_text="Tillad forhåndsvisning af ændringer før de publiceres"
    )
    preview_url_override = models.CharField(
        max_length=255, blank=True,
        verbose_name="Forhåndsvisning URL",
        help_text="Valgfri specifik URL for forhåndsvisning (lad være tom for standard)"
    )
    
    # Navigation settings
    show_navigation = models.BooleanField(
        default=True,
        verbose_name="Vis navigation", 
        help_text="Vis hovednavigation i headeren"
    )
    navigation_cta_text = models.CharField(
        max_length=100, blank=True,
        verbose_name="Navigation CTA tekst",
        help_text="Tekst for CTA knap i navigation (fx 'Få et tilbud')"
    )
    navigation_cta_page = models.ForeignKey(
        'wagtailcore.Page', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Navigation CTA side",
        help_text="Side som CTA knap linker til"
    )
    
    # Footer content
    footer_description = RichTextField(
        blank=True,
        verbose_name="Footer beskrivelse",
        help_text="Beskrivelse af firmaet i footer"
    )
    footer_contact_title = models.CharField(
        max_length=100, default="Kontakt",
        verbose_name="Footer kontakt titel"
    )
    footer_services_title = models.CharField(
        max_length=100, default="Services", blank=True,
        verbose_name="Footer services titel (deprecated)"
    )
    footer_cta_title = models.CharField(
        max_length=100, default="Klar til at starte?", blank=True,
        verbose_name="Footer CTA titel",
        help_text="Call-to-action titel i footer"
    )
    footer_cta_text = models.CharField(
        max_length=255, default="Kontakt os i dag for et uforpligtende tilbud på dit projekt.", blank=True,
        verbose_name="Footer CTA tekst",
        help_text="Call-to-action beskrivelse i footer"
    )
    footer_cta_button_text = models.CharField(
        max_length=50, default="Få et tilbud", blank=True,
        verbose_name="Footer CTA knap tekst"
    )
    opening_hours = models.TextField(
        blank=True, default="",
        verbose_name="Åbningstider",
        help_text="Åbningstider der vises i footer (en linje per dag)"
    )
    facebook_url = models.URLField(
        blank=True, null=True,
        verbose_name="Facebook URL"
    )
    instagram_url = models.URLField(
        blank=True, null=True,
        verbose_name="Instagram URL"
    )
    linkedin_url = models.URLField(
        blank=True, null=True,
        verbose_name="LinkedIn URL"
    )
    copyright_text = models.CharField(
        max_length=255, blank=True,
        verbose_name="Copyright tekst",
        help_text="Tekst i bunden af footer (fx '© 2025 Company Name. Alle rettigheder forbeholdes.')"
    )

    panels = [
        # Company Information
        FieldPanel("company_name"),
        FieldPanel("logo"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("cvr"),
        FieldPanel("address"),
        FieldPanel("opening_hours"),
        
        # Design & Layout
        FieldPanel("default_theme"),
        FieldPanel("font_choice"),
        FieldPanel("enable_preview"),
        FieldPanel("preview_url_override"),
        
        # Navigation
        FieldPanel("show_navigation"),
        FieldPanel("navigation_cta_text"),
        FieldPanel("navigation_cta_page"),
        
        # Footer
        FieldPanel("footer_description"),
        FieldPanel("footer_contact_title"),
        FieldPanel("footer_cta_title"),
        FieldPanel("footer_cta_text"),
        FieldPanel("footer_cta_button_text"),
        
        # Social Media
        FieldPanel("facebook_url"),
        FieldPanel("instagram_url"),
        FieldPanel("linkedin_url"),
        FieldPanel("copyright_text"),
    ]

    class Meta:
        verbose_name = "Generelle indstillinger"
        verbose_name_plural = "Generelle indstillinger"


# Reusable snippets for modular components
@register_snippet
class Testimonial(index.Indexed, models.Model):
    name = models.CharField(max_length=120)
    quote = models.TextField()
    role = models.CharField(max_length=120, blank=True)

    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.SearchField('quote'),
        index.SearchField('role'),
        index.AutocompleteField('name'),
    ]

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
class Logo(index.Indexed, models.Model):
    title = models.CharField(max_length=120)
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    url = models.URLField(blank=True)

    # Search index configuration
    search_fields = [
        index.SearchField('title'),
        index.AutocompleteField('title'),
    ]

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
class Service(index.Indexed, models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    # Search index configuration
    search_fields = [
        index.SearchField('title'),
        index.SearchField('description'),
        index.AutocompleteField('title'),
    ]

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
    ]

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


