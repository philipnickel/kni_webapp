# Generated manually to add Google Maps and footer settings

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_update_default_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='show_google_maps',
            field=models.BooleanField(default=True, verbose_name='Vis Google Maps', help_text='Vis Google Maps widget i footer'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='google_maps_api_key',
            field=models.CharField(blank=True, max_length=255, verbose_name='Google Maps API nøgle', help_text='API nøgle til Google Maps (krævet for at vise kort)'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='footer_style',
            field=models.CharField(choices=[('standard', 'Standard'), ('minimal', 'Minimal'), ('extended', 'Udvidet')], default='standard', max_length=20, verbose_name='Footer stil', help_text='Stil for footer'),
        ),
    ]

