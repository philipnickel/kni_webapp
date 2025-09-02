import datetime
import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wagtail.models import Site
from .models import AnalyticsDaily


@csrf_exempt
def collect(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"ok": False}, status=405)
    site = Site.find_for_request(request)
    if not site:
        return JsonResponse({"ok": False}, status=400)
    try:
        payload = json.loads(request.body.decode("utf-8")) if request.body else {}
    except Exception:
        payload = {}
    path = payload.get("path") or "/"
    kind = payload.get("type", "pageview")
    today = datetime.date.today()
    daily, _ = AnalyticsDaily.objects.get_or_create(site=site, date=today, path=path)
    daily.views += 1
    if kind == "conversion":
        daily.conversions += 1
    daily.save()
    return JsonResponse({"ok": True})

