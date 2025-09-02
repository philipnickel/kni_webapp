from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("projekter/", views.gallery_index, name="gallery_index"),
    path("projekter/<slug:slug>/", views.project_detail, name="project_detail"),
]

