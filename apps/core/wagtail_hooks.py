from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.models import Page
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from wagtail.admin.views.home import HomeView


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


@hooks.register('construct_main_menu')
def hide_unused_menu_items(request, menu_items):
    """Hide menu items that Johann doesn't need"""
    # Remove specific unwanted menu items
    items_to_remove = ['images', 'documents', 'users', 'groups', 'sites', 'collections', 'redirects', 'snippets']
    
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
        
        /* Hide images menu since they're managed within projects */
        nav [href="/admin/images/"] {{
            display: none !important;
        }}
        
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
        </style>
        '''
    )


@hooks.register('construct_main_menu') 
def customize_branding_logo(request, menu_items):
    """Add dynamic tenant branding to the sidebar"""
    from django.utils.safestring import mark_safe
    from wagtail.admin.menu import MenuItem
    from apps.pages.models import SiteSettings
    
    try:
        # Get the current site settings for this tenant
        site_settings = SiteSettings.for_request(request)
        company_name = site_settings.company_name or "Admin"
        
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
