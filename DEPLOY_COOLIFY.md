Deploying to Coolify (Hostinger VPS)
====================================

This repo is optimized for Coolify’s “Deploy from Repo” with minimal per-customer setup.

What we automated
-----------------
- `PRIMARY_DOMAIN` auto-derives `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and `WAGTAILADMIN_BASE_URL`.
- Production security defaults: HTTPS redirect, HSTS when `DEBUG=false`, secure cookies, DB SSL when remote.
- Health endpoint at `/health/` returns 200 without leaking info.

Prerequisites
-------------
- A Coolify instance running on your Hostinger VPS with a reachable domain
- This GitHub repo connected to Coolify
- DNS A/AAAA record for the customer domain pointing to your VPS IP

Fast path: Deploy from repo (5-minute flow)
------------------------------------------
1) Create app: Coolify → New App → Deploy from Git Repository → select this repo (Dockerfile).
2) Volumes: add persistent volumes
   - `/app/staticfiles`
   - `/app/media`
3) Environment: paste minimal block, change ONLY the placeholders
   ```bash
   DJANGO_SETTINGS_MODULE=project.settings
   DEBUG=false
   DJANGO_SECRET_KEY=<strong-random>
   PRIMARY_DOMAIN=customer.com
   EXTRA_DOMAINS=
   SECURE_SSL_REDIRECT=true
   DATABASE_URL=postgresql://user:pass@db-host:5432/dbname?sslmode=require
   REDIS_URL=redis://:password@redis-host:6379/0
   ```
4) Domains: attach `customer.com` in Coolify and enable SSL (Let’s Encrypt).
5) Deploy.
6) One-off commands (once per app): Coolify → App → Run Command
   - `python manage.py migrate`
   - Optional: `python manage.py createsuperuser`

Optional: Quick env generation (no Coolify API)
-----------------------------------------------
From Coolify Run Command or locally:
```bash
python manage.py generate_coolify_env customer.com \
  --database-url "postgresql://user:pass@db-host:5432/dbname?sslmode=require" \
  --redis-url "redis://:password@redis-host:6379/0"
```
Copy the output block into Environment and redeploy.

Optional: Post-deploy automation
--------------------------------
In Coolify → App → Commands → add a Post Deploy command:
```bash
sh docker/post_deploy.sh
```
Enable “Run after deployment” to auto-apply migrations and collect static on each deploy.

Notes
-----
- The Dockerfile builds with a non-root user and collects static at build time.
- WhiteNoise serves static files; media persists in the `/app/media` volume.
- Redis must not be exposed publicly; use a strong password in `REDIS_URL`.
- If you host Postgres yourself, ensure it enforces TLS (`sslmode=require`).

Local Docker testing
====================

Use the dev stack with baseline data:
```bash
make docker-up
make docker-logs
make docker-shell
make docker-down
open http://localhost:8001
```

Troubleshooting
---------------
- 502/Bad Gateway: check container health and logs; ensure `/health/` responds 200.
- CSRF failures: confirm `PRIMARY_DOMAIN` is set or `CSRF_TRUSTED_ORIGINS` are correct (HTTPS scheme).
- Admin login unavailable: ensure migrations ran and database is reachable.
- Static not loading: confirm `/app/staticfiles` volume exists and build didn’t fail collectstatic.
