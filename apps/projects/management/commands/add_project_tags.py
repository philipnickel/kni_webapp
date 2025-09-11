from django.core.management.base import BaseCommand
from apps.projects.models import ProjectPage
from taggit.models import Tag


class Command(BaseCommand):
    help = 'Add appropriate tags to existing ProjectPage instances'

    def handle(self, *args, **options):
        # Define tag mappings based on project titles and materials
        tag_mappings = {
            'Træ terrasse og udendørs køkken': ['udendoers', 'terrasse', 'koekken', 'traeterre'],
            'Villa renovering i København': ['renovering', 'villa', 'historisk', 'koebenhavn'],
            'Skræddersyet køkken installation': ['koekken', 'skreddersyet', 'installation'],
            'Badeværelse renovering': ['badevaerelse', 'renovering', 'luksurios'],
            'Moderne kontorbygning': ['kontor', 'moderne', 'erhverv', 'baeredygtig']
        }

        projects_updated = 0
        
        for project in ProjectPage.objects.all():
            if project.title in tag_mappings:
                tags_to_add = tag_mappings[project.title]
                
                # Clear existing tags first
                project.tags.clear()
                
                # Add new tags
                for tag_name in tags_to_add:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    project.tags.add(tag)
                    if created:
                        self.stdout.write(f'Created new tag: {tag_name}')
                
                project.save()
                projects_updated += 1
                self.stdout.write(f'Updated tags for: {project.title} - Tags: {", ".join(tags_to_add)}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated tags for {projects_updated} projects')
        )