import os
from django.http import FileResponse, Http404
from django.conf import settings

def favicon_view(request):
    favicon_path = os.path.join(settings.MEDIA_ROOT, "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(open(favicon_path, "rb"), content_type="image/x-icon")
    raise Http404
