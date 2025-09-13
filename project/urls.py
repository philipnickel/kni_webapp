from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
from .favicon_view import favicon_view

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    # Health
    path("health/", lambda request: HttpResponse(status=200)),
    # Favicon
    path("favicon.ico", favicon_view),
    
    # Django admin
    path("django-admin/", admin.site.urls),
    
    # Wagtail admin
    path("admin/", include(wagtailadmin_urls)),
    
    # SEO URLs
    path("sitemap.xml", sitemap),
    
    # App URLs
    path("", include("apps.core.urls")),
    path("", include("apps.projects.urls")),
    path("", include("apps.contacts.urls")),
]

# Serve media files in all environments (production uses Docker volumes)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Wagtail URLs - must be last as it has a catch-all pattern
urlpatterns += [
    re_path(r"", include(wagtail_urls)),
]

# Serve static files only in DEBUG mode (production uses WhiteNoise)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)