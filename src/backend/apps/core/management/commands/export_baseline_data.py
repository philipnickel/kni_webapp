"""
Django management command to export baseline data
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core import serializers
from wagtail.models import Site, Page
import json
import os


class Command(BaseCommand):
    help = 'Export baseline data to fixtures'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output-dir',
            type=str,
            default='backups',
            help='Directory to save baseline data fixtures',
        )

    def handle(self, *args, **options):
        output_dir = options.get('output_dir', 'backups')
        os.makedirs(output_dir, exist_ok=True)

        self.stdout.write(self.style.SUCCESS('📦 Exporting baseline data...'))

        try:
            # Export core Wagtail data
            fixtures = {
                'sites': Site.objects.all(),
                'pages': Page.objects.filter(depth__lte=3),  # Root, home, and first level pages
            }

            for fixture_name, queryset in fixtures.items():
                if queryset.exists():
                    fixture_file = os.path.join(output_dir, f'{fixture_name}_baseline.json')

                    with open(fixture_file, 'w') as f:
                        serialized_data = serializers.serialize('json', queryset, indent=2)
                        f.write(serialized_data)

                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Exported {queryset.count()} {fixture_name} to {fixture_file}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'⚠️ No {fixture_name} data to export')
                    )

            self.stdout.write(
                self.style.SUCCESS('🎉 Baseline data export completed!')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error exporting baseline data: {e}')
            )
            raise