from django import template
from apps.pages.blocks import section_classes

register = template.Library()


@register.filter
def section_classes(style):
    """
    Template filter to convert style dict to CSS classes
    Used in block templates to apply styling options
    """
    if not style:
        return "bg-surface py-16 max-w-5xl mx-auto"

    from apps.pages.blocks import section_classes as get_section_classes
    return get_section_classes(style)