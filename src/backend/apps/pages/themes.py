"""
Theme definitions for the website
Based on official Nord documentation: https://www.nordtheme.com/docs/colors-and-palettes
"""

# Official Nord color palettes from https://www.nordtheme.com/docs/colors-and-palettes
NORD_THEMES = {
    'nord_polar_night': {
        'name': 'Nord Polar Night',
        'description': 'Dark base colors for backgrounds and text in bright designs',
        'colors': {
            'primary': '#2e3440',      # Nord0 - Polar Night origin
            'secondary': '#3b4252',    # Nord1 - Brighter shade
            'accent': '#434c5e',       # Nord2 - Even brighter
            'success': '#4c566a',      # Nord3 - Brightest shade
            'warning': '#5e81ac',      # Nord10 - Deep arctic ocean
            'error': '#bf616a',        # Nord11 - Aurora red
            'background': '#2e3440',   # Nord0 - Base background
            'surface': '#3b4252',      # Nord1 - Elevated elements
            'text_primary': '#d8dee9', # Nord4 - Snow Storm origin
            'text_secondary': '#e5e9f0' # Nord5 - Brighter text
        }
    },
    'nord_snow_storm': {
        'name': 'Nord Snow Storm',
        'description': 'Bright colors for text and base UI elements',
        'colors': {
            'primary': '#d8dee9',      # Nord4 - Snow Storm origin
            'secondary': '#e5e9f0',    # Nord5 - Brighter shade
            'accent': '#eceff4',       # Nord6 - Brightest shade
            'success': '#a3be8c',      # Nord14 - Aurora green
            'warning': '#ebcb8b',      # Nord13 - Aurora yellow
            'error': '#bf616a',        # Nord11 - Aurora red
            'background': '#eceff4',   # Nord6 - Bright background
            'surface': '#e5e9f0',      # Nord5 - Elevated elements
            'text_primary': '#2e3440', # Nord0 - Dark text
            'text_secondary': '#3b4252' # Nord1 - Secondary text
        }
    },
    'nord_frost': {
        'name': 'Nord Frost',
        'description': 'Bluish colors for primary UI components and syntax highlighting',
        'colors': {
            'primary': '#88c0d0',      # Nord8 - Primary accent (pure ice)
            'secondary': '#8fbcbb',    # Nord7 - Frozen polar water
            'accent': '#81a1c1',       # Nord9 - Arctic waters
            'success': '#5e81ac',      # Nord10 - Deep arctic ocean
            'warning': '#ebcb8b',      # Nord13 - Aurora yellow
            'error': '#bf616a',        # Nord11 - Aurora red
            'background': '#2e3440',   # Nord0 - Polar Night
            'surface': '#3b4252',      # Nord1 - Elevated elements
            'text_primary': '#d8dee9', # Nord4 - Snow Storm
            'text_secondary': '#e5e9f0' # Nord5 - Brighter text
        }
    },
    'nord_aurora': {
        'name': 'Nord Aurora',
        'description': 'Colorful components reminiscent of Aurora borealis',
        'colors': {
            'primary': '#bf616a',      # Nord11 - Aurora red
            'secondary': '#d08770',    # Nord12 - Aurora orange
            'accent': '#ebcb8b',       # Nord13 - Aurora yellow
            'success': '#a3be8c',      # Nord14 - Aurora green
            'warning': '#b48ead',      # Nord15 - Aurora purple
            'error': '#bf616a',        # Nord11 - Aurora red
            'background': '#2e3440',   # Nord0 - Polar Night
            'surface': '#3b4252',      # Nord1 - Elevated elements
            'text_primary': '#d8dee9', # Nord4 - Snow Storm
            'text_secondary': '#e5e9f0' # Nord5 - Brighter text
        }
    },
}

# Additional popular themes
ADDITIONAL_THEMES = {
    'tailwind': {
        'name': 'Tailwind',
        'description': 'Modern utility-first design system with clean colors',
        'colors': {
            'primary': '#3b82f6',      # Blue-500
            'secondary': '#6366f1',    # Indigo-500
            'accent': '#f59e0b',       # Amber-500
            'success': '#10b981',      # Emerald-500
            'warning': '#f59e0b',      # Amber-500
            'error': '#ef4444',        # Red-500
            'background': '#ffffff',   # White
            'surface': '#f9fafb',      # Gray-50
            'text_primary': '#111827', # Gray-900
            'text_secondary': '#6b7280' # Gray-500
        }
    },
    'forest': {
        'name': 'Forest',
        'description': 'Natural green tones inspired by Danish forests',
        'colors': {
            'primary': '#16a34a',      # Green-600
            'secondary': '#4b5563',    # Gray-600
            'accent': '#d97706',       # Amber-600
            'success': '#16a34a',
            'warning': '#facc15',
            'error': '#dc2626',
            'background': '#f0fdf4',
            'surface': '#dcfce7',
            'text_primary': '#1f2937',
            'text_secondary': '#4b5563',
        }
    },
    'ocean': {
        'name': 'Ocean',
        'description': 'Deep blue and aquatic palette',
        'colors': {
            'primary': '#0ea5e9',      # Sky-500
            'secondary': '#64748b',    # Slate-500
            'accent': '#06b6d4',       # Cyan-500
            'success': '#22c55e',
            'warning': '#f59e0b',
            'error': '#ef4444',
            'background': '#eff6ff',
            'surface': '#dbeafe',
            'text_primary': '#1e293b',
            'text_secondary': '#475569',
        }
    },
    'sunset': {
        'name': 'Sunset',
        'description': 'Warm orange, pink, and purple hues',
        'colors': {
            'primary': '#f97316',      # Orange-500
            'secondary': '#a855f7',    # Purple-500
            'accent': '#ec4899',       # Pink-500
            'success': '#22c55e',
            'warning': '#f59e0b',
            'error': '#ef4444',
            'background': '#fff7ed',
            'surface': '#ffedd5',
            'text_primary': '#431407',
            'text_secondary': '#7c2d12',
        }
    },
    'monochrome': {
        'name': 'Monochrome',
        'description': 'Classic black, white, and gray scale',
        'colors': {
            'primary': '#1f2937',      # Gray-800
            'secondary': '#4b5563',    # Gray-600
            'accent': '#9ca3af',       # Gray-400
            'success': '#22c55e',
            'warning': '#f59e0b',
            'error': '#ef4444',
            'background': '#ffffff',
            'surface': '#f3f4f6',
            'text_primary': '#111827',
            'text_secondary': '#374151',
        }
    },
}

# Combine all themes
ALL_THEMES = {**NORD_THEMES, **ADDITIONAL_THEMES}

# Theme choices for Django model
THEME_CHOICES = [
    (key, theme['name'] + ' - ' + theme['description'])
    for key, theme in ALL_THEMES.items()
]

def get_theme_colors(theme_key):
    """Get colors for a specific theme"""
    return ALL_THEMES.get(theme_key, ALL_THEMES['tailwind'])['colors']

def get_theme_choices():
    """Get theme choices for Django model"""
    return THEME_CHOICES
