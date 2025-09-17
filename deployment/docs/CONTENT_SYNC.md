# Content Synchronisation with Wagtail Transfer

Wagtail Transfer replaces the legacy JSON "baseline" fixture workflow. One environment (usually staging) remains the canonical source of content, and other environments pull from it on demand.

## Prerequisites

1. **Matching secrets**
   - Set `WAGTAILTRANSFER_SECRET_KEY` on every environment.
   - Define `WAGTAILTRANSFER_SOURCES` as JSON, e.g.
     ```env
     WAGTAILTRANSFER_SOURCES={"staging": {"BASE_URL": "https://staging.example.com/wagtail-transfer/", "SECRET_KEY": "transfer-secret"}}
     ```
   - The `SECRET_KEY` for each source entry must equal the `WAGTAILTRANSFER_SECRET_KEY` on that source instance.
2. **Baseline identifiers**
   - `BASELINE_SOURCE` → key inside `WAGTAILTRANSFER_SOURCES` you want to pull from (e.g. `staging`).
   - `BASELINE_ROOT_PAGE_ID` → numeric page ID on the source tree to replicate (commonly the staging home page ID).
3. **UUID seeding**
   - Run once on both source and destination:
     ```bash
     python manage.py preseed_transfer_table wagtailcore.page
     ```

## Importing content

Use the management command from any destination environment:

```bash
python manage.py baseline_pull --flush
```

- `--flush` removes existing children of the default site root before importing.
- The command fetches the source tree via HTTPS, plans the operations using Wagtail Transfer, and replaces/updates all pages and snippets referenced by the export.
- Run the command inside Docker (`docker compose exec web ...`) or via the Dokploy console.

## Automation

- Set `BASELINE_PULL_ON_START=true` to make the Dokploy entrypoint call `baseline_pull --flush` automatically when the container starts.
- Leave the flag `false` for production once the site holds real content, and run the command manually when you intend to replace it.

## Updating staging (source of truth)

Edit pages directly on the staging site using Wagtail admin. No additional commands are required. When you need production to match staging, run `python manage.py baseline_pull --flush` on production.

## Troubleshooting

| Symptom | Resolution |
| --- | --- |
| `Unknown wagtail-transfer source` | Ensure the `BASELINE_SOURCE` key exists in `WAGTAILTRANSFER_SOURCES`. |
| `HTTP error communicating with source` | Verify the source URL is reachable and ends with `/wagtail-transfer/`. Check firewalls between environments. |
| Duplicate pages after import | Run `preseed_transfer_table wagtailcore.page` on both environments, then rerun `baseline_pull --flush`. |
| Permission denied | The source instance must have the `wagtail-transfer` app installed and expose `/wagtail-transfer/api/*`. |

## Handy Make targets

```
make dev          # starts docker compose, migrates, and attempts baseline_pull
make baseline     # forces baseline_pull --flush with the active .env file
ENV_FILE=.env.prod make baseline  # run against production via docker context
```

This approach removes the need to maintain JSON fixtures or bundled media inside the Docker image while keeping deployments predictable and reproducible.
