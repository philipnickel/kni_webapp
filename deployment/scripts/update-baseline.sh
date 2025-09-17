#!/bin/bash
set -euo pipefail

# Sync the latest named baseline backup into deployment/baseline/
BACKUPS_DIR="${1:-backups}"
DEST_DIR="${2:-deployment/baseline}"

if ! ls "$BACKUPS_DIR"/baseline_*.json >/dev/null 2>&1; then
  echo "No baseline backups found in $BACKUPS_DIR. Run 'python manage.py native_backup --name baseline --include-media' first." >&2
  exit 1
fi

LATEST_JSON=$(ls -1t "$BACKUPS_DIR"/baseline_*.json | head -n1)
BASE_NAME=$(basename "$LATEST_JSON" .json)
BASE_ROOT=$(dirname "$LATEST_JSON")
TIMESTAMP=${BASE_NAME#baseline_}
MEDIA_SOURCE="$BASE_ROOT/baseline_media_${TIMESTAMP}"
METADATA_SOURCE="$LATEST_JSON.metadata.json"

mkdir -p "$DEST_DIR"
cp "$LATEST_JSON" "$DEST_DIR/baseline.json"

if [ -f "$METADATA_SOURCE" ]; then
  cp "$METADATA_SOURCE" "$DEST_DIR/baseline.metadata.json"
fi

if [ -d "$MEDIA_SOURCE" ]; then
  rm -rf "$DEST_DIR/baseline_media"
  mkdir -p "$DEST_DIR"
  cp -R "$MEDIA_SOURCE" "$DEST_DIR/baseline_media"
else
  echo "Warning: no media directory found at $MEDIA_SOURCE" >&2
  rm -rf "$DEST_DIR/baseline_media"
  mkdir -p "$DEST_DIR/baseline_media"
fi

echo "Baseline package updated in $DEST_DIR"
