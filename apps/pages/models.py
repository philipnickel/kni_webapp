from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.forms import widgets
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, Panel
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
    # Construction-appropriate DaisyUI themes
    ('light', 'Light - Klassisk lyst design'),
    ('corporate', 'Corporate - Professionelt design'),
    ('business', 'Business - Elegant forretningsdesign'),
    ('emerald', 'Emerald - Naturligt og miljøvenligt design'),
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
        ("modern_hero", site_blocks.ModernHeroBlock()),
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
        
        # Featured projects for homepage - use Project model only
        from apps.projects.models import Project
        qs = Project.objects.filter(published=True, featured=True)
        context['featured_projects'] = qs.order_by('-date', 'title')[:6]
            
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
    # No subpages - projects are managed as snippets, not pages
    subpage_types = []

    class Meta:
        verbose_name = "Galleri Side"
        verbose_name_plural = "Galleri Sider"

    def get_context(self, request):
        context = super().get_context(request)
        
        # Import here to avoid circular imports
        from apps.projects.models import Project
        
        # Get published Project instances (not ProjectPage)
        projects = Project.objects.filter(published=True)
        
        # Apply filters
        featured_filter = request.GET.get('featured')
        tag_filter = request.GET.get('tag')
        
        if featured_filter == 'true':
            projects = projects.filter(featured=True)
        
        if tag_filter:
            projects = projects.filter(tags__name=tag_filter)
        
        # Sort by date (newest first), then by title
        projects = projects.order_by('-date', 'title')
        
        context['project_pages'] = projects  # Keep same variable name for template compatibility
        context['tag_filter'] = tag_filter
        context['featured_filter'] = featured_filter
        
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
        ("modern_hero", site_blocks.ModernHeroBlock()),
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


# Company Settings - Separate from design settings
@register_setting
class CompanySettings(BaseSiteSetting):
    """Company information and contact details"""
    
    company_name = models.CharField(
        max_length=255, default="JCleemann Byg",
        verbose_name="Firmanavn", 
        help_text="Navn der vises på websitet"
    )
    logo = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Logo", 
        help_text="Firmalogo der vises i headeren"
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
    
    # Footer content
    footer_description = RichTextField(
        blank=True,
        verbose_name="Footer beskrivelse",
        help_text="Beskrivelse af firmaet i footer"
    )
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    
    # Google Maps settings
    show_google_maps = models.BooleanField(
        default=True,
        verbose_name="Vis Google Maps",
        help_text="Vis Google Maps widget i footer"
    )
    google_maps_api_key = models.CharField(
        max_length=255, blank=True,
        verbose_name="Google Maps API nøgle",
        help_text="API nøgle til Google Maps (krævet for at vise kort)"
    )
    
    # Copyright
    copyright_text = models.CharField(
        max_length=255, blank=True,
        verbose_name="Copyright tekst",
        help_text="Tekst i bunden af footer (fx '© 2025 Company Name. Alle rettigheder forbeholdes.')"
    )

    panels = [
        FieldPanel("company_name"),
        FieldPanel("logo"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("cvr"),
        FieldPanel("address"),
        FieldPanel("footer_description"),
        FieldPanel("facebook_url"),
        FieldPanel("instagram_url"),
        FieldPanel("linkedin_url"),
        FieldPanel("show_google_maps"),
        FieldPanel("google_maps_api_key"),
        FieldPanel("copyright_text"),
    ]


# Design Settings - Theme and navigation customization
@register_setting
class DesignSettings(BaseSiteSetting):
    """Website design, theme, and navigation settings"""
    
    # Theme Selection
    theme = models.CharField(
        max_length=20, choices=THEME_CHOICES, default='light',
        verbose_name="Tema", 
        help_text="Vælg det visuelle tema for dit website"
    )
    
    # Font Settings
    font_choice = models.CharField(
        max_length=30, choices=FONT_CHOICES, default='inter-playfair',
        verbose_name="Skrifttype", 
        help_text="Skrifttype kombination for websitet"
    )
    
    # Navigation Settings
    NAVIGATION_STYLE_CHOICES = [
        ('horizontal', 'Horisontal navigation'),
        ('dropdown', 'Dropdown navigation'),
        ('minimal', 'Minimal navigation'),
        ('centered', 'Centreret navigation'),
    ]
    
    navigation_style = models.CharField(
        max_length=30,
        choices=NAVIGATION_STYLE_CHOICES,
        default='horizontal',
        verbose_name="Navigation stil",
        help_text="Hvordan skal navigationen se ud"
    )
    
    show_navigation = models.BooleanField(
        default=True,
        verbose_name="Vis navigation", 
        help_text="Vis hovednavigation i headeren"
    )
    
    show_search_in_nav = models.BooleanField(
        default=False,
        verbose_name="Vis søg i navigation",
        help_text="Vis søgefelt i navigation"
    )
    
    # Header Settings
    header_style = models.CharField(
        max_length=20, choices=[
            ('standard', 'Standard'),
            ('minimal', 'Minimal'),
            ('centered', 'Centreret'),
        ], default='standard',
        verbose_name="Header stil",
        help_text="Stil for headeren"
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

    panels = [
        FieldPanel("theme"),
        FieldPanel("font_choice"),
        FieldPanel("navigation_style"),
        FieldPanel("show_navigation"),
        FieldPanel("show_search_in_nav"),
        FieldPanel("header_style"),
        FieldPanel("navigation_cta_text"),
        FieldPanel("navigation_cta_page"),
        FieldPanel("enable_preview"),
        FieldPanel("preview_url_override"),
    ]




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


@register_snippet
class TeamMember(index.Indexed, models.Model):
    """Team member for About page team section"""
    name = models.CharField(max_length=120, verbose_name="Navn")
    position = models.CharField(max_length=120, verbose_name="Stilling")
    bio = models.TextField(blank=True, verbose_name="Biografi")
    photo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Foto",
        related_name="+"
    )
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    years_experience = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="År med erfaring",
        help_text="Antal års erfaring i branchen"
    )
    specializations = models.TextField(
        blank=True,
        verbose_name="Specialiseringer",
        help_text="Kommasepareret liste af specialiseringer"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Lavere tal vises først"
    )

    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.SearchField('position'),
        index.SearchField('bio'),
        index.SearchField('specializations'),
        index.AutocompleteField('name'),
        index.AutocompleteField('position'),
    ]

    panels = [
        FieldPanel("name"),
        FieldPanel("position"),
        FieldPanel("bio"),
        FieldPanel("photo"),
        FieldPanel("email"),
        FieldPanel("phone"),
        FieldPanel("linkedin_url"),
        FieldPanel("years_experience"),
        FieldPanel("specializations"),
        FieldPanel("order"),
    ]

    class Meta:
        verbose_name = "Teammedlem"
        verbose_name_plural = "Teammedlemmer"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"

    def get_specializations_list(self):
        """Return specializations as a list"""
        if self.specializations:
            return [spec.strip() for spec in self.specializations.split(',') if spec.strip()]
        return []


@register_snippet
class CompanyMilestone(index.Indexed, models.Model):
    """Company achievements and milestones for About page"""
    year = models.PositiveIntegerField(verbose_name="År")
    title = models.CharField(max_length=200, verbose_name="Titel")
    description = models.TextField(verbose_name="Beskrivelse")
    milestone_type = models.CharField(
        max_length=50,
        choices=[
            ('founding', 'Grundlæggelse'),
            ('expansion', 'Udvidelse'),
            ('certification', 'Certificering'),
            ('award', 'Pris/Anerkendelse'),
            ('project', 'Stort projekt'),
            ('milestone', 'Milepæl'),
        ],
        default='milestone',
        verbose_name="Type"
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Billede",
        related_name="+"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Lavere tal vises først"
    )

    # Search index configuration
    search_fields = [
        index.SearchField('title'),
        index.SearchField('description'),
        index.AutocompleteField('title'),
    ]

    panels = [
        FieldPanel("year"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("milestone_type"),
        FieldPanel("image"),
        FieldPanel("order"),
    ]

    class Meta:
        verbose_name = "Virksomheds milepæl"
        verbose_name_plural = "Virksomheds milepæle"
        ordering = ['order', '-year']

    def __str__(self):
        return f"{self.year} - {self.title}"


@register_snippet
class Certification(index.Indexed, models.Model):
    """Professional certifications and qualifications"""
    name = models.CharField(max_length=200, verbose_name="Certificering navn")
    issuer = models.CharField(max_length=200, verbose_name="Udstedt af")
    description = models.TextField(blank=True, verbose_name="Beskrivelse")
    logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Logo",
        related_name="+"
    )
    url = models.URLField(blank=True, verbose_name="Website URL")
    expiry_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Udløbsdato",
        help_text="Lad være tom hvis certificeringen ikke udløber"
    )
    certificate_number = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Certifikatnummer"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Lavere tal vises først"
    )

    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.SearchField('issuer'),
        index.SearchField('description'),
        index.AutocompleteField('name'),
        index.AutocompleteField('issuer'),
    ]

    panels = [
        FieldPanel("name"),
        FieldPanel("issuer"),
        FieldPanel("description"),
        FieldPanel("logo"),
        FieldPanel("url"),
        FieldPanel("expiry_date"),
        FieldPanel("certificate_number"),
        FieldPanel("order"),
    ]

    class Meta:
        verbose_name = "Certificering"
        verbose_name_plural = "Certificeringer"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.issuer}"

    @property
    def is_expired(self):
        """Check if certification is expired"""
        if self.expiry_date:
            from django.utils import timezone
            return self.expiry_date < timezone.now().date()
        return False


class FAQPage(Page):
    """FAQ page with MerakiUI collapse and side links"""
    
    intro = RichTextField(
        blank=True,
        verbose_name="Intro tekst",
        help_text="Kort introduktion til FAQ siden"
    )
    
    # Modular content sections
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("faq", site_blocks.FAQBlock()),
        ("cta", site_blocks.CTABlock()),
    ], use_json_field=True, blank=True, verbose_name="Indhold sektioner")
    
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

    # No subpages - this is a standalone FAQ page
    subpage_types = []

    class Meta:
        verbose_name = "FAQ Side"
        verbose_name_plural = "FAQ Sider"


class AboutPage(Page):
    """Comprehensive About/Om Os page for construction company"""

    # SEO and basic content
    intro = RichTextField(
        blank=True,
        verbose_name="Intro tekst",
        help_text="Kort introduktion til virksomheden"
    )

    # Company overview section
    company_story = RichTextField(
        blank=True,
        verbose_name="Virksomhedens historie",
        help_text="Fortæl historien om hvordan virksomheden blev grundlagt og udviklet"
    )

    mission_statement = RichTextField(
        blank=True,
        verbose_name="Mission",
        help_text="Virksomhedens mission og formål"
    )

    vision_statement = RichTextField(
        blank=True,
        verbose_name="Vision",
        help_text="Virksomhedens vision for fremtiden"
    )

    core_values = RichTextField(
        blank=True,
        verbose_name="Kernev værdierne",
        help_text="De grundlæggende værdier virksomheden bygger på"
    )

    # Experience and expertise
    years_in_business = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="År i branchen",
        help_text="Antal år virksomheden har været aktiv"
    )

    projects_completed = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Gennemførte projekter",
        help_text="Antal projekter der er gennemført"
    )

    team_size = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Teamstørrelse",
        help_text="Antal medarbejdere"
    )

    # Service areas
    service_areas = RichTextField(
        blank=True,
        verbose_name="Serviceområder",
        help_text="Geografiske områder hvor virksomheden opererer"
    )

    specializations = RichTextField(
        blank=True,
        verbose_name="Specialiseringer",
        help_text="Områder hvor virksomheden har særlig ekspertise"
    )

    # Trust and credibility
    insurance_info = RichTextField(
        blank=True,
        verbose_name="Forsikring",
        help_text="Information om virksomhedens forsikringer"
    )

    licenses_info = RichTextField(
        blank=True,
        verbose_name="Licenser",
        help_text="Relevante licenser og tilladelser"
    )

    # Sustainability (important for modern construction)
    sustainability_commitment = RichTextField(
        blank=True,
        verbose_name="Bæredygtighed",
        help_text="Virksomhedens tilgang til bæredygtig byggeri"
    )

    # Modular content sections
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("team_section", site_blocks.TeamSectionBlock()),
        ("company_milestones", site_blocks.CompanyMilestonesBlock()),
        ("certifications_section", site_blocks.CertificationsBlock()),
        ("company_stats", site_blocks.CompanyStatsBlock()),
        ("features", site_blocks.FeaturesBlock()),
        ("testimonials_snippets", site_blocks.TestimonialsBlock()),
        ("cta", site_blocks.CTABlock()),
        ("image_gallery", site_blocks.ImageGalleryBlock()),
        ("faq", site_blocks.FAQBlock()),
    ], use_json_field=True, blank=True, verbose_name="Indhold sektioner")

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('company_story'),
        index.SearchField('mission_statement'),
        index.SearchField('vision_statement'),
        index.SearchField('core_values'),
        index.SearchField('service_areas'),
        index.SearchField('specializations'),
        index.SearchField('sustainability_commitment'),
        index.SearchField('body'),
        index.AutocompleteField('title'),
        index.AutocompleteField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("company_story"),
        FieldPanel("mission_statement"),
        FieldPanel("vision_statement"),
        FieldPanel("core_values"),
        FieldPanel("years_in_business"),
        FieldPanel("projects_completed"),
        FieldPanel("team_size"),
        FieldPanel("service_areas"),
        FieldPanel("specializations"),
        FieldPanel("insurance_info"),
        FieldPanel("licenses_info"),
        FieldPanel("sustainability_commitment"),
        FieldPanel("body"),
    ]

    # Enable PromoteTab functionality for SEO
    promote_panels = Page.promote_panels

    # No subpages - this is a standalone about page
    subpage_types = []

    class Meta:
        verbose_name = "Om Os Side"
        verbose_name_plural = "Om Os Sider"

    def get_context(self, request):
        context = super().get_context(request)

        # Add team members for template use
        context['team_members'] = TeamMember.objects.all().order_by('order', 'name')

        # Add milestones for template use
        context['company_milestones'] = CompanyMilestone.objects.all().order_by('order', '-year')

        # Add certifications for template use
        context['certifications'] = Certification.objects.filter(
            models.Q(expiry_date__isnull=True) |
            models.Q(expiry_date__gte=models.functions.Now())
        ).order_by('order', 'name')

        return context


