import os
import re
from datetime import date
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.core.files.images import ImageFile
from wagtail.images.models import Image
from apps.projects.models import Project, ProjectImage


class Command(BaseCommand):
    help = "Import stock projects from baselineData/media/original_images as Project instances (not ProjectPage)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="baselineData/media/original_images",
            help="Path to the folder containing stock project images (default: baselineData/media/original_images)"
        )

    def handle(self, *args, **options):
        images_dir = options['path']
        
        if not os.path.exists(images_dir):
            self.stdout.write(self.style.ERROR(f"Images directory '{images_dir}' does not exist."))
            return

        # Group images by project name (e.g., carpenter1, carpenter2, carpenter3 → "Carpenter Project")
        project_groups = {}
        for filename in sorted(os.listdir(images_dir)):
            if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                continue

            base_name = os.path.splitext(filename)[0]
            project_key = re.sub(r'\d+$', '', base_name).lower()  # Remove trailing digits
            if not project_key:
                project_key = base_name.lower()

            if project_key not in project_groups:
                project_groups[project_key] = []
            project_groups[project_key].append(filename)

        created_projects = 0
        for project_key, filenames in project_groups.items():
            title = project_key.replace("_", " ").replace("-", " ").title() + " Project"
            slug = slugify(title)

            # Check if Project already exists
            existing_project = Project.objects.filter(slug=slug).first()
            if existing_project:
                project = existing_project
                proj_created = False
                self.stdout.write(self.style.WARNING(f"Project already exists: {project.title}"))
            else:
                project = Project(
                    title=title,
                    slug=slug,
                    description=f"Professional {project_key.replace('_', ' ')} work showcasing quality craftsmanship and attention to detail.",
                    date=date.today(),
                    featured=False,
                    published=True,
                    location="Stock Location",
                    materials=f"High-quality materials for {project_key.replace('_', ' ')} work",
                )
                project.save()
                created_projects += 1
                proj_created = True
                self.stdout.write(self.style.SUCCESS(f"Created project: {project.title}"))

            # Add all images for this project
            for filename in filenames:
                image_path = os.path.join(images_dir, filename)
                
                # Check if this image is already attached to this project
                if ProjectImage.objects.filter(project=project, image__title=filename).exists():
                    continue

                try:
                    with open(image_path, "rb") as f:
                        wag_img, img_created = Image.objects.get_or_create(
                            title=filename,
                            defaults={'file': ImageFile(f)}
                        )
                        if not img_created:
                            self.stdout.write(self.style.WARNING(f"  Image '{filename}' already exists in Wagtail."))

                    ProjectImage.objects.create(
                        project=project,
                        image=wag_img,
                        caption=f"{project.title} - {filename}",
                        alt_text=f"{project.title} project image",
                    )
                    self.stdout.write(self.style.SUCCESS(f"  Added image: {filename}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  Failed to add image {filename}: {e}"))

        if created_projects == 0:
            self.stdout.write(self.style.WARNING("No new projects created (they may already exist)."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Imported {created_projects} stock projects."))
