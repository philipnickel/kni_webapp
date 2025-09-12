import os
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from wagtail.images.models import Image
from wagtail.models import Site
from apps.pages.models import SiteSettings


class Command(BaseCommand):
    help = "Set a stock company logo from stock_media/project_images/alternativeHand1.jpg (or first available)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="baselineData/media/original_images",
            help="Directory to search for a stock logo image",
        )

    def handle(self, *args, **options):
        directory = options["path"]
        if not os.path.isdir(directory):
            self.stdout.write(self.style.ERROR(f"Directory not found: {directory}"))
            return

        preferred = [
            "alternativeHand1.jpg",
            "carpenter1.jpg",
            "carpenter2.jpg",
            "carpenter3.png",
            "handwork1.jpg",
            "roof1.jpg",
            "woodworking1.jpg",
        ]

        logo_path = None
        for name in preferred:
            candidate = os.path.join(directory, name)
            if os.path.isfile(candidate):
                logo_path = candidate
                break

        if not logo_path:
            # fallback: first image in directory
            for fn in os.listdir(directory):
                if fn.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                    logo_path = os.path.join(directory, fn)
                    break

        if not logo_path:
            self.stdout.write(self.style.ERROR("No image files found for logo."))
            return

        with open(logo_path, "rb") as f:
            img = Image(title=os.path.basename(logo_path), file=ImageFile(f))
            img.save()

        # Update default SiteSettings (use default site)
        site = Site.objects.filter(is_default_site=True).first() or Site.objects.first()
        if not site:
            self.stdout.write(self.style.ERROR("No Wagtail Site found. Create a site first."))
            return
        settings = SiteSettings.for_site(site)
        settings.logo = img
        if not settings.company_name:
            settings.company_name = "Company"
        settings.save()

        self.stdout.write(self.style.SUCCESS(f"Set stock logo: {os.path.basename(logo_path)}"))


