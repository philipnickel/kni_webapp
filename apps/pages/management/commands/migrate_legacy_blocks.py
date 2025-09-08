import json
from django.core.management.base import BaseCommand
from wagtail.models import Page
from apps.pages.models import HomePage, Testimonial


class Command(BaseCommand):
    help = "Migrate legacy HomePage blocks (hero, trust_badges, featured_projects, testimonials) to new modular components."

    def add_arguments(self, parser):
        parser.add_argument('--apply', action='store_true', help='Apply changes (default is dry-run)')

    def handle(self, *args, **options):
        apply = options['apply']
        pages = HomePage.objects.all()
        if not pages.exists():
            self.stdout.write(self.style.WARNING('No HomePage instances found.'))
            return

        for page in pages:
            orig = page.body.stream_data if page.body else []
            if not orig:
                self.stdout.write(f"Skipping {page.title} (no body)")
                continue

            new_stream = []
            changes = []

            for block in orig:
                btype = block.get('type')
                value = block.get('value')

                if btype == 'hero':
                    new_stream.append(('hero_v2', {
                        'heading': value.get('heading'),
                        'subheading': value.get('subheading'),
                        'primary_text': value.get('cta_text') or 'Få et tilbud',
                        'primary_url': f"#{value.get('cta_anchor')}" if value.get('cta_anchor') else '/fa-tilbud/',
                        'style': {'background': 'hero', 'spacing': 'lg', 'container': 'wide'}
                    }))
                    changes.append('hero -> hero_v2')

                elif btype == 'trust_badges':
                    items = []
                    for it in value:
                        items.append({'title': it.get('label'), 'text': it.get('description') or '', 'icon': 'check'})
                    new_stream.append(('features', {
                        'heading': 'Derfor os',
                        'items': items,
                        'columns': '4',
                        'style': {'background': 'surface-soft', 'spacing': 'md', 'container': 'wide'}
                    }))
                    changes.append('trust_badges -> features')

                elif btype == 'featured_projects':
                    new_stream.append(('cta', {
                        'title': 'Se vores træprojekter',
                        'text': 'Udforsk tidligere arbejde og få inspiration.',
                        'button_text': 'Se projekter',
                        'button_url': '/projekter/',
                        'style': {'background': 'surface', 'spacing': 'md', 'container': 'narrow'}
                    }))
                    changes.append('featured_projects -> cta')

                elif btype == 'testimonials':
                    pks = []
                    for quote in value:
                        qt = (quote or '').strip()
                        if not qt:
                            continue
                        # Reuse existing identical quote if present
                        snip = Testimonial.objects.filter(quote=qt).first()
                        if not snip:
                            snip = Testimonial.objects.create(name='Kunde', role='', quote=qt)
                        pks.append(snip.pk)
                    if pks:
                        new_stream.append(('testimonials_snippets', {
                            'testimonials': pks,
                            'style': {'background': 'surface', 'spacing': 'md', 'container': 'normal'}
                        }))
                        changes.append('testimonials -> testimonials_snippets')
                else:
                    # Keep any other blocks as-is (including newer modular ones)
                    new_stream.append((btype, value))

            if not changes:
                self.stdout.write(f"{page.title}: no legacy blocks to migrate.")
                continue

            self.stdout.write(f"{page.title}: will apply changes -> {', '.join(changes)}")

            if apply:
                page.body = new_stream
                page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS(f"{page.title}: migrated and published"))
            else:
                self.stdout.write(self.style.WARNING("Dry run: pass --apply to commit changes"))

