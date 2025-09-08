from django.core.management.base import BaseCommand
from django.utils.text import slugify
from wagtail.models import Page, Site
from apps.pages.models import ModularPage, Testimonial, Logo, Service


class Command(BaseCommand):
    help = "Seed demo modular page with components and sample snippets"

    def handle(self, *args, **options):
        site = Site.objects.get(is_default_site=True)
        root = site.root_page

        # Find a HomePage to attach under, else root
        parent = root

        # Create sample snippets if none
        if not Testimonial.objects.exists():
            Testimonial.objects.create(name="Anders Jensen", role="Boligejer", quote="Fantastisk samarbejde og flot håndværk – kan varmt anbefales!")
            Testimonial.objects.create(name="Mette Sørensen", role="Virksomhedsejer", quote="Professionelt arbejde leveret til tiden og i topkvalitet.")

        if not Service.objects.exists():
            Service.objects.create(title="Nybyggeri i træ", description="Fra fundament til nøglefærdig bolig i naturlige materialer.")
            Service.objects.create(title="Renovering", description="Opdatering og restaurering af eksisterende træbyggeri.")
            Service.objects.create(title="Tilbygninger", description="Udvid hjemmet med harmoniske træløsninger.")

        if not Logo.objects.exists():
            Logo.objects.create(title="Kunde A")
            Logo.objects.create(title="Kunde B")
            Logo.objects.create(title="Kunde C")
            Logo.objects.create(title="Kunde D")

        # Create or update demo modular page
        slug = "demo"
        existing = parent.get_children().filter(slug=slug).specific().first()
        if existing and isinstance(existing, ModularPage):
            page = existing
            created = False
        else:
            page = ModularPage(title="Demo modul side", slug=slug)
            parent.add_child(instance=page)
            page.save_revision().publish()
            created = True

        # Compose simple body if empty
        if not page.body:
            from wagtail.images.models import Image
            page.body = [
                ("hero_v2", {
                    "heading": "Velkommen til JCleemann Byg",
                    "subheading": "Kvalitets træbyggeri med omtanke",
                    "primary_text": "Få et tilbud",
                    "primary_url": "/fa-tilbud/",
                    "secondary_text": "Se projekter",
                    "secondary_url": "/projekter/",
                    "style": {"background": "hero", "spacing": "lg", "container": "wide"}
                }),
                ("services_grid", {
                    "heading": "Vores services",
                    "columns": "3",
                    "services": [s for s in Service.objects.all()[:3]],
                    "style": {"background": "surface", "spacing": "md", "container": "wide"}
                }),
                ("testimonials_snippets", {
                    "testimonials": [t for t in Testimonial.objects.all()[:2]],
                    "style": {"background": "surface-soft", "spacing": "md", "container": "normal"}
                }),
                ("logo_cloud", {
                    "logos": [l for l in Logo.objects.all()[:4]],
                    "style": {"background": "surface", "spacing": "md", "container": "wide"}
                }),
                ("cta", {
                    "title": "Klar til at starte dit projekt?",
                    "text": "Kontakt os i dag for et uforpligtende tilbud.",
                    "button_text": "Kontakt os",
                    "button_url": "/fa-tilbud/",
                    "style": {"background": "hero", "spacing": "md", "container": "narrow"}
                })
            ]
            page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS(f"Demo page {'created' if created else 'updated'} at /{slug}/"))
