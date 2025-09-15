from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.blocks import PageChooserBlock


class StyleOptionsBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(
        choices=[
            ("surface", "Surface (Standard)"),
            ("surface-soft", "Surface Soft"),
            ("hero", "Hero Gradient"),
            ("base-200", "Base 200"),
            ("base-300", "Base 300"),
        ], default="surface", required=False, help_text="Baggrundsfarve for sektionen"
    )
    spacing = blocks.ChoiceBlock(
        choices=[("sm", "Small (py-10)"), ("md", "Medium (py-16)"), ("lg", "Large (py-24)")],
        default="md", required=False, help_text="Vertikal spacing for sektionen"
    )
    container = blocks.ChoiceBlock(
        choices=[("narrow", "Narrow (max-w-3xl)"), ("normal", "Normal (max-w-5xl)"), ("wide", "Wide (max-w-7xl)")],
        default="normal", required=False, help_text="Bredde af indholdet"
    )
    divider = blocks.BooleanBlock(required=False, help_text="Vis en subtil top divider")

    class Meta:
        icon = "cog"
        label = "Styling indstillinger"


def section_classes(style: dict) -> str:
    bg = style.get("background") or "surface"
    spacing = style.get("spacing") or "md"
    container = style.get("container") or "normal"
    classes = []
    
    # Background classes
    if bg == "hero":
        classes.append("bg-gradient-to-br from-primary via-secondary to-accent text-primary-content")
    elif bg == "surface-soft":
        classes.append("bg-base-200")
    else:
        classes.append(f"bg-{bg}")
    
    # Spacing classes
    if spacing == "sm":
        classes.append("py-10")
    elif spacing == "lg":
        classes.append("py-24")
    else:
        classes.append("py-16")
    
    # Container width classes
    if container == "narrow":
        classes.append("max-w-3xl mx-auto")
    elif container == "wide":
        classes.append("max-w-7xl mx-auto")
    else:
        classes.append("max-w-5xl mx-auto")
    
    return " ".join(classes)


class HeroV2Block(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Hovedoverskrift for hero sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Undertitel eller beskrivende tekst")
    primary_text = blocks.CharBlock(required=False, help_text="Tekst for primær knap (fx 'Få et tilbud')")
    primary_page = PageChooserBlock(required=False, help_text="Side som primær knap linker til")
    secondary_text = blocks.CharBlock(required=False, help_text="Tekst for sekundær knap (fx 'Se projekter')")
    secondary_page = PageChooserBlock(required=False, help_text="Side som sekundær knap linker til")
    image = ImageChooserBlock(required=False, help_text="Billede der vises under teksten")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "pick"
        label = "Hero sektion"
        template = "blocks/hero_v2.html"


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Overskrift for call-to-action sektionen")
    text = blocks.TextBlock(required=False, help_text="Beskrivende tekst under overskriften")
    button_text = blocks.CharBlock(required=True, help_text="Tekst på knappen (fx 'Kontakt os nu')")
    button_page = PageChooserBlock(required=True, help_text="Side som knappen linker til")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "site"
        label = "Call-to-Action"
        template = "blocks/cta.html"


class FeatureItem(blocks.StructBlock):
    title = blocks.CharBlock(help_text="Titel for denne feature")
    text = blocks.TextBlock(required=False, help_text="Beskrivelse af featuren")
    icon = blocks.ChoiceBlock(
        choices=[
            ("check", "Checkmark"),
            ("hammer", "Hammer (Håndværk)"),
            ("leaf", "Leaf (Miljø)"),
            ("home", "Home (Hjem)"),
            ("shield", "Shield (Sikkerhed)"),
            ("star", "Star (Kvalitet)"),
            ("clock", "Clock (Tid)"),
            ("heart", "Heart (Kærlighed)"),
        ],
        default="check",
        help_text="Ikon der vises ved siden af teksten"
    )


class FeaturesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for features sektionen")
    items = blocks.ListBlock(FeatureItem(), help_text="Liste af features der skal vises")
    columns = blocks.ChoiceBlock(choices=[("2", "2 kolonner"), ("3", "3 kolonner"), ("4", "4 kolonner")], default="3", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "list-ul"
        label = "Features"
        template = "blocks/features.html"


class RichTextSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for tekstsektionen")
    body = blocks.RichTextBlock(
        features=["h2","h3","bold","italic","link","ol","ul","hr","blockquote"],
        help_text="Rich text indhold med formatering"
    )
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Tekst sektion"
        template = "blocks/richtext_section.html"


class TestimonialsBlock(blocks.StructBlock):
    testimonials = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.Testimonial"),
        help_text="Vælg udtalelser fra kunder der skal vises"
    )
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "quote"
        label = "Udtalelser"
        template = "blocks/testimonials.html"


class LogoCloudBlock(blocks.StructBlock):
    logos = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.Logo"),
        help_text="Vælg logoer der skal vises i skyen"
    )
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "image"
        label = "Logo sky"
        template = "blocks/logo_cloud.html"


class FAQItem(blocks.StructBlock):
    question = blocks.CharBlock(help_text="Spørgsmålet der skal besvares")
    answer = blocks.RichTextBlock(
        features=["bold","italic","link","ol","ul","hr","blockquote"],
        help_text="Svar på spørgsmålet med mulighed for formatering"
    )


class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for FAQ sektionen")
    items = blocks.ListBlock(FAQItem(), help_text="Liste af spørgsmål og svar")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "help"
        label = "Ofte stillede spørgsmål"
        template = "blocks/faq.html"


class ServicesGridBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for services sektionen")
    services = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.Service"),
        help_text="Vælg services der skal vises"
    )
    columns = blocks.ChoiceBlock(choices=[("2","2 kolonner"),("3","3 kolonner")], default="3", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "folder-open-inverse"
        label = "Services grid"
        template = "blocks/services_grid.html"


class GalleryImage(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Billede der skal vises")
    caption = blocks.CharBlock(required=False, help_text="Billedtekst (valgfri)")


class ImageGalleryBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for billedgalleriet")
    images = blocks.ListBlock(GalleryImage(), help_text="Liste af billeder der skal vises")
    columns = blocks.ChoiceBlock(choices=[("2","2 kolonner"),("3","3 kolonner"),("4","4 kolonner")], default="3", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "image"
        label = "Billedgalleri"
        template = "blocks/image_gallery.html"


class ServiceInlineItem(blocks.StructBlock):
    title = blocks.CharBlock(help_text="Titel for denne service")
    description = blocks.TextBlock(required=False, help_text="Beskrivelse af servicen")
    icon = blocks.ChoiceBlock(choices=[
        ("check", "Checkmark"),
        ("hammer", "Hammer (Håndværk)"),
        ("home", "Home (Hjem)"),
        ("leaf", "Leaf (Miljø)"),
        ("clock", "Clock (Tid)"),
        ("shield", "Shield (Sikkerhed)"),
        ("dollar", "Dollar (Pris)"),
        ("star", "Star (Kvalitet)"),
        ("building", "Building (Bygning)"),
        ("wrench", "Wrench (Værktøj)"),
    ], required=False, default="check", help_text="Ikon der vises ved siden af teksten")


class ServicesGridInlineBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for services sektionen")
    items = blocks.ListBlock(ServiceInlineItem(), help_text="Liste af services der skal vises")
    columns = blocks.ChoiceBlock(choices=[("2","2 kolonner"),("3","3 kolonner")], default="3", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "list-ul"
        label = "Services grid (inline)"
        template = "blocks/services_grid_inline.html"


class TrustBadgeItem(blocks.StructBlock):
    title = blocks.CharBlock(help_text="Titel for trust badge")
    description = blocks.TextBlock(required=False, help_text="Beskrivelse af trust badge")
    icon = blocks.ChoiceBlock(choices=[
        ("clock", "Clock (Tid)"),
        ("shield", "Shield (Sikkerhed)"),
        ("dollar", "Dollar (Pris)"),
        ("heart", "Heart (Kærlighed)"),
        ("star", "Star (Kvalitet)"),
        ("check", "Check (Verificeret)"),
        ("hammer", "Hammer (Værktøj)"),
        ("home", "Home (Bygning)"),
    ], default="check", help_text="Ikon der vises ved siden af teksten")


class TrustBadgesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text="Overskrift for trust badges sektionen")
    items = blocks.ListBlock(TrustBadgeItem(), help_text="Liste af trust badges der skal vises")
    columns = blocks.ChoiceBlock(choices=[("2","2 kolonner"),("3","3 kolonner"),("4","4 kolonner")], default="4", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "success"
        label = "Trust badges"
        template = "blocks/trust_badges.html"


class FeaturedProjectsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Fremhævede projekter", help_text="Overskrift for projekter sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Undertitel eller beskrivelse")
    show_all_link = blocks.BooleanBlock(required=False, default=True, help_text="Vis 'Se alle projekter' link")
    all_projects_page = PageChooserBlock(required=False, help_text="Side som 'Se alle projekter' linker til")
    columns = blocks.ChoiceBlock(choices=[("2","2 kolonner"),("3","3 kolonner")], default="3", help_text="Antal kolonner for layout")
    style = StyleOptionsBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        try:
            from apps.projects.models import Project
            featured_projects = Project.objects.filter(published=True, featured=True).order_by('-date', 'title')[:6]
            context['featured_projects'] = featured_projects
        except Exception:
            context['featured_projects'] = []
        return context

    class Meta:
        icon = "image"
        label = "Fremhævede projekter"
        template = "blocks/featured_projects.html"


class TeamSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Vores team", help_text="Overskrift for team sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Undertitel eller beskrivelse af teamet")
    team_members = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.TeamMember"),
        help_text="Vælg teammedlemmer der skal vises"
    )
    show_all_members = blocks.BooleanBlock(
        required=False,
        default=False,
        help_text="Vis alle teammedlemmer automatisk (ignorerer valgte medlemmer)"
    )
    columns = blocks.ChoiceBlock(
        choices=[("2","2 kolonner"),("3","3 kolonner"),("4","4 kolonner")],
        default="3",
        help_text="Antal kolonner for layout"
    )
    style = StyleOptionsBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        if value.get('show_all_members'):
            # Show all team members if option is selected
            from apps.pages.models import TeamMember
            context['team_members'] = TeamMember.objects.all().order_by('order', 'name')
        else:
            # Use selected team members
            context['team_members'] = value.get('team_members', [])
        return context

    class Meta:
        icon = "group"
        label = "Team sektion"
        template = "blocks/team_section.html"


class CompanyMilestonesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Vores rejse", help_text="Overskrift for milepæle sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Beskrivelse af virksomhedens udvikling")
    milestones = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.CompanyMilestone"),
        help_text="Vælg milepæle der skal vises"
    )
    show_all_milestones = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Vis alle milepæle automatisk (ignorerer valgte milepæle)"
    )
    timeline_style = blocks.ChoiceBlock(
        choices=[
            ("vertical", "Vertikal tidslinje"),
            ("horizontal", "Horisontal tidslinje"),
            ("grid", "Grid layout"),
        ],
        default="vertical",
        help_text="Hvordan milepælene skal vises"
    )
    style = StyleOptionsBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        if value.get('show_all_milestones'):
            # Show all milestones if option is selected
            from apps.pages.models import CompanyMilestone
            context['milestones'] = CompanyMilestone.objects.all().order_by('order', '-year')
        else:
            # Use selected milestones
            context['milestones'] = value.get('milestones', [])
        return context

    class Meta:
        icon = "time"
        label = "Virksomheds milepæle"
        template = "blocks/company_milestones.html"


class CertificationsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Certificeringer & kvalifikationer", help_text="Overskrift for certificeringer sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Beskrivelse af certificeringer og kvalifikationer")
    certifications = blocks.ListBlock(
        SnippetChooserBlock(target_model="pages.Certification"),
        help_text="Vælg certificeringer der skal vises"
    )
    show_all_certifications = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Vis alle certificeringer automatisk (ignorerer valgte certificeringer)"
    )
    hide_expired = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Skjul udløbne certificeringer"
    )
    columns = blocks.ChoiceBlock(
        choices=[("2","2 kolonner"),("3","3 kolonner"),("4","4 kolonner")],
        default="3",
        help_text="Antal kolonner for layout"
    )
    style = StyleOptionsBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        if value.get('show_all_certifications'):
            # Show all certifications if option is selected
            from apps.pages.models import Certification
            from django.db import models
            certifications = Certification.objects.all().order_by('order', 'name')

            # Filter out expired if requested
            if value.get('hide_expired'):
                certifications = certifications.filter(
                    models.Q(expiry_date__isnull=True) |
                    models.Q(expiry_date__gte=models.functions.Now())
                )

            context['certifications'] = certifications
        else:
            # Use selected certifications
            context['certifications'] = value.get('certifications', [])
        return context

    class Meta:
        icon = "success"
        label = "Certificeringer"
        template = "blocks/certifications.html"


class CompanyStatItem(blocks.StructBlock):
    number = blocks.CharBlock(help_text="Tal eller statistik (fx '25+', '500')")
    label = blocks.CharBlock(help_text="Beskrivelse af statistikken (fx 'År i branchen', 'Projekter gennemført')")
    description = blocks.TextBlock(required=False, help_text="Ekstra beskrivelse eller detaljer")
    icon = blocks.ChoiceBlock(
        choices=[
            ("calendar", "Kalender (år)"),
            ("home", "Hjem (projekter)"),
            ("group", "Gruppe (team)"),
            ("star", "Stjerne (kvalitet)"),
            ("shield", "Skjold (sikkerhed)"),
            ("check", "Check (succes)"),
            ("award", "Pris (anerkendelse)"),
            ("clock", "Ur (erfaring)"),
        ],
        default="star",
        help_text="Ikon der vises ved statistikken"
    )


class CompanyStatsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, default="Fakta om os", help_text="Overskrift for statistik sektionen")
    subheading = blocks.TextBlock(required=False, help_text="Beskrivelse af virksomhedens styrker")
    stats = blocks.ListBlock(CompanyStatItem(), help_text="Statistikker der skal vises")
    columns = blocks.ChoiceBlock(
        choices=[("2","2 kolonner"),("3","3 kolonner"),("4","4 kolonner")],
        default="4",
        help_text="Antal kolonner for layout"
    )
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "snippet"
        label = "Virksomheds statistikker"
        template = "blocks/company_stats.html"


class ModernHeroBlock(blocks.StructBlock):
    """Modern hero section with gradient backgrounds and editable content"""
    
    announcement_text = blocks.CharBlock(
        max_length=200,
        required=False,
        help_text="Tekst til announcement banner (f.eks. 'JCleemann Byg: Professionel byggeri siden 1998')"
    )
    
    announcement_link = PageChooserBlock(
        required=False,
        help_text="Side at linke til fra announcement banner"
    )
    
    hero_title = blocks.CharBlock(
        max_length=200,
        required=True,
        help_text="Hovedtitel for hero sektionen"
    )
    
    hero_subtitle = blocks.TextBlock(
        required=False,
        help_text="Undertekst/beskrivelse under hovedtitlen"
    )
    
    primary_button_text = blocks.CharBlock(
        max_length=50,
        default="Få et tilbud",
        help_text="Tekst til primær knap"
    )
    
    primary_button_link = PageChooserBlock(
        required=False,
        help_text="Side at linke til fra primær knap"
    )
    
    secondary_button_text = blocks.CharBlock(
        max_length=50,
        default="Se vores projekter",
        help_text="Tekst til sekundær knap"
    )
    
    secondary_button_link = PageChooserBlock(
        required=False,
        help_text="Side at linke til fra sekundær knap"
    )

    class Meta:
        icon = "home"
        label = "Moderne Hero"
        template = "blocks/modern_hero.html"


class CarouselSlide(blocks.StructBlock):
    """Individual carousel slide with image, title, subtitle and button"""
    
    image = ImageChooserBlock(
        required=True,
        help_text="Baggrundsbillede for denne slide"
    )
    
    title = blocks.CharBlock(
        max_length=100,
        required=True,
        help_text="Titel der vises på billedet"
    )
    
    subtitle = blocks.CharBlock(
        max_length=200,
        required=True,
        help_text="Undertitel der vises under titlen"
    )
    
    button_text = blocks.CharBlock(
        max_length=50,
        default="Læs mere",
        help_text="Tekst på knappen"
    )
    
    button_link = PageChooserBlock(
        required=False,
        help_text="Side som knappen linker til"
    )


class CarouselBlock(blocks.StructBlock):
    """Full-width carousel with multiple slides"""
    
    slides = blocks.ListBlock(
        CarouselSlide(),
        help_text="Tilføj slides til carousel - du kan tilføje så mange som du vil"
    )
    
    autoplay = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Start carousel automatisk (auto-play)"
    )
    
    autoplay_interval = blocks.ChoiceBlock(
        choices=[
            ("3000", "3 sekunder"),
            ("5000", "5 sekunder"),
            ("7000", "7 sekunder"),
            ("10000", "10 sekunder"),
        ],
        default="5000",
        required=False,
        help_text="Hvor hurtigt carousel skal skifte slide"
    )

    class Meta:
        icon = "image"
        label = "Carousel"
        template = "blocks/carousel.html"
