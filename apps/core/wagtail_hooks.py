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


# Enhanced settings preview functionality
@hooks.register('register_admin_urls')
def register_enhanced_settings_urls():
    """Register enhanced settings URLs for theme preview"""
    from django.urls import path
    from django.shortcuts import redirect
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.contrib.admin.views.decorators import staff_member_required

    @staff_member_required
    @csrf_exempt
    def save_theme_preview(request):
        if request.method == 'POST':
            theme = request.POST.get('theme')
            # Here you could save the theme to user preferences or site settings
            # For now, just return success
            return JsonResponse({'status': 'success', 'message': f'Tema {theme} gemt'})
        return JsonResponse({'status': 'error', 'message': 'Ugyldig anmodning'})

    def redirect_to_design_settings(request):
        return redirect('/admin/settings/pages/designsettings/')

    return [
        path('settings/theme-preview/save/', save_theme_preview, name='save_theme_preview'),
        path('settings/design/', redirect_to_design_settings, name='design_settings'),
    ]


@hooks.register('insert_global_admin_js')
def enhanced_admin_js():
    """Add enhanced JavaScript for admin interface functionality"""
    return format_html(
        '''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            initEnhancedAdmin();
        }});

        function initEnhancedAdmin() {{
            // Mobile navigation improvements
            enhanceMobileNavigation();

            // Theme preview functionality
            initThemePreview();

            // Enhanced form interactions
            enhanceFormInteractions();

            // Accessibility improvements
            improveAccessibility();
        }}

        function enhanceMobileNavigation() {{
            // Add swipe gestures for mobile navigation (if needed)
            const sidebar = document.querySelector('.sidebar');
            if (!sidebar) return;

            let startX = 0;
            let currentX = 0;
            let dragging = false;

            sidebar.addEventListener('touchstart', function(e) {{
                startX = e.touches[0].clientX;
                dragging = true;
            }});

            sidebar.addEventListener('touchmove', function(e) {{
                if (!dragging) return;
                currentX = e.touches[0].clientX;
                const diffX = currentX - startX;

                // Add visual feedback for swipe
                if (Math.abs(diffX) > 50) {{
                    sidebar.style.transform = `translateX(${{diffX > 0 ? '10px' : '-10px'}})`;
                }}
            }});

            sidebar.addEventListener('touchend', function() {{
                if (dragging) {{
                    sidebar.style.transform = '';
                    dragging = false;
                }}
            }});
        }}

        function initThemePreview() {{
            // Create theme preview panel if we're in settings
            if (window.location.pathname.includes('/admin/settings/')) {{
                createThemePreviewPanel();
            }}
        }}

        function createThemePreviewPanel() {{
            const panel = document.createElement('div');
            panel.className = 'theme-preview-panel';
            panel.innerHTML = `
                <h4>🎨 Preview Tema</h4>
                <div class="theme-preview-swatches">
                    <div class="theme-swatch" data-theme="light" style="background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);"></div>
                    <div class="theme-swatch" data-theme="dark" style="background: linear-gradient(135deg, #1f2937 0%, #111827 100%);"></div>
                    <div class="theme-swatch" data-theme="green" style="background: linear-gradient(135deg, #4d7a3a 0%, #3a5e2c 100%);"></div>
                    <div class="theme-swatch" data-theme="blue" style="background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);"></div>
                    <div class="theme-swatch" data-theme="purple" style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);"></div>
                    <div class="theme-swatch" data-theme="orange" style="background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);"></div>
                </div>
            `;

            document.body.appendChild(panel);

            // Add click handlers for theme swatches
            panel.querySelectorAll('.theme-swatch').forEach(swatch => {{
                swatch.addEventListener('click', function() {{
                    const theme = this.dataset.theme;
                    applyThemePreview(theme);

                    // Update active state
                    panel.querySelectorAll('.theme-swatch').forEach(s => s.classList.remove('active'));
                    this.classList.add('active');
                }});
            }});
        }}

        function applyThemePreview(theme) {{
            // Apply theme to current page for preview
            document.documentElement.setAttribute('data-theme', theme);

            // Show feedback
            showThemeFeedback(`Tema "${{theme}}" anvendt som preview`, 'success');

            // Store in localStorage for persistence during admin session
            localStorage.setItem('admin-theme-preview', theme);
        }}

        function showThemeFeedback(message, type) {{
            const feedback = document.createElement('div');
            feedback.className = `theme-feedback ${{type}}`;
            feedback.textContent = message;
            document.body.appendChild(feedback);

            // Show and auto-hide
            setTimeout(() => feedback.classList.add('show'), 100);
            setTimeout(() => {{
                feedback.classList.remove('show');
                setTimeout(() => feedback.remove(), 300);
            }}, 3000);
        }}

        function enhanceFormInteractions() {{
            // Add loading states to form submissions
            const forms = document.querySelectorAll('form');
            forms.forEach(form => {{
                form.addEventListener('submit', function() {{
                    const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
                    if (submitBtn) {{
                        submitBtn.innerHTML = '<span class="loading-spinner"></span> Gemmer...';
                        submitBtn.disabled = true;
                    }}
                }});
            }});

            // Enhanced image upload feedback
            const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
            imageInputs.forEach(input => {{
                input.addEventListener('change', function() {{
                    if (this.files.length > 0) {{
                        const fileName = this.files[0].name;
                        showThemeFeedback(`Billede "${{fileName}}" valgt`, 'success');
                    }}
                }});
            }});
        }}

        function improveAccessibility() {{
            // Add keyboard navigation improvements
            document.addEventListener('keydown', function(e) {{
                // Alt + M: Focus main menu
                if (e.altKey && e.key === 'm') {{
                    e.preventDefault();
                    const firstMenuItem = document.querySelector('.sidebar-main-menu .menu-item a');
                    if (firstMenuItem) firstMenuItem.focus();
                }}

                // Alt + S: Focus search
                if (e.altKey && e.key === 's') {{
                    e.preventDefault();
                    const searchInput = document.querySelector('input[type="search"]');
                    if (searchInput) searchInput.focus();
                }}
            }});

            // Add focus indicators
            document.addEventListener('focusin', function(e) {{
                if (e.target.matches('a, button, input, select, textarea')) {{
                    e.target.classList.add('keyboard-focused');
                }}
            }});

            document.addEventListener('focusout', function(e) {{
                e.target.classList.remove('keyboard-focused');
            }});
        }}

        // Load saved theme preview if it exists
        const savedTheme = localStorage.getItem('admin-theme-preview');
        if (savedTheme) {{
            document.documentElement.setAttribute('data-theme', savedTheme);
        }}

        </script>
        '''
    )


# Mobile admin notification system
@hooks.register('insert_global_admin_js')
def mobile_admin_enhancements():
    """Additional mobile admin enhancements"""
    return format_html(
        '''
        <script>
        // Add mobile-specific admin functionality
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.innerWidth <= 768) {{
                initMobileAdminFeatures();
            }}
        }});

        function initMobileAdminFeatures() {{
            // Add sticky save button for long forms on mobile
            const forms = document.querySelectorAll('form');
            forms.forEach(form => {{
                const saveButton = form.querySelector('button[type="submit"], input[type="submit"]');
                if (saveButton && form.scrollHeight > window.innerHeight) {{
                    createStickySaveButton(saveButton, form);
                }}
            }});

            // Add pull-to-refresh indication
            addPullToRefreshIndicator();

            // Improve mobile table scrolling
            improveMobileTableScrolling();
        }}

        function createStickySaveButton(originalButton, form) {{
            const stickyButton = originalButton.cloneNode(true);
            stickyButton.className += ' sticky-save-button';
            stickyButton.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 1000;
                min-width: 60px;
                min-height: 60px;
                border-radius: 50%;
                box-shadow: 0 4px 12px rgba(77, 122, 58, 0.3);
                background: #4d7a3a;
                color: white;
                border: none;
                display: none;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                cursor: pointer;
            `;

            // Show/hide based on scroll position
            let isVisible = false;
            window.addEventListener('scroll', function() {{
                const shouldShow = window.scrollY > 200;
                if (shouldShow !== isVisible) {{
                    isVisible = shouldShow;
                    stickyButton.style.display = isVisible ? 'flex' : 'none';
                }}
            }});

            // Click handler
            stickyButton.addEventListener('click', function(e) {{
                e.preventDefault();
                originalButton.click();
            }});

            document.body.appendChild(stickyButton);
        }}

        function addPullToRefreshIndicator() {{
            let startY = 0;
            let currentY = 0;
            let pulling = false;

            document.addEventListener('touchstart', function(e) {{
                if (window.scrollY === 0) {{
                    startY = e.touches[0].clientY;
                    pulling = true;
                }}
            }});

            document.addEventListener('touchmove', function(e) {{
                if (!pulling) return;
                currentY = e.touches[0].clientY;
                const pullDistance = currentY - startY;

                if (pullDistance > 100) {{
                    // Show pull-to-refresh indicator
                    document.body.style.transform = `translateY(${{Math.min(pullDistance - 100, 50)}}px)`;
                    document.body.style.transition = 'none';
                }}
            }});

            document.addEventListener('touchend', function() {{
                if (pulling) {{
                    document.body.style.transform = '';
                    document.body.style.transition = 'transform 0.3s ease';

                    if (currentY - startY > 150) {{
                        // Trigger refresh
                        window.location.reload();
                    }}

                    pulling = false;
                }}
            }});
        }}

        function improveMobileTableScrolling() {{
            const tables = document.querySelectorAll('.listing');
            tables.forEach(table => {{
                table.style.cssText += `
                    -webkit-overflow-scrolling: touch;
                    scroll-behavior: smooth;
                `;

                // Add scroll indicators
                const scrollIndicator = document.createElement('div');
                scrollIndicator.className = 'mobile-scroll-indicator';
                scrollIndicator.textContent = '← Swipe for more →';
                scrollIndicator.style.cssText = `
                    text-align: center;
                    padding: 8px;
                    background: #f3f4f6;
                    font-size: 12px;
                    color: #6b7280;
                    border-radius: 4px;
                    margin-top: 8px;
                `;

                table.parentNode.insertBefore(scrollIndicator, table.nextSibling);
            }});
        }}

        </script>
        '''
    )


# Temporarily disabled summary items - causing admin panel errors
# @hooks.register('construct_homepage_summary_items')
def add_mobile_optimized_summary_items_disabled(request, summary_items):
    """Add mobile-optimized summary items to admin dashboard"""
    # This was causing 'dict' object has no attribute 'is_shown' error
    # Need to create proper SummaryItem objects instead of dicts
    pass


# Enhanced error handling for mobile
@hooks.register('insert_global_admin_js')
def mobile_error_handling():
    """Enhanced error handling for mobile admin"""
    return format_html(
        '''
        <script>
        // Enhanced mobile error handling
        window.addEventListener('error', function(e) {{
            if (window.innerWidth <= 768) {{
                // Show mobile-friendly error notification
                showMobileNotification('Der opstod en fejl. Prøv igen.', 'error');
            }}
        }});

        function showMobileNotification(message, type = 'info') {{
            const notification = document.createElement('div');
            notification.className = `mobile-notification mobile-notification-${{type}}`;
            notification.innerHTML = `
                <div class="mobile-notification-content">
                    <span class="mobile-notification-icon">
                        ${{type === 'error' ? '⚠️' : type === 'success' ? '✅' : 'ℹ️'}}
                    </span>
                    <span class="mobile-notification-text">${{message}}</span>
                    <button class="mobile-notification-close">&times;</button>
                </div>
            `;

            notification.style.cssText = `
                position: fixed;
                top: 20px;
                left: 20px;
                right: 20px;
                background: ${{type === 'error' ? '#fee2e2' : type === 'success' ? '#dcfce7' : '#dbeafe'}};
                border: 1px solid ${{type === 'error' ? '#fecaca' : type === 'success' ? '#bbf7d0' : '#bfdbfe'}};
                color: ${{type === 'error' ? '#991b1b' : type === 'success' ? '#166534' : '#1e40af'}};
                border-radius: 8px;
                z-index: 10002;
                transform: translateY(-100%);
                transition: transform 0.3s ease;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            `;

            notification.querySelector('.mobile-notification-content').style.cssText = `
                display: flex;
                align-items: center;
                padding: 12px 16px;
            `;

            notification.querySelector('.mobile-notification-icon').style.cssText = `
                margin-right: 12px;
                font-size: 18px;
            `;

            notification.querySelector('.mobile-notification-text').style.cssText = `
                flex: 1;
                font-weight: 500;
            `;

            notification.querySelector('.mobile-notification-close').style.cssText = `
                background: none;
                border: none;
                font-size: 20px;
                cursor: pointer;
                padding: 0;
                margin-left: 12px;
                opacity: 0.7;
            `;

            document.body.appendChild(notification);

            // Show notification
            setTimeout(() => {{
                notification.style.transform = 'translateY(0)';
            }}, 100);

            // Handle close button
            notification.querySelector('.mobile-notification-close').addEventListener('click', function() {{
                hideNotification(notification);
            }});

            // Auto-hide after 5 seconds
            setTimeout(() => {{
                hideNotification(notification);
            }}, 5000);

            function hideNotification(notif) {{
                notif.style.transform = 'translateY(-100%)';
                setTimeout(() => {{
                    if (notif.parentNode) {{
                        notif.remove();
                    }}
                }}, 300);
            }}
        }}

        // Make function globally available
        window.showMobileNotification = showMobileNotification;
        </script>
        '''
    )


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
