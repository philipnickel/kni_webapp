#!/usr/bin/env python3
"""
Django Management Command: restore

Restores Django-native backups using loaddata.
Replaces the old PostgreSQL-specific restore system.
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = """
    Restore Django-native backups using loaddata.

    Usage Examples:
    # Restore specific backup
    python manage.py restore --backup my_backup_20240915_123456.json

    # Restore latest backup with name
    python manage.py restore --name baseline

    # Include media files and flush database
    python manage.py restore --name baseline --include-media --flush

    This command uses Django's native loaddata for database-agnostic restores.
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
            '--force',
            action='store_true',
            help='Force restore even if data exists'
        )

        parser.add_argument(
            '--flush',
            action='store_true',
            help='Flush database before restore (recommended for clean restore)'
        )

    def handle(self, *args, **options):
        # Redirect to the native restore system
        cmd_args = ['native_restore']

        if options.get('backup'):
            cmd_args.extend(['--backup', options['backup']])

        if options.get('name'):
            cmd_args.extend(['--name', options['name']])

        if options.get('include_media'):
            cmd_args.append('--include-media')

        if options.get('dry_run'):
            cmd_args.append('--dry-run')

        if options.get('force'):
            cmd_args.append('--force')

        if options.get('flush'):
            cmd_args.append('--flush')

        call_command(*cmd_args)