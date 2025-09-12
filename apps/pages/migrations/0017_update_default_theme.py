# Generated manually to update default theme from 'forest' to 'light'

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_contactpage_contact_form_intro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='default_theme',
            field=models.CharField(
                choices=[
                    ('light', 'Light'),
                    ('dark', 'Dark'),
                    ('cupcake', 'Cupcake'),
                    ('bumblebee', 'Bumblebee'),
                    ('emerald', 'Emerald'),
                    ('corporate', 'Corporate'),
                    ('synthwave', 'Synthwave'),
                    ('retro', 'Retro'),
                    ('cyberpunk', 'Cyberpunk'),
                    ('valentine', 'Valentine'),
                    ('halloween', 'Halloween'),
                    ('garden', 'Garden'),
                    ('aqua', 'Aqua'),
                    ('lofi', 'Lo-Fi'),
                    ('pastel', 'Pastel'),
                    ('fantasy', 'Fantasy'),
                    ('wireframe', 'Wireframe'),
                    ('black', 'Black'),
                    ('luxury', 'Luxury'),
                    ('dracula', 'Dracula'),
                    ('cmyk', 'CMYK'),
                    ('autumn', 'Autumn'),
                    ('business', 'Business'),
                    ('acid', 'Acid'),
                    ('lemonade', 'Lemonade'),
                    ('night', 'Night'),
                    ('coffee', 'Coffee'),
                    ('winter', 'Winter'),
                    ('dim', 'Dim'),
                    ('nord', 'Nord'),
                    ('sunset', 'Sunset')
                ],
                default='light',
                help_text='Tema for hele websitet',
                max_length=20,
                verbose_name='Standard tema'
            ),
        ),
    ]
