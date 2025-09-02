# JCleemannByg — Django + Wagtail Implementation Plan

This plan is optimized for simplicity, maintainability, and owner‑friendly editing. It focuses on: Velkomstside (homepage), Projekt‑galleri (gallery + project pages), Owner Dashboard (media control), Quote form (store‑only), and built‑in analytics. Mail integration is deferred.

No timelines — stages are sequence only.

---

## Scope

- Velkomstside: themeable hero, trust badges, featured services/projects, testimonials, CTA anchors.
- Projekt‑galleri: projects with images, captions, tags, before/after pairing, and ordering.
- Owner Dashboard: manage projects, media, site settings (brand kit, footer/NAP/CVR), and homepage blocks.
- Quote form (store‑only): collect submissions, list/manage in dashboard; no emails.
- Analytics: privacy‑friendly pageviews + conversions; dashboard snapshot/charts.

Out of scope for MVP: email sending, calendar, webmail, invoice scanning, multi‑site control plane beyond core Sites support.

---

## Stack & Architecture

- Django 4.x/5.x + Postgres; use Django Sites for per‑site content separation.
- Wagtail 6.x: pages, images/renditions, StreamField, ModelAdmin, permissions, Sites & Settings.
- Images: Wagtail Images for responsive renditions (WebP/AVIF), focal points, alt enforcement.
- Storage: local in dev; `django-storages` for S3/R2 later (config ready but disabled).
- Frontend: Django templates + Tailwind CSS; HTMX for light interactivity (filters, reorder posts only in admin via inlines).
- Analytics: in‑house collector (cookieless until consent), daily rollups.
- Caching: conservative template caching; option to add `wagtail-cache` later.

---

## Repository Layout

```
project/                 # Django project (settings, urls, wsgi/asgi)
apps/
  core/                  # brand kit, site settings, theme vars, common utils
  pages/                 # Wagtail Page types (HomePage, generic pages)
  projects/              # Project, ProjectImage (orderable), admin, templates
  contacts/              # Quote form (store‑only), inbox admin
  analytics/             # collector endpoint, daily rollups, dashboard views
templates/               # global templates (base, partials, blocks)
static/                  # Tailwind build output, JS, images
media/                   # local media (dev)
scripts/                 # management scripts, data import/export
```

---

## Environment & Setup

- Python: 3.11+
- DB: Postgres (dev can start on SQLite; prefer Postgres early for parity)
- Create virtualenv and install deps:
  - `pip install django wagtail psycopg2-binary django-taggit python-dotenv`
  - Optional: `django-storages boto3 whitenoise wagtail-seo htmx` (as needed)
- Env vars (`.env`):
  - `DJANGO_SECRET_KEY=...`
  - `DATABASE_URL=postgres://user:pass@host:5432/dbname`
  - `DEBUG=true`
  - `ALLOWED_HOSTS=localhost,127.0.0.1`
  - `SECURE_SSL_REDIRECT=false` (prod true)

Dev bootstrap commands (illustrative):

```
django-admin startproject project .
pip install wagtail
wagtail start jcbyg .     # or integrate Wagtail into existing project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Data Model

- Project (apps/projects/models.py)
  - site (ForeignKey to `wagtailcore.Site` or `sites.Site`)
  - title, slug, description (RichTextField), tags (taggit)
  - featured (bool), published (bool), date (DateField)
  - panels: title/slug, description, tags, featured/published/date, InlinePanel(images)

- ProjectImage (Orderable, ParentalKey to Project)
  - image (ForeignKey to `wagtailimages.Image`)
  - alt (CharField), caption (TextField), before_after (Choice: none|before|after)
  - order (provided by Orderable)

- ContactSubmission (apps/contacts/models.py)
  - site, name, email, phone, message, files (Document uploads via Wagtail)
  - consent (bool), status (choice: new|in_progress|closed), created_at

- AnalyticsDaily (apps/analytics/models.py)
  - site, date, path (nullable for site rollup)
  - views (int), uniques (int), conversions (int)

- SiteSettings (apps/core/wagtailsettings.py)
  - brand kit: logo (Image), colors (JSON), fonts (choices), theme (choice)
  - footer: NAP/CVR, social links
  - homepage featured: featured services (simple list), featured projects (Chooser)

Notes
- Enforce alt text on all images used publicly.
- Use Wagtail Images renditions for responsive variants and WebP/AVIF.

---

## Page Types & Components

- HomePage (StreamField blocks)
  - Hero: heading, subheading, background/media, primary CTA anchors
  - TrustBadges: items with icon/text (CVR, years, associations)
  - FeaturedServices: list of cards
  - FeaturedProjects: chooser of Project pages or queryset by tag
  - Testimonials: simple list (manual for now)
  - Map/Contact strip: address, hours, map embed

- Project detail (TemplateView)
  - Title, description (rich text), tags, date
  - Image gallery with before/after slider when paired; captions

- Gallery index (TemplateView)
  - Filters: tags, featured, year
  - Grid/masonry layout with pagination and lightbox

---

## Stages (Sequence Only)

Stage 0 — Bootstrap & Foundations
- Install Django + Wagtail; configure Sites; base settings for dev/prod.
- Create `apps/core`, `apps/pages`, wire base templates and theme variables.
- Add cookie/consent banner scaffold (no logic yet), robots.txt, sitemap.
- Definition of Done (DoD): Wagtail admin accessible; Home page exists; theme variables render.

Stage 1 — Projects & Media Pipeline
- Models: Project, ProjectImage (Orderable), tagging (taggit).
- Admin: Wagtail ModelAdmin for Projects; InlinePanel for images with drag‑order.
- Renditions: responsive presets (thumb, grid, hero) with WebP/AVIF; LQIP placeholders.
- Validation: require alt; enforce image type/size limits; strip EXIF.
- DoD: Create project → upload images → set alt/captions → order saved and visible in preview.

Stage 2 — Owner Dashboard Essentials
- Groups/Permissions: Owner (full for site), Staff (projects/media only).
- SiteSettings: brand kit, footer NAP/CVR, homepage featured.
- UX: ModelAdmin tweaks (list filters, search, bulk publish/unpublish).
- DoD: Non‑technical owner can manage projects/media and settings for their site.

Stage 3 — Public Gallery & Project Pages
- Views/templates: gallery index (filters, pagination, lightbox), project detail with before/after.
- Accessibility: keyboard nav, focus styles, alt enforcement, reduced motion.
- Performance: lazy‑load, aspect‑ratio boxes, cache headers.
- DoD: Gallery loads quickly; filters work; detail pages display ordered media and before/after slider.

Stage 4 — Velkomstside (Homepage)
- HomePage with StreamField blocks (hero, trust, featured services/projects, testimonials, map/contact strip).
- Editable from Wagtail; featured projects pulled from Projects app.
- DoD: Owner can edit homepage blocks; CTA anchors route to correct sections.

Stage 5 — Quote Form (Store‑Only)
- Model/Form/View: ContactSubmission with file uploads; thank‑you page.
- Spam: honeypot + rate limit; optional CAPTCHA toggle (setting).
- Admin inbox: ModelAdmin list + detail; statuses; CSV export.
- DoD: Submissions stored and visible; no emails sent.

Stage 6 — Analytics (Built‑In)
- Client: tiny tracker snippet gated by consent; sendBeacon on pageview and key events (quote submitted, CTA clicks, gallery interactions).
- Server: `/analytics/collect` endpoint → increment raw counters; nightly rollup to AnalyticsDaily; purge raw (optional) to keep it simple.
- Dashboard: Wagtail admin view with snapshot cards (views/uniques/conversions) and charts (7/28/90 days), top pages.
- DoD: Analytics appears in dashboard with accurate counts; tracker respects consent.

Stage 7 — Polish (SEO, A11y, CWV)
- SEO: meta/OG editors, sitemap, robots, LocalBusiness/Project schema.
- A11y: contrast, focus, labels, skip links.
- Performance: Lighthouse budgets, preconnect/preload, image sizes verified.
- DoD: Core Web Vitals budget met on key pages; schema validates.

---

## Owner Roles & Permissions

- Groups (Wagtail):
  - Owner: full access to Pages, Projects, Images, Documents, SiteSettings for their site.
  - Staff: access to Projects and Images only.
- Scope all querysets by `site` in custom ModelAdmin and views.

---

## Admin & Editor UX

- Projects: list (title, tags, featured, published, date), filters (tag, published), bulk publish.
- Project edit: title, desc, tags, featured/published/date, images (sortable inline), alt/captions, before/after.
- Site settings: logo upload, colors, fonts, footer NAP/CVR, homepage featured selectors.
- Contacts inbox: table (date, name, status), detail view with attachments; status workflow.
- Analytics: snapshot cards, timeseries chart, top pages; date range filter.

---

## Public Templates & UX

- Base: responsive, Tailwind, mobile‑first; skip links, semantic landmarks.
- Homepage: hero with CTA anchors, trust badges, featured services/projects, testimonials, map/contact strip.
- Gallery: tag filters (progressive enhancement with HTMX), masonry/grid; lightbox; pagination.
- Project detail: ordered images with captions; before/after slider; related projects by tag.

---

## Analytics Details

- Event schema: { site_id, ts, type: pageview|conversion|gallery, path, referrer, utm, session_id (rotating anon), device, lang, meta }
- Consent: tracker loads only after “accept analytics”; store minimal cookie or use session storage; no IP/PII persisted.
- Aggregation: management command to roll up daily counts; optional cron (Heroku scheduler/cron in prod).

---

## Definition of Done (Per Stage)

- Stage 0: Admin up; Sites configured; base theme renders.
- Stage 1: Projects + images CRUD with renditions; alt enforced; ordering works.
- Stage 2: Roles/permissions applied; brand kit/settings editable.
- Stage 3: Gallery/Project public pages fast and accessible.
- Stage 4: Homepage editable via StreamField; featured projects render.
- Stage 5: Submissions stored; inbox usable; spam mitigations work.
- Stage 6: Analytics events collected and shown; consent respected.
- Stage 7: SEO/A11y/CWV checks pass; sitemaps/robots present; schema valid.

---

## Testing Strategy

- Unit: models (constraints, methods), rendering of image renditions, serializers.
- Integration: create project → upload images → render gallery; contact form submission stored; analytics collector increments counters.
- E2E (optional, Playwright): homepage load, gallery filters, project page, quote submit.
- Accessibility: axe checks in CI for key templates; keyboard nav verified.

---

## Risks & Mitigations

- Image bloat: quotas in settings; validate sizes; background cleanup for orphans.
- Multi‑site leakage: strict `site` filters; add tenancy tests; Wagtail group permissions.
- Performance regressions: Lighthouse budgets; image rendition presets; caching headers.
- Editor confusion: concise help text; sensible defaults; minimal required fields.

---

## Backlog (Post‑MVP)

- Email integration (Microsoft Graph) for drafts/notifications.
- Testimonials and Services CRUD with blocks.
- Multilingual pages; control plane (create site from template); backups/monitoring.
- Advanced analytics (events table, funnels) or integration with Plausible/PostHog.

---

## Runbook (Dev)

1) Create virtualenv and install dependencies.
2) Configure `.env` and database.
3) `python manage.py migrate && python manage.py createsuperuser`
4) `python manage.py runserver`
5) In admin: set up Site (hostname, root page), add HomePage, set SiteSettings, create first Project with images.

---

## Quick Task Index (for agents)

- T0. Bootstrap Django + Wagtail; base settings; Sites config.
- T1. Add `apps/projects` with Project + ProjectImage models, inlines, ModelAdmin.
- T2. Configure Wagtail Images renditions (thumb/grid/hero), alt enforcement.
- T3. Add `apps/core` SiteSettings (brand kit, footer, homepage featured).
- T4. Implement Gallery index + Project detail templates with filters and before/after.
- T5. Create `HomePage` with StreamField blocks; render homepage.
- T6. Add `apps/contacts` with ContactSubmission; public form + admin inbox.
- T7. Add `apps/analytics` collector endpoint, daily rollups, dashboard view.
- T8. Polish: SEO meta/OG, sitemaps/robots, accessibility fixes, perf budgets.

