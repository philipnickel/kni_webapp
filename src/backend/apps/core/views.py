from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
from django.conf import settings
import json
import colorsys

from apps.pages.models import CompanySettings, DesignPage
from apps.pages.themes import ALL_THEMES


def home(request):
    """Home page view"""
    return render(request, 'pages/home_page.html')


def design_preview(request):
    """Design preview page"""
    return render(request, 'pages/design_preview.html')


@cache_page(60 * 15)  # Cache for 15 minutes
def dynamic_theme_css(request):
    """
    Generate dynamic CSS based on Wagtail design settings
    Simplified version to isolate the error
    """
    try:
        # Get the design settings
        design_page = DesignPage.objects.filter(live=True).first()
        
        if not design_page:
            # Return default CSS if no design settings found
            return HttpResponse("/* No design settings found */", content_type="text/css")
        
        # Get the selected theme
        selected_theme_id = design_page.theme or 'tailwind'
        theme_data = ALL_THEMES.get(selected_theme_id, ALL_THEMES['tailwind'])
        
        # Extract colors from the theme
        primary_color = theme_data['colors'].get('primary', '#3b82f6')
        secondary_color = theme_data['colors'].get('secondary', '#6366f1')
        accent_color = theme_data['colors'].get('accent', '#f59e0b')
        
        # Generate comprehensive CSS with all theme colors
        colors = theme_data['colors']
        primary = colors.get('primary', '#3b82f6')
        secondary = colors.get('secondary', '#6366f1')
        accent = colors.get('accent', '#f59e0b')
        success = colors.get('success', '#10b981')
        warning = colors.get('warning', '#f59e0b')
        error = colors.get('error', '#ef4444')
        background = colors.get('background', '#ffffff')
        surface = colors.get('surface', '#f9fafb')
        text_primary = colors.get('text_primary', '#111827')
        text_secondary = colors.get('text_secondary', '#6b7280')
        
        css_content = f"""
/* Dynamic theme CSS generated from Wagtail settings - Theme: {theme_data['name']} */
:root {{
  /* Primary colors */
  --color-primary-500: {primary};
  --color-secondary-500: {secondary};
  --color-accent-500: {accent};
  --color-success-500: {success};
  --color-warning-500: {warning};
  --color-error-500: {error};
  --color-background: {background};
  --color-surface: {surface};
  --color-text-primary: {text_primary};
  --color-text-secondary: {text_secondary};
}}

/* Tailwind CSS compatible classes for PrelineUI */
.bg-primary {{ background-color: {primary} !important; }}
.bg-secondary {{ background-color: {secondary} !important; }}
.bg-accent {{ background-color: {accent} !important; }}
.bg-success {{ background-color: {success} !important; }}
.bg-warning {{ background-color: {warning} !important; }}
.bg-error {{ background-color: {error} !important; }}

.text-primary {{ color: {primary} !important; }}
.text-secondary {{ color: {secondary} !important; }}
.text-accent {{ color: {accent} !important; }}
.text-success {{ color: {success} !important; }}
.text-warning {{ color: {warning} !important; }}
.text-error {{ color: {error} !important; }}

/* Gradient classes */
.from-primary {{ --tw-gradient-from: {primary} !important; }}
.via-secondary {{ --tw-gradient-via: {secondary} !important; }}
.to-accent {{ --tw-gradient-to: {accent} !important; }}

/* Border colors */
.border-primary {{ border-color: {primary} !important; }}
.border-secondary {{ border-color: {secondary} !important; }}
.border-accent {{ border-color: {accent} !important; }}

/* Focus and hover states */
.focus\\:ring-primary:focus {{ --tw-ring-color: {primary} !important; }}
.hover\\:bg-primary:hover {{ background-color: {primary} !important; }}
.hover\\:text-primary:hover {{ color: {primary} !important; }}

/* PrelineUI specific overrides */
.hs-button-primary {{ background-color: {primary} !important; border-color: {primary} !important; }}
.hs-button-primary:hover {{ background-color: {secondary} !important; border-color: {secondary} !important; }}
.hs-button-secondary {{ background-color: {secondary} !important; border-color: {secondary} !important; }}
.hs-button-secondary:hover {{ background-color: {accent} !important; border-color: {accent} !important; }}
"""
        
        return HttpResponse(css_content, content_type="text/css")
        
    except Exception as e:
        # Return error CSS with more details
        import traceback
        error_details = traceback.format_exc()
        return HttpResponse(f"/* Error generating theme CSS: {str(e)} */\n/* Traceback: {error_details} */", content_type="text/css")


def search(request):
    """Search functionality"""
    from wagtail.search.models import Query
    from django.core.paginator import Paginator
    from django.db.models import Q
    
    search_query = request.GET.get('query', '')
    page_type = request.GET.get('type', '')
    featured_only = request.GET.get('featured') == 'true'
    page_number = request.GET.get('page', 1)
    
    search_results = None
    safe_results = []
    
    if search_query:
        # Record the search query
        Query.get(search_query).add_hit()
        
        # Build search query
        from apps.pages.models import HomePage, AboutPage, ContactPage, GalleryPage, ModularPage, FAQPage, DesignPage
        from apps.projects.models import Project
        
        # Start with all searchable models
        all_models = [HomePage, AboutPage, ContactPage, GalleryPage, ModularPage, FAQPage, DesignPage, Project]
        
        # Filter by type if specified
        if page_type == 'projects':
            all_models = [Project]
        
        # Build search results
        results = []
        for model in all_models:
            if hasattr(model, 'search_fields'):
                # Use Wagtail's search functionality
                model_results = model.objects.live().search(search_query)
                
                # Apply featured filter if requested
                if featured_only and hasattr(model, 'featured'):
                    model_results = model_results.filter(featured=True)
                
                # Add to results with type information
                for result in model_results:
                    result.page_type_label = model._meta.verbose_name.title()
                    results.append(result)
        
        # Sort results by relevance (you could implement more sophisticated sorting)
        results = sorted(results, key=lambda x: getattr(x, 'first_published_at', None) or getattr(x, 'date', None), reverse=True)
        
        # Paginate results
        paginator = Paginator(results, 10)  # 10 results per page
        try:
            search_results = paginator.page(page_number)
            safe_results = search_results.object_list
        except:
            search_results = None
            safe_results = []
    
    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'safe_results': safe_results,
        'page_type': page_type,
        'featured_only': featured_only,
    })


def search_autocomplete(request):
    """Search autocomplete functionality"""
    from wagtail.search.models import Query
    from django.db.models import Q
    
    query = request.GET.get('q', '')
    suggestions = []
    
    if len(query) >= 2:
        # Get search suggestions from existing queries
        query_objects = Query.objects.filter(
            query_string__icontains=query
        ).order_by('-daily_hits')[:5]
        
        # Also search for matching pages/projects
        from apps.pages.models import HomePage, AboutPage, ContactPage, GalleryPage, ModularPage, FAQPage, DesignPage
        from apps.projects.models import Project
        
        all_models = [HomePage, AboutPage, ContactPage, GalleryPage, ModularPage, FAQPage, DesignPage, Project]
        
        for model in all_models:
            if hasattr(model, 'search_fields'):
                # Search in title and description fields
                model_results = model.objects.live().filter(
                    Q(title__icontains=query) | 
                    Q(description__icontains=query) |
                    Q(intro__icontains=query)
                )[:3]
                
                for result in model_results:
                    suggestions.append({
                        'title': result.title,
                        'url': result.url,
                        'type': model._meta.verbose_name.title()
                    })
        
        # Add query suggestions
        for query_obj in query_objects:
            suggestions.append({
                'title': query_obj.query_string,
                'url': f'/search/?query={query_obj.query_string}',
                'type': 'Søgning'
            })
    
    return JsonResponse({'suggestions': suggestions})


def gallery_redirect(request):
    """Redirect to gallery page"""
    from django.shortcuts import redirect
    return redirect('/galleri/')


def health_check(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'healthy'})


def test_view(request):
    """Test view for development"""
    return render(request, 'test.html')


def test_components_view(request):
    """Test components view for development"""
    return render(request, 'test_components.html')


def color_preview_api(request):
    """API endpoint for color preview functionality"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process color preview data
            return JsonResponse({'status': 'success', 'data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


def project_create_shim(request):
    """Shim for project creation"""
    from django.shortcuts import redirect
    return redirect('/admin/projects/project/add/')


def form(request):
    """Form submission handler"""
    return render(request, 'forms/quote_form.html')


def thanks(request):
    """Thank you page after form submission"""
    return render(request, 'forms/thanks.html')


def quote_request(request):
    """Quote request form"""
    return render(request, 'forms/quote_request.html')


def quote_request_thanks(request):
    """Thank you page after quote request"""
    return render(request, 'forms/quote_request_thanks.html')