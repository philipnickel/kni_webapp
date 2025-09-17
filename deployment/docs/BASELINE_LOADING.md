# Production Baseline Data Loading

This document explains how to load baseline data in production deployments using Dokploy and Docker.

## Overview

The system supports loading baseline data during container startup, which is useful for:
- Initial deployment with sample content
- Setting up new environments with predefined data
- Demo deployments with realistic content

## Environment Variables

### `LOAD_BASELINE_ON_START`
- **Type**: Boolean (`true`/`false`)
- **Default**: `false`
- **Description**: Enable/disable baseline data loading on container startup

### `BASELINE_BACKUP_FILE`
- **Type**: String
- **Default**: `baseline.json`
- **Description**: Filename of the baseline backup file to load

## Usage

### For Initial Deployment (First Time)

1. **Set environment variables in Dokploy**:
   ```env
   LOAD_BASELINE_ON_START=true
   BASELINE_BACKUP_FILE=baseline.json
   ```

2. **Deploy the application**
   - The container will automatically load baseline data during startup
   - Check logs for confirmation: "✅ Baseline restored successfully"

### For Subsequent Deployments

1. **Disable baseline loading**:
   ```env
   LOAD_BASELINE_ON_START=false
   ```

2. **Deploy the application**
   - The container will skip baseline loading and run normal migrations
   - Existing data will be preserved

## Baseline Data Files

The baseline data is included in the Docker image at `/app/backups/`:
- `baseline.json` - Database fixture with 83+ objects
- `baseline.metadata.json` - Metadata about the backup
- `baseline_media/` - Associated media files

## How It Works

1. **Container Startup**: The entrypoint script checks `LOAD_BASELINE_ON_START`
2. **Baseline Loading**: If enabled, runs `python manage.py native_restore --backup baseline.json --include-media --flush --force`
3. **Fallback**: If baseline loading fails or is disabled, runs normal migrations
4. **Verification**: Logs show number of objects loaded and success status

## Workflow Example

### Initial Deployment
```bash
# In Dokploy environment variables:
LOAD_BASELINE_ON_START=true
BASELINE_BACKUP_FILE=baseline.json

# Deploy → Container starts → Baseline data loaded (83 objects)
# Result: JCleemann Byg website with sample content
```

### Production Updates
```bash
# In Dokploy environment variables:
LOAD_BASELINE_ON_START=false

# Deploy → Container starts → Normal migrations run
# Result: Existing content preserved, only schema updates applied
```

## Troubleshooting

### Baseline Loading Failed
- Check container logs for error messages
- Verify baseline file exists in `/app/backups/`
- Ensure database is accessible and empty

### Baseline Not Loading
- Verify `LOAD_BASELINE_ON_START=true` is set
- Check that baseline file contains valid JSON data
- Confirm file permissions allow reading

### Performance Impact
- Baseline loading adds ~30 seconds to startup time
- Only runs once during initial deployment
- No impact on normal application performance

## Security Considerations

- Baseline data is bundled in the Docker image
- Contains sample data, not production secrets
- Safe to use in demo/staging environments
- For production, review baseline content before deployment

## Custom Baseline Data

To use custom baseline data:

1. **Create your baseline**:
   ```bash
   make baseline  # Creates baseline from current local state
   ```

2. **Update deployment baseline**:
   ```bash
   cp backups/baseline_*.json deployment/baseline/baseline.json
   cp backups/baseline_*.metadata.json deployment/baseline/baseline.metadata.json
   cp -r backups/baseline_media_* deployment/baseline/baseline_media/
   ```

3. **Rebuild Docker image**:
   ```bash
   docker build -f deployment/Dockerfile .
   ```

4. **Deploy with custom baseline**:
   ```env
   LOAD_BASELINE_ON_START=true
   ```