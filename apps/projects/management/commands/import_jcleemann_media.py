import json
import os
from pathlib import Path
from datetime import datetime
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from wagtail.images import get_image_model
from wagtail.models import Page, Site

from apps.pages.models import GalleryPage
from apps.projects.models import ProjectPage, ProjectPageImage


class Command(BaseCommand):
    help = "Import projects from jcleemann_bygMEDIA into Wagtail ProjectPages"

    def add_arguments(self, parser):
        parser.add_argument(
            "--root",
            default=str(Path.cwd() / "jcleemann_bygMEDIA"),
            help="Path to jcleemann_bygMEDIA folder",
        )
        parser.add_argument(
            "--parent",
            default="Galleri",
            help="Title of GalleryPage to import under (created if missing)",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        root = Path(options["root"]).resolve()
        if not root.exists():
            raise CommandError(f"Root folder not found: {root}")

        site = Site.objects.get(is_default_site=True)
        home_page = site.root_page.specific

        # Ensure a GalleryPage exists under home
        gallery_page = (
            GalleryPage.objects.child_of(home_page).filter(title=options["parent"]).first()
        )
        if not gallery_page:
            gallery_page = GalleryPage(title=options["parent"])  # type: ignore
            home_page.add_child(instance=gallery_page)
            gallery_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f"Created GalleryPage: {gallery_page.title}"))

        ImageModel = get_image_model()

        created = 0
        for subdir in sorted(root.iterdir()):
            if not subdir.is_dir():
                continue

            # Defaults
            title = subdir.name
            description_rich = ""
            tags_list: list[str] = []
            location_val = ""
            featured_val = False
            project_date_val = None

            # caption.txt: first line as title, rest as description
            caption_txt = subdir / "caption.txt"
            if caption_txt.exists():
                try:
                    lines = caption_txt.read_text(encoding="utf-8").strip().splitlines()
                    if lines:
                        title = (lines[0] or title)[:250]
                        if len(lines) > 1:
                            description_rich = "\n".join(lines[1:])
                except Exception:
                    pass

            # Optional JSON metadata
            meta_json = None
            for p in subdir.glob("*.json"):
                meta_json = p
                break
            if meta_json and meta_json.exists():
                try:
                    data = json.loads(meta_json.read_text(encoding="utf-8"))
                    # common fields
                    tags_list = list({t.strip() for t in data.get("tags", []) if isinstance(t, str) and t.strip()})
                    location_val = data.get("location", "")[:255]
                    featured_val = bool(data.get("featured", False))
                    # try multiple date keys
                    date_str = data.get("date") or data.get("project_date") or data.get("created_at")
                    if date_str:
                        try:
                            project_date_val = datetime.fromisoformat(date_str.replace("Z", "+00:00")).date()
                        except Exception:
                            project_date_val = None
                except Exception:
                    pass

            # Upsert by slug (derived from title)
            from django.utils.text import slugify
            slug = slugify(title)[:255]
            project = ProjectPage.objects.child_of(gallery_page).filter(slug=slug).first()
            is_new = False
            if not project:
                project = ProjectPage(title=title)  # type: ignore
                gallery_page.add_child(instance=project)
                is_new = True

            # Assign fields
            project.title = title
            if description_rich:
                project.description = description_rich
            if location_val:
                project.location = location_val
            project.featured = featured_val
            if project_date_val:
                project.project_date = project_date_val

            # Save and publish
            project.save()
            project.save_revision().publish()

            # Tags
            if tags_list:
                project.tags.set(tags_list)
                project.save()

            # Attach images (jpg/jpeg/png)
            for img_path in sorted(subdir.glob("*.jpg")) + sorted(subdir.glob("*.jpeg")) + sorted(subdir.glob("*.png")):
                with img_path.open("rb") as f:
                    image = ImageModel(title=img_path.stem)
                    image.file.save(img_path.name, File(f), save=True)
                # Avoid duplicate attachments of same filename
                if not project.project_images.filter(image__title=img_path.stem).exists():
                    ProjectPageImage.objects.create(project_page=project, image=image)
            if is_new:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {created} projects into '{gallery_page.title}'."))


