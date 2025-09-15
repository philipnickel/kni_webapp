from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),
    path('api/search/autocomplete/', views.search_autocomplete, name='search_autocomplete_api'),
    path('gallery/', views.gallery_redirect, name='gallery_legacy'),
    path('health/', views.health_check, name='health_check'),
    path('admin/preview-settings/', views.preview_settings, name='preview_settings'),
    path('test/', views.test_view, name='test_view'),
    path('test-components/', views.test_components_view, name='test_components_view'),
]