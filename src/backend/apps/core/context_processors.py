from wagtail.models import Site


def settings(request):
    """
    Custom settings context processor that provides company_settings, design_settings, header_settings, footer_settings, and navigation_links.
    """
    try:
        # Import here to avoid circular imports
        from apps.pages.models import CompanySettings, DesignPage, HeaderManagementPage, FooterSettings, NavigationLink
        
        # Get the site using Wagtail's site detection
        site = Site.find_for_request(request)
        
        # Get the settings for the site
        try:
            company_settings = CompanySettings.for_site(site) if site else CompanySettings.objects.first()
        except:
            company_settings = None
            
        try:
            design_settings = DesignPage.objects.live().first()
        except:
            design_settings = None
            
        try:
            header_settings = HeaderManagementPage.objects.live().first()
        except:
            header_settings = None
            
        try:
            footer_settings = FooterSettings.objects.first()
        except:
            footer_settings = None
            
        try:
            navigation_links = NavigationLink.objects.filter(show_in_header=True).order_by('order', 'name')
        except:
            navigation_links = []

        # Separate navigation links for mega menu
        main_nav_items = []
        mega_menu_items = []

        for link in navigation_links:
            link_name_lower = link.name.lower()
            # Main navigation items that should be displayed directly
            if 'kontakt' in link_name_lower or 'galleri' in link_name_lower:
                main_nav_items.append(link)
            else:
                # Everything else goes into mega menu
                mega_menu_items.append(link)

        return {
            'company_settings': company_settings,
            'design_settings': design_settings,
            'header_settings': header_settings,
            'footer_settings': footer_settings,
            'navigation_links': navigation_links,
            'main_nav_items': main_nav_items,
            'mega_menu_items': mega_menu_items,
        }
    except Exception:
        # If we can't get any site, return empty settings
        return {
            'company_settings': None,
            'design_settings': None,
            'header_settings': None,
            'footer_settings': None,
            'navigation_links': [],
            'main_nav_items': [],
            'mega_menu_items': [],
        }