from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

# URL patterns - django-tenants middleware will handle schema routing
urlpatterns = [
    # Django admin - available in both schemas
    path("django-admin/", admin.site.urls),
    
    # Wagtail admin - only works in tenant schemas (where Wagtail apps are installed)
    path("admin/", include(wagtailadmin_urls)),
    
    # App URLs - only available in tenant schemas
    path("", include("apps.projects.urls")),
    path("", include("apps.contacts.urls")),
    
    # Wagtail page serving - only available in tenant schemas
    re_path(r"", include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

