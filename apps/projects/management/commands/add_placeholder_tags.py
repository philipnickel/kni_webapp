from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context


class Command(BaseCommand):
    help = "Add placeholder tags to projects in a tenant schema so tag UI can be previewed."

    def add_arguments(self, parser):
        parser.add_argument('--schema', default='johann', help='Tenant schema (default: johann)')
        parser.add_argument('--force', action='store_true', help='Add tags even if a project already has tags')

    def handle(self, *args, **options):
        schema = options['schema']
        force = options['force']

        from apps.projects.models import Project

        sample_tags = [
            'Træ', 'Renovering', 'Nybyggeri', 'Tilbygning', 'Håndværk',
            'Vinduer', 'Køkken', 'Badeværelse', 'Facade', 'Gulv'
        ]

        added = 0
        total = 0
        with schema_context(schema):
            projects = Project.objects.all().order_by('id')
            for i, p in enumerate(projects):
                total += 1
                if p.tags.exists() and not force:
                    continue
                # assign 2-3 tags in a round-robin fashion
                chosen = [sample_tags[i % len(sample_tags)], sample_tags[(i+3) % len(sample_tags)]]
                # add a third occasionally
                if i % 2 == 0:
                    chosen.append(sample_tags[(i+6) % len(sample_tags)])
                p.tags.set(chosen)
                p.save()
                added += 1

        self.stdout.write(self.style.SUCCESS(
            f"Processed {total} projects; set placeholder tags for {added} of them"
        ))

