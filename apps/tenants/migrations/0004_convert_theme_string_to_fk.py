# Convert existing theme string values to ForeignKey references

from django.db import migrations


def convert_theme_to_fk(apps, schema_editor):
    """Convert theme string values to theme_fk references"""
    Client = apps.get_model('tenants', 'Client')
    Theme = apps.get_model('tenants', 'Theme')
    
    # Mapping from string values to theme slugs
    theme_mapping = {
        'forest': 'forest',
        'wood': 'wood', 
        'slate': 'slate',
    }
    
    for client in Client.objects.all():
        if client.theme in theme_mapping:
            theme_slug = theme_mapping[client.theme]
            try:
                theme = Theme.objects.get(slug=theme_slug)
                client.theme_fk = theme
                client.save(update_fields=['theme_fk'])
            except Theme.DoesNotExist:
                # If theme doesn't exist, use default forest theme
                theme = Theme.objects.get(slug='forest')
                client.theme_fk = theme
                client.save(update_fields=['theme_fk'])


def reverse_convert_theme_to_fk(apps, schema_editor):
    """Clear theme_fk references"""
    Client = apps.get_model('tenants', 'Client')
    Client.objects.update(theme_fk=None)


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0003_populate_themes_add_theme_fk'),
    ]

    operations = [
        migrations.RunPython(
            convert_theme_to_fk,
            reverse_convert_theme_to_fk,
        ),
    ]