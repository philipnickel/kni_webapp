from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images import get_image_model_string
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.search import index


class ProjectTag(TaggedItemBase):
    content_object = ParentalKey(
        "Project", related_name="tagged_items", on_delete=models.CASCADE
    )


class Project(ClusterableModel, index.Indexed):
    site = models.ForeignKey("wagtailcore.Site", on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255,
        verbose_name="Projekt titel",
        help_text="F.eks. 'Køkken renovering' eller 'Træ terrasse'"
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True,
        verbose_name="URL slug",
        help_text="Automatisk genereret fra titlen"
    )
    description = RichTextField(
        blank=True,
        verbose_name="Projekt beskrivelse",
        help_text="Beskriv arbejdet, materialer og proces"
    )
    # Deprecated in UI: use tags instead of a single project type
    materials = models.TextField(
        blank=True,
        verbose_name="Materialer brugt",
        help_text="F.eks. 'Jatoba træ', 'Lærk', 'Eg', osv."
    )
    client_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Kunde navn",
        help_text="Valgfrit - kunde navn (anonymt eller med tilladelse)"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Lokation",
        help_text="F.eks. 'København', 'Privat bolig', eller 'Erhverv'"
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured projekt",
        help_text="Vis dette projekt fremhævet på forsiden"
    )
    published = models.BooleanField(
        default=True,
        verbose_name="Synlig på hjemmeside",
        help_text="Skal projektet vises på hjemmesiden?"
    )
    date = models.DateField(
        null=True, 
        blank=True,
        verbose_name="Projekt dato",
        help_text="Hvornår blev projektet færdiggjort?"
    )
    unsplash_image_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Unsplash billede ID",
        help_text="Unsplash foto ID til fallback billede (f.eks. 'photo-1560518883-ce09059eeffa')"
    )
    tags = ClusterTaggableManager(through=ProjectTag, blank=True)

    search_fields = [
        index.SearchField("title"),
        index.SearchField("description"),
        index.FilterField("tags"),
        index.FilterField("featured"),
        index.FilterField("published"),
    ]

    class Meta:
        ordering = ["-date", "title"]
        verbose_name = "Projekt"
        verbose_name_plural = "Projekter"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_first_image(self):
        """Get the first image for thumbnails"""
        first_image = self.images.first()
        return first_image.image if first_image else None
    
    @property
    def featured_image(self):
        """Get the featured image (first image)"""
        return self.get_first_image()
    
    def get_absolute_url(self):
        return f'/projekter/{self.slug}/'
    
    def admin_thumb(self):
        """Display thumbnail in admin list"""
        from django.utils.html import format_html
        first_image = self.get_first_image()
        if first_image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 4px;" />',
                first_image.get_rendition('fill-60x60').url
            )
        elif self.unsplash_image_id:
            return format_html(
                '<img src="https://images.unsplash.com/{}" width="60" height="60" style="object-fit: cover; border-radius: 4px;" />',
                f"{self.unsplash_image_id}?w=60&h=60&fit=crop&auto=format&q=80"
            )
        return format_html('<div style="width: 60px; height: 60px; background: #f5f5f5; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 12px;">Ingen billede</div>')
    admin_thumb.short_description = 'Billede'

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('published'),
            FieldPanel('featured'),
        ], heading="Grundlæggende information"),
        
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Projekt detaljer"),
        
        MultiFieldPanel([
            FieldPanel('client_name'),
            FieldPanel('location'),
            FieldPanel('materials'),
            FieldPanel('unsplash_image_id'),
        ], heading="Yderligere information"),
        
        InlinePanel('images', label="Projekt billeder", min_num=0, max_num=20),
    ]


class ProjectImage(Orderable):
    project = ParentalKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Projekt"
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Billede"
    )
    caption = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Billedtekst",
        help_text="Valgfri beskrivelse af billedet"
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Alt tekst",
        help_text="Beskrivelse for skærmlæsere"
    )

    panels = [
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = "Projekt billede"
        verbose_name_plural = "Projekt billeder"

    def __str__(self):
        order = self.sort_order if self.sort_order is not None else 0
        return f"{self.project.title} - Billede {order + 1}"