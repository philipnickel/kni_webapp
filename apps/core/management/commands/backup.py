#!/usr/bin/env python3
"""
Django Management Command: backup

Creates Django-native backups using dumpdata with natural keys.
Replaces the old PostgreSQL-specific backup system.
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = """
    Create Django-native backups using dumpdata.

    Usage Examples:
    # Create regular backup
    python manage.py backup --include-media

    # Create named backup
    python manage.py backup --name my_backup --include-media

    This command uses Django's native dumpdata for database-agnostic backups.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='Name for the backup (default: timestamp)'
        )

        parser.add_argument(
            '--include-media',
            action='store_true',
            help='Include media files in backup'
        )

        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be backed up without creating backup'
        )

    def handle(self, *args, **options):
        # Redirect to the native backup system
        cmd_args = ['native_backup']

        if options.get('name'):
            cmd_args.extend(['--name', options['name']])

        if options.get('include_media'):
            cmd_args.append('--include-media')

        if options.get('dry_run'):
            cmd_args.append('--dry-run')

        call_command(*cmd_args)