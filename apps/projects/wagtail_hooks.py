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
    list_display = ['admin_thumb', 'title', 'date', 'published']
    list_filter = ['published', 'featured', 'date']
    search_fields = ['title', 'description', 'materials']
    ordering = ['-date', 'title']  # Show newest projects first
    list_per_page = 10
    
    def get_queryset(self, request):
        # Get base queryset from the model and apply ordering
        return self.model.objects.all().order_by('-featured', '-date')


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
