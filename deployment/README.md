# Configuration Directory

This directory contains all configuration files for the KNI Webapp project.

## Structure

### `deployment/`
Contains deployment configuration files:
- `dokploy-template.yml` - Production SaaS deployment template
- `dokploy-preview.yml` - Preview deployment template  
- `docker-compose.yml` - Production Docker Compose
- `compose.dev.yml` - Development Docker Compose

### `docker/`
Contains Docker-related files:
- `Dockerfile` - Multi-stage Docker build configuration
- `.dockerignore` - Docker build ignore patterns

### `frontend/`
Contains frontend build configuration:
- `package.json` - Node.js dependencies and scripts
- `package-lock.json` - Dependency lock file
- `tailwind.config.js` - Tailwind CSS configuration
- `postcss.config.js` - PostCSS configuration

### `environments/`
Contains environment configuration templates:
- `env.dev.template` - Development environment template
- `env.saas.template` - SaaS deployment environment template
- `.env.dev` - Active development environment (symlinked to root)

## Usage

### Development
```bash
# Copy template to create your environment
cp config/environments/env.dev.template .env.dev

# Or use the make command
make dev-setup
```

### Production Deployment
```bash
# Use the deployment templates in Dokploy
# Files are located in config/deployment/
```

## File Locations

- **Development**: `config/environments/.env.dev` (symlinked to `.env.dev`)
- **Production**: Use `config/deployment/dokploy-template.yml`
- **Preview**: Use `config/deployment/dokploy-preview.yml`
