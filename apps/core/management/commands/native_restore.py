#!/usr/bin/env python3
"""
Django Management Command: native_restore

Django/Wagtail native restore system using Django's built-in loaddata.
This is the proper Django way - no manual site configuration needed.
"""

import os
import json
from pathlib import Path
import shutil
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
from django.db import transaction


class Command(BaseCommand):
    help = """
    Restore database backups using Django's native loaddata command.
    This is the proper Django way - works with any database backend.

    Usage Examples:
    # Restore specific backup
    python manage.py native_restore --backup baseline_20240915_123456.json

    # Restore latest backup with name
    python manage.py native_restore --name baseline

    # Include media files
    python manage.py native_restore --backup baseline_20240915_123456.json --include-media

    # Dry run
    python manage.py native_restore --backup baseline_20240915_123456.json --dry-run

    # Clear database first (fresh start)
    python manage.py native_restore --backup baseline_20240915_123456.json --flush
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup',
            help='Specific backup file to restore'
        )

        parser.add_argument(
            '--name',
            help='Find latest backup with this name'
        )

        parser.add_argument(
            '--include-media',
            action='store_true',
            help='Include media files in restore'
        )

        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be restored without restoring'
        )

        parser.add_argument(
            '--flush',
            action='store_true',
            help='Flush database before restore (fresh start)'
        )

        parser.add_argument(
            '--force',
            action='store_true',
            help='Force restore even if data exists'
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('📥 Django Native Restore System')
        )
        self.stdout.write('=' * 40)

        backup_dir = Path('backups')

        # Find backup file
        backup_file = self.find_backup_file(backup_dir, options)
        if not backup_file:
            raise CommandError('❌ No backup file found')

        self.stdout.write(f'📁 Found backup: {backup_file}')

        # Load and display metadata
        metadata = self.load_metadata(backup_file)
        if metadata:
            self.display_metadata(metadata)

        if options['dry_run']:
            self.show_dry_run_info(backup_file, options, metadata)
            return

        # Safety check
        if not options['force'] and not options['flush'] and self.database_has_data():
            self.stdout.write(
                self.style.WARNING('⚠️  Database already contains data.')
            )
            self.stdout.write('💡 Use --force to merge or --flush for fresh start')
            raise CommandError('Operation cancelled for data safety.')

        # Restore backup
        try:
            with transaction.atomic():
                if options['flush']:
                    self.flush_database()

                self.restore_django_backup(backup_file)

                if options['include_media']:
                    self.restore_media_files(backup_file, backup_dir)

            self.stdout.write(
                self.style.SUCCESS('✅ Django native restore completed successfully!')
            )

        except Exception as e:
            raise CommandError(f'❌ Restore failed: {e}')

    def find_backup_file(self, backup_dir, options):
        """Find the backup file to restore."""
        if not backup_dir.exists():
            return None

        if options['backup']:
            # Specific file
            backup_file = backup_dir / options['backup']
            if backup_file.exists():
                return backup_file
            else:
                raise CommandError(f'Backup file not found: {backup_file}')

        elif options['name']:
            # Find latest with name - look for JSON files, exclude metadata
            pattern = f"{options['name']}_*.json"
            backups = list(backup_dir.glob(pattern))
            # Filter out metadata files
            backups = [b for b in backups if not b.name.endswith('.metadata.json')]
            if backups:
                return max(backups, key=lambda p: p.stat().st_mtime)
            else:
                raise CommandError(f'No backups found with name: {options["name"]}')

        else:
            # Find latest backup - look for JSON files
            backups = list(backup_dir.glob('*.json'))
            # Filter out metadata files
            backups = [b for b in backups if not b.name.endswith('.metadata.json')]
            if backups:
                return max(backups, key=lambda p: p.stat().st_mtime)
            else:
                raise CommandError('No backup files found')

    def load_metadata(self, backup_file):
        """Load backup metadata if available."""
        metadata_path = backup_file.with_suffix('.json.metadata.json')
        if metadata_path.exists():
            try:
                with open(metadata_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                self.stdout.write(f'⚠️  Could not load metadata: {e}')
        return None

    def display_metadata(self, metadata):
        """Display backup metadata."""
        self.stdout.write('')
        self.stdout.write('📋 Backup Information:')
        self.stdout.write(f'   Created: {metadata.get("created_at", "unknown")}')
        self.stdout.write(f'   Type: {metadata.get("backup_type", "unknown")}')
        self.stdout.write(f'   Django: {metadata.get("django_version", "unknown")}')
        self.stdout.write(f'   Wagtail: {metadata.get("wagtail_version", "unknown")}')
        self.stdout.write(f'   Database: {metadata.get("database_engine", "unknown")}')

        options = metadata.get('options', {})
        if options.get('excluded'):
            self.stdout.write(f'   Excluded: {", ".join(options["excluded"])}')
        self.stdout.write('')

    def show_dry_run_info(self, backup_file, options, metadata):
        """Show what would be restored in dry-run mode."""
        self.stdout.write('')
        self.stdout.write(self.style.WARNING('🔍 DRY RUN MODE - No changes will be made'))
        self.stdout.write('')
        self.stdout.write(f'Would restore: {backup_file}')

        size_mb = backup_file.stat().st_size / (1024 * 1024)
        self.stdout.write(f'Backup size: {size_mb:.1f}MB')

        if options['flush']:
            self.stdout.write('Would flush database first (complete replacement)')
        elif options['force']:
            self.stdout.write('Would merge with existing data')
        else:
            self.stdout.write('Would check for existing data first')

        if options['include_media']:
            media_backup = self.find_media_backup(backup_file)
            if media_backup:
                self.stdout.write(f'Would restore media: {media_backup}')
            else:
                self.stdout.write('No media backup found')

        # Preview data structure
        self.preview_backup_structure(backup_file)

        self.stdout.write('')
        self.stdout.write('To actually restore, run without --dry-run')

    def preview_backup_structure(self, backup_file):
        """Preview the structure of backup data."""
        try:
            with open(backup_file, 'r') as f:
                data = json.load(f)

            if isinstance(data, list):
                models = {}
                for item in data:
                    model = item.get('model', 'unknown')
                    models[model] = models.get(model, 0) + 1

                self.stdout.write('')
                self.stdout.write('📊 Data structure:')
                for model, count in sorted(models.items()):
                    self.stdout.write(f'   {model}: {count} records')

        except Exception as e:
            self.stdout.write(f'⚠️  Could not preview data structure: {e}')

    def database_has_data(self):
        """Check if database already contains data."""
        try:
            from django.contrib.auth import get_user_model
            from wagtail.models import Page

            User = get_user_model()
            return User.objects.exists() or Page.objects.filter(depth__gt=1).exists()
        except Exception:
            return False

    def flush_database(self):
        """Flush database and run migrations to start fresh."""
        self.stdout.write('🗑️  Flushing database for fresh start...')

        try:
            # Flush database
            call_command('flush', '--noinput', verbosity=0)
            self.stdout.write('✅ Database flushed successfully')

            # Run migrations to recreate content types and permissions
            self.stdout.write('🔧 Running migrations to recreate schema...')
            call_command('migrate', '--noinput', verbosity=0)
            self.stdout.write('✅ Migrations completed')

        except Exception as e:
            raise CommandError(f'❌ Database preparation failed: {e}')

    def restore_django_backup(self, backup_file):
        """Restore Django native backup using loaddata."""
        self.stdout.write(f'📥 Restoring Django data from: {backup_file}')

        try:
            # Use Django's loaddata command
            call_command('loaddata', str(backup_file), verbosity=2)
            self.stdout.write('✅ Django data restored successfully')

        except Exception as e:
            raise CommandError(f'❌ Data restore failed: {e}')

    def find_media_backup(self, backup_file):
        """Find corresponding media backup."""
        backup_name = backup_file.stem  # Remove .json extension
        backup_dir = backup_file.parent

        # The media backup has pattern: {base_name}_media_{timestamp}
        # Extract base name without timestamp for matching
        parts = backup_name.split('_')
        if len(parts) >= 3:  # name_timestamp1_timestamp2 or name_part1_timestamp1_timestamp2
            # Try to find timestamp part and extract base name
            base_name = '_'.join(parts[:-2])  # Remove last 2 parts (date and time)
            media_pattern = f"{base_name}_media_*"
        else:
            # Fallback pattern
            media_pattern = f"*_media_*"

        media_dirs = list(backup_dir.glob(media_pattern))

        # Filter to find the one with matching timestamp
        backup_timestamp = '_'.join(parts[-2:])  # Get timestamp from backup name
        for media_dir in media_dirs:
            if backup_timestamp in media_dir.name:
                return media_dir

        # Fallback: return first match if any
        if media_dirs:
            return media_dirs[0]
        return None

    def restore_media_files(self, backup_file, backup_dir):
        """Restore media files using Django settings."""
        self.stdout.write('📁 Restoring media files...')

        media_backup = self.find_media_backup(backup_file)
        if not media_backup:
            self.stdout.write('⚠️  No media backup found')
            return

        media_root = Path(settings.MEDIA_ROOT)

        try:
            # Ensure media root exists
            media_root.mkdir(parents=True, exist_ok=True)

            # For Docker volumes, we need to be more careful about clearing files
            if media_root.exists() and any(media_root.iterdir()):
                self.stdout.write('🗑️  Clearing existing media files...')
                try:
                    # Try to remove individual files/dirs instead of the root
                    for item in media_root.iterdir():
                        if item.is_file():
                            item.unlink()
                        elif item.is_dir():
                            shutil.rmtree(item)
                except Exception as e:
                    self.stdout.write(f'⚠️  Partial clearing of media files: {e}')

            # Copy media backup contents
            for item in media_backup.iterdir():
                dest_path = media_root / item.name
                if item.is_file():
                    shutil.copy2(item, dest_path)
                elif item.is_dir():
                    # Remove destination if exists to avoid conflicts
                    if dest_path.exists():
                        shutil.rmtree(dest_path)
                    shutil.copytree(item, dest_path)

            self.stdout.write('✅ Media files restored successfully')

        except Exception as e:
            self.stdout.write(f'⚠️  Media restore failed: {e}')
            # Don't raise - media restore failure shouldn't fail the whole operation
            self.stdout.write('📝 Data restore completed successfully despite media issues')