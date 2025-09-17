# Baseline Package

This directory holds the database fixture and media assets that are baked into the production image. Replace `baseline.json` and the contents of `baseline_media/` with the latest export generated via `python manage.py native_backup --name baseline --include-media` followed by `deployment/scripts/update-baseline.sh`.
