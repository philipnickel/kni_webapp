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
    """Custom column for displaying project image previews"""
    
    def get_cell_context_data(self, instance, parent_context):
        context = super().get_cell_context_data(instance, parent_context)
        
        # Get the first image from the project
        first_image = instance.get_first_image()
        if first_image:
            # Create a small rendition for the preview
            try:
                rendition = first_image.get_rendition('fill-100x100-c100')
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
        
        if context['image_url']:
            return format_html(
                '<img src="{}" alt="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;">',
                context['image_url'],
                context['image_alt']
            )
        else:
            return format_html(
                '<div style="width: 50px; height: 50px; background: #f0f0f0; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #999; font-size: 12px;">No image</div>'
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


# Custom admin menu items
@hooks.register('register_admin_menu_item')
def register_project_analytics_menu_item():
    """Add project analytics to admin menu"""
    return MenuItem(
        'Projekt Analytics',
        reverse('wagtailadmin_home'),  # For now, link to home - can be custom view later
        icon_name='doc-full-inverse',
        order=250
    )


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
    """Add custom CSS to admin"""
    return format_html('''
        <link rel="stylesheet" href="/static/projects/admin/css/project-admin.css">
        <style>
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
    featured = django_filters.BooleanFilter()
    published = django_filters.BooleanFilter()
    
    class Meta:
        model = Project
        fields = ['featured', 'published']


# Custom ViewSet for Project management
class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = 'folder-inverse'
    menu_label = 'Projekter'
    menu_name = 'projects'
    menu_order = 200
    add_to_admin_menu = True
    
    list_display = ['admin_thumb', 'title', 'client_name', 'date', 'featured', 'published']
    list_filter = ['featured', 'published']
    search_fields = ['title', 'description', 'client_name', 'location', 'materials']
    list_per_page = 20
    ordering = ['-date', 'title']
    
    
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
