"""
Management command to create tenant schema with all tables
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django_tenants.utils import schema_context

from apps.tenants.models import Client


class Command(BaseCommand):
    help = 'Create tenant schema with all necessary tables'

    def add_arguments(self, parser):
        parser.add_argument('schema_name', type=str, help='The tenant schema name to create')

    def handle(self, *args, **options):
        schema_name = options['schema_name']

        try:
            # Get the tenant
            client = Client.objects.get(schema_name=schema_name)
        except Client.DoesNotExist:
            raise CommandError(f'Tenant with schema "{schema_name}" does not exist')

        self.stdout.write(f'Creating schema for tenant: {client.name} (schema: {schema_name})')

        try:
            # Create the schema
            with connection.cursor() as cursor:
                cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {schema_name}')
                self.stdout.write(f'Created schema: {schema_name}')

            # Run migrations for the tenant schema
            with schema_context(schema_name):
                from django.core.management import call_command
                call_command('migrate', verbosity=1, interactive=False)
                self.stdout.write(f'Applied migrations to schema: {schema_name}')

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created schema for "{client.name}"'
                )
            )
                
        except Exception as e:
            raise CommandError(f'Error creating schema: {e}')