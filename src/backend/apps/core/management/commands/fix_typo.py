from django.core.management.base import BaseCommand
from apps.pages.models import HomePage
import json


class Command(BaseCommand):
    help = 'Fix "servicesaa" typo in homepage content'

    def handle(self, *args, **options):
        try:
            homepage = HomePage.objects.first()
            if not homepage:
                self.stdout.write(self.style.ERROR('No HomePage found'))
                return

            # Work directly with raw JSON data
            if hasattr(homepage, 'body') and hasattr(homepage.body, 'stream_data'):
                body_data = homepage.body.stream_data
            else:
                self.stdout.write(self.style.ERROR('Homepage body structure not found'))
                return

            fixed = False
            for block in body_data:
                if block.get('type') == 'services_grid_inline':
                    value = block.get('value', {})
                    if value.get('heading') == 'Vores servicesaa':
                        value['heading'] = 'Vores services'
                        fixed = True
                        self.stdout.write(
                            self.style.SUCCESS('Fixed typo: "servicesaa" → "services"')
                        )
                        break

            if fixed:
                # Force save and publish
                revision = homepage.save_revision()
                revision.publish()
                self.stdout.write(
                    self.style.SUCCESS('Successfully published homepage with fixed typo')
                )
            else:
                # Direct database approach
                self.stdout.write(self.style.WARNING('Trying direct database fix...'))
                from django.db import connection

                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE pages_homepage
                        SET body = REPLACE(body::text, '"Vores servicesaa"', '"Vores services"')::jsonb
                        WHERE body::text LIKE '%servicesaa%'
                    """)
                    if cursor.rowcount > 0:
                        self.stdout.write(self.style.SUCCESS(f'Fixed {cursor.rowcount} homepage(s) via database'))

                        # Update latest revision too
                        cursor.execute("""
                            UPDATE wagtailcore_revision
                            SET content_json = REPLACE(content_json, '"Vores servicesaa"', '"Vores services"')
                            WHERE content_json LIKE '%servicesaa%'
                        """)
                        self.stdout.write(self.style.SUCCESS(f'Fixed {cursor.rowcount} revision(s) via database'))
                    else:
                        self.stdout.write(self.style.WARNING('No "servicesaa" typo found'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))