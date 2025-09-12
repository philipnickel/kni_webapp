# URL patterns removed - projects are now handled as Wagtail pages
# Projects are accessible via the page tree:
# - Gallery pages (parent) handle project listings
# - Project pages (children) handle individual project display
# 
# This file is kept for backwards compatibility during transition
# but can be removed once all projects are converted to pages.

from django.urls import path
from . import admin_views

app_name = "projects"

# Empty urlpatterns - all routing handled by Wagtail page tree
urlpatterns = [
    path('admin/projects/create/', admin_views.project_create_shim, name='project_create_shim'),
]

# Legacy URL patterns (removed - projects now handled by Wagtail pages only):
# - Gallery page shows all projects with modal popups
# - No individual project pages

