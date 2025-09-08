from wagtail import hooks
from django.utils.html import format_html
from django.templatetags.static import static


# Custom admin CSS removed - using default Wagtail theme


@hooks.register('construct_main_menu')
def customize_menu_items(request, menu_items):
    """Keep only essential menu items for Johann's construction business"""
    essential_items = []
    
# Debug output removed for clean console
    
    for item in menu_items:
        # Get item properties safely
        item_name = getattr(item, 'name', '')
        
        # Only keep essential items Johann needs
        if item_name == 'explorer':
            item.label = 'Sider'  # Rename to Danish
            essential_items.append(item)
        elif item_name == 'images':
            # Keep images for project images
            item.label = 'Billeder'
            essential_items.append(item)
        elif item_name == 'settings':
            essential_items.append(item)
        # Skip all others: documents, reports, help
    
# Debug output removed for clean console
    return essential_items




@hooks.register('construct_page_action_menu')
def remove_moderation_actions(menu_items, request, context):
    """Remove submit for moderation and other complex workflow actions"""
    # Keep only essential page actions: Save, Save & Publish, Delete
    essential_actions = []
    
    for item in menu_items:
        # Keep basic actions Johann needs
        action_name = getattr(item, 'name', '')
        if action_name in ['action-publish', 'action-submit', 'action-delete']:
            essential_actions.append(item)
    
    return essential_actions


@hooks.register('construct_homepage_summary_items') 
def customize_dashboard_summary(request, summary_items):
    """
    Simplify dashboard summary for Johann.
    Show only Pages counts.
    """
    relevant_items = []
    
    for item in summary_items:
        # Keep only essential summary items
        if hasattr(item, 'template_name'):
            template = item.template_name
            # Keep pages summaries only
            if 'pages' in template:
                relevant_items.append(item)
        else:
            # Keep items without template_name 
            relevant_items.append(item)
    
    return relevant_items