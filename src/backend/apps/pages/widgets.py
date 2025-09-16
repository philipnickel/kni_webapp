from django import forms
from django.utils.safestring import mark_safe
import json
from .themes import ALL_THEMES


class ColorPickerWidget(forms.TextInput):
    """
    Enhanced color picker widget inspired by Preline's theming system
    """
    
    def __init__(self, attrs=None):
        default_attrs = {
            'type': 'color',
            'class': 'color-picker-widget',
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        """Render the color picker with live preview"""
        
        # Color name mapping for better UX
        color_names = {
            'primary_color': 'Primary',
            'secondary_color': 'Secondary', 
            'accent_color': 'Accent',
            'success_color': 'Success',
            'warning_color': 'Warning',
            'error_color': 'Error',
            'background_color': 'Background',
            'surface_color': 'Surface',
            'text_primary': 'Text Primary',
            'text_secondary': 'Text Secondary',
        }
        color_name = color_names.get(name, 'Color')
        
        # Get the current value or default
        current_value = value or '#4d7a3a'
        
        html = f'''
        <div class="color-picker-container" id="{name}-container">
            <div class="flex items-center space-x-3">
                <input type="color" 
                       name="{name}" 
                       id="{name}" 
                       value="{current_value}"
                       class="w-12 h-12 rounded-lg border-2 border-gray-300 cursor-pointer"
                       onchange="updateColorPreview('{name}', this.value)">
                
                <div class="flex-1">
                    <input type="text" 
                           id="{name}-text" 
                           value="{current_value}"
                           class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                           placeholder="#000000"
                           onchange="updateColorFromText('{name}', this.value)">
                    <p class="text-sm text-gray-500 mt-1">{color_name} Color</p>
                </div>
                
                <div class="flex flex-col items-center">
                    <div class="w-8 h-8 rounded-full border-2 border-gray-300" 
                         id="{name}-preview-ring" 
                         style="background-color: {current_value}; border-color: {current_value};"></div>
                    <span class="text-xs text-gray-600 mt-1" id="{name}-color-name">{current_value}</span>
                </div>
            </div>
            
            <!-- Color Scale Preview -->
            <div class="mt-3 grid grid-cols-10 gap-1">
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.1;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.2;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.3;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.4;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.5;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.6;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.7;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.8;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 0.9;"></div>
                <div class="h-4 rounded" style="background-color: {current_value}; opacity: 1.0;"></div>
            </div>
            
            <!-- Live Preview Components -->
            <div class="mt-4 p-3 bg-gray-50 rounded-lg">
                <p class="text-sm font-medium text-gray-700 mb-2">Live Preview:</p>
                <div class="flex space-x-3">
                    <button class="px-4 py-2 rounded-md text-white text-sm" 
                            id="{name}-preview-button" 
                            style="background-color: {current_value};">
                        Button
                    </button>
                    <button class="px-4 py-2 rounded-md border-2 text-sm" 
                            id="{name}-preview-outline" 
                            style="border-color: {current_value}; color: {current_value};">
                        Outline
                    </button>
                    <div class="px-3 py-2 rounded-md text-sm" 
                         id="{name}-preview-light" 
                         style="background-color: {current_value}; color: white;">
                        Light
                    </div>
                </div>
            </div>
        </div>
        
        <script>
        function updateColorPreview(colorPickerId, color) {{
            const textInput = document.getElementById(colorPickerId + '-text');
            const previewRing = document.getElementById(colorPickerId + '-preview-ring');
            const colorName = document.getElementById(colorPickerId + '-color-name');
            
            // Update text input
            if (textInput) {{
                textInput.value = color;
            }}
            
            // Update preview ring
            if (previewRing) {{
                previewRing.style.borderColor = color;
            }}
            
            // Update color name
            if (colorName) {{
                colorName.textContent = color;
            }}
            
            // Update color scale
            const container = document.getElementById(colorPickerId + '-container');
            if (container) {{
                const scaleDivs = container.querySelectorAll('.grid > div');
                scaleDivs.forEach(div => {{
                    div.style.background = color;
                }});
            }}
            
            // Update live preview
            const button = document.getElementById(colorPickerId + '-preview-button');
            const outline = document.getElementById(colorPickerId + '-preview-outline');
            const light = document.getElementById(colorPickerId + '-preview-light');
            
            if (button) {{
                button.style.background = color;
            }}
            if (outline) {{
                outline.style.borderColor = color;
                outline.style.color = color;
            }}
            if (light) {{
                light.style.background = color;
                light.style.color = color;
            }}
        }}
        
        function updateColorFromText(colorPickerId, color) {{
            const colorPicker = document.getElementById(colorPickerId);
            if (colorPicker && /^#[0-9A-F]{{6}}$/i.test(color)) {{
                colorPicker.value = color;
                updateColorPreview(colorPickerId, color);
            }} else {{
                // Reset to current color if invalid
                if (colorPicker) {{
                    colorPicker.value = colorPicker.value;
                }}
            }}
        }}
        </script>
        '''
        
        return mark_safe(html)


class ThemeSelectorWidget(forms.Widget):
    """
    Theme selector widget with predefined color schemes
    Inspired by Nord, Tailwind, and other popular design systems
    """
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        """Render the theme selector widget"""
        
        # Use themes from the separate themes.py file
        themes = ALL_THEMES
        
        # Get current theme or default to 'tailwind'
        current_theme = value if value else 'tailwind'
        
        html = f'''
        <div class="theme-selector-container" style="margin: 1rem 0;">
            <style>
                .theme-selector-container .grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 1rem;
                    margin: 1rem 0;
                }}
                .theme-selector-container .theme-card {{
                    border: 1px solid #e5e7eb;
                    border-radius: 0.5rem;
                    padding: 1rem;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    background: white;
                }}
                .theme-selector-container .theme-card:hover {{
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                    transform: translateY(-1px);
                }}
                .theme-selector-container .theme-card.ring-2 {{
                    border-color: #3b82f6;
                    background-color: #eff6ff;
                    box-shadow: 0 0 0 2px #3b82f6;
                }}
                .theme-selector-container .theme-card h4 {{
                    margin: 0 0 0.5rem 0;
                    font-size: 1.125rem;
                    font-weight: 600;
                    color: #111827;
                }}
                .theme-selector-container .theme-card p {{
                    margin: 0 0 1rem 0;
                    font-size: 0.875rem;
                    color: #6b7280;
                }}
                .theme-selector-container .color-swatches {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 0.5rem;
                    margin-bottom: 1rem;
                }}
                .theme-selector-container .color-swatch {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}
                .theme-selector-container .color-circle {{
                    width: 2rem;
                    height: 2rem;
                    border-radius: 50%;
                    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                    margin-bottom: 0.25rem;
                }}
                .theme-selector-container .color-label {{
                    font-size: 0.75rem;
                    color: #6b7280;
                    text-align: center;
                }}
                .theme-selector-container .preview-components {{
                    display: flex;
                    flex-direction: column;
                    gap: 0.5rem;
                }}
                .theme-selector-container .preview-button {{
                    padding: 0.5rem 1rem;
                    border-radius: 0.375rem;
                    color: white;
                    font-size: 0.875rem;
                    border: none;
                    width: 100%;
                }}
                .theme-selector-container .preview-card {{
                    padding: 0.5rem;
                    border-radius: 0.375rem;
                    font-size: 0.75rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }}
                .theme-selector-container .preview-accent {{
                    width: 1.5rem;
                    height: 1.5rem;
                    border-radius: 50%;
                }}
                .theme-selector-container .selected-badge {{
                    display: inline-flex;
                    align-items: center;
                    padding: 0.25rem 0.5rem;
                    border-radius: 9999px;
                    font-size: 0.75rem;
                    font-weight: 500;
                    background-color: #dbeafe;
                    color: #1e40af;
                    margin-left: 0.5rem;
                }}
            </style>
            <div class="grid">
        '''
        
        for theme_key, theme_data in themes.items():
            is_selected = theme_key == current_theme
            selected_class = 'ring-2 ring-blue-500 bg-blue-50' if is_selected else ''
            selected_badge = '<span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">Selected</span>' if is_selected else ''
            
            html += f'''
                <div class="theme-card {selected_class}" 
                     onclick="selectTheme('{theme_key}')" 
                     data-theme="{theme_key}">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
                        <h4>{theme_data['name']}</h4>
                        {selected_badge}
                    </div>
                    <p>{theme_data['description']}</p>
                    
                    <!-- Color Swatches -->
                    <div class="color-swatches">
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['primary']};"></div>
                            <span class="color-label">Primary</span>
                        </div>
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['secondary']};"></div>
                            <span class="color-label">Secondary</span>
                        </div>
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['accent']};"></div>
                            <span class="color-label">Accent</span>
                        </div>
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['success']};"></div>
                            <span class="color-label">Success</span>
                        </div>
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['warning']};"></div>
                            <span class="color-label">Warning</span>
                        </div>
                        <div class="color-swatch">
                            <div class="color-circle" style="background-color: {theme_data['colors']['error']};"></div>
                            <span class="color-label">Error</span>
                        </div>
                    </div>
                    
                    <!-- Live Preview Components -->
                    <div class="preview-components">
                        <button class="preview-button" 
                                style="background-color: {theme_data['colors']['primary']};">
                            Preview Button
                        </button>
                        <div class="preview-card" 
                             style="background-color: {theme_data['colors']['surface']}; color: {theme_data['colors']['text_primary']};">
                            <span>Card Preview</span>
                            <div class="preview-accent" 
                                 style="background-color: {theme_data['colors']['accent']};"></div>
                        </div>
                    </div>
                </div>
            '''
        
        html += f'''
            </div>
            
            <!-- Hidden input to store selected theme -->
            <input type="hidden" name="{name}" id="{name}" value="{current_theme}">
        </div>
        
        <script>
        (function() {{
            const themes = {json.dumps(themes)};
            
            window.selectTheme = function(themeKey) {{
                console.log('Selecting theme:', themeKey);
                
                // Update hidden input
                const hiddenInput = document.getElementById('{name}');
                if (hiddenInput) {{
                    hiddenInput.value = themeKey;
                    console.log('Updated hidden input value to:', themeKey);
                }}
                
                // Update visual selection
                document.querySelectorAll('.theme-card').forEach(card => {{
                    const isSelected = card.dataset.theme === themeKey;
                    if (isSelected) {{
                        card.classList.add('ring-2');
                        card.style.borderColor = '#3b82f6';
                        card.style.backgroundColor = '#eff6ff';
                        card.style.boxShadow = '0 0 0 2px #3b82f6';
                        
                        // Show selected badge
                        let badge = card.querySelector('.selected-badge');
                        if (badge) {{
                            badge.style.display = 'inline-flex';
                        }}
                    }} else {{
                        card.classList.remove('ring-2');
                        card.style.borderColor = '#e5e7eb';
                        card.style.backgroundColor = 'white';
                        card.style.boxShadow = 'none';
                        
                        // Hide selected badge
                        let badge = card.querySelector('.selected-badge');
                        if (badge) {{
                            badge.style.display = 'none';
                        }}
                    }}
                }});
                
                // Update individual color fields if they exist
                updateColorFields(themeKey);
            }};
            
            function updateColorFields(themeKey) {{
                const theme = themes[themeKey];
                if (!theme) return;
                
                // Map theme colors to form field names
                const colorMappings = {{
                    'primary_color': theme.colors.primary,
                    'secondary_color': theme.colors.secondary,
                    'accent_color': theme.colors.accent,
                    'success_color': theme.colors.success,
                    'warning_color': theme.colors.warning,
                    'error_color': theme.colors.error,
                    'background_color': theme.colors.background,
                    'surface_color': theme.colors.surface,
                    'text_primary': theme.colors.text_primary,
                    'text_secondary': theme.colors.text_secondary
                }};
                
                Object.entries(colorMappings).forEach(([fieldName, colorValue]) => {{
                    const colorInput = document.getElementById(fieldName);
                    if (colorInput) {{
                        colorInput.value = colorValue;
                        // Trigger change event to update previews
                        colorInput.dispatchEvent(new Event('change'));
                    }}
                }});
            }}
            
            // Initialize on page load
            document.addEventListener('DOMContentLoaded', function() {{
                console.log('Theme selector initialized');
                
                // Add click handlers to all theme cards
                document.querySelectorAll('.theme-card').forEach(card => {{
                    card.addEventListener('click', function(e) {{
                        e.preventDefault();
                        const themeKey = this.dataset.theme;
                        console.log('Theme card clicked:', themeKey);
                        window.selectTheme(themeKey);
                    }});
                }});
            }});
        }})();
        </script>
        '''
        
        return mark_safe(html)
    
    def value_from_datadict(self, data, files, name):
        """
        Extract the value from the form data dictionary.
        This is crucial for form submission to work properly.
        """
        value = data.get(name)
        print(f"DEBUG: ThemeSelectorWidget.value_from_datadict - name: {name}, value: {value}")
        return value


class ColorPreviewWidget(forms.Widget):
    """
    Widget for displaying color previews in the admin
    """
    
    def render(self, name, value, attrs=None, renderer=None):
        """Render color preview"""
        if not value:
            return mark_safe('<div class="w-8 h-8 bg-gray-200 rounded"></div>')
        
        return mark_safe(f'''
            <div class="flex items-center space-x-2">
                <div class="w-8 h-8 rounded border" style="background-color: {value};"></div>
                <span class="text-sm text-gray-600">{value}</span>
            </div>
        ''')