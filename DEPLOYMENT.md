# Deployment Configuration

This document describes the deployment configuration and secret key handling for the KNI Webapp.

## Secret Key Management

The application now includes robust secret key handling that works across different deployment environments:

### Automatic Secret Key Generation

The deployment process will automatically handle Django secret keys with the following priority:

1. **Environment Variable**: Uses `DJANGO_SECRET_KEY` if provided
2. **Auto-Generation**: Generates a secure key if none exists
3. **Development Fallback**: Uses development key in DEBUG mode

### Coolify Deployment

For Coolify deployments:

- **Production**: Set `DJANGO_SECRET_KEY` in the main environment variables
- **Preview**: Secret keys are automatically generated if not set
- **Fresh Deployments**: Work out-of-the-box without manual configuration

### Manual Secret Key Generation

To generate a new secret key manually:

```bash
# Print a new secret key
python manage.py generate_secret_key --print-only

# Write to .env file
python manage.py generate_secret_key --env-file .env
```

### Security Notes

- Each deployment generates its own unique secret key if none is provided
- Production deployments will log a warning if using auto-generated keys
- Auto-generated keys are cryptographically secure using Django's built-in utilities

## Environment Variables

### Required for Production
- None! The application will work with minimal configuration

### Optional Configuration
- `DJANGO_SECRET_KEY`: Custom secret key (recommended for production)
- `DEBUG`: Enable/disable debug mode (default: False in production)
- `DATABASE_URL`: Database connection string (auto-configured in Docker)
- `REDIS_URL`: Redis connection string (auto-configured in Docker)

### Domain Configuration
The application automatically detects domains from Coolify environment variables:
- `COOLIFY_FQDN`: Primary domain source
- `COOLIFY_URL`: Fallback domain source

## Deployment Process

1. **Docker Build**: Creates production-ready image with static files
2. **Database Setup**: Waits for database, runs migrations or loads baseline
3. **Secret Key**: Generates if missing
4. **Static Files**: Collects and serves via WhiteNoise
5. **Health Checks**: Provides readiness and liveness endpoints

## Troubleshooting

### Common Issues

**"required variable DJANGO_SECRET_KEY is missing a value"**
- Fixed: Docker Compose now handles missing keys gracefully

**Preview deployments fail**
- Fixed: Auto-generation works in all deployment contexts

**Manual environment configuration needed**
- Fixed: Works out-of-the-box on fresh Coolify instances