# Finalize theme field conversion

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0004_convert_theme_string_to_fk'),
    ]

    operations = [
        # Remove old theme CharField
        migrations.RemoveField(
            model_name='client',
            name='theme',
        ),
        
        # Rename theme_fk to theme
        migrations.RenameField(
            model_name='client',
            old_name='theme_fk',
            new_name='theme',
        ),
    ]