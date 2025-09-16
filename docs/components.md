# Component Library Documentation

This document provides a comprehensive overview of all available components in the JCleemann Byg webapp, their sources, and usage.

## Overview

The webapp uses a hybrid approach combining multiple UI libraries and custom components:

- **Primary UI Library**: Preline (v2.0.3) - Modern, accessible components
- **Secondary Libraries**: Flowbite (v3.1.2), TW Elements (v2.0.0)
- **Styling**: Tailwind CSS (v3.4.0) with custom design system
- **Framework**: Django/Wagtail CMS with StreamField blocks

## Component Categories

### 🎨 **UI Library Sources**

| Library | Version | Purpose | Status |
|---------|---------|---------|--------|
| **Preline** | 2.0.3 | Primary UI components | ✅ Active |
| **Flowbite** | 3.1.2 | Secondary components | ❌ Removed |
| **TW Elements** | 2.0.0 | Additional components | ❌ Removed |
| **Tailwind CSS** | 3.4.0 | Styling framework | ✅ Active |

## Available Components

### 🏗️ **Core Layout Components**

#### 1. **Modern Hero Block** (`ModernHeroBlock`)
- **Template**: `templates/blocks/modern_hero.html`
- **Source**: Custom component with Preline styling
- **Features**: 
  - Full-screen hero with background image
  - Call-to-action buttons
  - Responsive design
  - Construction-themed styling

#### 2. **Hero V2 Block** (`HeroV2Block`)
- **Template**: `templates/blocks/hero_v2.html` / `templates/blocks/hero_v2_preline.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Two-column layout (content + image)
  - Gradient backgrounds
  - Custom color integration
  - Mobile-responsive

#### 3. **Carousel Block** (`CarouselBlock`)
- **Template**: `templates/blocks/carousel.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Image carousel with navigation
  - Auto-play functionality
  - Touch/swipe support
  - Responsive design

### 🎯 **Content Components**

#### 4. **Features Block** (`FeaturesBlock`)
- **Template**: `templates/blocks/features.html` / `templates/blocks/features_preline.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Grid layout for feature items
  - Custom icons (checkmark, hammer, leaf, etc.)
  - Configurable columns (2, 3, 4)
  - Color customization

#### 5. **Call-to-Action Block** (`CTABlock`)
- **Template**: `templates/blocks/cta.html` / `templates/blocks/cta_preline.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Prominent action buttons
  - Background customization
  - Multiple button styles
  - Responsive layout

#### 6. **Rich Text Section Block** (`RichTextSectionBlock`)
- **Template**: `templates/blocks/richtext_section.html`
- **Source**: Wagtail RichTextField with custom styling
- **Features**:
  - WYSIWYG content editing
  - Custom styling options
  - Responsive typography
  - Color integration

### 🏢 **Business Components**

#### 7. **Services Grid Block** (`ServicesGridBlock`)
- **Template**: `templates/blocks/services_grid.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Grid layout for services
  - Service icons and descriptions
  - Hover effects
  - Responsive design

#### 8. **Services Grid Inline Block** (`ServicesGridInlineBlock`)
- **Template**: `templates/blocks/services_grid_inline.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Inline service display
  - Compact layout
  - Icon integration
  - Mobile-optimized

#### 9. **Featured Projects Block** (`FeaturedProjectsBlock`)
- **Template**: `templates/blocks/featured_projects.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Project showcase
  - Image galleries
  - Project details
  - Filtering capabilities

### 👥 **Social & Trust Components**

#### 10. **Testimonials Block** (`TestimonialsBlock`)
- **Template**: `templates/blocks/testimonials.html` / `templates/blocks/testimonials_legacy.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Customer testimonials
  - Star ratings
  - Author information
  - Carousel display

#### 11. **Trust Badges Block** (`TrustBadgesBlock`)
- **Template**: `templates/blocks/trust_badges.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Trust indicators
  - Certification badges
  - Company credentials
  - Responsive layout

#### 12. **Logo Cloud Block** (`LogoCloudBlock`)
- **Template**: `templates/blocks/logo_cloud.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Partner/client logos
  - Grid layout
  - Hover effects
  - Responsive design

### 🖼️ **Media Components**

#### 13. **Image Gallery Block** (`ImageGalleryBlock`)
- **Template**: `templates/blocks/image_gallery.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Masonry/grid layout
  - Lightbox functionality
  - Image optimization
  - Responsive design

### 📋 **Interactive Components**

#### 14. **FAQ Block** (`FAQBlock`)
- **Template**: `templates/blocks/faq.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Accordion-style FAQ
  - Expandable answers
  - Search functionality
  - Mobile-friendly

#### 15. **Quote Request Block** (`QuoteRequestBlock`)
- **Template**: `templates/blocks/quote_request.html`
- **Source**: Custom component with Preline styling
- **Features**:
  - Contact form
  - Form validation
  - Email integration
  - Responsive design

### 🏢 **Company-Specific Components**

#### 16. **Team Section Block** (`TeamSectionBlock`)
- **Template**: `templates/blocks/team_section.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Team member profiles
  - Professional photos
  - Role descriptions
  - Social links

#### 17. **Company Milestones Block** (`CompanyMilestonesBlock`)
- **Template**: `templates/blocks/company_milestones.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Timeline display
  - Company achievements
  - Date-based organization
  - Visual timeline

#### 18. **Certifications Block** (`CertificationsBlock`)
- **Template**: `templates/blocks/certifications.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Certification badges
  - Industry credentials
  - Grid layout
  - Hover effects

#### 19. **Company Stats Block** (`CompanyStatsBlock`)
- **Template**: `templates/blocks/company_stats.html`
- **Source**: Custom component with Tailwind CSS
- **Features**:
  - Statistical counters
  - Animated numbers
  - Key metrics display
  - Visual indicators

## 🎨 **Styling System**

### Design Settings Integration
All components integrate with the custom design system through:

- **Color Customization**: Primary, secondary, accent colors
- **Theme Support**: Light, corporate, business, emerald themes
- **Typography**: Inter + Playfair Display, Inter + Georgia, system fonts
- **Responsive Design**: Mobile-first approach with Tailwind breakpoints

### Style Options Block
Every component includes a `StyleOptionsBlock` with:
- **Background**: Surface, Surface Soft, Hero Gradient, Base 200/300
- **Spacing**: Small (py-10), Medium (py-16), Large (py-24)
- **Container**: Narrow (max-w-3xl), Normal (max-w-5xl), Wide (max-w-7xl)
- **Divider**: Optional top divider

## 📁 **File Structure**

```
templates/blocks/
├── carousel.html                 # Image carousel
├── certifications.html          # Company certifications
├── company_milestones.html      # Company timeline
├── company_stats.html           # Statistical counters
├── cta.html                     # Call-to-action (legacy)
├── cta_preline.html            # Call-to-action (Preline)
├── faq.html                     # FAQ accordion
├── featured_projects.html       # Project showcase
├── features.html                # Features grid (legacy)
├── features_preline.html        # Features grid (Preline)
├── hero.html                    # Basic hero (legacy)
├── hero_v2.html                 # Hero V2 (legacy)
├── hero_v2_preline.html         # Hero V2 (Preline)
├── image_gallery.html           # Image gallery
├── logo_cloud.html              # Partner logos
├── modern_hero.html             # Modern hero section
├── quote_request.html           # Contact form
├── richtext_section.html        # Rich text content
├── services_grid.html           # Services grid
├── services_grid_inline.html    # Inline services
├── team_section.html            # Team members
├── testimonials.html            # Customer testimonials
├── testimonials_legacy.html     # Legacy testimonials
└── trust_badges.html            # Trust indicators
```

## 🔄 **Migration Status**

### ✅ **Migration Complete**
All legacy components have been removed and the system now uses Preline exclusively. All components are available and working in the DesignPage streamfield.

## 🚀 **Usage in DesignPage**

All components are available in the DesignPage streamfield for comprehensive preview:

```python
body = StreamField([
    ("modern_hero", site_blocks.ModernHeroBlock()),
    ("carousel", site_blocks.CarouselBlock()),
    ("hero_v2", site_blocks.HeroV2Block()),
    ("trust_badges", site_blocks.TrustBadgesBlock()),
    ("featured_projects", site_blocks.FeaturedProjectsBlock()),
    ("services_grid_inline", site_blocks.ServicesGridInlineBlock()),
    ("cta", site_blocks.CTABlock()),
    ("features", site_blocks.FeaturesBlock()),
    ("richtext_section", site_blocks.RichTextSectionBlock()),
    ("testimonials_snippets", site_blocks.TestimonialsBlock()),
    ("logo_cloud", site_blocks.LogoCloudBlock()),
    ("services_grid", site_blocks.ServicesGridBlock()),
    ("faq", site_blocks.FAQBlock()),
    ("image_gallery", site_blocks.ImageGalleryBlock()),
    ("quote_request", site_blocks.QuoteRequestBlock()),
    ("team_section", site_blocks.TeamSectionBlock()),
    ("company_milestones", site_blocks.CompanyMilestonesBlock()),
    ("certifications_section", site_blocks.CertificationsBlock()),
    ("company_stats", site_blocks.CompanyStatsBlock()),
], use_json_field=True, blank=True)
```

## 📝 **Development Notes**

- **Preline Priority**: New components should use Preline for consistency
- **Legacy Migration**: Existing components should be migrated to Preline when updated
- **Design System**: All components should integrate with the custom design settings
- **Responsive**: All components must be mobile-first and responsive
- **Accessibility**: Components should follow WCAG guidelines
- **Performance**: Optimize for Core Web Vitals

## 🔗 **Related Documentation**

- [Preline Documentation](https://preline.co/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Wagtail StreamField Documentation](https://docs.wagtail.org/en/stable/topics/streamfield.html)
- [Django Template Documentation](https://docs.djangoproject.com/en/stable/topics/templates/)

---

*Last updated: January 2025*
*Version: 1.0.0*
