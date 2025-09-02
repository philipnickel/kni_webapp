from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    subheading = blocks.TextBlock(required=False)
    background_image = ImageChooserBlock(required=False)
    cta_text = blocks.CharBlock(required=False, help_text="Button text")
    cta_anchor = blocks.CharBlock(required=False, help_text="Anchor id to scroll to")

    class Meta:
        icon = "placeholder"
        label = "Hero"


class TrustBadge(blocks.StructBlock):
    label = blocks.CharBlock()
    description = blocks.CharBlock(required=False)


class FeaturedProject(blocks.StructBlock):
    project_slug = blocks.CharBlock(help_text="Slug of a Project to feature")


class HomePage(Page):
    intro = RichTextField(blank=True)
    body = StreamField([
        ("hero", HeroBlock()),
        ("trust_badges", blocks.ListBlock(TrustBadge())),
        ("featured_projects", blocks.ListBlock(FeaturedProject())),
        ("testimonials", blocks.ListBlock(blocks.TextBlock())),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

