# Production Deployment Guide

This guide covers the production-ready optimizations implemented for the KNI Webapp Django/Wagtail application.

## Performance Optimizations Implemented

### 1. Redis Caching
- **Page Caching**: Full-page caching with 1-hour TTL
- **Session Caching**: Redis-backed sessions with 24-hour TTL
- **Database Query Caching**: Query result caching
- **Wagtail Cache**: Wagtail-specific page caching

### 2. Database Optimizations
- **Connection Pooling**: 60-second connection max age
- **Keep-Alive Settings**: Configured for optimal connection reuse
- **SSL Enforcement**: Automatic SSL for production databases

### 3. Static File Optimization
- **WhiteNoise**: Compressed static file serving
- **ETags**: Enabled for better caching
- **GZIP Compression**: Middleware-level compression
- **Long-term Caching**: 1-year cache headers for production

### 4. Gunicorn Configuration
- **Workers**: Configurable worker count (default: 2, recommended: 4 for production)
- **Request Limits**: Max 1000 requests per worker with jitter
- **Timeouts**: 60-second default, configurable
- **Logging**: Access and error logs to stdout

## Security Enhancements

### 1. HTTPS & SSL
- **Forced HTTPS Redirect**: All HTTP traffic redirected to HTTPS
- **HSTS Headers**: 1-year HSTS with subdomain inclusion
- **Secure Cookies**: All cookies marked secure and HTTP-only

### 2. Security Headers
- **Content Security Policy**: Basic CSP implementation
- **XSS Protection**: Browser XSS filter enabled
- **Content Type Sniffing**: Disabled
- **Frame Options**: Deny framing
- **Referrer Policy**: Strict origin when cross-origin

### 3. Session Security
- **Redis Sessions**: Sessions stored in Redis, not database
- **Secure Session Cookies**: HTTPOnly, Secure, SameSite=Lax
- **CSRF Protection**: Enhanced CSRF cookie security

## Monitoring & Health Checks

### Health Check Endpoints
- `/health/` - Basic health check
- `/health/detailed/` - Comprehensive health check with all services
- `/health/ready/` - Kubernetes readiness probe
- `/health/live/` - Kubernetes liveness probe

### Logging
- **Structured Logging**: JSON format in production
- **Log Rotation**: 10MB files, 5 backups
- **Security Logging**: Separate security event log
- **Error Tracking**: Comprehensive error logging

## Environment Variables

### Required Production Variables
```bash
# Security
DJANGO_SECRET_KEY=your-50+-character-secret-key
DEBUG=False

# Domain
PRIMARY_DOMAIN=your-domain.com
SECURE_SSL_REDIRECT=True

# Database
DATABASE_NAME=kni_webapp_prod
DATABASE_USER=kni_user_prod
DATABASE_PASSWORD=secure-password

# Redis
REDIS_PASSWORD=secure-redis-password
REDIS_URL=redis://:password@redis:6379/0

# Email
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=app-specific-password
```

### Performance Variables
```bash
# Gunicorn
GUNICORN_WORKERS=4                    # CPU cores * 2 + 1
GUNICORN_TIMEOUT=120                  # Request timeout
GUNICORN_MAX_REQUESTS=2000           # Requests per worker
GUNICORN_MAX_REQUESTS_JITTER=200     # Jitter for worker recycling
```

## Deployment Checklist

### Pre-Deployment
- [ ] Set all required environment variables
- [ ] Generate strong Django secret key (50+ characters)
- [ ] Configure secure database passwords
- [ ] Set up Redis with authentication
- [ ] Configure email settings
- [ ] Verify domain configuration

### Security Checklist
- [ ] DEBUG=False in production
- [ ] Strong secret key configured
- [ ] HTTPS redirect enabled
- [ ] Secure cookie settings active
- [ ] CSRF protection configured
- [ ] Database SSL enabled (for remote DBs)
- [ ] Redis password protection enabled

### Performance Checklist
- [ ] Redis caching configured and working
- [ ] Static files compressed (WhiteNoise)
- [ ] Gunicorn workers optimized for server capacity
- [ ] Database connection pooling enabled
- [ ] GZIP compression middleware active

### Monitoring Checklist
- [ ] Health check endpoints responding
- [ ] Detailed health check shows all services healthy
- [ ] Logging configured and rotating
- [ ] Error notifications set up (if applicable)

## Performance Targets

With these optimizations, you should achieve:

- **Page Load Times**: < 2 seconds for most pages
- **Database Response**: < 100ms for typical queries
- **Cache Hit Ratio**: > 80% for frequently accessed pages
- **Uptime**: > 99.5% with proper infrastructure
- **Security Score**: A+ rating on security headers scan

## Scaling Recommendations

### For Higher Traffic
1. Increase Gunicorn workers: `GUNICORN_WORKERS=8`
2. Add Redis clustering for cache scaling
3. Implement CDN for static assets
4. Consider database read replicas
5. Enable Redis persistence for cache resilience

### For Better Performance
1. Implement Elasticsearch for Wagtail search
2. Add image optimization and WebP support
3. Implement API caching for dynamic content
4. Add database query optimization and indexing
5. Consider async task processing with Celery

## Troubleshooting

### Common Issues
1. **500 Errors**: Check logs in `/app/logs/django.log`
2. **Cache Issues**: Verify Redis connectivity via `/health/detailed/`
3. **Static Files**: Ensure collectstatic ran successfully
4. **Database**: Check connection settings and SSL requirements

### Debug Commands
```bash
# Check health status
curl https://your-domain.com/health/detailed/

# View logs
docker logs container-name

# Test Redis connection
docker exec -it redis-container redis-cli ping
```

## Security Maintenance

### Regular Tasks
- [ ] Rotate Django secret key periodically
- [ ] Update database passwords regularly
- [ ] Monitor security logs for suspicious activity
- [ ] Keep dependencies updated
- [ ] Review and update CSP policies

### Monitoring
- Set up alerts for health check failures
- Monitor cache hit ratios
- Track response times and error rates
- Review security logs regularly

## Baseline Bootstrap Behavior

This repository bakes a small, versioned baseline dataset directly into the Docker image under `/app/baselineData` (~13MB). The entrypoint applies a strict, production-safe gate so this data only loads on brand new databases.

- New VPS Deployment
  - Fresh container starts with baseline data built in
  - Database is empty (0 tables)
  - Entrypoint detects empty DB and baseline.sql exists
  - Baseline loads automatically (SQL + media copy)
  - App is ready with initial data

- Redeploy/Update (push to main)
  - Container rebuilds with new code
  - Database already has tables (>0)
  - Baseline loading is skipped
  - Only migrations run
  - All user data preserved

- Development Override
  - You can still mount a local `baselineData` directory if needed
  - Useful for testing alternative datasets
  - Default behavior keeps image’s baked baseline

Implementation details
- Safety check: Entrypoint counts tables in `information_schema.tables` for schema `public`. If count == 0 and `LOAD_BASELINE=true` and `/app/baselineData/baseline.sql` exists → restore baseline; otherwise → run migrations only.
- Media: If `/app/baselineData/media` exists, it is copied into `/app/media` before the SQL restore.
- Config: `LOAD_BASELINE` defaults to `true` in Docker Compose. You can set it to `false` to disable automatic baseline restores entirely.

How to test the safety mechanism
1. Fresh bootstrap (should load baseline)
   - `docker compose down -v`
   - `docker compose --env-file .env.local up -d`
   - Check `docker compose logs web` for:
     - `Empty database detected, will load baseline data`
     - `Baseline data loaded successfully!`
   - Visit `/admin/` to confirm content exists

2. Redeploy/update (should skip baseline)
   - Keep volumes intact (do NOT run `-v`)
   - Rebuild/restart web: `docker compose build web && docker compose up -d web`
   - Check logs show migrations only (no baseline restore):
     - `Running database migrations...`

Notes
- This approach is CI/CD-safe: the baseline never overwrites existing data.
- For one-off resets in development, delete the `postgres_data` volume and keep `LOAD_BASELINE=true`.
