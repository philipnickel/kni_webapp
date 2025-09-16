"""
Grouped StreamField blocks organized by Preline UI categories
Based on https://preline.co/examples.html component organization
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from . import blocks as site_blocks


# =============================================================================
# PAGE SECTIONS (Marketing Components)
# =============================================================================

class PageSectionsGroup:
    """Hero Sections, Features, Testimonials, etc."""
    
    @staticmethod
    def get_blocks():
        return [
            # Hero Sections
            ("modern_hero", site_blocks.ModernHeroBlock()),
            ("hero_v2", site_blocks.HeroV2Block()),
            
            # Features
            ("features", site_blocks.FeaturesBlock()),
            
            # Testimonials
            ("testimonials_snippets", site_blocks.TestimonialsBlock()),
            
            # Team Sections
            ("team_section", site_blocks.TeamSectionBlock()),
            
            # Company Stats
            ("company_stats", site_blocks.CompanyStatsBlock()),
            
            # Company Milestones (Timeline)
            ("company_milestones", site_blocks.CompanyMilestonesBlock()),
            
            # Trust Badges (Clients Sections)
            ("trust_badges", site_blocks.TrustBadgesBlock()),
            
            # Logo Cloud (Clients Sections)
            ("logo_cloud", site_blocks.LogoCloudBlock()),
            
            # Rich Text Section (Description Lists)
            ("richtext_section", site_blocks.RichTextSectionBlock()),
        ]


# =============================================================================
# USER INTERFACE (UI) CONTROLS
# =============================================================================

class UIControlsGroup:
    """Buttons, Dropdowns, Selects, etc."""
    
    @staticmethod
    def get_blocks():
        return [
            # Call-to-Action (Button Groups)
            ("cta", site_blocks.CTABlock()),
            
            # Services Grid (Button Groups)
            ("services_grid", site_blocks.ServicesGridBlock()),
            ("services_grid_inline", site_blocks.ServicesGridInlineBlock()),
        ]


# =============================================================================
# OVERLAYS
# =============================================================================

class OverlaysGroup:
    """Modals, Dropdowns, Popovers, etc."""
    
    @staticmethod
    def get_blocks():
        return [
            # Quote Request (Modal-like form)
            ("quote_request", site_blocks.QuoteRequestBlock()),
        ]


# =============================================================================
# FORMS
# =============================================================================

class FormsGroup:
    """Authentication, Feedback, Subscribe, etc."""
    
    @staticmethod
    def get_blocks():
        return [
            # FAQ (Feedback)
            ("faq", site_blocks.FAQBlock()),
        ]


# =============================================================================
# GALLERIES & MEDIA
# =============================================================================

class MediaGroup:
    """Image galleries, carousels, etc."""
    
    @staticmethod
    def get_blocks():
        return [
            # Carousel
            ("carousel", site_blocks.CarouselBlock()),
            
            # Image Gallery
            ("image_gallery", site_blocks.ImageGalleryBlock()),
            
            # Featured Projects (Gallery-like)
            ("featured_projects", site_blocks.FeaturedProjectsBlock()),
        ]


# =============================================================================
# BUSINESS & COMPANY
# =============================================================================

class BusinessGroup:
    """Company-specific components"""
    
    @staticmethod
    def get_blocks():
        return [
            # Certifications
            ("certifications_section", site_blocks.CertificationsBlock()),
        ]


# =============================================================================
# MAIN GROUPED STREAMFIELD
# =============================================================================

def get_grouped_streamfield_blocks():
    """
    Returns all blocks organized by Preline UI categories
    Based on https://preline.co/examples.html
    """
    
    # Get all blocks from each group
    all_blocks = []
    
    # Page Sections (Marketing Components)
    for block_name, block_instance in PageSectionsGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    # User Interface Controls
    for block_name, block_instance in UIControlsGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    # Media & Galleries
    for block_name, block_instance in MediaGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    # Forms
    for block_name, block_instance in FormsGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    # Overlays
    for block_name, block_instance in OverlaysGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    # Business & Company
    for block_name, block_instance in BusinessGroup.get_blocks():
        all_blocks.append((block_name, block_instance))
    
    return all_blocks


# =============================================================================
# FUTURE EXPANSION HELPERS
# =============================================================================

class PrelineComponentAdder:
    """
    Helper class to easily add new Preline components to the appropriate groups
    """
    
    @staticmethod
    def add_to_page_sections(block_name, block_instance):
        """Add a new block to the Page Sections group"""
        PageSectionsGroup.get_blocks().append((block_name, block_instance))
    
    @staticmethod
    def add_to_ui_controls(block_name, block_instance):
        """Add a new block to the UI Controls group"""
        UIControlsGroup.get_blocks().append((block_name, block_instance))
    
    @staticmethod
    def add_to_media(block_name, block_instance):
        """Add a new block to the Media & Galleries group"""
        MediaGroup.get_blocks().append((block_name, block_instance))
    
    @staticmethod
    def add_to_forms(block_name, block_instance):
        """Add a new block to the Forms group"""
        FormsGroup.get_blocks().append((block_name, block_instance))
    
    @staticmethod
    def add_to_overlays(block_name, block_instance):
        """Add a new block to the Overlays group"""
        OverlaysGroup.get_blocks().append((block_name, block_instance))
    
    @staticmethod
    def add_to_business(block_name, block_instance):
        """Add a new block to the Business & Company group"""
        BusinessGroup.get_blocks().append((block_name, block_instance))


# =============================================================================
# EXAMPLE: How to add new Preline components
# =============================================================================

"""
Example of how to add new Preline components:

# 1. Create your new block in blocks.py
class NewPrelineButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    style = blocks.ChoiceBlock(choices=[
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
    ])
    
    class Meta:
        icon = 'button'
        template = 'blocks/new_preline_button.html'

# 2. Add it to the appropriate group
from .grouped_blocks import PrelineComponentAdder

PrelineComponentAdder.add_to_ui_controls('new_preline_button', NewPrelineButtonBlock())

# 3. The component will automatically appear in the grouped StreamField
"""
