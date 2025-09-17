from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.forms import widgets
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, Panel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.search import index

from . import blocks as site_blocks
from .grouped_blocks import get_grouped_streamfield_blocks
from .widgets import ColorPickerWidget, ColorPreviewWidget, ThemeSelectorWidget
from .themes import get_theme_choices






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


# Legacy theme and font choices removed - now using Preline/Tailwind native styling


class HomePage(Page):
    intro = RichTextField(blank=True, verbose_name="Intro tekst")
    body = StreamField(
        get_grouped_streamfield_blocks(), 
        use_json_field=True, 
        blank=True, 
        verbose_name="Indhold"
    )

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
    
    # StreamField for configurable gallery content
    body = StreamField([
        ("hero_v2", site_blocks.HeroV2Block()),
        ("featured_projects", site_blocks.FeaturedProjectsBlock()),
        ("image_gallery", site_blocks.ImageGalleryBlock()),
        ("richtext_section", site_blocks.RichTextSectionBlock()),
        ("cta", site_blocks.CTABlock()),
    ], use_json_field=True, blank=True, verbose_name="Galleri indhold")
    
    # Gallery settings
    default_layout = models.CharField(
        max_length=20,
        choices=[
            ("masonry", "Masonry (Pinterest-stil)"),
            ("grid", "Grid (standard)"),
            ("carousel", "Karussel"),
        ],
        default="masonry",
        help_text="Standard layout for projekter der ikke er i StreamField"
    )
    default_columns = models.CharField(
        max_length=10,
        choices=[("2", "2 kolonner"), ("3", "3 kolonner"), ("4", "4 kolonner")],
        default="3",
        help_text="Standard antal kolonner"
    )
    default_image_height = models.CharField(
        max_length=10,
        choices=[
            ("200", "200px (Lille)"),
            ("300", "300px (Standard)"),
            ("400", "400px (Stor)"),
            ("500", "500px (Meget stor)"),
        ],
        default="300",
        help_text="Standard billedhøjde"
    )
    
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
        FieldPanel("default_layout"),
        FieldPanel("default_columns"),
        FieldPanel("default_image_height"),
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
        
        # Add default gallery settings for fallback display
        context['default_layout'] = getattr(self, 'default_layout', 'masonry')
        context['default_columns'] = getattr(self, 'default_columns', '3')
        context['default_image_height'] = getattr(self, 'default_image_height', '300')
        
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
    body = StreamField(
        get_grouped_streamfield_blocks(), 
        use_json_field=True, 
        blank=True, 
        verbose_name="Indhold"
    )

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
class DesignPage(Page):
    """Website design, theme, and navigation settings"""
    
    # Remove the name field since Page already has title
    
    # Legacy theme and font fields removed - now using Preline/Tailwind native styling
    
    # Theme selection
    theme = models.CharField(
        max_length=30,
        default='tailwind',
        choices=get_theme_choices(),
        help_text="Vælg et foruddefineret farvetema",
        verbose_name="Tema"
    )
    
    # Individual color fields removed - now using predefined themes
    
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
        help_text="Side som CTA knap linker til",
        related_name="design_settings_cta"
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
    
    # Color Preview Settings
    enable_color_preview = models.BooleanField(
        default=True,
        verbose_name="Aktivér farve forhåndsvisning",
        help_text="Vis farve ændringer i real-time i admin interface"
    )

    # Comprehensive component preview - includes ALL available blocks organized by Preline categories
    body = StreamField(
        get_grouped_streamfield_blocks(), 
        use_json_field=True, 
        blank=True, 
        verbose_name="Komponent Forhåndsvisning"
    )

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.AutocompleteField('title'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("theme", widget=ThemeSelectorWidget, heading="Tema Valg - Vælg et foruddefineret farvetema"),
        MultiFieldPanel([
            FieldPanel("navigation_style"),
            FieldPanel("show_navigation"),
            FieldPanel("show_search_in_nav"),
            FieldPanel("header_style"),
            FieldPanel("navigation_cta_text"),
            FieldPanel("navigation_cta_page"),
        ], heading="Navigation Indstillinger"),
        MultiFieldPanel([
            FieldPanel("enable_preview"),
            FieldPanel("preview_url_override"),
            FieldPanel("enable_color_preview"),
        ], heading="Forhåndsvisning"),
        FieldPanel("body", heading="Komponent Forhåndsvisning - Tilføj komponenter for at se hvordan de ser ud med dine design indstillinger"),
    ]

    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
    
    class Meta:
        verbose_name = "Design Indstillinger"
        verbose_name_plural = "Design Indstillinger"


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


@register_snippet
class NavigationLink(index.Indexed, models.Model):
    """Enhanced navigation links for header and footer with better admin experience"""

    name = models.CharField(
        max_length=100,
        verbose_name="Link navn",
        help_text="Navn der vises i navigationen"
    )

    # Link destination options
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Intern side",
        help_text="Vælg en side fra dit website",
        related_name="navigation_links"
    )

    external_url = models.URLField(
        blank=True,
        verbose_name="Ekstern URL",
        help_text="Ekstern URL (fx https://example.com) - bruges kun hvis ingen intern side er valgt"
    )

    # Link type for different styling and behavior
    LINK_TYPE_CHOICES = [
        ('internal', '🏠 Intern side'),
        ('external', '🔗 Ekstern link'),
        ('email', '📧 Email link'),
        ('phone', '📞 Telefon link'),
    ]

    link_type = models.CharField(
        max_length=20,
        choices=LINK_TYPE_CHOICES,
        default='internal',
        verbose_name="Link type",
        help_text="Type af link - bestemmer adfærd og ikon"
    )

    # Display settings
    show_in_header = models.BooleanField(
        default=True,
        verbose_name="Vis i header",
        help_text="Vis dette link i header navigationen"
    )

    show_in_footer = models.BooleanField(
        default=True,
        verbose_name="Vis i footer",
        help_text="Vis dette link i footer navigationen"
    )

    # Special link behaviors
    open_in_new_tab = models.BooleanField(
        default=False,
        verbose_name="Åbn i nyt faneblad",
        help_text="Åbn linket i et nyt faneblad (anbefales for eksterne links)"
    )

    highlight_as_cta = models.BooleanField(
        default=False,
        verbose_name="Fremhæv som CTA",
        help_text="Vis dette link som en call-to-action knap"
    )

    # Ordering and organization
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Rækkefølge i navigation (lavere tal vises først)"
    )

    # Optional icon
    icon_class = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Ikon CSS klasse",
        help_text="Valgfri CSS klasse for ikon (fx 'fas fa-home' for Font Awesome)"
    )

    # Accessibility
    aria_label = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Tilgængeligheds beskrivelse",
        help_text="Beskrivelse for skærmlæsere (valgfrit)"
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Ikon",
        help_text="Heroicon navn (fx 'home', 'user', 'phone')"
    )

    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.AutocompleteField('name'),
    ]

    panels = [
        FieldPanel("name"),
        FieldPanel("internal_page"),
        FieldPanel("external_url"),
        FieldPanel("link_type"),
        MultiFieldPanel([
            FieldPanel("show_in_header"),
            FieldPanel("show_in_footer"),
            FieldPanel("order"),
        ], heading="Visning Indstillinger"),
        MultiFieldPanel([
            FieldPanel("icon"),
            FieldPanel("icon_class"),
            FieldPanel("aria_label"),
            FieldPanel("open_in_new_tab"),
            FieldPanel("highlight_as_cta"),
        ], heading="Avancerede Indstillinger"),
    ]

    class Meta:
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def url(self):
        """Get the URL for this navigation link"""
        if self.internal_page and self.internal_page.url:
            return self.internal_page.url
        elif self.external_url:
            return self.external_url
        elif self.link_type == 'email' and self.external_url:
            return f"mailto:{self.external_url}"
        elif self.link_type == 'phone' and self.external_url:
            return f"tel:{self.external_url}"
        return "#"


class HeaderManagementPage(Page):
    """Enhanced header management with live preview functionality"""

    # Header Appearance
    header_style = models.CharField(
        max_length=20,
        choices=[
            ('standard', 'Standard - Klassisk navigation'),
            ('minimal', 'Minimal - Kun logo og navigation'),
            ('centered', 'Centreret - Centreret logo og navigation'),
            ('split', 'Split - Logo venstre, navigation højre'),
        ],
        default='standard',
        verbose_name="Header stil",
        help_text="Vælg overordnet stil for headeren"
    )

    # Logo & Branding
    custom_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Brugerdefineret logo",
        help_text="Upload et logo billede (valgfrit - ellers bruges automatisk genereret logo)",
        related_name="+"
    )

    show_company_name = models.BooleanField(
        default=True,
        verbose_name="Vis firmanavn",
        help_text="Vis firmanavnet ved siden af logoet"
    )

    # Navigation Features
    show_search = models.BooleanField(
        default=True,
        verbose_name="Vis søg",
        help_text="Vis søgeknap i headeren"
    )

    show_theme_toggle = models.BooleanField(
        default=True,
        verbose_name="Vis tema skifter",
        help_text="Vis mørk/lys tema skifter knap"
    )

    # CTA Button
    show_cta_button = models.BooleanField(
        default=False,
        verbose_name="Vis CTA knap",
        help_text="Vis call-to-action knap i headeren"
    )

    cta_button_text = models.CharField(
        max_length=50,
        default="Kontakt os",
        verbose_name="CTA knap tekst",
        help_text="Tekst der vises på CTA knappen"
    )

    cta_button_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="CTA destination side",
        help_text="Side som CTA knappen linker til",
        related_name="header_cta_pages"
    )

    cta_button_external_url = models.URLField(
        blank=True,
        verbose_name="CTA ekstern URL",
        help_text="Alternativ ekstern URL (bruges kun hvis ingen side er valgt)"
    )

    # Layout & Behavior
    sticky_header = models.BooleanField(
        default=True,
        verbose_name="Fast header",
        help_text="Header bliver fast øverst når siden scrolles"
    )

    header_height = models.CharField(
        max_length=10,
        choices=[
            ('py-4', 'Kompakt (16px padding)'),
            ('py-6', 'Standard (24px padding)'),
            ('py-8', 'Stor (32px padding)'),
            ('py-7', 'Preline standard (28px padding)'),
        ],
        default='py-7',
        verbose_name="Header højde",
        help_text="Højde af headeren"
    )

    # Mobile Settings
    mobile_menu_style = models.CharField(
        max_length=20,
        choices=[
            ('slide', 'Slide ind fra side'),
            ('dropdown', 'Dropdown fra top'),
            ('overlay', 'Overlay over indhold'),
        ],
        default='slide',
        verbose_name="Mobil menu stil",
        help_text="Hvordan skal navigation vises på mobile enheder"
    )

    # Advanced Settings
    header_background_transparent = models.BooleanField(
        default=False,
        verbose_name="Gennemsigtig baggrund",
        help_text="Gør header baggrunden gennemsigtig (kun for specielle designs)"
    )

    hide_on_scroll = models.BooleanField(
        default=False,
        verbose_name="Skjul ved scroll",
        help_text="Skjul headeren når brugeren scroller ned (vises igen ved scroll op)"
    )

    # Preview Settings
    preview_mode = models.CharField(
        max_length=20,
        choices=[
            ('desktop', 'Desktop visning'),
            ('tablet', 'Tablet visning'),
            ('mobile', 'Mobil visning'),
        ],
        default='desktop',
        verbose_name="Forhåndsvisning",
        help_text="Enheds type for forhåndsvisning"
    )

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('cta_button_text'),
        index.AutocompleteField('title'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("header_style"),
            FieldPanel("header_height"),
            FieldPanel("sticky_header"),
            FieldPanel("header_background_transparent"),
            FieldPanel("hide_on_scroll"),
        ], heading="🎨 Header Udseende",
           help_text="Grundlæggende udseende og adfærd for headeren"),

        MultiFieldPanel([
            FieldPanel("custom_logo"),
            FieldPanel("show_company_name"),
        ], heading="🏢 Logo & Branding",
           help_text="Firmalogo og branding indstillinger"),

        MultiFieldPanel([
            FieldPanel("show_search"),
            FieldPanel("show_theme_toggle"),
        ], heading="🔧 Navigation Features",
           help_text="Ekstra funktionalitet i headeren"),

        MultiFieldPanel([
            FieldPanel("show_cta_button"),
            FieldPanel("cta_button_text"),
            FieldPanel("cta_button_page"),
            FieldPanel("cta_button_external_url"),
        ], heading="📢 Call-to-Action Knap",
           help_text="Konfigurer CTA knap (valgfrit)"),

        MultiFieldPanel([
            FieldPanel("mobile_menu_style"),
            FieldPanel("preview_mode"),
        ], heading="📱 Mobil & Forhåndsvisning",
           help_text="Mobil indstillinger og forhåndsvisning"),
    ]

    # Enable preview
    preview_modes = [
        ('desktop', 'Desktop'),
        ('tablet', 'Tablet'),
        ('mobile', 'Mobile'),
    ]

    def get_preview_template(self, request, mode_name):
        """Return template for header preview"""
        return "admin/header_preview.html"

    def get_preview_context(self, request, mode_name):
        """Get context for header preview"""
        context = super().get_preview_context(request, mode_name)
        context['header_settings'] = self
        context['preview_mode'] = mode_name

        # Add navigation links for preview
        context['navigation_links'] = NavigationLink.objects.filter(
            show_in_header=True
        ).order_by('order')

        # Add company settings for preview
        try:
            from apps.pages.models import CompanySettings
            context['company_settings'] = CompanySettings.objects.first()
        except:
            context['company_settings'] = None

        return context

    @property
    def cta_button_url(self):
        """Get the URL for CTA button (page or external)"""
        if self.cta_button_page:
            return self.cta_button_page.url
        return self.cta_button_external_url or "#"

    def clean(self):
        """Validate CTA button settings"""
        super().clean()
        if self.show_cta_button and not self.cta_button_text:
            from django.core.exceptions import ValidationError
            raise ValidationError({
                'cta_button_text': 'CTA knap tekst er påkrævet når CTA knap er aktiveret'
            })

    class Meta:
        verbose_name = "Header Administration"
        verbose_name_plural = "Header Administration"

    # Restrict to only one instance
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
    max_count = 1


@register_snippet
class HeaderSettings(index.Indexed, models.Model):
    """Legacy header settings - kept for backwards compatibility"""

    name = models.CharField(
        max_length=100,
        default="Standard Header",
        verbose_name="Navn",
        help_text="Identifikation for denne header konfiguration"
    )

    # Header Style Options
    HEADER_STYLE_CHOICES = [
        ('standard', 'Standard - Klassisk navigation'),
        ('minimal', 'Minimal - Kun logo og navigation'),
        ('centered', 'Centreret - Centreret logo og navigation'),
        ('split', 'Split - Logo venstre, navigation højre'),
        ('sticky', 'Sticky - Fast navigation der følger scroll'),
    ]

    header_style = models.CharField(
        max_length=20,
        choices=HEADER_STYLE_CHOICES,
        default='standard',
        verbose_name="Header stil"
    )

    # Navigation Settings
    show_search = models.BooleanField(
        default=True,
        verbose_name="Vis søg",
        help_text="Vis søgefelt i navigation"
    )

    show_theme_toggle = models.BooleanField(
        default=True,
        verbose_name="Vis tema skifter",
        help_text="Vis mørk/lys tema skifter"
    )

    # CTA Button Settings
    show_cta_button = models.BooleanField(
        default=False,
        verbose_name="Vis CTA knap",
        help_text="Vis call-to-action knap i navigation"
    )

    cta_button_text = models.CharField(
        max_length=50,
        default="Kontakt os",
        verbose_name="CTA knap tekst"
    )

    cta_button_url = models.CharField(
        max_length=200,
        default="/kontakt/",
        verbose_name="CTA knap URL"
    )

    # Mobile Settings
    mobile_menu_style = models.CharField(
        max_length=20,
        choices=[
            ('slide', 'Slide ind fra side'),
            ('dropdown', 'Dropdown fra top'),
            ('overlay', 'Overlay over indhold'),
        ],
        default='slide',
        verbose_name="Mobil menu stil"
    )

    # Advanced Settings
    sticky_header = models.BooleanField(
        default=True,
        verbose_name="Fast header",
        help_text="Header følger scroll"
    )

    header_height = models.CharField(
        max_length=10,
        choices=[
            ('h-16', '64px (Standard)'),
            ('h-20', '80px (Stor)'),
            ('h-14', '56px (Kompakt)'),
        ],
        default='h-16',
        verbose_name="Header højde"
    )

    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.AutocompleteField('name'),
    ]

    panels = [
        FieldPanel("name"),
        FieldPanel("header_style"),
        MultiFieldPanel([
            FieldPanel("show_search"),
            FieldPanel("show_theme_toggle"),
            FieldPanel("show_cta_button"),
            FieldPanel("cta_button_text"),
            FieldPanel("cta_button_url"),
        ], heading="Navigation Indstillinger"),
        MultiFieldPanel([
            FieldPanel("mobile_menu_style"),
            FieldPanel("sticky_header"),
            FieldPanel("header_height"),
        ], heading="Mobil Indstillinger"),
    ]

    class Meta:
        verbose_name = "Header Indstillinger (Legacy)"
        verbose_name_plural = "Header Indstillinger (Legacy)"
        ordering = ['name']

    def __str__(self):
        return self.name


@register_snippet
class FooterSettings(index.Indexed, models.Model):
    """Customizable footer settings using Preline components"""
    
    name = models.CharField(
        max_length=100,
        default="Standard Footer",
        verbose_name="Navn",
        help_text="Identifikation for denne footer konfiguration"
    )
    
    # Footer Style Options
    FOOTER_STYLE_CHOICES = [
        ('standard', 'Standard - Fuld footer med alle sektioner'),
        ('minimal', 'Minimal - Kun logo og copyright'),
        ('centered', 'Centreret - Centreret indhold'),
        ('split', 'Split - Logo venstre, links højre'),
    ]
    
    footer_style = models.CharField(
        max_length=20,
        choices=FOOTER_STYLE_CHOICES,
        default='standard',
        verbose_name="Footer stil"
    )
    
    # Color customization now handled by theme system in DesignPage
    
    # Content Settings
    show_company_info = models.BooleanField(
        default=True,
        verbose_name="Vis firma information",
        help_text="Vis firma beskrivelse og kontakt info"
    )
    
    show_social_links = models.BooleanField(
        default=True,
        verbose_name="Vis sociale links",
        help_text="Vis sociale medie links"
    )
    
    show_quick_links = models.BooleanField(
        default=True,
        verbose_name="Vis hurtige links",
        help_text="Vis navigation links i footer"
    )
    
    show_newsletter_signup = models.BooleanField(
        default=False,
        verbose_name="Vis nyhedsbrev tilmelding",
        help_text="Vis tilmeldingsformular for nyhedsbrev"
    )
    
    # Newsletter Settings
    newsletter_title = models.CharField(
        max_length=100,
        default="Tilmeld dig vores nyhedsbrev",
        verbose_name="Nyhedsbrev titel"
    )
    
    newsletter_description = models.TextField(
        default="Få de seneste nyheder og tilbud direkte i din indbakke.",
        verbose_name="Nyhedsbrev beskrivelse"
    )
    
    # Copyright Settings
    copyright_text = models.CharField(
        max_length=200,
        default="© 2025 JCleemann Byg. Alle rettigheder forbeholdes.",
        verbose_name="Copyright tekst"
    )
    
    # Advanced Settings
    footer_height = models.CharField(
        max_length=10,
        choices=[
            ('auto', 'Automatisk (Standard)'),
            ('h-64', '256px (Fast højde)'),
            ('h-80', '320px (Stor højde)'),
        ],
        default='auto',
        verbose_name="Footer højde"
    )
    
    # Search index configuration
    search_fields = [
        index.SearchField('name'),
        index.AutocompleteField('name'),
    ]
    
    panels = [
        FieldPanel("name"),
        FieldPanel("footer_style"),
        MultiFieldPanel([
            FieldPanel("show_company_info"),
            FieldPanel("show_social_links"),
            FieldPanel("show_quick_links"),
            FieldPanel("show_newsletter_signup"),
        ], heading="Indhold Indstillinger"),
        MultiFieldPanel([
            FieldPanel("newsletter_title"),
            FieldPanel("newsletter_description"),
        ], heading="Nyhedsbrev Indstillinger"),
        MultiFieldPanel([
            FieldPanel("copyright_text"),
            FieldPanel("footer_height"),
        ], heading="Copyright Indstillinger"),
    ]
    
    class Meta:
        verbose_name = "Footer Indstillinger"
        verbose_name_plural = "Footer Indstillinger"
        ordering = ['name']
    
    def __str__(self):
        return self.name


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


