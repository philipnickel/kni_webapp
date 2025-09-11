from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from wagtail.models import Site
from wagtail.admin import messages as wagtail_messages
from wagtail.admin.views.generic import IndexView

from .models import Project


def _site(request: HttpRequest) -> Site:
    return Site.find_for_request(request)


def gallery_index(request: HttpRequest) -> HttpResponse:
    qs = Project.objects.filter(published=True).order_by('-date')
    tag = request.GET.get("tag")
    if tag:
        qs = qs.filter(tags__name=tag)
    paginator = Paginator(qs, 12)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "projects/gallery_index.html", {"page_obj": page, "tag": tag})


def project_detail(request: HttpRequest, slug: str) -> HttpResponse:
    project = get_object_or_404(Project, slug=slug, published=True)
    return render(request, "projects/project_detail.html", {"project": project})


# Admin views for Projects
class ProjectIndexView(ListView):
    """List view for Projects in admin"""
    model = Project
    template_name = 'wagtailadmin/generic/index.html'
    context_object_name = 'object_list'
    paginate_by = 20
    
    def get_queryset(self):
        return Project.objects.all().order_by('-date', 'title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Projekter',
            'header_icon': 'folder-open-1',
            'add_url': reverse('projects_create'),
            'add_item_label': 'Tilføj projekt',
        })
        return context


class ProjectCreateView(CreateView):
    """Create view for Projects in admin"""
    model = Project
    fields = ['title', 'description', 'featured', 'published', 'date', 'tags']
    template_name = 'wagtailadmin/generic/create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Tilføj projekt',
            'header_icon': 'folder-open-1',
        })
        return context
    
    def get_success_url(self):
        wagtail_messages.success(self.request, f"Projekt '{self.object.title}' er oprettet.")
        return reverse('projects_index')
    
    def form_valid(self, form):
        return super().form_valid(form)


class ProjectEditView(UpdateView):
    """Edit view for Projects in admin"""
    model = Project
    fields = ['title', 'description', 'featured', 'published', 'date', 'tags']
    template_name = 'wagtailadmin/generic/edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': f'Rediger: {self.object.title}',
            'header_icon': 'folder-open-1',
        })
        return context
    
    def get_success_url(self):
        wagtail_messages.success(self.request, f"Projekt '{self.object.title}' er opdateret.")
        return reverse('projects_index')

