from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),
    path('api/search/autocomplete/', views.search_autocomplete, name='search_autocomplete_api'),
    path('gallery/', views.gallery_redirect, name='gallery_legacy'),
]