from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from wagtail.models import Site

from .models import Project


def _site(request: HttpRequest) -> Site:
    return Site.find_for_request(request)


def gallery_index(request: HttpRequest) -> HttpResponse:
    site = _site(request)
    qs = Project.objects.filter(site=site, published=True)
    tag = request.GET.get("tag")
    if tag:
        qs = qs.filter(tags__name=tag)
    paginator = Paginator(qs, 12)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "projects/gallery_index.html", {"page_obj": page, "tag": tag})


def project_detail(request: HttpRequest, slug: str) -> HttpResponse:
    site = _site(request)
    project = get_object_or_404(Project, site=site, slug=slug, published=True)
    return render(request, "projects/project_detail.html", {"project": project})

