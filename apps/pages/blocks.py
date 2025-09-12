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
