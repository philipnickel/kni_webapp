"""Management command to import baseline content via wagtail-transfer"""
import json
from collections import defaultdict

import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from wagtail.models import Page, Site

from wagtail_transfer.auth import digest_for_source
from wagtail_transfer.operations import ImportPlanner


class Command(BaseCommand):
    help = "Import the baseline content tree from a configured wagtail-transfer source"

    def add_arguments(self, parser):
        parser.add_argument(
            "--source",
            help="Name of the wagtail-transfer source to import from (defaults to BASELINE_SOURCE env)",
        )
        parser.add_argument(
            "--root",
            dest="root_page_id",
            type=int,
            help="ID of the root page (on the source site) to import",
        )
        parser.add_argument(
            "--destination-parent",
            dest="destination_parent_id",
            type=int,
            help="Optional ID of the parent page to import into locally",
        )
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete the existing default site's page tree before importing",
        )
        parser.add_argument(
            "--timeout",
            type=float,
            default=float(settings.BASELINE_TRANSFER_TIMEOUT),
            help="HTTP timeout in seconds when talking to the source (default: %(default)s)",
        )

    def handle(self, *args, **options):
        source_name = options["source"] or getattr(settings, "BASELINE_SOURCE", None)
        if not source_name:
            raise CommandError("No baseline source configured. Set BASELINE_SOURCE env var or use --source.")

        try:
            root_page_id = options["root_page_id"] or settings.BASELINE_ROOT_PAGE_ID
        except AttributeError as exc:
            raise CommandError("BASELINE_ROOT_PAGE_ID must be configured or provided via --root") from exc

        if not root_page_id:
            raise CommandError("A root page ID is required; set BASELINE_ROOT_PAGE_ID or pass --root.")

        sources_config = getattr(settings, "WAGTAILTRANSFER_SOURCES", {})
        source_config = sources_config.get(source_name)
        if not source_config:
            raise CommandError(f"Unknown wagtail-transfer source '{source_name}'. Check WAGTAILTRANSFER_SOURCES.")

        base_url = source_config.get("BASE_URL")
        if not base_url:
            raise CommandError(f"Source '{source_name}' is missing BASE_URL in WAGTAILTRANSFER_SOURCES.")

        timeout = options["timeout"]
        destination_parent_id = options.get("destination_parent_id")

        if destination_parent_id is None:
            destination_parent_id = self._default_destination_parent()
            if destination_parent_id is None:
                raise CommandError("Unable to determine destination parent page. Use --destination-parent explicitly.")

        if options["flush"]:
            self._flush_existing_tree()

        self.stdout.write(self.style.SUCCESS(f"🌐 Importing baseline from '{source_name}' (page {root_page_id})"))

        try:
            importer = self._fetch_root_page(source_name, base_url, root_page_id, destination_parent_id, timeout)
            importer = self._import_missing(source_name, base_url, importer, timeout)
        except requests.RequestException as exc:
            raise CommandError(f"HTTP error communicating with source '{source_name}': {exc}") from exc

        with transaction.atomic():
            importer.run()
            self._update_site_root(root_page_id, importer)

        created = len([op for op in importer.operations if op.__class__.__name__.startswith("Create")])
        updated = len([op for op in importer.operations if op.__class__.__name__.startswith("Update")])
        self.stdout.write(self.style.SUCCESS(f"✅ Baseline import complete (created {created}, updated {updated})"))

    def _fetch_root_page(self, source_name, base_url, root_page_id, destination_parent_id, timeout):
        digest = digest_for_source(source_name, str(root_page_id))
        response = requests.get(
            f"{base_url}api/pages/{root_page_id}/",
            params={"digest": digest},
            timeout=timeout,
        )
        response.raise_for_status()

        importer = ImportPlanner.for_page(source=root_page_id, destination=destination_parent_id)
        importer.add_json(response.content)
        return importer

    def _import_missing(self, source_name, base_url, importer, timeout):
        while importer.missing_object_data:
            missing_object_data_by_type = defaultdict(list)
            for model_class, source_id in importer.missing_object_data:
                missing_object_data_by_type[model_class].append(source_id)

            request_data = json.dumps({
                model_class._meta.label_lower: ids
                for model_class, ids in missing_object_data_by_type.items()
            })
            digest = digest_for_source(source_name, request_data)

            response = requests.post(
                f"{base_url}api/objects/",
                params={"digest": digest},
                data=request_data,
                timeout=timeout,
            )
            response.raise_for_status()
            importer.add_json(response.content)

        return importer

    def _default_destination_parent(self):
        site = Site.objects.filter(is_default_site=True).first()
        if site and site.root_page:
            parent = site.root_page.get_parent()
            return parent.id if parent else site.root_page.id

        root = Page.get_first_root_node()
        return root.id if root else None

    def _flush_existing_tree(self):
        site = Site.objects.filter(is_default_site=True).first()
        if not site or not site.root_page:
            self.stdout.write(self.style.WARNING("⚠️ No default site configured; skipping flush."))
            return

        root_page = site.root_page.specific
        descendants = list(root_page.get_children())
        if not descendants:
            self.stdout.write("ℹ️  No existing pages to remove before import.")
            return

        self.stdout.write("🧹 Removing existing pages under the site root before import...")
        for page in descendants:
            self.stdout.write(f" - Deleting '{page.title}' (id {page.id})")
            page.delete()

    def _update_site_root(self, source_root_id, importer):
        site = Site.objects.filter(is_default_site=True).first()
        if not site:
            return

        key = (Page, int(source_root_id))
        destination_id = importer.context.destination_ids_by_source.get(key)
        if not destination_id:
            return

        if site.root_page_id != destination_id:
            site.root_page_id = destination_id
            site.save(update_fields=["root_page"])
            self.stdout.write(self.style.SUCCESS(
                f"🏠 Default site root page updated to imported page ID {destination_id}"
            ))
