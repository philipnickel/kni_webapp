# Dokploy Deployment Checklist

Use this checklist when standing up a new Dokploy environment.

## 1. Configure environment variables

Mandatory:

```env
DJANGO_SECRET_KEY=your-super-secret-key
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

Recommended:

```env
DOMAIN=example.com
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=generate-a-strong-password
DEBUG=False

# Wagtail Transfer (content sync)
WAGTAILTRANSFER_SECRET_KEY=transfer-secret
WAGTAILTRANSFER_SOURCES={"staging":{"BASE_URL":"https://staging.example.com/wagtail-transfer/","SECRET_KEY":"transfer-secret"}}
BASELINE_SOURCE=staging
BASELINE_ROOT_PAGE_ID=3
BASELINE_TRANSFER_TIMEOUT=10
BASELINE_PULL_ON_START=false
```

> The JSON value can be kept on a single line so it pastes cleanly in Dokploy. Every environment that appears inside `WAGTAILTRANSFER_SOURCES` must expose `/wagtail-transfer/` and use the same `SECRET_KEY` shown above.

## 2. Build & deploy

- Point Dokploy at `deployment/Dockerfile` (target `production`).
- Deploy once; Dokploy builds the Docker image and runs database migrations automatically via the entrypoint.
- Optional: set `BASELINE_PULL_ON_START=true` for the first boot if you want the container to import content immediately from your canonical staging site.

## 3. Bootstrap Wagtail Transfer (run once per environment)

```
python manage.py preseed_transfer_table wagtailcore.page
```

This seeds UUIDs so that subsequent imports recognise existing pages instead of creating duplicates.

## 4. Replace content when needed

```
python manage.py baseline_pull --flush    # or: make baseline (with the correct ENV_FILE)
```

- Use this on production or review environments whenever you need them to match staging.
- The command talks to the configured source over HTTPS, downloads the export, and applies it via Wagtail Transfer.

## 5. Verify

- Visit `/health/ready/` to confirm the health endpoint passes.
- Log in to `/admin/` using the admin credentials.
- Confirm that pages/snippets look correct after a baseline pull (if you ran one).

## Troubleshooting

| Issue | Fix |
| --- | --- |
| `Unknown wagtail-transfer source` | Check `BASELINE_SOURCE` against the keys inside `WAGTAILTRANSFER_SOURCES`. |
| HMAC digest errors | Ensure the destination `WAGTAILTRANSFER_SECRET_KEY` matches the `SECRET_KEY` configured for it in the source JSON. |
| Empty content after deploy | Run `python manage.py baseline_pull --flush` manually; leave `BASELINE_PULL_ON_START=true` only when you intentionally want to replace content on every boot. |
| Cannot reach staging | Verify staging is accessible from the Dokploy network and that HTTPS certificates are valid. |

Keep this checklist with the new [`deployment/docs/CONTENT_SYNC.md`](CONTENT_SYNC.md) reference for detailed Wagtail Transfer usage.
