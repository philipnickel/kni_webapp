from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from .favicon_view import favicon_view

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    # Favicon
    path("favicon.ico", favicon_view),
    
    # Django admin
    path("django-admin/", admin.site.urls),
    
    # Wagtail admin
    path("admin/", include(wagtailadmin_urls)),
    
    # App URLs
    path("", include("apps.projects.urls")),
    path("", include("apps.contacts.urls")),
    
    # Wagtail page serving - must be last
    re_path(r"", include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)