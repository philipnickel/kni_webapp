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
        gallery_html = '''
        <div class="color-palette-gallery" style="margin-top: 12px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 16px;">
        '''
        
        for palette_key, colors in color_schemes.items():
            is_selected = 'checked' if value == palette_key else ''
            gallery_html += f'''
            <label style="cursor: pointer; border: 2px solid {'#e5e7eb' if not is_selected else colors['primary']}; border-radius: 8px; padding: 12px; background: white; transition: all 0.2s;">
                <input type="radio" name="{name}" value="{palette_key}" {is_selected} style="display: none;" onchange="this.form.querySelector('select[name=\\'{name}\\']').value = this.value; this.form.querySelector('select[name=\\'{name}\\']').dispatchEvent(new Event('change'));">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <div style="display: flex; gap: 4px;">
                        <div style="width: 20px; height: 20px; border-radius: 4px; background: {colors['primary']};"></div>
                        <div style="width: 20px; height: 20px; border-radius: 4px; background: {colors['secondary']};"></div>
                        <div style="width: 20px; height: 20px; border-radius: 4px; background: {colors['accent']};"></div>
                    </div>
                </div>
                <div style="font-weight: 500; color: #374151; font-size: 14px;">
                    {colors['name']}
                </div>
            </label>
            '''
        
        gallery_html += '''
            </div>
        </div>
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const gallery = document.querySelector('.color-palette-gallery');
            const select = document.querySelector('select[name="''' + name + '''"]');
            
            if (gallery && select) {
                // Hide the original select
                select.style.display = 'none';
                
                // Update radio buttons when select changes
                select.addEventListener('change', function() {
                    const radios = gallery.querySelectorAll('input[type="radio"]');
                    radios.forEach(radio => {
                        const label = radio.parentElement;
                        if (radio.value === select.value) {
                            radio.checked = true;
                            label.style.borderColor = getComputedStyle(label.querySelector('div > div')).backgroundColor;
                        } else {
                            radio.checked = false;
                            label.style.borderColor = '#e5e7eb';
                        }
                    });
                });
            }
        });
        </script>
        '''
        
        return mark_safe(select_html + gallery_html)