from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.filters import WagtailFilterSet
from django.utils.html import format_html
from .models import Project


class ProjectViewSet(SnippetViewSet):
    model = Project
    icon = 'folder-open-1'
    menu_label = 'Projekter'
    list_display = ['admin_thumb', 'title', 'project_type', 'date', 'published']
    list_filter = ['published', 'featured', 'project_type', 'date']
    search_fields = ['title', 'description', 'materials']


# Register the custom viewset
register_snippet(ProjectViewSet)


@hooks.register('register_admin_menu_item')
def register_projects_menu_item():
    return MenuItem(
        'Projekter', 
        '/admin/snippets/projects/project/',
        icon_name='folder-open-1',
        order=200
    )