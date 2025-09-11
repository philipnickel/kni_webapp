from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.models import Page
from wagtail.contrib.search_promotions.models import Query
from apps.projects.models import ProjectPage


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
        search_results = paginator.page(page_num)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)
    
    # Build safe result dicts for template to avoid using _meta directly
    safe_results = []
    for item in search_results:
        page = getattr(item, 'specific', item)
        page_type_label = getattr(getattr(page, '_meta', None), 'verbose_name', 'Side')
        safe_results.append({
            'url': getattr(page, 'url', ''),
            'title': getattr(page, 'title', ''),
            'page_type_label': page_type_label,
            'project_date': getattr(page, 'project_date', None),
            'first_published_at': getattr(page, 'first_published_at', None),
            'featured': getattr(page, 'featured', False),
            'search_description': getattr(page, 'search_description', ''),
            'description': getattr(page, 'description', ''),
            'featured_image': getattr(page, 'featured_image', None),
            'tags': getattr(page, 'tags', None),
        })

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'safe_results': safe_results,
        'promoted_results': promoted_results,
        'page_type': page_type,
        'featured_only': featured_only,
    })


def search_autocomplete(request):
    """
    Autocomplete API for search suggestions
    """
    query = request.GET.get('q', '').strip()
    suggestions = []
    
    if query and len(query) >= 2:
        # Get page suggestions
        pages = Page.objects.live().public().search(query, fields=['title'])[:5]
        for page in pages:
            suggestions.append({
                'title': page.title,
                'url': page.url,
                'type': page._meta.verbose_name
            })
        
        # Get project-specific suggestions
        if len(suggestions) < 5:
            projects = ProjectPage.objects.live().public().search(query)[:3]
            for project in projects:
                if not any(s['url'] == project.url for s in suggestions):
                    suggestions.append({
                        'title': project.title,
                        'url': project.url,
                        'type': 'Projekt'
                    })
    
    return render(request, 'search/autocomplete.json', {
        'suggestions': suggestions
    }, content_type='application/json')


def gallery_redirect(request):
    """
    Legacy support for /gallery/ path expected by tests.
    Redirect to first live GalleryPage or 404 if none exists.
    """
    try:
        from apps.pages.models import GalleryPage
        page = GalleryPage.objects.live().public().first()
        if page and getattr(page, 'url', None):
            return HttpResponseRedirect(page.url)
    except Exception:
        pass
    raise Http404("Gallery not found")