from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from wagtail import hooks
from wagtail.admin.menu import MenuItem, AdminOnlyMenuItem
from wagtail.admin.widgets import Button
# ModelAdmin removed in newer Wagtail versions - using Snippets/ViewSets instead
# from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.admin.ui.tables import UpdatedAtColumn, Column
from wagtail.admin.filters import WagtailFilterSet

from .models import ProjectPage, Project
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
    
    if isinstance(page.specific, ProjectPage):
        project = page.specific
        
        # Quick status change button
        if user.has_perm('projects.change_projectpage'):
            if project.project_status != 'completed':
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


# Add custom CSS and JS to admin
@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add custom CSS to admin"""
    return '<link rel="stylesheet" href="/static/projects/admin/css/project-admin.css">'


@hooks.register('insert_global_admin_js')
def global_admin_js():
    """Add custom JavaScript to admin"""
    return '<script src="/static/projects/admin/js/project-admin.js"></script>'


# Custom user permissions setup
@hooks.register('register_permissions')
def register_project_permissions():
    """Register custom permissions for projects"""
    
    # Get or create project-related groups
    project_managers, created = Group.objects.get_or_create(
        name='Project Managers',
        defaults={'name': 'Project Managers'}
    )
    
    quality_control, created = Group.objects.get_or_create(
        name='Quality Control',
        defaults={'name': 'Quality Control'}
    )
    
    budget_managers, created = Group.objects.get_or_create(
        name='Budget Managers', 
        defaults={'name': 'Budget Managers'}
    )
    
    # Get project content type
    project_ct = ContentType.objects.get_for_model(ProjectPage)
    
    # Define custom permissions if they don't exist
    custom_permissions = [
        ('can_approve_projects', 'Can approve projects'),
        ('can_manage_project_budget', 'Can manage project budget'),
        ('can_set_project_priority', 'Can set project priority'),
        ('can_bulk_edit_projects', 'Can bulk edit projects'),
    ]
    
    for codename, name in custom_permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            content_type=project_ct,
            defaults={'name': name}
        )
        
        # Assign to appropriate groups
        if 'approve' in codename:
            project_managers.permissions.add(permission)
        elif 'budget' in codename:
            budget_managers.permissions.add(permission)
        elif 'priority' in codename or 'bulk' in codename:
            project_managers.permissions.add(permission)
            quality_control.permissions.add(permission)


# Workflow integration
@hooks.register('after_publish_page')
def after_project_publish(request, page):
    """Handle actions after project page is published"""
    
    if isinstance(page.specific, ProjectPage):
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
    
    if isinstance(page.specific, ProjectPage):
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
    
    if isinstance(page.specific, ProjectPage):
        project = page.specific
        
        # Validate required fields for publishing
        if project.project_status == 'completed' and not project.project_date:
            # Could add validation or auto-set completion date
            pass


# Search customization
@hooks.register('register_page_listing_more_buttons')
def add_search_filters_button(page, user, next_url=None):
    """Add advanced search/filter options"""
    
    if user.is_staff:
        yield Button(
            'Advanced Filters',
            reverse('wagtailadmin_pages:index') + '?advanced=true',
            icon_name='cogs',
            priority=100
        )


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