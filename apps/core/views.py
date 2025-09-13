from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from wagtail.models import Page, Site
from wagtail.contrib.search_promotions.models import Query
# from wagtail.contrib.settings.views import get_setting
from apps.projects.models import ProjectPage
from apps.pages.models import CompanySettings, DesignSettings


def search(request):
    """
    Search view with filtering and promotion support
    """
    search_query = request.GET.get('query', None)
    search_results = Page.objects.none()
    promoted_results = []
    
    # Filters
    page_type = request.GET.get('type', '')
    featured_only = request.GET.get('featured') == 'true'
    
    if search_query:
        # Get basic search results
        search_results = Page.objects.live().public().search(search_query)
        
        # Apply filters
        if page_type == 'projects':
            # Filter to only ProjectPage instances
            project_pages = []
            for result in search_results:
                specific_page = result.specific
                if isinstance(specific_page, ProjectPage):
                    if not featured_only or getattr(specific_page, 'featured', False):
                        project_pages.append(specific_page)
            search_results = project_pages
        elif featured_only and hasattr(search_results.first(), 'featured'):
            # Filter to featured items only
            search_results = [r for r in search_results if getattr(r.specific, 'featured', False)]
        
        # Log the query for promoted results
        query = Query.get(search_query)
        query.add_hit()
        
        # Get promoted search results
        from wagtail.contrib.search_promotions.models import SearchPromotion
        promoted_results = SearchPromotion.objects.filter(
            query__query_string=search_query
        ).select_related('page')[:3]  # Show top 3 promoted results
    
    # Pagination
    paginator = Paginator(search_results, 10)
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'search_query': search_query,
        'search_results': page_obj,
        'promoted_results': promoted_results,
        'page_type': page_type,
        'featured_only': featured_only,
    }
    
    return render(request, 'search/search.html', context)


@staff_member_required
def preview_settings(request):
    """
    Preview view for DesignSettings - shows how the website would look with current settings
    """
    # Get the current site settings
    site = Site.find_for_request(request)
    company_settings = CompanySettings.for_site(site)
    design_settings = DesignSettings.for_site(site)
    
    # Get the homepage for preview
    try:
        homepage = Page.objects.get(slug='').specific
    except Page.DoesNotExist:
        # Fallback to first live page
        homepage = Page.objects.live().first()
        if homepage:
            homepage = homepage.specific
    
    if not homepage:
        raise Http404("No homepage found for preview")
    
    # Create a context similar to what the base template expects
    context = {
        'page': homepage,
        'company_settings': company_settings,
        'design_settings': design_settings,
        'request': request,
        'is_preview': True,  # Flag to indicate this is a preview
    }
    
    # Use the homepage's template for preview
    return render(request, homepage.template, context)


def search_autocomplete(request):
    """
    Autocomplete search suggestions
    """
    query = request.GET.get('query', '')
    if len(query) < 2:
        return JsonResponse({'suggestions': []})
    
    # Get search suggestions from existing queries
    suggestions = Query.objects.filter(
        query_string__icontains=query
    ).order_by('-daily_hits')[:5]
    
    return JsonResponse({
        'suggestions': [q.query_string for q in suggestions]
    })


def gallery_redirect(request):
    """
    Redirect old gallery URL to new projects URL
    """
    return HttpResponseRedirect('/galleri/')


def health_check(request):
    """
    Simple health check endpoint
    """
    return JsonResponse({'status': 'healthy'})


def test_view(request):
    """
    Simple test view to check if basic Django setup works
    """
    return render(request, 'test.html')