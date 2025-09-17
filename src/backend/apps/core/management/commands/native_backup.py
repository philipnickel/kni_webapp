#!/usr/bin/env python3
"""
Django Management Command: native_backup

Django/Wagtail native backup system using Django's built-in dumpdata.
This is the proper Django way to backup data - no PostgreSQL dependencies.
"""

import os
import datetime
import json
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
import subprocess
import shutil


class Command(BaseCommand):
    help = """
    Create database backups using Django's native dumpdata command.
    This is the proper Django way - works with any database backend.

    Usage Examples:
    # Create regular backup
    python manage.py native_backup

    # Create named backup (e.g., baseline)
    python manage.py native_backup --name baseline

    # Include media files
    python manage.py native_backup --name baseline --include-media

    # Exclude specific apps/models
    python manage.py native_backup --exclude auth.logentry --exclude sessions
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            type=str,
            help='Custom name for the backup (e.g., "baseline", "before-update")'
        )

        parser.add_argument(
            '--include-media',
            action='store_true',
            help='Include media files in backup'
        )

        parser.add_argument(
            '--exclude',
            action='append',
            default=[],
            help='Exclude specific app.model (can be used multiple times)'
        )

        parser.add_argument(
            '--natural-foreign',
            action='store_true',
            default=True,
            help='Use natural foreign keys (default: True)'
        )

        parser.add_argument(
            '--natural-primary',
            action='store_true',
            default=True,
            help='Use natural primary keys (default: True)'
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('💾 Django Native Backup System')
        )
        self.stdout.write('=' * 40)

        # Setup backup directory
        backup_dir = Path('backups')
        backup_dir.mkdir(exist_ok=True)

        # Remove old files if creating named backup (e.g., baseline)
        if options['name']:
            self.remove_old_named_backups(backup_dir, options['name'])

        # Generate filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        if options['name']:
            filename = f"{options['name']}_{timestamp}.json"
        else:
            filename = f"backup_{timestamp}.json"

        backup_path = backup_dir / filename

        # Create database backup using Django's dumpdata
        self.create_django_backup(backup_path, options)

        # Include media if requested
        if options['include_media']:
            self.backup_media(backup_dir, options['name'], timestamp)

        # Create metadata file
        self.create_metadata(backup_path, options)

        self.stdout.write(
            self.style.SUCCESS(f'✅ Django native backup completed: {backup_path}')
        )

    def create_django_backup(self, backup_path, options):
        """Create Django native backup using dumpdata."""
        self.stdout.write('📦 Creating Django native backup...')

        try:
            # Build dumpdata command arguments
            dumpdata_args = [
                '--format=json',
                '--indent=2',
                '--output', str(backup_path)
            ]

            # Add natural key options
            if options['natural_foreign']:
                dumpdata_args.append('--natural-foreign')

            if options['natural_primary']:
                dumpdata_args.append('--natural-primary')

            # Add exclusions - skip problematic models by default
            default_exclusions = [
                'auth.permission',      # Django permissions (auto-generated)
                'contenttypes.contenttype',  # Django content types (auto-generated)
                'sessions.session',     # Session data (temporary)
                'admin.logentry',       # Admin log entries (non-essential)
                'wagtailcore.modellogentry',  # Wagtail model log entries (causes content type issues)
                'wagtailsearch.indexentry',   # Search index entries (auto-regenerated)
            ]

            # Ensure we include critical site configuration
            # wagtailcore.site is included automatically and contains site root configuration

            all_exclusions = default_exclusions + options['exclude']

            for exclusion in all_exclusions:
                dumpdata_args.extend(['--exclude', exclusion])

            # Run Django's dumpdata command
            call_command('dumpdata', *dumpdata_args)

            self.stdout.write('✅ Django native backup created successfully')

        except Exception as e:
            raise CommandError(f"❌ Backup failed: {e}")

    def backup_media(self, backup_dir, backup_name, timestamp):
        """Backup media files using Django settings."""
        self.stdout.write('📁 Backing up media files...')

        media_root = Path(settings.MEDIA_ROOT)
        if not media_root.exists():
            self.stdout.write('ℹ️  No media directory found')
            return

        # Create media backup
        if backup_name:
            media_backup_name = f"{backup_name}_media_{timestamp}"
        else:
            media_backup_name = f"backup_media_{timestamp}"

        media_backup_path = backup_dir / media_backup_name

        try:
            # Use shutil.copytree for cross-platform compatibility
            shutil.copytree(media_root, media_backup_path, dirs_exist_ok=True)
            self.stdout.write(f'✅ Media backed up to: {media_backup_path}')

        except Exception as e:
            self.stdout.write(f'⚠️  Media backup failed: {e}')

    def create_metadata(self, backup_path, options):
        """Create metadata file with backup information."""
        metadata_path = backup_path.with_suffix('.metadata.json')

        metadata = {
            'created_at': datetime.datetime.now().isoformat(),
            'backup_type': 'django_native',
            'django_version': self.get_django_version(),
            'wagtail_version': self.get_wagtail_version(),
            'database_engine': self.get_database_engine(),
            'options': {
                'natural_foreign': options['natural_foreign'],
                'natural_primary': options['natural_primary'],
                'excluded': options['exclude'],
                'include_media': options['include_media']
            }
        }

        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)

        self.stdout.write(f'📋 Metadata saved to: {metadata_path}')

    def get_django_version(self):
        """Get Django version."""
        try:
            import django
            return django.get_version()
        except ImportError:
            return 'unknown'

    def get_wagtail_version(self):
        """Get Wagtail version."""
        try:
            import wagtail
            return wagtail.__version__
        except ImportError:
            return 'unknown'

    def get_database_engine(self):
        """Get database engine from Django settings."""
        try:
            return settings.DATABASES['default']['ENGINE']
        except (KeyError, AttributeError):
            return 'unknown'

    def remove_old_named_backups(self, backup_dir, name):
        """Remove old backup files with the same name."""
        pattern = f"{name}_*.json"
        media_pattern = f"{name}_media_*"
        metadata_pattern = f"{name}_*.metadata.json"

        # Remove old JSON backup files
        old_files = list(backup_dir.glob(pattern))
        for old_file in old_files:
            try:
                old_file.unlink()
                self.stdout.write(f'🗑️  Removed old backup: {old_file.name}')
            except OSError as e:
                self.stdout.write(f'⚠️  Could not remove {old_file.name}: {e}')

        # Remove old media directories
        old_media_dirs = [d for d in backup_dir.iterdir() if d.is_dir() and d.name.startswith(f"{name}_media_")]
        for old_dir in old_media_dirs:
            try:
                shutil.rmtree(old_dir)
                self.stdout.write(f'🗑️  Removed old media: {old_dir.name}')
            except OSError as e:
                self.stdout.write(f'⚠️  Could not remove {old_dir.name}: {e}')

        # Remove old metadata files
        old_metadata = list(backup_dir.glob(metadata_pattern))
        for old_file in old_metadata:
            try:
                old_file.unlink()
                self.stdout.write(f'🗑️  Removed old metadata: {old_file.name}')
            except OSError as e:
                self.stdout.write(f'⚠️  Could not remove {old_file.name}: {e}')
