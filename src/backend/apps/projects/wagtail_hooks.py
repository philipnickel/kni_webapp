from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
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


# Removed ClickableTitleColumn - using Wagtail's built-in list_display_add_buttons instead

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
# Clean, production-ready Wagtail hooks for SaaS deployment


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
            // Fix project edit URLs - replace /edit/on/ with correct project IDs
            function fixProjectEditUrls() {{
                console.log('🔧 Fixing project edit URLs...');
                const projectRows = document.querySelectorAll('table tbody tr');
                console.log('📋 Found', projectRows.length, 'project rows');
                
                projectRows.forEach(function(row, index) {{
                    const cells = row.querySelectorAll('td');
                    if (cells.length >= 3) {{
                        // The title is typically in the 3rd cell (index 2)
                        const titleCell = cells[2];
                        if (titleCell && titleCell.querySelector('a')) {{
                            const link = titleCell.querySelector('a');
                            console.log(`🔗 Row ${{index}}: Link href = ${{link.href}}`);
                            
                            if (link.href.includes('/edit/on/')) {{
                                // Extract project ID from the row's checkbox value
                                const rowId = row.querySelector('input[type="checkbox"]');
                                console.log(`📋 Row ${{index}}: Checkbox value = ${{rowId ? rowId.value : 'none'}}`);
                                
                                if (rowId && rowId.value) {{
                                    const projectId = rowId.value;
                                    const newUrl = `/admin/snippets/projects/project/edit/${{projectId}}/`;
                                    link.href = newUrl;
                                    console.log(`✅ Fixed URL for row ${{index}}: ${{newUrl}}`);
                                }}
                            }}
                        }}
                    }}
                }});
                console.log('🔧 URL fixing complete');
            }}
            
            // Run on page load
            fixProjectEditUrls();
            
            // Re-run when the page content changes (for AJAX updates)
            const observer = new MutationObserver(function(mutations) {{
                mutations.forEach(function(mutation) {{
                    if (mutation.type === 'childList') {{
                        fixProjectEditUrls();
                    }}
                }});
            }});
            
            const tableContainer = document.querySelector('table');
            if (tableContainer) {{
                observer.observe(tableContainer, {{ childList: true, subtree: true }});
            }}
            
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
            
            // Add theme preview link to Wagtail admin header
            function addThemePreviewLink() {{
                const header = document.querySelector('header');
                if (header && !document.querySelector('.admin-theme-preview-link')) {{
                    const previewLink = document.createElement('div');
                    previewLink.className = 'admin-theme-preview-link';
                    previewLink.style.cssText = 'margin-left: auto; margin-right: 10px;';
                    previewLink.innerHTML = `
                        <a href="/admin/settings/pages/designsettings/" class="button button-secondary" style="display: flex; align-items: center; gap: 5px; text-decoration: none; font-size: 12px;">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width: 16px; height: 16px;">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM21 5a2 2 0 00-2-2h-4a2 2 0 00-2 2v12a4 4 0 004 4h4a2 2 0 002-2V5z"></path>
                            </svg>
                            <span>Tema Preview</span>
                        </a>
                    `;
                    
                    // Add to the right side of the header
                    const headerActions = header.querySelector('.c-header__actions') || header.querySelector('.c-header__inner') || header;
                    if (headerActions) {{
                        headerActions.appendChild(previewLink);
                    }}
                }}
            }}
            
            // Add theme preview link when page loads
            addThemePreviewLink();
            
            // Also add it when navigating (for SPA-like behavior)
            const adminObserver = new MutationObserver(function(mutations) {{
                mutations.forEach(function(mutation) {{
                    if (mutation.type === 'childList') {{
                        addThemePreviewLink();
                    }}
                }});
            }});
            
            adminObserver.observe(document.body, {{
                childList: true,
                subtree: true
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


# Custom filter for Project admin - simplified to avoid template issues
class ProjectFilterSet(WagtailFilterSet):
    """Enhanced filtering for projects with visual cards"""
    featured = django_filters.BooleanFilter(
        label='Featured Projects'
    )
    published = django_filters.BooleanFilter(
        label='Published'
    )
    date = django_filters.DateFilter(
        label='Project Date',
        lookup_expr='gte'
    )

    class Meta:
        model = Project
        fields = ['featured', 'published', 'date']


# Enhanced ViewSet for Project management with visual gallery
class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = 'folder-inverse'
    menu_label = 'Projekter'
    menu_name = 'projects'
    menu_order = 200
    add_to_admin_menu = True

    # Simple list display - let JavaScript fix the URLs
    list_display = ['admin_thumb', 'title', 'client_name', 'date', 'featured', 'published']

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


# Dashboard enhancements hook - temporarily disabled to fix admin panel error
# @hooks.register('construct_homepage_panels')
def add_project_dashboard_metrics_disabled(request, panels):
    """Add project metrics dashboard to Wagtail admin home - DISABLED due to media attribute error"""
    # This hook was causing 'dict' object has no attribute 'media' error
    # The issue is that we were appending a dict to panels instead of a proper panel object
    # TODO: Implement this using proper Wagtail panel objects or custom admin views
    pass
