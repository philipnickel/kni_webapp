from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


class ProjectTag(TaggedItemBase):
    content_object = ParentalKey(
        "Project", related_name="tagged_items", on_delete=models.CASCADE
    )


class Project(ClusterableModel, index.Indexed):
    site = models.ForeignKey("wagtailcore.Site", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True)
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

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        FieldPanel("description"),
        FieldPanel("tags"),
        MultiFieldPanel([
            FieldPanel("featured"),
            FieldPanel("published"),
            FieldPanel("date"),
        ], heading="Flags"),
        InlinePanel("images", label="Images"),
    ]


class ProjectImage(Orderable):
    project = ParentalKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name="project_images",
    )
    alt = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, blank=True)
    BEFORE_AFTER_CHOICES = [
        ("none", "None"),
        ("before", "Before"),
        ("after", "After"),
    ]
    before_after = models.CharField(
        max_length=8, choices=BEFORE_AFTER_CHOICES, default="none"
    )

    def __str__(self):
        return f"{self.project.title} — {self.alt}"

    panels = [
        FieldPanel("image"),
        FieldPanel("alt"),
        FieldPanel("caption"),
        FieldPanel("before_after"),
    ]
