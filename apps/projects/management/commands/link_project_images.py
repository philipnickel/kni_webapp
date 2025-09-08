from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context
from django.db import transaction
import json
from pathlib import Path


class Command(BaseCommand):
    help = "Link ProjectImage rows in tenant schema using exported JSON (projects.json, images.json, project_images.json)."

    def add_arguments(self, parser):
        parser.add_argument('--schema', default='johann', help='Tenant schema (default: johann)')
        parser.add_argument('--export-dir', default='johann_content_export', help='Path to export JSON directory')

    def handle(self, *args, **options):
        schema = options['schema']
        export_dir = Path(options['export_dir'])

        projects_json = export_dir / 'projects.json'
        images_json = export_dir / 'images.json'
        proj_images_json = export_dir / 'project_images.json'

        if not (projects_json.exists() and images_json.exists() and proj_images_json.exists()):
            raise SystemExit(f"Missing export files in {export_dir}. Required: projects.json, images.json, project_images.json")

        with projects_json.open('r', encoding='utf-8') as f:
            projects_data = json.load(f)
        with images_json.open('r', encoding='utf-8') as f:
            images_data = json.load(f)
        with proj_images_json.open('r', encoding='utf-8') as f:
            proj_images_data = json.load(f)

        # Build lookup maps from export: old IDs -> title/slug, and old image IDs -> file path
        old_project_by_id = {}
        for obj in projects_data:
            if obj.get('model') == 'projects.project':
                fields = obj['fields']
                old_project_by_id[obj['pk']] = {
                    'title': fields.get('title'),
                    'slug': fields.get('slug'),
                }

        old_image_file_by_id = {}
        for obj in images_data:
            if obj.get('model') == 'wagtailimages.image':
                fields = obj['fields']
                old_image_file_by_id[obj['pk']] = fields.get('file')  # e.g. original_images/...

        from apps.projects.models import Project, ProjectImage
        from wagtail.images.models import Image

        created = 0
        skipped = 0

        with schema_context(schema), transaction.atomic():
            # Build in-DB lookups by slug and by title (best-effort)
            projects = list(Project.objects.all())
            projects_by_slug = {p.slug: p for p in projects}
            projects_by_title = {p.title: p for p in projects}
            # Fuzzy matcher fallback
            from difflib import SequenceMatcher
            import unicodedata
            def norm(s: str) -> str:
                s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode('ascii')
                return ' '.join(''.join(ch if ch.isalnum() else ' ' for ch in s.lower()).split())
            norm_title_to_project = {norm(p.title): p for p in projects}

            # Build image lookup by file path ending (since storage prefixes may differ)
            images = list(Image.objects.all())
            images_by_relpath = {str(img.file): img for img in images}
            images_by_basename = {Path(str(img.file)).name: img for img in images}

            for obj in proj_images_data:
                if obj.get('model') != 'projects.projectimage':
                    continue
                fields = obj['fields']
                old_proj_id = fields.get('project')
                old_img_id = fields.get('image')

                old_proj = old_project_by_id.get(old_proj_id)
                img_rel = old_image_file_by_id.get(old_img_id)  # may be None
                if not old_proj or not img_rel:
                    skipped += 1
                    continue

                # Resolve project
                proj = projects_by_slug.get(old_proj['slug']) or projects_by_title.get(old_proj['title'])
                if not proj:
                    # Fuzzy by normalized title
                    target = norm(old_proj['title'])
                    best = None
                    best_ratio = 0.0
                    for nt, p in norm_title_to_project.items():
                        r = SequenceMatcher(None, target, nt).ratio()
                        if r > best_ratio:
                            best_ratio, best = r, p
                    if best_ratio >= 0.6:
                        proj = best
                if not proj:
                    skipped += 1
                    continue

                # Resolve image
                img = images_by_relpath.get(img_rel)
                if not img:
                    # Try by basename match
                    img = images_by_basename.get(Path(img_rel).name)
                if not img:
                    skipped += 1
                    continue

                # Create ProjectImage if not already linked
                exists = ProjectImage.objects.filter(project=proj, image=img).exists()
                if not exists:
                    ProjectImage.objects.create(project=proj, image=img, caption=fields.get('caption',''), alt_text=fields.get('alt_text',''))
                    created += 1

        self.stdout.write(self.style.SUCCESS(f"Linked project images: created={created}, skipped={skipped}"))
