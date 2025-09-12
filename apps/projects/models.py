from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Orderable, Page, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.images import get_image_model_string
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.search import index
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError


class ProjectTag(TaggedItemBase):
    content_object = ParentalKey(
        "Project", related_name="tagged_items", on_delete=models.CASCADE
    )


class Project(ClusterableModel, index.Indexed):
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


# New Page-based models for Wagtail-native architecture

class ProjectPageTag(TaggedItemBase):
    """Tags for ProjectPage model"""
    content_object = ParentalKey(
        "ProjectPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class ProjectPage(Page):
    """Page-based Project model with workflow, draft, locking, and revision capabilities"""
    
    
    # Core content fields
    description = RichTextField(
        blank=True,
        verbose_name="Projekt beskrivelse",
        help_text="Beskriv arbejdet, materialer og proces"
    )
    
    # Project details
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
    
    # Status fields
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured projekt",
        help_text="Vis dette projekt fremhævet på forsiden"
    )
    project_date = models.DateField(
        null=True, 
        blank=True,
        verbose_name="Projekt dato",
        help_text="Hvornår blev projektet færdiggjort?"
    )
    
    # Tags
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)
    
    # Priority level for project management
    priority = models.CharField(
        max_length=10,
        choices=[
            ('low', 'Lav'),
            ('medium', 'Medium'),
            ('high', 'Høj'),
            ('urgent', 'Akut')
        ],
        default='medium',
        verbose_name="Prioritet",
        help_text="Projekt prioritet for planlægning"
    )
    
    # Project status
    project_status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planlægning'),
            ('in_progress', 'I gang'),
            ('completed', 'Færdig'),
            ('on_hold', 'På pause'),
            ('cancelled', 'Annulleret')
        ],
        default='planning',
        verbose_name="Status",
        help_text="Nuværende projekt status"
    )
    
    # Budget information
    estimated_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Estimeret budget",
        help_text="Estimeret budget for projektet (DKK)"
    )
    
    # Page inherits revision and workflow capabilities automatically

    # Search configuration
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("materials"),
        index.SearchField("location"),
        index.SearchField("client_name"),
        index.FilterField("tags"),
        index.FilterField("featured"),
        index.FilterField("project_date"),
        index.FilterField("priority"),
        index.FilterField("project_status"),
        index.AutocompleteField('title'),
        index.AutocompleteField('description'),
        index.RelatedFields('tags', [
            index.SearchField('name'),
        ]),
    ]

    @property
    def revisions(self):
        return self._revisions
    
    def clean(self):
        super().clean()
        # Add custom validation
        if self.estimated_budget and self.estimated_budget < 0:
            raise ValidationError({'estimated_budget': 'Budget kan ikke være negativt'})

    # Admin panels with improved organization using TabbedInterface
    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('featured'),
            FieldPanel('priority'),
            FieldPanel('project_status'),
        ], heading="Status"),
        
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('project_date'),
            FieldPanel('tags'),
        ], heading="Projekt detaljer"),
        
        InlinePanel('project_images', label="Projekt billeder", min_num=0, max_num=20),
    ]
    
    # Additional details tab
    details_panels = [
        MultiFieldPanel([
            FieldPanel('client_name'),
            FieldPanel('location'),
            FieldPanel('materials'),
        ], heading="Kunde information"),
        
        MultiFieldPanel([
            FieldPanel('estimated_budget'),
        ], heading="Økonomi"),
    ]
    
    # Use TabbedInterface for better organization
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Indhold'),
        ObjectList(details_panels, heading='Detaljer'),
        ObjectList(Page.promote_panels, heading='SEO & Markedsføring'),
        ObjectList(Page.settings_panels, heading='Indstillinger'),
    ])

    # Page hierarchy rules - DEPRECATED: ProjectPage is no longer used
    # Projects are now managed as snippets, not pages
    parent_page_types = []  # No parent pages allowed
    subpage_types = []

    # Template - DEPRECATED: Individual project pages are no longer used
    # Projects are now managed as snippets and displayed only in the gallery
    template = 'projects/project_page.html'  # This template has been removed

    class Meta:
        verbose_name = "Projekt Side"
        verbose_name_plural = "Projekt Sider"
        permissions = [
            ('can_approve_projects', 'Can approve projects'),
            ('can_manage_project_budget', 'Can manage project budget'),
            ('can_set_project_priority', 'Can set project priority'),
        ]

    def get_first_image(self):
        """Get the first image for thumbnails"""
        first_image = self.project_images.first()
        return first_image.image if first_image else None
    
    @property
    def featured_image(self):
        """Get the featured image (first image)"""
        return self.get_first_image()
    
    def admin_thumb(self):
        """Display thumbnail in admin list with status indicators"""
        from django.utils.html import format_html
        first_image = self.get_first_image()
        
        status_color = self.get_project_status_color()
        priority_color = self.get_priority_color()
        
        if first_image:
            return format_html(
                '<div style="position: relative; display: inline-block;">'
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 4px;" />'
                '<div style="position: absolute; top: 2px; right: 2px; width: 8px; height: 8px; background: {}; border-radius: 50%; border: 1px solid white;"></div>'
                '<div style="position: absolute; bottom: 2px; right: 2px; width: 8px; height: 8px; background: {}; border-radius: 50%; border: 1px solid white;"></div>'
                '</div>',
                first_image.get_rendition('fill-60x60').url,
                status_color,
                priority_color
            )
        return format_html(
            '<div style="width: 60px; height: 60px; background: #f5f5f5; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 12px; position: relative;">'
            'Ingen billede'
            '<div style="position: absolute; top: 2px; right: 2px; width: 8px; height: 8px; background: {}; border-radius: 50%; border: 1px solid white;"></div>'
            '<div style="position: absolute; bottom: 2px; right: 2px; width: 8px; height: 8px; background: {}; border-radius: 50%; border: 1px solid white;"></div>'
            '</div>',
            status_color,
            priority_color
        )
    admin_thumb.short_description = 'Billede'
    
    def get_project_status_color(self):
        """Get color class for project status"""
        status_colors = {
            'planning': 'blue',
            'in_progress': 'yellow', 
            'completed': 'green',
            'on_hold': 'gray',
            'cancelled': 'red'
        }
        return status_colors.get(self.project_status, 'blue')
    
    def get_priority_color(self):
        """Get color class for priority"""
        priority_colors = {
            'low': 'green',
            'medium': 'yellow',
            'high': 'orange', 
            'urgent': 'red'
        }
        return priority_colors.get(self.priority, 'yellow')

    def get_context(self, request):
        """Add extra context to the template"""
        context = super().get_context(request)
        
        # Add other projects from the same parent
        if self.get_parent():
            context['other_projects'] = (
                self.get_parent().get_children().live().public()
                .not_page(self).specific()[:6]
            )
            
            # Add related projects with similar tags
            if self.tags.exists():
                # Get projects that share tags with this project
                project_tags = self.tags.values_list('pk', flat=True)
                context['related_projects'] = (
                    ProjectPage.objects.live().public()
                    .filter(tags__in=project_tags)
                    .exclude(id=self.id)
                    .distinct()[:4]
                )
            else:
                context['related_projects'] = []
        else:
            context['other_projects'] = []
            context['related_projects'] = []
            
        return context


class ProjectPageImage(Orderable):
    """Images for ProjectPage"""
    project_page = ParentalKey(
        'ProjectPage',
        related_name='project_images',
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
        FieldPanel('caption'),
        FieldPanel('alt_text'),
    ]

    class Meta:
        verbose_name = "Projekt billede"
        verbose_name_plural = "Projekt billeder"

    def __str__(self):
        order = self.sort_order if self.sort_order is not None else 0
        return f"{self.project_page.title} - Billede {order + 1}"