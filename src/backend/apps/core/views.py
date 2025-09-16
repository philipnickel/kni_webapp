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
    query = request.GET.get('q', '')
    # Implement search logic here
    return JsonResponse({'results': [], 'query': query})


def search_autocomplete(request):
    """Search autocomplete functionality"""
    query = request.GET.get('q', '')
    # Implement autocomplete logic here
    return JsonResponse({'suggestions': []})


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