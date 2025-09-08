"""
Public schema URLs - for super admin and tenant management
This runs on the public schema only
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def public_index(request):
    """Simple public schema index page"""
    return HttpResponse("""
    <h1>Construction Business Multi-Tenant Platform</h1>
    <p>This is the public schema for tenant management.</p>
    <p><a href="/admin/">Access Admin Panel</a></p>
    """)


urlpatterns = [
    # Django admin for public (super admin)
    path('admin/', admin.site.urls),
    # Optional alias matching tenant convention
    path('django-admin/', admin.site.urls),
    # Public index
    path('', public_index, name='public_index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
