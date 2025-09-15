#!/bin/bash

# =============================================================================
# KNI Webapp - Automated Backup Scheduler
# =============================================================================
# This script implements automated backup scheduling with retention policies
# Compatible with cron and Docker environments
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="${PROJECT_DIR}/logs/backup"
BACKUP_DIR="${PROJECT_DIR}/backups"
LOCK_FILE="/tmp/kni_backup.lock"

# Default settings
BACKUP_TYPE="full"
RETENTION_DAYS=30
INCLUDE_MEDIA="false"
COMPRESS="true"
TENANT_SCHEMA=""
LOG_LEVEL="INFO"
NOTIFICATION_EMAIL=""
SLACK_WEBHOOK=""

# Load environment variables if available
if [ -f "${PROJECT_DIR}/.env.local" ]; then
    export $(grep -v '^#' "${PROJECT_DIR}/.env.local" | xargs)
fi

# Override with environment variables
BACKUP_TYPE="${BACKUP_SCHEDULE_TYPE:-$BACKUP_TYPE}"
RETENTION_DAYS="${BACKUP_RETENTION_DAYS:-$RETENTION_DAYS}"
INCLUDE_MEDIA="${BACKUP_INCLUDE_MEDIA:-$INCLUDE_MEDIA}"
COMPRESS="${BACKUP_COMPRESS:-$COMPRESS}"
TENANT_SCHEMA="${BACKUP_TENANT_SCHEMA:-$TENANT_SCHEMA}"
LOG_LEVEL="${BACKUP_LOG_LEVEL:-$LOG_LEVEL}"
NOTIFICATION_EMAIL="${BACKUP_NOTIFICATION_EMAIL:-$NOTIFICATION_EMAIL}"
SLACK_WEBHOOK="${BACKUP_SLACK_WEBHOOK:-$SLACK_WEBHOOK}"

# =============================================================================
# Utility Functions
# =============================================================================

log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    case "$level" in
        "ERROR")
            echo -e "${RED}[$timestamp] ERROR: $message${NC}" >&2
            ;;
        "WARN")
            echo -e "${YELLOW}[$timestamp] WARN: $message${NC}" >&2
            ;;
        "INFO")
            echo -e "${GREEN}[$timestamp] INFO: $message${NC}"
            ;;
        "DEBUG")
            if [ "$LOG_LEVEL" = "DEBUG" ]; then
                echo -e "${BLUE}[$timestamp] DEBUG: $message${NC}"
            fi
            ;;
    esac

    # Also log to file
    mkdir -p "$LOG_DIR"
    echo "[$timestamp] $level: $message" >> "$LOG_DIR/backup_scheduler.log"
}

acquire_lock() {
    if [ -f "$LOCK_FILE" ]; then
        local pid=$(cat "$LOCK_FILE")
        if kill -0 "$pid" 2>/dev/null; then
            log "WARN" "Another backup process is running (PID: $pid)"
            exit 1
        else
            log "DEBUG" "Removing stale lock file"
            rm -f "$LOCK_FILE"
        fi
    fi

    echo $$ > "$LOCK_FILE"
    log "DEBUG" "Acquired lock (PID: $$)"
}

release_lock() {
    rm -f "$LOCK_FILE"
    log "DEBUG" "Released lock"
}

cleanup() {
    release_lock
    log "INFO" "Backup scheduler cleanup completed"
}

trap cleanup EXIT

send_notification() {
    local status="$1"
    local message="$2"
    local details="$3"

    # Email notification
    if [ -n "$NOTIFICATION_EMAIL" ] && command -v mail >/dev/null 2>&1; then
        {
            echo "KNI Webapp Backup Status: $status"
            echo ""
            echo "Message: $message"
            echo "Time: $(date)"
            echo "Host: $(hostname)"
            echo ""
            echo "Details:"
            echo "$details"
        } | mail -s "KNI Backup $status" "$NOTIFICATION_EMAIL"

        log "DEBUG" "Email notification sent to $NOTIFICATION_EMAIL"
    fi

    # Slack notification
    if [ -n "$SLACK_WEBHOOK" ] && command -v curl >/dev/null 2>&1; then
        local color="good"
        [ "$status" != "SUCCESS" ] && color="danger"

        local payload=$(cat <<EOF
{
    "attachments": [
        {
            "color": "$color",
            "title": "KNI Webapp Backup $status",
            "text": "$message",
            "fields": [
                {
                    "title": "Time",
                    "value": "$(date)",
                    "short": true
                },
                {
                    "title": "Host",
                    "value": "$(hostname)",
                    "short": true
                }
            ],
            "footer": "KNI Backup Scheduler"
        }
    ]
}
EOF
        )

        curl -X POST -H 'Content-type: application/json' \
             --data "$payload" "$SLACK_WEBHOOK" >/dev/null 2>&1

        log "DEBUG" "Slack notification sent"
    fi
}

check_dependencies() {
    local missing_deps=()

    # Check for Python and Django
    if ! command -v python >/dev/null 2>&1; then
        missing_deps+=("python")
    fi

    # Check for PostgreSQL client tools
    local pg_dump_found=false
    for pg_path in "/usr/bin/pg_dump" "/opt/homebrew/bin/pg_dump" "/usr/local/bin/pg_dump" "pg_dump"; do
        if command -v "$pg_path" >/dev/null 2>&1; then
            pg_dump_found=true
            break
        fi
    done

    if [ "$pg_dump_found" = false ]; then
        missing_deps+=("pg_dump")
    fi

    # Check for compression tools if needed
    if [ "$COMPRESS" = "true" ]; then
        if ! command -v gzip >/dev/null 2>&1; then
            missing_deps+=("gzip")
        fi
    fi

    if [ ${#missing_deps[@]} -gt 0 ]; then
        log "ERROR" "Missing dependencies: ${missing_deps[*]}"
        exit 1
    fi

    log "DEBUG" "All dependencies satisfied"
}

determine_backup_type() {
    local hour=$(date +%H)
    local day=$(date +%u)  # 1=Monday, 7=Sunday
    local date=$(date +%d)

    # Monthly backup on 1st of month at 2 AM
    if [ "$date" = "01" ] && [ "$hour" = "02" ]; then
        echo "baseline"
        return
    fi

    # Weekly full backup on Sunday at 1 AM
    if [ "$day" = "7" ] && [ "$hour" = "01" ]; then
        echo "full"
        return
    fi

    # Daily incremental backup at midnight
    if [ "$hour" = "00" ]; then
        echo "incremental"
        return
    fi

    # Default to the configured type
    echo "$BACKUP_TYPE"
}

# =============================================================================
# Main Backup Functions
# =============================================================================

run_backup() {
    local backup_type="$1"
    local start_time=$(date +%s)

    log "INFO" "Starting $backup_type backup"

    # Build Django command
    local cmd_args=(
        "backup_tenant"
        "--backup-type" "$backup_type"
        "--retention-days" "$RETENTION_DAYS"
    )

    if [ "$INCLUDE_MEDIA" = "true" ]; then
        cmd_args+=("--include-media")
    fi

    if [ "$COMPRESS" = "true" ]; then
        cmd_args+=("--compress")
    fi

    if [ -n "$TENANT_SCHEMA" ]; then
        cmd_args+=("--schema" "$TENANT_SCHEMA")
    fi

    # Execute backup
    local backup_output
    local backup_exit_code

    log "DEBUG" "Executing: python manage.py ${cmd_args[*]}"

    if backup_output=$(cd "$PROJECT_DIR" && python manage.py "${cmd_args[@]}" 2>&1); then
        backup_exit_code=0
    else
        backup_exit_code=$?
    fi

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))

    if [ $backup_exit_code -eq 0 ]; then
        log "INFO" "Backup completed successfully in ${duration}s"

        # Parse backup output for details
        local backup_details=$(echo "$backup_output" | grep -E "(Schema|Backup|manifest)" | tail -10)

        send_notification "SUCCESS" "Backup completed successfully" "$backup_details"

        return 0
    else
        log "ERROR" "Backup failed with exit code $backup_exit_code"
        log "ERROR" "Output: $backup_output"

        send_notification "FAILED" "Backup failed" "$backup_output"

        return 1
    fi
}

run_cleanup() {
    log "INFO" "Running backup cleanup"

    local cleanup_output
    local cleanup_exit_code

    if cleanup_output=$(cd "$PROJECT_DIR" && python manage.py cleanup_backups --retention-policy default --force 2>&1); then
        cleanup_exit_code=0
        log "INFO" "Cleanup completed successfully"
        log "DEBUG" "Cleanup output: $cleanup_output"
    else
        cleanup_exit_code=$?
        log "WARN" "Cleanup failed with exit code $cleanup_exit_code"
        log "WARN" "Output: $cleanup_output"
    fi

    return $cleanup_exit_code
}

check_backup_health() {
    local health_status="HEALTHY"
    local health_details=""

    # Check backup directory
    if [ ! -d "$BACKUP_DIR" ]; then
        health_status="UNHEALTHY"
        health_details+="Backup directory missing\n"
    fi

    # Check for recent backups
    local recent_backup=$(find "$BACKUP_DIR" -name "*.sql*" -mtime -1 | head -1)
    if [ -z "$recent_backup" ]; then
        health_status="WARNING"
        health_details+="No recent backups found (last 24 hours)\n"
    fi

    # Check disk space
    local disk_usage=$(df "$BACKUP_DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ "$disk_usage" -gt 90 ]; then
        health_status="WARNING"
        health_details+="Disk usage high: ${disk_usage}%\n"
    fi

    # Check for corrupted backups
    local corrupted_count=0
    if [ -d "$BACKUP_DIR/manifests" ]; then
        for manifest in "$BACKUP_DIR/manifests"/backup_manifest_*.json; do
            [ -f "$manifest" ] || continue
            if ! python -m json.tool "$manifest" >/dev/null 2>&1; then
                ((corrupted_count++))
            fi
        done
    fi

    if [ $corrupted_count -gt 0 ]; then
        health_status="WARNING"
        health_details+="Found $corrupted_count corrupted backup manifests\n"
    fi

    log "INFO" "Backup health check: $health_status"
    if [ -n "$health_details" ]; then
        log "INFO" "Health details: $health_details"
    fi

    # Send notification if unhealthy
    if [ "$health_status" != "HEALTHY" ]; then
        send_notification "$health_status" "Backup health check warning" "$health_details"
    fi
}

# =============================================================================
# CLI Interface
# =============================================================================

show_help() {
    cat << EOF
KNI Webapp Backup Scheduler

USAGE:
    $0 [OPTIONS] [COMMAND]

COMMANDS:
    backup [TYPE]     Run backup (auto-detect type if not specified)
    cleanup          Run backup cleanup with retention policy
    health           Check backup system health
    schedule         Run scheduled backup (auto-determine type)
    help             Show this help

BACKUP TYPES:
    full             Complete database backup
    incremental      Data-only backup
    baseline         Template baseline backup

OPTIONS:
    --retention-days N    Retention period (default: 30)
    --include-media      Include media files
    --compress           Compress backup files
    --schema SCHEMA      Backup specific schema only
    --log-level LEVEL    Set log level (DEBUG, INFO, WARN, ERROR)

ENVIRONMENT VARIABLES:
    BACKUP_SCHEDULE_TYPE       Default backup type
    BACKUP_RETENTION_DAYS      Retention period
    BACKUP_INCLUDE_MEDIA       Include media files (true/false)
    BACKUP_COMPRESS            Compress backups (true/false)
    BACKUP_TENANT_SCHEMA       Specific tenant schema
    BACKUP_LOG_LEVEL           Logging level
    BACKUP_NOTIFICATION_EMAIL  Email for notifications
    BACKUP_SLACK_WEBHOOK       Slack webhook URL

EXAMPLES:
    $0 backup full              # Run full backup
    $0 schedule                 # Run scheduled backup
    $0 cleanup                  # Clean up old backups
    $0 health                   # Check system health

CRON EXAMPLES:
    # Daily backup at midnight
    0 0 * * * /path/to/backup_scheduler.sh schedule

    # Weekly cleanup on Sunday at 3 AM
    0 3 * * 0 /path/to/backup_scheduler.sh cleanup

    # Health check every 6 hours
    0 */6 * * * /path/to/backup_scheduler.sh health

EOF
}

# =============================================================================
# Main Script Logic
# =============================================================================

main() {
    # Parse command line arguments
    local command="schedule"  # default command

    while [[ $# -gt 0 ]]; do
        case $1 in
            --retention-days)
                RETENTION_DAYS="$2"
                shift 2
                ;;
            --include-media)
                INCLUDE_MEDIA="true"
                shift
                ;;
            --compress)
                COMPRESS="true"
                shift
                ;;
            --schema)
                TENANT_SCHEMA="$2"
                shift 2
                ;;
            --log-level)
                LOG_LEVEL="$2"
                shift 2
                ;;
            backup|cleanup|health|schedule|help)
                command="$1"
                shift
                ;;
            full|incremental|baseline)
                if [ "$command" = "backup" ]; then
                    BACKUP_TYPE="$1"
                fi
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                log "ERROR" "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done

    # Initialize
    log "INFO" "KNI Webapp Backup Scheduler starting"
    log "DEBUG" "Command: $command, Type: $BACKUP_TYPE, Retention: $RETENTION_DAYS days"

    acquire_lock
    check_dependencies

    # Execute command
    case "$command" in
        "backup")
            run_backup "$BACKUP_TYPE"
            ;;
        "cleanup")
            run_cleanup
            ;;
        "health")
            check_backup_health
            ;;
        "schedule")
            local auto_type=$(determine_backup_type)
            log "INFO" "Auto-determined backup type: $auto_type"
            run_backup "$auto_type"

            # Run cleanup after successful backup
            if [ $? -eq 0 ]; then
                run_cleanup
            fi
            ;;
        "help")
            show_help
            ;;
        *)
            log "ERROR" "Unknown command: $command"
            show_help
            exit 1
            ;;
    esac

    log "INFO" "Backup scheduler completed"
}

# Run main function with all arguments
main "$@"