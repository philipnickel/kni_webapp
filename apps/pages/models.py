from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    subheading = blocks.TextBlock(required=False)
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
    intro = RichTextField(blank=True, verbose_name="Intro tekst")
    body = StreamField([
        ("hero", HeroBlock()),
        ("trust_badges", blocks.ListBlock(TrustBadge())),
        ("featured_projects", blocks.ListBlock(FeaturedProject())),
        ("testimonials", blocks.ListBlock(blocks.TextBlock())),
    ], use_json_field=True, blank=True, verbose_name="Indhold")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Hjemmeside"
        verbose_name_plural = "Hjemmesider"


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

