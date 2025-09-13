from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
from django.views.static import serve
from django.urls import re_path
from .favicon_view import favicon_view
from apps.core.health import health_check, health_check_detailed, readiness_check, liveness_check

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    # Health checks
    path("health/", health_check, name="health_check"),
    path("health/detailed/", health_check_detailed, name="health_check_detailed"),
    path("health/ready/", readiness_check, name="readiness_check"),
    path("health/live/", liveness_check, name="liveness_check"),
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

# Serve media files - use Django's serve view for production compatibility
if settings.DEBUG:
    # In development, use static() helper
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, explicitly serve media files using serve view
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# Add Wagtail URLs - must be last as it has a catch-all pattern
urlpatterns += [
    re_path(r"", include(wagtail_urls)),
]

# Serve static files only in DEBUG mode (production uses WhiteNoise)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)