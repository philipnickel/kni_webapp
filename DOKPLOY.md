# Dokploy Deployment Guide

This project ships with a Dockerfile that Dokploy can build directly—no extra manifests required.

## Quick Start

1. **Import the repository** in Dokploy.
2. **Select the Dockerfile** at `deployment/Dockerfile`.
3. **Provide the required environment variables** (see below).
4. **Deploy.** Dokploy will build the image and start the container.

## Required Environment Variables

Set these in your Dokploy application:

```bash
DJANGO_SECRET_KEY=your-super-secret-key
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

## Recommended Extras

```bash
DOMAIN=yourdomain.com
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=super-secure
REDIS_URL=redis://:password@redis-host:6379/0
DEBUG=False

# Wagtail Transfer configuration (see "Content sync" below)
WAGTAILTRANSFER_SECRET_KEY=prod-transfer-secret
WAGTAILTRANSFER_SOURCES={"staging": {"BASE_URL": "https://staging.yourdomain.com/wagtail-transfer/", "SECRET_KEY": "prod-transfer-secret"}}
BASELINE_SOURCE=staging
BASELINE_ROOT_PAGE_ID=3
BASELINE_TRANSFER_TIMEOUT=10
BASELINE_PULL_ON_START=false
```

> ⚠️ Replace the placeholders above with values from your source environment. Dokploy supports multi-line values—keep the JSON compact (single line) for ease of entry.

## Docker Configuration

- **Dockerfile**: `deployment/Dockerfile`
- **Port**: 8000 (exposed via OCI labels, Dokploy auto-detects)
- **Health Endpoint**: `/health/ready/`
- **Entrypoint**: handles migrations and optional baseline pull via Wagtail Transfer

## Content Sync with Wagtail Transfer

Wagtail Transfer keeps one environment (typically staging) as the source of truth and lets other environments pull content on demand.

1. **Assign matching secrets**: `WAGTAILTRANSFER_SECRET_KEY` on every environment must match the `SECRET_KEY` entry for that environment inside `WAGTAILTRANSFER_SOURCES` on its peers.
2. **Identify your source**: set `BASELINE_SOURCE` to the key (e.g. `staging`) inside `WAGTAILTRANSFER_SOURCES` that points to the canonical site. Set `BASELINE_ROOT_PAGE_ID` to the page ID you want to replicate (commonly the staging home page ID).
3. **Bootstrap once**: on both source and destination, run
   ```bash
   python manage.py preseed_transfer_table wagtailcore.page
   ```
   to seed predictable UUIDs for existing pages.
4. **Pull content**: run `python manage.py baseline_pull --flush` (or `make baseline` using the correct `.env` file) on any environment to replace its content with the source tree. The command talks to the source over HTTP using the credentials above.
5. **Automate if desired**: set `BASELINE_PULL_ON_START=true` in Dokploy to make the entrypoint run the import automatically on each boot.

### Local development shortcut

```
make dev                      # starts docker compose, migrates, tries baseline_pull
make baseline                 # re-imports content from the configured source
ENV_FILE=.env.prod make baseline  # run against production config
```

The `baseline_pull` command is resilient—if the variables are missing it aborts and `make dev` simply warns you.

## Deployment Workflow

- **Initial deploy**: point Dokploy at your repo, set env vars, deploy. If you want content immediately, set `BASELINE_PULL_ON_START=true` for the first boot or run `python manage.py baseline_pull --flush` manually from the Dokploy console.
- **Subsequent deploys**: leave `BASELINE_PULL_ON_START=false` and only pull content when you intend to replace production with the canonical source.
- **Updating staging**: edit content directly on the canonical staging environment; the next pull elsewhere will mirror those changes.

## Troubleshooting

- **Wagtail Transfer auth errors**: confirm the secret key values match on both sides and that the source URL ends with `/wagtail-transfer/`.
- **Import stuck fetching objects**: ensure `BASELINE_ROOT_PAGE_ID` refers to an actual page and the source host is reachable from the destination.
- **Pages duplicated after import**: run `python manage.py preseed_transfer_table wagtailcore.page` on both environments, then retry with `--flush` to clear existing descendants before importing.
- **General logs**: Dokploy’s container logs include the entrypoint output (migrations, optional baseline pull) and application logs. Use `/health/ready/` for liveness checks.

## Useful Commands

```bash
# Run inside the Dokploy container (or via `make` locally)
python manage.py baseline_pull --flush           # Import from the configured baseline source
python manage.py preseed_transfer_table wagtailcore.page  # One-time UUID seeding
python manage.py createsuperuser                 # Create additional admins
```

That’s it—deploy with Dokploy, let staging hold your canonical content, and use `baseline_pull` whenever another environment needs to line up with it.
