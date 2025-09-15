# Enhanced Baseline and Backup System Documentation

## Overview

The KNI Webapp now includes a comprehensive backup and restore system designed for multi-tenant customer data protection. This system provides schema-aware backups, automatic scheduling, rollback capabilities, and seamless integration with the existing Docker workflow.

## System Architecture

### Core Components

1. **Core Baseline**: Framework infrastructure (public schema)
2. **Tenant Schemas**: Customer-specific content (customer_a, customer_b, etc.)
3. **Template Baselines**: Industry-specific starter content

### Backup Strategy

- **Incremental Daily**: Schema changes only
- **Full Weekly**: Complete schema dump
- **Baseline Monthly**: Update template baselines
- **Retention**: 7 daily, 4 weekly, 12 monthly

## Management Commands

### 1. `backup_tenant` - Schema-aware Backups

Creates backups for specific schemas or all schemas with comprehensive metadata.

```bash
# Full backup with media files
python manage.py backup_tenant --backup-type full --include-media --compress

# Incremental backup for specific schema
python manage.py backup_tenant --schema customer_a --backup-type incremental

# Baseline backup for templates
python manage.py backup_tenant --backup-type baseline --include-media
```

**Options:**
- `--schema SCHEMA`: Specific schema to backup
- `--tenant TENANT`: Tenant identifier for naming
- `--backup-type {full,incremental,baseline}`: Type of backup
- `--include-media`: Include media files
- `--compress`: Compress backup files with gzip
- `--retention-days N`: Retention period in days

### 2. `restore_tenant` - Restore with Rollback

Restores tenant data from backups or baselines with automatic rollback capability.

```bash
# Interactive restore mode
python manage.py restore_tenant --list-available

# Restore from baseline
python manage.py restore_tenant --baseline --include-media

# Restore from specific backup
python manage.py restore_tenant --backup-file backups/data/customer_a_20241215_143022.sql

# Restore from manifest
python manage.py restore_tenant --manifest backups/manifests/backup_manifest_20241215_143022.json
```

**Options:**
- `--baseline`: Restore from baseline template
- `--backup-file PATH`: Restore from specific backup file
- `--manifest PATH`: Restore from backup manifest
- `--create-rollback`: Create rollback backup before restore (default: true)
- `--dry-run`: Show what would be restored without making changes

### 3. `list_backups` - Backup Inventory

Lists available backups with detailed information and filtering options.

```bash
# List all backups in table format
python manage.py list_backups --include-baselines

# JSON output for programmatic use
python manage.py list_backups --format json

# Filter by schema
python manage.py list_backups --schema customer_a --limit 10
```

**Options:**
- `--format {table,json,csv}`: Output format
- `--schema SCHEMA`: Filter by specific schema
- `--type {full,incremental,baseline}`: Filter by backup type
- `--limit N`: Limit number of results

### 4. `cleanup_backups` - Retention Management

Enforces retention policies and cleans up old backups.

```bash
# Default retention policy
python manage.py cleanup_backups --retention-policy default

# Custom retention settings
python manage.py cleanup_backups --retention-policy custom --daily-retention 14 --weekly-retention 8

# Dry run to see what would be deleted
python manage.py cleanup_backups --dry-run
```

**Retention Policies:**
- `default`: 7 daily, 4 weekly, 12 monthly
- `aggressive`: 3 daily, 2 weekly, 6 monthly
- `conservative`: 14 daily, 8 weekly, 24 monthly
- `custom`: User-defined settings

## Makefile Integration

### Quick Commands

```bash
# Manual backup creation
make backup

# Interactive restore interface
make restore

# List available backups
make list-backups

# Clean old backups
make clean-backups

# Check backup system health
make backup-health
```

### Advanced Commands

```bash
# Full backup with all options
make backup-full

# Incremental backup only
make backup-incremental

# Schema-specific backup
make backup-schema

# Restore from baseline only
make restore-baseline

# Scheduled backup (auto-determine type)
make backup-schedule
```

## Automated Scheduling

### Backup Scheduler Script

The `scripts/backup_scheduler.sh` script provides automated backup scheduling compatible with cron.

```bash
# Manual execution
./scripts/backup_scheduler.sh schedule

# Health check
./scripts/backup_scheduler.sh health

# Specific backup type
./scripts/backup_scheduler.sh backup full
```

### Cron Configuration

```bash
# Daily backup at midnight
0 0 * * * /path/to/kni_webapp/scripts/backup_scheduler.sh schedule

# Weekly cleanup on Sunday at 3 AM
0 3 * * 0 /path/to/kni_webapp/scripts/backup_scheduler.sh cleanup

# Health check every 6 hours
0 */6 * * * /path/to/kni_webapp/scripts/backup_scheduler.sh health
```

### Environment Variables

```bash
# Backup configuration
BACKUP_SCHEDULE_TYPE=full           # Default backup type
BACKUP_RETENTION_DAYS=30            # Retention period
BACKUP_INCLUDE_MEDIA=true           # Include media files
BACKUP_COMPRESS=true                # Compress backups
BACKUP_TENANT_SCHEMA=customer_a     # Specific tenant schema

# Notification settings
BACKUP_NOTIFICATION_EMAIL=admin@example.com
BACKUP_SLACK_WEBHOOK=https://hooks.slack.com/...

# Logging
BACKUP_LOG_LEVEL=INFO               # DEBUG, INFO, WARN, ERROR
```

## Docker Integration

### Environment Variables for Restore

```bash
# Restore from specific backup file
RESTORE_BACKUP_FILE=/app/backups/data/backup.sql

# Restore from backup manifest
RESTORE_BACKUP_MANIFEST=/app/backups/manifests/manifest.json

# Restore from latest backup
RESTORE_LATEST_BACKUP=true

# Load baseline data (default behavior)
LOAD_BASELINE=true
```

### Container Startup Behavior

1. **Priority Order**: Specific backup file → Backup manifest → Latest backup → Baseline
2. **Empty Database Check**: Only restores if database has no tables
3. **Fallback Logic**: Falls back to baseline if backup restore fails
4. **Migration Handling**: Skips migrations if data is restored from backup/baseline

### Volume Mounting

```yaml
# docker-compose.yml
volumes:
  - ./backups:/app/backups          # Backup storage
  - ./baselineData:/app/baselineData # Baseline templates
```

## Multi-tenant Considerations

### Schema Detection

The system automatically detects tenant schemas by excluding system schemas:
- `public` (always included for core data)
- `information_schema`, `pg_catalog`, `pg_toast` (excluded)

### Tenant Isolation

- Each tenant schema is backed up separately
- Cross-tenant data isolation maintained
- Schema-specific restore capabilities
- Tenant-aware file naming conventions

### Security

- No cross-tenant data leakage
- Secure file permissions on backup files
- Hash verification for backup integrity
- Rollback protection with automatic backup creation

## File Structure

```
kni_webapp/
├── apps/core/management/commands/
│   ├── backup_tenant.py           # Main backup command
│   ├── restore_tenant.py          # Restore with rollback
│   ├── list_backups.py           # Backup inventory
│   └── cleanup_backups.py        # Retention management
├── scripts/
│   └── backup_scheduler.sh       # Automated scheduling
├── backups/                      # Backup storage (created automatically)
│   ├── data/                    # Database dumps
│   ├── media/                   # Media file backups
│   ├── manifests/               # Backup metadata
│   └── rollback/                # Rollback backups
├── baselineData/                # Baseline templates
│   ├── baseline.sql            # Core baseline
│   └── media/                  # Baseline media files
└── logs/backup/                 # Backup logs (created by scheduler)
```

## Backup Manifest Format

```json
{
  "timestamp": "2024-12-15T14:30:22.123456",
  "backup_type": "full",
  "retention_days": 30,
  "compressed": true,
  "include_media": true,
  "schemas": [
    {
      "schema": "public",
      "tenant": "core",
      "filename": "core_public_full_20241215_143022.sql.gz",
      "filepath": "/app/backups/data/core_public_full_20241215_143022.sql.gz",
      "size": 1048576,
      "hash": "sha256:abc123...",
      "media_backup": "/app/backups/media/core_media_20241215_143022.tar.gz",
      "timestamp": "20241215_143022",
      "type": "full"
    }
  ]
}
```

## Workflows

### Fresh Customer Deployment

1. **Container Start**: `LOAD_BASELINE=true`
2. **Baseline Loading**: Automatic baseline data load
3. **First Backup**: Create initial customer backup
4. **Schedule Setup**: Configure automated backups

```bash
# Deploy new customer
LOAD_BASELINE=true docker-compose up -d

# Create first backup
make backup-full

# Setup automated backups
./scripts/backup_scheduler.sh schedule
```

### Daily Operations

1. **Automated Backups**: Cron-scheduled backups
2. **Health Monitoring**: Regular health checks
3. **Retention Management**: Automatic cleanup

### Issue Recovery

1. **Problem Detection**: System monitoring alerts
2. **Backup Assessment**: List available backups
3. **Restoration**: Choose appropriate backup
4. **Verification**: Confirm system functionality

```bash
# Assess available backups
make list-backups

# Interactive restore
make restore

# Verify restoration
make backup-health
```

### Reset to Baseline

1. **Confirmation**: User confirmation required
2. **Rollback Creation**: Automatic backup before reset
3. **Baseline Restoration**: Clean slate deployment

```bash
# Reset to baseline with confirmation
make restore-baseline
```

## Monitoring and Health Checks

### Health Check Indicators

- **Backup Freshness**: Recent backups within 24 hours
- **Disk Space**: Backup directory disk usage
- **File Integrity**: Backup file corruption detection
- **Retention Compliance**: Backup retention policy adherence

### Notification Systems

- **Email Notifications**: Success/failure alerts
- **Slack Integration**: Real-time backup status
- **Log Files**: Detailed operation logs
- **Health Endpoints**: Programmatic health checks

## Best Practices

### Backup Strategy

1. **Regular Schedule**: Daily incremental, weekly full, monthly baseline
2. **Retention Policy**: Balance storage cost with recovery needs
3. **Compression**: Enable for storage efficiency
4. **Media Inclusion**: Include for complete restoration
5. **Health Monitoring**: Regular system health checks

### Recovery Planning

1. **Test Restores**: Regular restoration testing
2. **Recovery Documentation**: Clear recovery procedures
3. **Rollback Preparation**: Always create rollback backups
4. **Verification Steps**: Post-restore verification checklist

### Security Considerations

1. **File Permissions**: Secure backup file access
2. **Data Encryption**: Consider encrypting sensitive backups
3. **Access Control**: Limit backup management access
4. **Audit Trail**: Maintain backup operation logs

## Troubleshooting

### Common Issues

#### Backup Creation Fails

```bash
# Check PostgreSQL client tools
which pg_dump

# Verify database connectivity
python manage.py dbshell

# Check disk space
df -h /path/to/backups

# Review logs
tail -f logs/backup/backup_scheduler.log
```

#### Restore Operation Fails

```bash
# Verify backup file integrity
python manage.py list_backups --format json

# Check database permissions
python manage.py dbshell

# Test with dry run
python manage.py restore_tenant --dry-run --backup-file path/to/backup.sql
```

#### Scheduler Not Running

```bash
# Check script permissions
ls -la scripts/backup_scheduler.sh

# Test manual execution
./scripts/backup_scheduler.sh health

# Verify cron configuration
crontab -l
```

### Log Analysis

```bash
# Backup scheduler logs
tail -f logs/backup/backup_scheduler.log

# Django management command logs
python manage.py backup_tenant --verbosity 2

# System logs
journalctl -u cron -f
```

## Migration from Existing System

If you have an existing backup system, follow these steps:

1. **Backup Current Data**: Create backup with existing system
2. **Install New System**: Deploy enhanced backup commands
3. **Create New Baseline**: Generate baseline from current state
4. **Test Restoration**: Verify new system works
5. **Update Automation**: Switch to new scheduler
6. **Monitor Transition**: Ensure smooth operation

```bash
# Create baseline from existing system
make dev-baseline

# Test new backup system
make backup-full

# Verify restoration capability
make restore --dry-run
```

This enhanced backup and restore system provides enterprise-grade data protection for the KNI Webapp with comprehensive automation, monitoring, and recovery capabilities.