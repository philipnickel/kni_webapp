from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail import hooks
from wagtail.admin.menu import MenuItem, AdminOnlyMenuItem
from wagtail.admin.widgets import Button
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.ui.tables import UpdatedAtColumn, Column
from wagtail.images.models import Image
from wagtail.images import get_image_model_string
import django_filters

from .models import Project, ProjectImage
# ProjectPage import removed - individual project pages are no longer used


class ImagePreviewColumn(Column):
    """Custom column for displaying project image previews with enhanced card-style layout"""

    def get_cell_context_data(self, instance, parent_context):
        context = super().get_cell_context_data(instance, parent_context)

        # Get the first image from the project
        first_image = instance.get_first_image()
        if first_image:
            # Create a small rendition for the preview
            try:
                rendition = first_image.get_rendition('fill-80x80-c100')
                context['image_url'] = rendition.url
                context['image_alt'] = first_image.title or instance.title
            except Exception:
                context['image_url'] = None
                context['image_alt'] = None
        else:
            context['image_url'] = None
            context['image_alt'] = None

        return context

    def render_html(self, parent_context):
        context = self.get_cell_context_data(parent_context['instance'], parent_context)
        instance = parent_context['instance']

        # Enhanced card-style thumbnail with status indicators
        if context['image_url']:
            featured_badge = '<div class="featured-badge">★</div>' if instance.featured else ''
            published_dot = 'published' if instance.published else 'unpublished'

            return format_html(
                '<div class="project-card-thumbnail">' +
                '<img src="{}" alt="{}" class="project-thumb-img">' +
                '<div class="project-status-indicator {}"></div>' +
                '{}' +
                '</div>',
                context['image_url'],
                context['image_alt'],
                published_dot,
                featured_badge
            )
        else:
            return format_html(
                '<div class="project-card-thumbnail no-image">' +
                '<div class="no-image-placeholder">' +
                '<svg width="24" height="24" viewBox="0 0 24 24" fill="#999">' +
                '<path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>' +
                '</svg>' +
                '</div>' +
                '<div class="project-status-indicator {}"></div>' +
                '</div>',
                'published' if instance.published else 'unpublished'
            )
# Temporarily disabled imports for compatibility - will fix these later
# from .admin_dashboard import (
#     ProjectDashboardSummary, ProjectStatusWidget, ProjectBudgetWidget,
#     RecentActivityWidget, WorkflowStatusWidget, CollectionDistributionWidget,
#     QuickActionsWidget
# )
# from .filters import ProjectPageFilterSet
# from . import bulk_actions  # Import to register bulk actions


# Legacy ModelAdmin code - commented out for new Wagtail version compatibility
# Will be replaced with ViewSets or Snippets registration

# class ProjectPagePermissionHelper(PermissionHelper):
#     """Custom permission helper for project pages"""
#     
#     def user_can_list(self, user):
#         """Allow all admin users to list projects"""
#         return user.has_perm('wagtailadmin.access_admin')
#     
#     def user_can_create(self, user):
#         """Control who can create projects"""
#         return user.has_perm('projects.add_projectpage') or user.is_superuser
#     
#     def user_can_edit_obj(self, user, obj):
#         """Control who can edit specific projects"""
#         # Superusers can edit all
#         if user.is_superuser:
#             return True
#             
#         # Owners can edit their own projects
#         if hasattr(obj, 'owner') and obj.owner == user:
#             return True
#             
#         # Staff with permission can edit
#         if user.is_staff and user.has_perm('projects.change_projectpage'):
#             return True
#             
#         return False
#     
#     def user_can_delete_obj(self, user, obj):
#         """Control who can delete projects"""
#         # Only superusers and project owners can delete
#         if user.is_superuser:
#             return True
#             
#         if hasattr(obj, 'owner') and obj.owner == user:
#             return user.has_perm('projects.delete_projectpage')
#             
#         return False


# class ProjectAdmin(ModelAdmin):
#     """ModelAdmin for the legacy Project model (transitional)"""
#     model = Project
#     menu_label = 'Legacy Projekter'
#     menu_icon = 'folder-inverse'
#     menu_order = 300
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     
#     list_display = ['admin_thumb', 'title', 'client_name', 'date', 'featured', 'published']
#     list_filter = ['featured', 'published', 'date', 'tags']
#     search_fields = ['title', 'description', 'client_name', 'location', 'materials']
#     list_per_page = 20
#     ordering = ['-date', 'title']
#     
#     def admin_thumb(self, obj):
#         return obj.admin_thumb()
#     admin_thumb.short_description = 'Billede'


# Register legacy project admin
# modeladmin_register(ProjectAdmin)


# Custom dashboard panels - temporarily disabled
# @hooks.register('construct_homepage_panels')
# def add_project_dashboard_panels(request, panels):
#     """Add custom project dashboard panels to Wagtail admin home"""
#     
#     # Only show to users with project access
#     if not request.user.has_perm('wagtailadmin.access_admin'):
#         return
#     
#     # Dashboard summary (always first)
#     summary_widget = ProjectDashboardSummary()
#     summary_data = summary_widget.render()
#     panels.append({
#         'template': summary_data['template'],
#         'context': summary_data['context'],
#         'order': 100
#     })
#     
#     # Quick actions
#     actions_widget = QuickActionsWidget()
#     actions_data = actions_widget.render()
#     panels.append({
#         'template': actions_data['template'],
#         'context': actions_data['context'],
#         'order': 150
#     })
#     
#     # Project status chart
#     status_widget = ProjectStatusWidget()
#     status_data = status_widget.render()
#     panels.append({
#         'template': status_data['template'],
#         'context': status_data['context'],
#         'order': 200
#     })
#     
#     # Recent activity (for staff users)
#     if request.user.is_staff:
#         activity_widget = RecentActivityWidget()
#         activity_data = activity_widget.render()
#         panels.append({
#             'template': activity_data['template'],
#             'context': activity_data['context'],
#             'order': 250
#         })
#     
#     # Workflow status (for users with workflow access)
#     if request.user.is_staff or request.user.has_perm('projects.can_approve_projects'):
#         workflow_widget = WorkflowStatusWidget()
#         workflow_data = workflow_widget.render()
#         panels.append({
#             'template': workflow_data['template'],
#             'context': workflow_data['context'],
#             'order': 300
#         })


# Custom admin menu items - removed Project Analytics as requested
# Note: Images should appear in Wagtail sidebar by default via wagtail.images app


# Custom page listing buttons
@hooks.register('register_page_listing_buttons')
def add_project_listing_buttons(page, user, next_url=None):
    """Add custom buttons to project page listings"""
    try:
        # ProjectPage check removed - individual project pages are no longer used
        if False:  # isinstance(page.specific, ProjectPage):
            project = page.specific
            
            # Quick status change button
            if user.has_perm('projects.change_projectpage'):
                if getattr(project, 'project_status', None) != 'completed':
                    yield Button(
                        'Mark Complete',
                        f'/admin/projects/quick-complete/{project.id}/',
                        icon_name='success',
                        priority=10
                    )
            
            # Workflow button
            if user.is_staff and hasattr(project, 'current_workflow_state'):
                workflow_state = project.current_workflow_state
                if workflow_state and workflow_state.status == 'in_progress':
                    yield Button(
                        'Review Workflow',
                        f'/admin/workflows/{workflow_state.id}/',
                        icon_name='list-ul',
                        priority=20
                    )
    except Exception:
        # Never break the listing on hook failure
        return


# Add custom CSS and JS to admin
@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add custom CSS to admin with enhanced project gallery styling"""
    return format_html('''
        <link rel="stylesheet" href="/static/projects/admin/css/project-admin.css">
        <style>
            /* Enhanced Project Gallery Cards */
            .project-card-thumbnail {{
                position: relative;
                display: inline-block;
                width: 80px;
                height: 80px;
                border-radius: 8px;
                overflow: hidden;
                border: 2px solid #e5e7eb;
                transition: all 0.2s ease;
                background: #f9fafb;
            }}

            .project-card-thumbnail:hover {{
                border-color: #4d7a3a;
                transform: scale(1.05);
                box-shadow: 0 4px 12px rgba(77, 122, 58, 0.2);
            }}

            .project-thumb-img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
            }}

            .project-card-thumbnail.no-image {{
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
            }}

            .no-image-placeholder {{
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0.5;
            }}

            .project-status-indicator {{
                position: absolute;
                top: 4px;
                right: 4px;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                border: 2px solid white;
                box-shadow: 0 1px 3px rgba(0,0,0,0.2);
            }}

            .project-status-indicator.published {{
                background: #22c55e;
            }}

            .project-status-indicator.unpublished {{
                background: #ef4444;
            }}

            .featured-badge {{
                position: absolute;
                top: -2px;
                left: -2px;
                background: #f59e0b;
                color: white;
                font-size: 12px;
                padding: 2px 4px;
                border-radius: 0 0 8px 0;
                font-weight: bold;
                box-shadow: 0 1px 3px rgba(0,0,0,0.2);
            }}

            /* Enhanced table row styling for project gallery */
            .listing tbody tr:hover .project-card-thumbnail {{
                transform: scale(1.1);
            }}

            .listing tbody tr {{
                transition: all 0.2s ease;
            }}

            .listing tbody tr:hover {{
                background-color: #f8fffe;
                border-left: 3px solid #4d7a3a;
            }}

            /* Image upload helper styling */
            .image-upload-helper {{
                background: #e8f4fd;
                border: 1px solid #bee5eb;
                border-radius: 4px;
                padding: 15px;
                margin: 15px 0;
                font-size: 14px;
                line-height: 1.5;
            }}

            .image-upload-helper .icon {{
                font-size: 18px;
                margin-right: 8px;
            }}

            .bulk-upload-link {{
                display: inline-block;
                background: #007cba;
                color: white !important;
                padding: 8px 16px;
                border-radius: 4px;
                text-decoration: none;
                margin: 0 4px;
                font-weight: 500;
                font-size: 12px;
            }}

            .bulk-upload-link:hover {{
                background: #005a87;
                color: white !important;
                text-decoration: none;
            }}

            .inline-panel .w-panel__heading {{
                position: relative;
            }}

            /* Filter enhancements */
            .filter-panel {{
                background: white;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}

            .filter-row {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-bottom: 15px;
            }}
        </style>
    ''')


@hooks.register('insert_global_admin_js')
def global_admin_js():
    """Add custom JavaScript to admin"""
    return format_html('''
        <script src="/static/projects/admin/js/project-admin.js"></script>
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Add helpful guidance for image uploads in projects
            const imagesPanels = document.querySelectorAll('[data-contentpath="images"]');
            imagesPanels.forEach(function(panel) {{
                const panelContent = panel.querySelector('.w-panel__content');
                if (panelContent && !panel.querySelector('.image-upload-helper')) {{
                    const helper = document.createElement('div');
                    helper.className = 'image-upload-helper';
                    helper.innerHTML = `
                        <div style="display: flex; align-items: center; margin-bottom: 10px;">
                            <span class="icon">💡</span>
                            <strong>Tip til hurtig upload af flere billeder:</strong>
                        </div>
                        <ol style="margin: 0; padding-left: 20px;">
                            <li>Klik på <a href="/admin/images/multiple/add/" target="_blank" class="bulk-upload-link">📁 Upload flere billeder</a> (åbner i nyt vindue)</li>
                            <li>Vælg og upload alle dine billeder på én gang</li>
                            <li>Kom tilbage til denne side og vælg billederne fra listen</li>
                        </ol>
                        <div style="margin-top: 8px; font-size: 12px; opacity: 0.8;">
                            Du kan også uploade billeder individuelt ved at klikke "Tilføj projekt billede" nedenfor.
                        </div>
                    `;
                    panelContent.insertBefore(helper, panelContent.firstChild);
                }}
            }});
        }});
        </script>
    ''')


# Custom user permissions setup
@hooks.register('register_permissions')
def register_project_permissions():
    """Register custom project permissions with Wagtail without side-effects.

    Note: Group creation/assignment should not happen in this hook because it
    runs during many admin requests (including publish actions). Side-effects
    here can cause unexpected errors within request transactions. The custom
    permissions themselves are declared on ProjectPage.Meta.permissions and are
    created by Django migrations.
    """

    # ProjectPage permissions removed - individual project pages are no longer used
    pass


# Workflow integration
@hooks.register('after_publish_page')
def after_project_publish(request, page):
    """Handle actions after project page is published"""
    
    # ProjectPage check removed - individual project pages are no longer used
    if False:  # isinstance(page.specific, ProjectPage):
        project = page.specific
        
        # Send notifications for completed projects
        if project.project_status == 'completed':
            # Logic to send completion notifications
            pass
        
        # Update related analytics/caches
        # Could trigger background tasks for analytics updates


@hooks.register('after_delete_page')
def after_project_delete(request, page):
    """Handle cleanup after project deletion"""
    
    # ProjectPage check removed - individual project pages are no longer used
    if False:  # isinstance(page.specific, ProjectPage):
        # Clean up related data, send notifications, etc.
        pass


# Custom admin views registration - temporarily disabled
# @hooks.register('register_admin_urls')
# def register_project_admin_urls():
#     """Register custom admin URLs"""
#     
#     from .admin_views import (
#         project_quick_complete,
#         project_analytics_view,
#         project_bulk_actions_view
#     )
#     
#     return [
#         path(
#             'projects/quick-complete/<int:project_id>/',
#             project_quick_complete,
#             name='project_quick_complete'
#         ),
#         path(
#             'projects/analytics/',
#             project_analytics_view,
#             name='project_analytics'
#         ),
#         path(
#             'projects/bulk-actions/',
#             project_bulk_actions_view,
#             name='project_bulk_actions'
#         ),
#     ]


# Content scheduling hooks
@hooks.register('before_publish_page')
def before_project_publish(request, page):
    """Actions before publishing a project"""
    
    # ProjectPage check removed - individual project pages are no longer used
    if False:  # isinstance(page.specific, ProjectPage):
        project = page.specific
        
        # Validate required fields for publishing
        if project.project_status == 'completed' and not project.project_date:
            # Could add validation or auto-set completion date
            pass


# Search customization
@hooks.register('register_page_listing_more_buttons')
def add_search_filters_button(page, user, next_url=None):
    """Add advanced search/filter options"""
    try:
        if user.is_staff:
            yield Button(
                'Advanced Filters',
                reverse('wagtailadmin_pages:index') + '?advanced=true',
                icon_name='cogs',
                priority=100
            )
    except Exception:
        return


# Email notifications for workflow events
@hooks.register('workflow_submitted')
def project_workflow_submitted(sender, **kwargs):
    """Send notifications when project enters workflow"""
    
    workflow_state = kwargs.get('workflow_state')
    if workflow_state and hasattr(workflow_state.content_object, '_meta'):
        if workflow_state.content_object._meta.model_name == 'projectpage':
            # Send notification to approvers
            pass


@hooks.register('workflow_approved')
def project_workflow_approved(sender, **kwargs):
    """Handle project workflow approval"""
    
    workflow_state = kwargs.get('workflow_state')
    if workflow_state and hasattr(workflow_state.content_object, '_meta'):
        if workflow_state.content_object._meta.model_name == 'projectpage':
            # Send approval notification
            # Update project status if needed
            pass


@hooks.register('workflow_rejected')
def project_workflow_rejected(sender, **kwargs):
    """Handle project workflow rejection"""
    
    workflow_state = kwargs.get('workflow_state')
    if workflow_state and hasattr(workflow_state.content_object, '_meta'):
        if workflow_state.content_object._meta.model_name == 'projectpage':
            # Send rejection notification with feedback
            pass


# Custom filter for Project admin
class ProjectFilterSet(WagtailFilterSet):
    """Enhanced filtering for projects with visual cards"""
    featured = django_filters.BooleanFilter(
        label='Featured Projects',
        widget=django_filters.widgets.BooleanWidget()
    )
    published = django_filters.BooleanFilter(
        label='Published',
        widget=django_filters.widgets.BooleanWidget()
    )
    date = django_filters.DateFromToRangeFilter(
        label='Project Date Range',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'})
    )

    # Tag filtering
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=None,  # Will be set in __init__
        label='Tags',
        widget=django_filters.widgets.QueryArrayWidget()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set tags queryset dynamically
        from taggit.models import Tag
        self.filters['tags'].queryset = Tag.objects.filter(
            taggit_taggeditem_items__content_type__model='project'
        ).distinct()

    class Meta:
        model = Project
        fields = ['featured', 'published', 'date', 'tags']


# Enhanced ViewSet for Project management with visual gallery
class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = 'folder-inverse'
    menu_label = 'Projekter'
    menu_name = 'projects'
    menu_order = 200
    add_to_admin_menu = True

    # Enhanced list display with visual cards
    list_display = [
        ImagePreviewColumn('admin_thumb', label='Billede', width='120px'),
        'title',
        'client_name',
        'date',
        'featured',
        'published'
    ]

    # Enhanced filtering
    filterset_class = ProjectFilterSet
    list_filter = ['featured', 'published', 'date', 'tags']
    search_fields = ['title', 'description', 'client_name', 'location', 'materials']
    list_per_page = 20
    ordering = ['-date', 'title']

    # Enable bulk actions
    list_export = ['title', 'client_name', 'date', 'featured', 'published']
    export_headings = {
        'title': 'Projekt Titel',
        'client_name': 'Kunde',
        'date': 'Dato',
        'featured': 'Featured',
        'published': 'Publiceret'
    }
    
    
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
            FieldPanel('description'),
        ], heading="Grundlæggende information"),
        
        MultiFieldPanel([
            FieldPanel('client_name'),
            FieldPanel('location'),
            FieldPanel('materials'),
            FieldPanel('date'),
        ], heading="Projekt detaljer"),
        
        MultiFieldPanel([
            FieldPanel('featured'),
            FieldPanel('published'),
            FieldPanel('tags'),
        ], heading="Visning og kategorisering"),
        
        InlinePanel(
            'images', 
            label="Projekt billeder",
            help_text="💡 Tip: For at uploade flere billeder på én gang, se vejledningen øverst i dette panel."
        ),
    ]


# Register the Project model as a snippet
register_snippet(ProjectViewSet)


# Dashboard enhancements hook
@hooks.register('construct_homepage_panels')
def add_project_dashboard_metrics(request, panels):
    """Add project metrics dashboard to Wagtail admin home"""
    if not request.user.has_perm('wagtailadmin.access_admin'):
        return

    try:
        # Get project statistics
        from django.db.models import Count, Q
        from datetime import datetime, timedelta

        total_projects = Project.objects.count()
        published_projects = Project.objects.filter(published=True).count()
        featured_projects = Project.objects.filter(featured=True).count()

        # Recent projects (last 30 days)
        thirty_days_ago = datetime.now().date() - timedelta(days=30)
        recent_projects = Project.objects.filter(
            date__gte=thirty_days_ago
        ).count() if total_projects > 0 else 0

        # Project status distribution (if using ProjectPage model)
        try:
            from .models import ProjectPage
            status_stats = ProjectPage.objects.aggregate(
                planning=Count('id', filter=Q(project_status='planning')),
                in_progress=Count('id', filter=Q(project_status='in_progress')),
                completed=Count('id', filter=Q(project_status='completed')),
                on_hold=Count('id', filter=Q(project_status='on_hold'))
            )
        except:
            status_stats = None

        # Create dashboard panel HTML
        dashboard_html = format_html(
            '''
            <div class="project-dashboard-metrics">
                <h3>📊 Projekt Oversigt</h3>
                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-number">{}</div>
                        <div class="metric-label">Total Projekter</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-number">{}</div>
                        <div class="metric-label">Publicerede</div>
                    </div>
                    <div class="metric-card featured">
                        <div class="metric-number">{}</div>
                        <div class="metric-label">Featured</div>
                    </div>
                    <div class="metric-card recent">
                        <div class="metric-number">{}</div>
                        <div class="metric-label">Seneste 30 dage</div>
                    </div>
                </div>
                <div class="quick-actions">
                    <a href="/admin/snippets/projects/project/add/" class="quick-action-btn primary">
                        ➕ Nyt Projekt
                    </a>
                    <a href="/admin/snippets/projects/project/" class="quick-action-btn secondary">
                        📁 Se Alle Projekter
                    </a>
                    <a href="/admin/images/multiple/add/" class="quick-action-btn tertiary">
                        🖼️ Upload Billeder
                    </a>
                </div>
            </div>
            <style>
                .project-dashboard-metrics {{
                    background: white;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .metrics-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                    gap: 15px;
                    margin: 15px 0;
                }}
                .metric-card {{
                    background: #f9fafb;
                    border: 1px solid #e5e7eb;
                    border-radius: 6px;
                    padding: 15px;
                    text-align: center;
                    transition: all 0.2s ease;
                }}
                .metric-card:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }}
                .metric-card.featured {{
                    border-color: #f59e0b;
                    background: #fef3c7;
                }}
                .metric-card.recent {{
                    border-color: #3b82f6;
                    background: #dbeafe;
                }}
                .metric-number {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #1f2937;
                    margin-bottom: 5px;
                }}
                .metric-label {{
                    font-size: 12px;
                    color: #6b7280;
                    text-transform: uppercase;
                    font-weight: 600;
                    letter-spacing: 0.05em;
                }}
                .quick-actions {{
                    display: flex;
                    gap: 10px;
                    flex-wrap: wrap;
                    margin-top: 15px;
                    padding-top: 15px;
                    border-top: 1px solid #e5e7eb;
                }}
                .quick-action-btn {{
                    display: inline-flex;
                    align-items: center;
                    padding: 8px 16px;
                    border-radius: 6px;
                    text-decoration: none;
                    font-weight: 500;
                    font-size: 14px;
                    transition: all 0.2s ease;
                }}
                .quick-action-btn.primary {{
                    background: #4d7a3a;
                    color: white;
                }}
                .quick-action-btn.primary:hover {{
                    background: #3a5e2c;
                    transform: translateY(-1px);
                }}
                .quick-action-btn.secondary {{
                    background: #f3f4f6;
                    color: #374151;
                    border: 1px solid #d1d5db;
                }}
                .quick-action-btn.secondary:hover {{
                    background: #e5e7eb;
                }}
                .quick-action-btn.tertiary {{
                    background: #3b82f6;
                    color: white;
                }}
                .quick-action-btn.tertiary:hover {{
                    background: #2563eb;
                }}
                @media (max-width: 768px) {{
                    .metrics-grid {{
                        grid-template-columns: repeat(2, 1fr);
                    }}
                    .quick-actions {{
                        flex-direction: column;
                    }}
                }}
            </style>
            ''',
            total_projects,
            published_projects,
            featured_projects,
            recent_projects
        )

        panels.append({
            'template_name': None,
            'content': dashboard_html,
            'order': 100
        })

    except Exception as e:
        # Fail silently if there are issues
        pass
