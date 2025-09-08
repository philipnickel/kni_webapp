# Data migration to populate themes and prepare for field conversion

import django.db.models.deletion
from django.db import migrations, models


def populate_themes(apps, schema_editor):
    """Create default themes and add temporary theme_fk field"""
    Theme = apps.get_model('tenants', 'Theme')
    
    # Create default themes
    themes_data = [
        {
            'name': 'Forest Green',
            'slug': 'forest',
            'description': 'Natural forest theme with earthy greens',
            'primary_color': '#4d7a3a',
            'primary_hover_color': '#3a5e2c',
            'hero_start_color': '#3a5e2c',
            'hero_end_color': '#654e33',
            'footer_bg_color': '#3d251b',
            'footer_text_color': '#e9e3d9',
        },
        {
            'name': 'Wood Brown',
            'slug': 'wood',
            'description': 'Warm wood construction theme',
            'primary_color': '#8b4513',
            'primary_hover_color': '#654321',
            'hero_start_color': '#654321',
            'hero_end_color': '#3d251b',
            'footer_bg_color': '#2f1b14',
            'footer_text_color': '#f4f1ec',
        },
        {
            'name': 'Slate Gray',
            'slug': 'slate',
            'description': 'Professional slate gray theme',
            'primary_color': '#475569',
            'primary_hover_color': '#334155',
            'hero_start_color': '#334155',
            'hero_end_color': '#1e293b',
            'footer_bg_color': '#0f172a',
            'footer_text_color': '#f1f5f9',
        },
    ]
    
    for theme_data in themes_data:
        Theme.objects.get_or_create(
            slug=theme_data['slug'],
            defaults=theme_data
        )


def reverse_populate_themes(apps, schema_editor):
    """Remove created themes"""
    Theme = apps.get_model('tenants', 'Theme')
    Theme.objects.filter(slug__in=['forest', 'wood', 'slate']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_add_theme_model'),
    ]

    operations = [
        # First populate themes
        migrations.RunPython(
            populate_themes,
            reverse_populate_themes,
        ),
        
        # Add temporary theme_fk field
        migrations.AddField(
            model_name='client',
            name='theme_fk',
            field=models.ForeignKey(
                blank=True,
                help_text="Visual theme for this tenant's website",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='clients_fk_temp',
                to='tenants.theme',
                verbose_name='Website Theme (FK)'
            ),
        ),
    ]