# Fix PostgreSQL SSL Connection Error

## Error
```
psycopg2.OperationalError: connection to server at "kni-webapp-db-mwzipf" (10.0.1.174), port 5432 failed: server does not support SSL, but SSL was required
```

## Root Cause
The current DATABASE_URL has `sslmode=disable` but PostgreSQL is still trying to use SSL.

## Solution

### Step 1: Update Environment Variable in Dokploy

Go to your application → **Environment** tab and update the DATABASE_URL:

**From:**
```
DATABASE_URL=postgresql://wagtail:${{project.DATABASE_PASSWORD}}@kni-webapp-db-mwzipf:5432/wagtail?sslmode=disable
```

**To:**
```
DATABASE_URL=postgresql://wagtail:${{project.DATABASE_PASSWORD}}@kni-webapp-db-mwzipf:5432/wagtail?sslmode=disable&connect_timeout=10
```

### Step 2: Alternative Format (if above doesn't work)

Try this format:
```
DATABASE_URL=postgres://wagtail:${{project.DATABASE_PASSWORD}}@kni-webapp-db-mwzipf:5432/wagtail?sslmode=disable
```

### Step 3: If Still Not Working - Use Internal Django Settings

Instead of relying on DATABASE_URL parsing, add these environment variables:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=wagtail
DB_USER=wagtail
DB_PASSWORD=${{project.DATABASE_PASSWORD}}
DB_HOST=kni-webapp-db-mwzipf
DB_PORT=5432
DB_OPTIONS={"sslmode": "disable"}
```

## Why This Happens

1. **Docker Network**: Your PostgreSQL is running without SSL support (common for internal Docker networks)
2. **Django/psycopg2**: Default behavior tries to use SSL even with `sslmode=disable` in some URL formats
3. **URL Parsing**: Sometimes the SSL parameter isn't parsed correctly from the URL

## Quick Test

After updating the environment variable:
1. **Save** the environment changes
2. **Deploy** the application again
3. **Check logs** - you should see successful database connection

## Expected Success Log
```
Starting production Django application...
Running migrations...
Operations to perform:
  Apply all migrations: ...
Running migrations:
  No migrations to apply.
Starting Gunicorn server...
```

This is a common Docker deployment issue and the fix above resolves the SSL mismatch problem.