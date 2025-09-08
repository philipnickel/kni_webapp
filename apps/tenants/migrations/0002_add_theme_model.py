# Generated manually for step-by-step theme migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="e.g. 'Forest Green', 'Wood Brown'", max_length=50, unique=True, verbose_name='Theme Name')),
                ('slug', models.SlugField(help_text="e.g. 'forest', 'wood' - used in CSS", max_length=50, unique=True, verbose_name='Theme Slug')),
                ('description', models.TextField(blank=True, help_text='Description of this theme', verbose_name='Description')),
                ('primary_color', models.CharField(default='#4d7a3a', help_text='Hex color code (e.g. #4d7a3a)', max_length=7, verbose_name='Primary Color')),
                ('primary_hover_color', models.CharField(default='#3a5e2c', help_text='Hex color code for hover state', max_length=7, verbose_name='Primary Hover Color')),
                ('hero_start_color', models.CharField(default='#3a5e2c', help_text='Hero section gradient start color', max_length=7, verbose_name='Hero Gradient Start')),
                ('hero_end_color', models.CharField(default='#654e33', help_text='Hero section gradient end color', max_length=7, verbose_name='Hero Gradient End')),
                ('footer_bg_color', models.CharField(default='#3d251b', help_text='Footer background color', max_length=7, verbose_name='Footer Background')),
                ('footer_text_color', models.CharField(default='#e9e3d9', help_text='Footer text color', max_length=7, verbose_name='Footer Text')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this theme is available for selection', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
                'ordering': ['name'],
            },
        ),
    ]