Deploying to Coolify (Hostinger VPS)
====================================

This repo is optimized for Coolify deployment with minimal setup using Docker Compose for a complete stack.

What we automated
-----------------
- `PRIMARY_DOMAIN` auto-derives `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and `WAGTAILADMIN_BASE_URL`.
- Production security defaults: HTTPS redirect, HSTS when `DEBUG=false`, secure cookies.
- Health endpoint at `/health/` returns 200 without leaking info.
- Complete stack: PostgreSQL + Redis + Django app in one deployment.

Prerequisites
-------------
- A Coolify instance running on your Hostinger VPS with a reachable domain
- This GitHub repo connected to Coolify
- DNS A/AAAA record for the customer domain pointing to your VPS IP

Recommended: Docker Compose deployment (2-minute flow)
-----------------------------------------------------
Deploys complete stack with PostgreSQL and Redis included.

1) **Create Service**: Coolify → New Service → select this repo → **Use Docker Compose**
2) **Compose File**: Select `docker-compose.coolify.yml` 
3) **Environment Variables**: Set only these essentials:
   ```bash
   PRIMARY_DOMAIN=customer.com
   DJANGO_SECRET_KEY=          # Leave empty, use Coolify's "Generate" button
   DATABASE_PASSWORD=          # Leave empty, use Coolify's "Generate" button
   REDIS_PASSWORD=             # Leave empty, use Coolify's "Generate" button
   ```
   **Pro tip**: Click the "Generate" button next to each secret field in Coolify UI.

4) **Domains**: Attach `customer.com` in Coolify and enable SSL (Let's Encrypt).
5) **Deploy**: Coolify will create PostgreSQL, Redis, and your app automatically.
6) **One-time setup**: Coolify → Service → Execute Command (on the `web` container):
   - `python manage.py migrate`
   - Optional: `python manage.py createsuperuser`

Alternative: Dockerfile-only deployment
--------------------------------------
Advanced option requiring external database services.

1) Create app: Coolify → New App → Deploy from Git Repository → select this repo (Dockerfile).
2) Volumes: add persistent volumes
   - `/app/staticfiles`
   - `/app/media`
3) Environment: requires external PostgreSQL and Redis
   ```bash
   DJANGO_SETTINGS_MODULE=project.settings
   DEBUG=false
   DJANGO_SECRET_KEY=          # Use Coolify's "Generate" button
   PRIMARY_DOMAIN=customer.com
   DATABASE_URL=postgresql://user:pass@db-host:5432/dbname?sslmode=require
   REDIS_URL=redis://:password@redis-host:6379/0
   ```
4) Domains: attach domain and enable SSL
5) Deploy and run migrations as above

Stack Information
-----------------
When using Docker Compose deployment, your stack includes:

- **PostgreSQL 15**: Accessible at `db:5432` (internal network only)
- **Redis 7**: Accessible at `redis:6379` (internal network only)  
- **Django App**: Exposed on port 8000 with health checks
- **Persistent Data**: 
  - Database: `postgres_data` volume
  - Redis: `redis_data` volume  
  - Media files: `media_volume` volume
  - Static files: `static_volume` volume

**Security**: Database and Redis are isolated on Docker's internal network and not exposed publicly.

Optional: Post-deploy automation
--------------------------------
For Docker Compose deployments, add this to Coolify → Service → Post Deploy Command:
```bash
docker compose exec web python manage.py migrate --noinput
docker compose exec web python manage.py collectstatic --noinput --clear
```

For Dockerfile deployments, use:
```bash
sh docker/post_deploy.sh
```
Enable "Run after deployment" to auto-apply migrations and collect static files on each deploy.

Production Notes
---------------
- **Static Files**: Served by WhiteNoise, collected automatically during build
- **Media Files**: Persisted in Docker volumes, automatically backed up by Coolify
- **Security**: All services isolated on internal Docker network
- **SSL**: Automatic Let's Encrypt certificates when domain is attached
- **Health Checks**: Built-in monitoring at `/health/` endpoint
- **Scaling**: Web container can be scaled horizontally in Coolify UI

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
**Docker Compose Issues:**
- Service won't start: Check Coolify logs for each service (web, db, redis)
- Database connection failed: Ensure `DATABASE_PASSWORD` is set and containers can communicate
- Redis connection failed: Ensure `REDIS_PASSWORD` matches between services

**General Issues:**
- 502/Bad Gateway: Check container health and logs; ensure `/health/` responds 200
- CSRF failures: Confirm `PRIMARY_DOMAIN` is set correctly (no http/https prefix needed)
- Admin login unavailable: Ensure migrations ran and database is reachable
- Static not loading: Check if static volume is mounted and build succeeded

**Quick Fixes:**
- Reset database: Delete `postgres_data` volume in Coolify and redeploy
- View logs: Coolify → Service → Logs (select specific container)
- Access database: Use Coolify's Execute Command to run `psql` on the db container
