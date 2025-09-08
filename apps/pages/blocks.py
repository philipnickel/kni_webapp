from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.blocks import PageChooserBlock


class StyleOptionsBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(
        choices=[
            ("surface", "Surface"),
            ("surface-soft", "Surface Soft"),
            ("hero", "Hero Gradient"),
        ], default="surface", required=False, help_text="Section background"
    )
    spacing = blocks.ChoiceBlock(
        choices=[("sm", "Small"), ("md", "Medium"), ("lg", "Large")],
        default="md", required=False
    )
    container = blocks.ChoiceBlock(
        choices=[("narrow", "Narrow"), ("normal", "Normal"), ("wide", "Wide")],
        default="normal", required=False
    )
    divider = blocks.BooleanBlock(required=False, help_text="Show a subtle top divider")

    class Meta:
        icon = "cog"
        label = "Style options"


def section_classes(style: dict) -> str:
    bg = style.get("background") or "surface"
    spacing = style.get("spacing") or "md"
    container = style.get("container") or "normal"
    classes = []
    classes.append("bg-hero text-inverse" if bg == "hero" else (f"bg-{bg}"))
    if spacing == "sm":
        classes.append("py-10")
    elif spacing == "lg":
        classes.append("py-24")
    else:
        classes.append("py-16")
    # container width
    if container == "narrow":
        classes.append("max-w-3xl mx-auto")
    elif container == "wide":
        classes.append("max-w-7xl mx-auto")
    else:
        classes.append("max-w-5xl mx-auto")
    return " ".join(classes)


class HeroV2Block(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    subheading = blocks.TextBlock(required=False)
    primary_text = blocks.CharBlock(required=False, help_text="Primary CTA label")
    primary_page = PageChooserBlock(required=False, help_text="Choose a page to link to")
    secondary_text = blocks.CharBlock(required=False)
    secondary_page = PageChooserBlock(required=False, help_text="Choose a page to link to")
    image = ImageChooserBlock(required=False)
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "pick"
        label = "Hero (V2)"
        template = "blocks/hero_v2.html"


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=False)
    button_text = blocks.CharBlock(required=True)
    button_page = PageChooserBlock(required=True, help_text="Choose a page to link to")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "site"
        label = "CTA"
        template = "blocks/cta.html"


class FeatureItem(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock(required=False)
    icon = blocks.ChoiceBlock(
        choices=[("check", "Check"), ("hammer", "Hammer"), ("leaf", "Leaf"), ("home", "Home")],
        default="check",
    )


class FeaturesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    items = blocks.ListBlock(FeatureItem())
    columns = blocks.ChoiceBlock(choices=[("2", "2"), ("3", "3"), ("4", "4")], default="3")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "list-ul"
        label = "Features"
        template = "blocks/features.html"


class RichTextSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(features=["h2","h3","bold","italic","link","ol","ul","hr","blockquote"])
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Rich text section"
        template = "blocks/richtext_section.html"


class TestimonialsBlock(blocks.StructBlock):
    testimonials = blocks.ListBlock(SnippetChooserBlock(target_model="pages.Testimonial"))
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "quote"
        label = "Testimonials"
        template = "blocks/testimonials.html"


class LogoCloudBlock(blocks.StructBlock):
    logos = blocks.ListBlock(SnippetChooserBlock(target_model="pages.Logo"))
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "image"
        label = "Logo cloud"
        template = "blocks/logo_cloud.html"


class FAQItem(blocks.StructBlock):
    question = blocks.CharBlock()
    answer = blocks.RichTextBlock(features=["bold","italic","link","ol","ul","hr","blockquote"])


class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    items = blocks.ListBlock(FAQItem())
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "help"
        label = "FAQ"
        template = "blocks/faq.html"


class ServicesGridBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    services = blocks.ListBlock(SnippetChooserBlock(target_model="pages.Service"))
    columns = blocks.ChoiceBlock(choices=[("2","2"),("3","3")], default="3")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "folder-open-inverse"
        label = "Services Grid"
        template = "blocks/services_grid.html"


class GalleryImage(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)


class ImageGalleryBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    images = blocks.ListBlock(GalleryImage())
    columns = blocks.ChoiceBlock(choices=[("2","2"),("3","3"),("4","4")], default="3")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "image"
        label = "Image Gallery"
        template = "blocks/image_gallery.html"


class ServiceInlineItem(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock(required=False)
    icon = blocks.ChoiceBlock(choices=[
        ("check", "Check"),
        ("hammer", "Hammer"),
        ("home", "Home"),
        ("leaf", "Leaf"),
    ], required=False, default="check")


class ServicesGridInlineBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    items = blocks.ListBlock(ServiceInlineItem())
    columns = blocks.ChoiceBlock(choices=[("2","2"),("3","3")], default="3")
    style = StyleOptionsBlock(required=False)

    class Meta:
        icon = "list-ul"
        label = "Services Grid (Inline)"
        template = "blocks/services_grid_inline.html"
