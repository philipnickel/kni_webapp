from django.core.management.base import BaseCommand
from wagtail.models import Site
from apps.pages.models import HomePage, Service, Testimonial


class Command(BaseCommand):
    help = "Setup homepage with Frostbite-styled content"

    def handle(self, *args, **options):
        site = Site.objects.get(is_default_site=True)
        root = site.root_page

        # Get or create home page
        home_page = HomePage.objects.filter(live=True).first()
        if not home_page:
            home_page = HomePage(title="Home", slug="home")
            root.add_child(instance=home_page)
            home_page.save_revision().publish()

        # Create sample snippets if none exist
        if not Service.objects.exists():
            Service.objects.create(
                title="Køkkenrenovering", 
                description="Totalrenovering af køkkener med skræddersyede løsninger, kvalitetsmaterialer og moderne design"
            )
            Service.objects.create(
                title="Badeværelse", 
                description="Komplet renovering af badeværelser med moderne installationer og stilfuld design"
            )
            Service.objects.create(
                title="Nybyggeri", 
                description="Fra fundament til nøglefærdig bolig - vi leverer håndværk af højeste kvalitet"
            )

        if not Testimonial.objects.exists():
            Testimonial.objects.create(
                name="Anders Jensen", 
                role="Boligejer", 
                quote="Fantastisk samarbejde og flot håndværk – kan varmt anbefales!"
            )
            Testimonial.objects.create(
                name="Mette Sørensen", 
                role="Virksomhedsejer", 
                quote="Professionelt arbejde leveret til tiden og i topkvalitet."
            )

        # Add Frostbite-styled content to home page
        if not home_page.body:
            home_page.body = [
                ("hero", {
                    "heading": "Professionelle byggeløsninger i København og omegn",
                    "subheading": "Fra køkkenrenovering til komplette nybyggerier - vi leverer håndværk af højeste kvalitet med fokus på kundetilfredshed og termintro fastholding.",
                    "cta_text": "Få et uforpligtende tilbud",
                    "cta_anchor": "contact"
                }),
                ("features", {
                    "heading": "Derfor vælger kunder JCleemannByg",
                    "features": [
                        {
                            "title": "Kvalitet i hver detalje",
                            "description": "Vi går aldrig på kompromis med kvaliteten. Alle materialer og håndværk lever op til de højeste standarder.",
                            "icon": "check"
                        },
                        {
                            "title": "Altid til tiden",
                            "description": "Vi overholder altid vores deadlines og leverer projekter til tiden. Planlægning og pålidelighed er i højsædet.",
                            "icon": "clock"
                        }
                    ],
                    "style": {"background": "surface", "spacing": "lg", "container": "wide"}
                }),
                ("featured_projects", {
                    "heading": "Udvalgte projekter",
                    "subheading": "Se eksempler på vores seneste arbejde og få inspiration til dit næste projekt",
                    "projects": [],  # Will be populated from actual projects
                    "style": {"background": "surface-soft", "spacing": "lg", "container": "wide"}
                }),
                ("services_grid_inline", {
                    "heading": "Vores services",
                    "services": [s for s in Service.objects.all()[:3]],
                    "style": {"background": "surface", "spacing": "lg", "container": "wide"}
                }),
                ("testimonials", {
                    "heading": "Hvad siger vores kunder",
                    "testimonials": [t for t in Testimonial.objects.all()[:2]],
                    "style": {"background": "surface-soft", "spacing": "lg", "container": "normal"}
                }),
                ("cta", {
                    "title": "Klar til at starte dit projekt?",
                    "text": "Kontakt JCleemannByg i dag for et uforpligtende tilbud på dit næste projekt.",
                    "button_text": "Få et tilbud",
                    "button_page": home_page,  # Will redirect to contact page
                    "style": {"background": "hero", "spacing": "lg", "container": "narrow"}
                })
            ]
            home_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Homepage content updated with Frostbite-styled blocks"))

        self.stdout.write(self.style.SUCCESS("Homepage setup complete!"))
