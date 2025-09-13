from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.models import Page
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from wagtail.admin.views.home import HomeView
from django.template.loader import render_to_string


# Removed custom "Alle Sider" menu item - users can access flat page listing via search


# Don't add custom Projekter menu - keep the built-in snippets but filter it properly


# Settings menu is already available by default, no need to duplicate


# Images are managed within projects, so we don't need a separate menu item


# Removed custom dashboard items - Johann can access everything directly from the menu


@hooks.register('register_admin_urls')
def register_custom_admin_urls():
    """Register custom admin URLs for better navigation"""
    from django.urls import path
    from django.shortcuts import redirect
    
    def redirect_to_homepage_edit(request):
        return redirect('/admin/pages/5/edit/')
    
    def redirect_to_main_pages(request):
        return redirect('/admin/pages/5/')
    
    return [
        path('hjemmeside/', redirect_to_homepage_edit, name='edit_homepage'),
        path('mine-sider/', redirect_to_main_pages, name='my_pages'),
    ]


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add custom CSS for preview button"""
    return format_html(
        '''
        <style>
        .preview-button-section {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            padding: 15px;
            margin: 20px 0;
        }}
        .preview-button-section h3 {{
            margin: 0 0 10px 0;
            color: #495057;
        }}
        .preview-button-section p {{
            margin: 0 0 10px 0;
            color: #6c757d;
        }}
        </style>
        '''
    )


@hooks.register('construct_settings_menu')
def add_preview_button_to_settings(request, menu_items):
    """Add preview button to settings pages"""
    # This will be handled by a custom template override instead


@hooks.register('construct_main_menu')
def hide_unused_menu_items(request, menu_items):
    """Hide menu items that Johann doesn't need"""
    # Remove specific unwanted menu items (removed 'images' to show Images in sidebar)
    items_to_remove = ['documents', 'users', 'groups', 'sites', 'collections', 'redirects', 'snippets']
    
    menu_items[:] = [
        item for item in menu_items 
        if not any(remove_name in item.name.lower() for remove_name in items_to_remove)
    ]


@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add custom CSS to improve the admin interface"""
    return format_html(
        '''
        <style>
        /* Removed dashboard quick actions panel CSS since the panel is removed */
        
        /* Better visual hierarchy for page explorer */
        .page-explorer .page {{
            border-left: 3px solid transparent;
            transition: all 0.2s ease;
        }}
        .page-explorer .page:hover {{
            border-left-color: #50b83c;
            background-color: #f8fffe;
        }}
        
        /* Make the main site page more prominent */
        .page-explorer .page[data-page-id="5"] {{
            background: linear-gradient(90deg, #f0f8f0 0%, #f8fffe 100%);
            border-left-color: #50b83c;
            font-weight: 600;
        }}
        
        /* Hide unused menu items */
        nav [href="/admin/documents/"] {{
            display: none !important;
        }}
        
        /* Hide snippets menu since we have direct project access */
        nav [href="/admin/snippets/"] {{
            display: none !important;
        }}
        
        /* Images menu is now visible in sidebar for easy access */
        
        /* Hide Groups, Collections, Redirects, and Sites - not needed for Johann */
        nav [href="/admin/groups/"] {{
            display: none !important;
        }}
        
        nav [href="/admin/collections/"] {{
            display: none !important;
        }}
        
        nav [href="/admin/redirects/"] {{
            display: none !important;
        }}
        
        nav [href="/admin/sites/"] {{
            display: none !important;
        }}
        
        /* Improve main navigation styling */
        .sidebar-main-menu .menu-item a {{
            border-radius: 6px;
            margin: 2px 0;
            transition: all 0.2s ease;
        }}
        .sidebar-main-menu .menu-item a:hover {{
            background: #f0f8f0;
            transform: translateX(3px);
        }}
        
        /* Brand the admin header */
        .header {{
            background: linear-gradient(135deg, #2e7d32 0%, #388e3c 100%);
        }}
        
        /* Improve form styling */
        .object-layout {{
            background: #fafafa;
        }}
        .w-panel {{
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        </style>
        '''
    )


@hooks.register('insert_global_admin_css')
def custom_branding_css():
    """Add custom branding CSS that uses the company logo from site settings"""
    return format_html(
        '''
        <style>
        /* Dynamic logo branding using site settings */
        .header-logo .logo-link {{ 
            display: flex;
            align-items: center;
            text-decoration: none;
        }}
        
        .header-logo .logo-link:before {{
            content: '';
            display: inline-block;
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, #4d7a3a, #3a5e2c);
            border-radius: 6px;
            margin-right: 8px;
            color: white;
            font-weight: bold;
            font-size: 14px;
            line-height: 32px;
            text-align: center;
        }}
        
        .header-logo .logo-link .logo-text {{
            color: white !important;
            font-weight: 600 !important;
            font-size: 16px !important;
        }}
        
        /* Custom login branding */
        .login-form h1 {{
            color: #4d7a3a;
            font-weight: 600;
            margin-bottom: 30px;
        }}
        
        .login-form .logo {{
            margin-bottom: 20px;
        }}
        
        /* Brand colors */
        .button--primary,
        .button[type="submit"] {{
            background-color: #4d7a3a !important;
            border-color: #4d7a3a !important;
        }}
        
        .button--primary:hover,
        .button[type="submit"]:hover {{
            background-color: #3a5e2c !important;
            border-color: #3a5e2c !important;
        }}
        
        /* Active navigation styling */
        .sidebar-main-menu .menu-item.menu-active a,
        .sidebar-main-menu .menu-item a[aria-current="page"] {{
            background-color: #4d7a3a !important;
            color: white !important;
        }}
        
        .sidebar-main-menu .menu-item a:hover {{
            background-color: #f0f8f0;
            color: #4d7a3a;
        }}
        
        /* DaisyUI theme support for admin */
        [data-theme="dark"] .header {{
            background: linear-gradient(135deg, #1f2937 0%, #111827 100%) !important;
        }}
        
        [data-theme="dark"] .sidebar-main-menu .menu-item.menu-active a,
        [data-theme="dark"] .sidebar-main-menu .menu-item a[aria-current="page"] {{
            background-color: #374151 !important;
            color: white !important;
        }}
        
        [data-theme="dark"] .sidebar-main-menu .menu-item a:hover {{
            background-color: #374151;
            color: white;
        }}
        
        </style>
        '''
    )


# Temporarily disabled - might be causing context issues
# @hooks.register('construct_main_menu') 
def customize_branding_logo_disabled(request, menu_items):
    """Add dynamic tenant branding to the sidebar"""
    from django.utils.safestring import mark_safe
    from wagtail.admin.menu import MenuItem
    from apps.pages.models import CompanySettings
    
    try:
        # Get the current company settings for this tenant
        site = request.site
        company_settings = CompanySettings.for_site(site)
        company_name = company_settings.company_name or "Admin"
        
        # Generate initials from company name (e.g., "JCleemann Byg" -> "JC")
        initials = ''.join([word[0].upper() for word in company_name.split()[:2] if word])
        if not initials:
            initials = company_name[:2].upper()
            
        # Create branded dashboard link
        branding_html = mark_safe(f'''
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 8px 0;">
            <div style="
                width: 48px; 
                height: 48px; 
                background: linear-gradient(135deg, #4d7a3a, #3a5e2c); 
                border-radius: 8px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                color: white; 
                font-weight: bold; 
                font-size: 18px;
                margin-bottom: 6px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                {initials}
            </div>
            <span style="color: white; font-weight: 600; font-size: 12px; line-height: 1.2;">{company_name}</span>
        </div>
        ''')
        
        # Create custom dashboard menu item with branding
        dashboard_item = MenuItem(
            label=branding_html,
            url='/admin/',
            name='dashboard',
            classnames='sidebar-custom-branding',
            order=0
        )
        
        # Remove the default dashboard item and add our custom one
        menu_items[:] = [item for item in menu_items if item.name != 'dashboard']
        menu_items.insert(0, dashboard_item)
        
    except Exception:
        # Fallback to default if there's any issue
        pass


# Temporarily disabled JavaScript hook that might be interfering with admin
# @hooks.register('insert_editor_js')
# def stay_on_editor_after_publish():
#     """Ensure edit form posts with a 'next' param so Wagtail returns to editor.
#
#     Wagtail's edit view honors a 'next' parameter and, after actions such as
#     Publish, redirects to it instead of the explorer. By injecting a hidden
#     input into the edit form with the current URL, the user remains on the
#     editor after publishing.
#     """
#     return format_html(
#         '''
#         <script>
#         document.addEventListener('DOMContentLoaded', function () {
#           try {
#             var form = document.querySelector('main form[method="post"]');
#             if (!form) return;
#             // Don't duplicate if Wagtail already provided one
#             if (form.querySelector('input[name="next"]')) return;
#             var input = document.createElement('input');
#             input.type = 'hidden';
#             input.name = 'next';
#             input.value = window.location.pathname + window.location.search;
#             form.appendChild(input);
#           } catch (e) { /* no-op */ }
#         });
#         </script>
#         '''
#     )
