from django import forms
from django.utils.safestring import mark_safe


class ColorPaletteWidget(forms.Select):
    """Custom widget for color palette selection with visual preview"""
    
    def format_value(self, value):
        return value
    
    def render(self, name, value, attrs=None, renderer=None):
        # Get the standard select HTML
        select_html = super().render(name, value, attrs, renderer)
        
        # Define color schemes for preview
        color_schemes = {
            'classic_orange': {
                'primary': '#ea580c',
                'secondary': '#1f2937', 
                'accent': '#f59e0b',
                'name': 'Klassisk Orange'
            },
            'modern_blue': {
                'primary': '#2563eb',
                'secondary': '#1e293b',
                'accent': '#0ea5e9', 
                'name': 'Moderne Blå'
            },
            'earthy_green': {
                'primary': '#16a34a',
                'secondary': '#365314',
                'accent': '#84cc16',
                'name': 'Jordnær Grøn'
            },
            'industrial_grey': {
                'primary': '#4b5563',
                'secondary': '#111827',
                'accent': '#6b7280',
                'name': 'Industri Grå'
            },
            'warm_red': {
                'primary': '#dc2626',
                'secondary': '#7f1d1d',
                'accent': '#f59e0b',
                'name': 'Varm Rød'
            },
            'deep_navy': {
                'primary': '#1e40af',
                'secondary': '#0f172a',
                'accent': '#0891b2',
                'name': 'Dyb Marineblå'
            },
            'construction_yellow': {
                'primary': '#eab308',
                'secondary': '#1f2937',
                'accent': '#f59e0b',
                'name': 'Bygge Gul'
            },
        }
        
        # Generate color gallery HTML
        gallery_html = '<div class="color-palette-gallery" style="margin-top: 10px;">'
        for key, scheme in color_schemes.items():
            is_selected = 'selected' if value == key else ''
            gallery_html += f'''
                <div class="color-scheme-preview" style="
                    display: inline-block; 
                    margin: 5px; 
                    padding: 10px; 
                    border: 2px solid {'#007cba' if is_selected else '#ddd'}; 
                    border-radius: 5px; 
                    cursor: pointer;
                    background: white;
                " data-value="{key}">
                    <div style="font-weight: bold; margin-bottom: 5px;">{scheme['name']}</div>
                    <div style="display: flex; gap: 3px;">
                        <div style="width: 20px; height: 20px; background: {scheme['primary']}; border-radius: 3px;" title="Primary"></div>
                        <div style="width: 20px; height: 20px; background: {scheme['secondary']}; border-radius: 3px;" title="Secondary"></div>
                        <div style="width: 20px; height: 20px; background: {scheme['accent']}; border-radius: 3px;" title="Accent"></div>
                    </div>
                </div>
            '''
        gallery_html += '</div>'
        
        # Add JavaScript for interaction
        js_html = '''
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const previews = document.querySelectorAll('.color-scheme-preview');
            const select = document.querySelector('select[name="' + name + '"]');
            
            previews.forEach(function(preview) {
                preview.addEventListener('click', function() {
                    const value = this.getAttribute('data-value');
                    select.value = value;
                    
                    // Update visual selection
                    previews.forEach(p => p.style.borderColor = '#ddd');
                    this.style.borderColor = '#007cba';
                });
            });
        });
        </script>
        '''
        
        return mark_safe(select_html + gallery_html + js_html)

