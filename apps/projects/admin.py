from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "published", "date")
    list_filter = ("featured", "published", "date")
    search_fields = ("title", "description")
