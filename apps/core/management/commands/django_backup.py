import os
import json
import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core import serializers
from django.apps import apps
from django.conf import settings


class Command(BaseCommand):
    help = "Create a Django fixture backup of the current development database (all models)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            dest="output",
            help="Output file path for the JSON fixture (default: backups/django-dev-YYYYmmdd_HHMMSS.json)",
        )
        parser.add_argument(
            "--include-media",
            action="store_true",
            help="Include media files in the backup (copies to backups/media/)",
        )

    def handle(self, *args, **options):
        backups_dir = Path(settings.BASE_DIR) / "backups"
        backups_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output = options.get("output") or backups_dir / f"django-dev-{ts}.json"
        output = Path(output)

        self.stdout.write(self.style.NOTICE(f"Creating Django fixture backup to {output} ..."))

        # Get all models from all installed apps
        all_models = []
        for app_config in apps.get_app_configs():
            if app_config.name.startswith('django.') or app_config.name == 'wagtail.contrib.redirects':
                continue  # Skip Django internal apps and some Wagtail apps that can cause issues
            for model in app_config.get_models():
                all_models.append(model)

        # Create fixtures for all models
        all_objects = []
        for model in all_models:
            try:
                objects = model.objects.all()
                if objects.exists():
                    self.stdout.write(f"Backing up {objects.count()} {model._meta.label} objects")
                    all_objects.extend(objects)
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f"Skipping {model._meta.label}: {e}")
                )

        # Serialize all objects
        try:
            fixture_data = serializers.serialize('json', all_objects, indent=2)
            with output.open('w', encoding='utf-8') as f:
                f.write(fixture_data)
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error creating fixture: {e}")
            )
            return

        # Optionally backup media files
        if options.get("include_media"):
            media_backup_dir = backups_dir / "media" / ts
            media_backup_dir.mkdir(parents=True, exist_ok=True)
            
            media_root = Path(settings.MEDIA_ROOT)
            if media_root.exists():
                self.stdout.write(f"Backing up media files to {media_backup_dir}")
                import shutil
                try:
                    shutil.copytree(media_root, media_backup_dir / "media", dirs_exist_ok=True)
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"Error backing up media: {e}")
                    )

        self.stdout.write(
            self.style.SUCCESS(f"Django fixture backup completed: {output}")
        )
        self.stdout.write(
            self.style.NOTICE(f"To restore: python manage.py loaddata {output}")
        )