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


def test_components_view(request):
    """
    Test view to verify all component libraries are working
    """
    return render(request, 'test_components.html')