import os
import json
from datetime import datetime
from django.core.management.base import BaseCommand
from wagtail.models import Site
from django.core.files import File
from django.core.files.images import ImageFile
from apps.projects.models import Project, ProjectImage
from wagtail.images.models import Image
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Import sample projects from jcleemann_bygMEDIA folder'

    def add_arguments(self, parser):
        parser.add_argument(
            '--media-path',
            type=str,
            default='jcleemann_bygMEDIA',
            help='Path to media folder (default: jcleemann_bygMEDIA)'
        )

    def handle(self, *args, **options):
        media_path = options['media_path']
        
        if not os.path.exists(media_path):
            self.stdout.write(
                self.style.ERROR(f'Media path {media_path} does not exist')
            )
            return

        # Get default site
        try:
            site = Site.objects.get(is_default_site=True)
        except Site.DoesNotExist:
            # Fallback to first site
            try:
                site = Site.objects.first()
                if not site:
                    raise Site.DoesNotExist("No sites found")
            except Site.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR('No Wagtail sites found. Please create a site first.')
                )
                return

        # Process each project folder
        for folder_name in os.listdir(media_path):
            folder_path = os.path.join(media_path, folder_name)
            
            if not os.path.isdir(folder_path):
                continue
                
            if folder_name.startswith('.'):
                continue
                
            self.process_project_folder(folder_path, folder_name, site)

    def process_project_folder(self, folder_path, folder_name, site):
        """Process a single project folder"""
        
        # Read caption.txt for project title/description
        caption_file = os.path.join(folder_path, 'caption.txt')
        title = folder_name  # fallback
        description = ''
        
        if os.path.exists(caption_file):
            try:
                with open(caption_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        # Use full content as description
                        description = content
                        
                        # Create a shorter, cleaner title from the content
                        first_sentence = content.split('.')[0].strip()
                        # Remove emojis and clean up
                        import re
                        clean_title = re.sub(r'[^\w\s\-åæøÅÆØ]', '', first_sentence)
                        clean_title = ' '.join(clean_title.split())  # normalize whitespace
                        
                        if len(clean_title) > 80:
                            clean_title = clean_title[:80].strip()
                            
                        if clean_title:
                            title = clean_title
                        else:
                            # Fallback: extract main action words
                            words = content.lower().split()
                            key_words = []
                            construction_words = ['trin', 'vinduer', 'døre', 'terrasse', 'køkken', 'bad', 'reparation', 'renovering', 'træ', 'byg']
                            for word in words:
                                if any(kw in word for kw in construction_words) and len(key_words) < 3:
                                    key_words.append(word)
                            if key_words:
                                title = ' '.join(key_words).title()
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Could not read caption for {folder_name}: {e}')
                )

        # Extract date from folder name (format: YYYYMMDD_HHMMSSUTC_*)
        date_str = folder_name.split('_')[0]
        try:
            project_date = datetime.strptime(date_str, '%Y%m%d').date()
        except ValueError:
            project_date = None

        # Create or get project
        slug = slugify(title)
        project, created = Project.objects.get_or_create(
            slug=slug,
            defaults={
                'site': site,
                'title': title,
                'description': description,
                'date': project_date,
                'project_type': 'haandvaerk',
                'published': True,
                'featured': False,
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created project: {title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Project already exists: {title}')
            )

        # Import images
        image_count = 0
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_path = os.path.join(folder_path, filename)
                
                # Check if image already exists
                if ProjectImage.objects.filter(
                    project=project,
                    image__title=filename
                ).exists():
                    continue

                try:
                    # Create Wagtail Image
                    with open(image_path, 'rb') as f:
                        image_file = ImageFile(f)
                        wagtail_image = Image(
                            title=filename,
                            file=image_file
                        )
                        wagtail_image.save()

                    # Create ProjectImage
                    project_image = ProjectImage(
                        project=project,
                        image=wagtail_image,
                        caption=f'{title} - Billede {image_count + 1}',
                        alt_text=f'{title} projekt billede'
                    )
                    project_image.save()
                    
                    image_count += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Could not import image {filename}: {e}')
                    )

        if image_count > 0:
            self.stdout.write(
                self.style.SUCCESS(f'  Imported {image_count} images for {title}')
            )