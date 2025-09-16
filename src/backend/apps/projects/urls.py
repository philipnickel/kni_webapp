# Projects are handled entirely by Wagtail pages
# This file is kept for potential future admin functionality
from django.urls import path
from . import admin_views

app_name = "projects"

# Minimal URL patterns for admin functionality only
urlpatterns = [
    path('admin/projects/create/', admin_views.project_create_shim, name='project_create_shim'),
]
# - Gallery page shows all projects with modal popups
# - No individual project pages

