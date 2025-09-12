Deploying to Coolify
====================

This project ships with Docker assets ready for Coolify. Use `docker-compose.coolify.yml` (no public DB/Redis ports, no extra Nginx).

Prerequisites
-------------
- A Coolify instance with a reachable domain
- A Git repository containing this project

Option A: Use the Coolify-optimized compose
-------------------------------------------
This file runs `web`, `db`, and `redis` only. No public ports are exposed for DB/Redis; Coolify’s proxy will route traffic to `web`.

1) In Coolify, create a new “Docker Compose Application”.
2) Repository: point to this repo and set the compose file to `docker-compose.coolify.yml`.
3) Service to expose: `web` (container port 8000).
4) Environment variables (add at minimum):
   - `DJANGO_SECRET_KEY` (strong, random)
   - `ALLOWED_HOSTS` (e.g. `your-domain.com,www.your-domain.com`)
   - `CSRF_TRUSTED_ORIGINS` (e.g. `https://your-domain.com,https://www.your-domain.com`)
   - `WAGTAILADMIN_BASE_URL` (e.g. `https://your-domain.com`)
   - `SECURE_SSL_REDIRECT=True`
   - `DATABASE_PASSWORD` (used by Postgres container)
   - `REDIS_PASSWORD` (used by Redis container)
5) Health check: path `/health/`, port 8000.
6) Domains: attach your domain(s) in Coolify and enable SSL.
7) Deploy.

Option B: Use Coolify Managed DB/Redis
-------------------------------------
If you prefer managed Postgres/Redis:
- Create those services in Coolify and copy their URLs.
- In the Coolify app env vars, set:
  - `DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME`
  - `REDIS_URL=redis://:PASSWORD@HOST:PORT/0`
- In `docker-compose.coolify.yml`, disable or remove the `db` and `redis` services (or set the app to ignore them). Only `web` must run.

Optional: Celery worker/beat
----------------------------
If you need background jobs later, add `worker` and/or `beat` services mirroring the `web` env vars in `docker-compose.coolify.yml` and deploy them as separate services.

Notes
-----
- The app exposes a health endpoint at `/health/` used by Docker and Coolify.
- Static files are collected on startup; WhiteNoise serves them. You do not need Nginx inside the app when behind Coolify’s proxy.
- Tenant seeding hooks exist via `SEED_TENANT_DATA=true` and `TENANT_*` vars, but the referenced management commands are optional and safe to skip.

Local Docker Testing
====================

Test the application locally using Docker to mimic production:

Local Development with Baseline Data
------------------------------------
Use the Docker development stack:

```bash
make docker-up     # Build and run with baseline data
make docker-logs   # Tail application logs
make docker-shell  # Shell into the app container
make docker-down   # Stop all services

# App URL
open http://localhost:8001
```

The local setup uses `.env.local` and loads your development baseline data automatically.

Environment Configuration
=========================

Production Environment Setup
----------------------------
1. Copy `.env.production` to `.env` on your Coolify server
2. Customize the values:
   ```bash
   DJANGO_SECRET_KEY=your-generated-secret-key
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://www.your-domain.com
   DATABASE_PASSWORD=your-secure-database-password
   REDIS_PASSWORD=your-secure-redis-password
   WAGTAILADMIN_BASE_URL=https://your-domain.com
   ```

Local Environment Setup
-----------------------
The `.env.local` file is already configured for Docker development and includes:
- Database credentials that match docker-compose.local.yml
- Baseline data loading enabled (`LOAD_BASELINE=true`)
- Local development settings (debug, non-SSL)

Troubleshooting
---------------
- 502/Bad Gateway: ensure `web` service is healthy; check `make docker-logs`.
- CSRF failures in production: confirm `CSRF_TRUSTED_ORIGINS` contains your HTTPS origins with scheme.
- Admin login unavailable: ensure migrations ran (entrypoint does this) and DB is reachable.
- Database connection issues: verify `DATABASE_PASSWORD` matches between app and database service.
