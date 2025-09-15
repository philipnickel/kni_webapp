import json
import datetime
from pathlib import Path
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Clean up old backups according to retention policies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--backup-dir",
            dest="backup_dir",
            help="Backup directory (default: backups/)",
        )
        parser.add_argument(
            "--retention-policy",
            dest="retention_policy",
            choices=["default", "aggressive", "conservative", "custom"],
            default="default",
            help="Retention policy to apply (default: default)",
        )
        parser.add_argument(
            "--daily-retention",
            dest="daily_retention",
            type=int,
            default=7,
            help="Keep daily backups for N days (default: 7)",
        )
        parser.add_argument(
            "--weekly-retention",
            dest="weekly_retention",
            type=int,
            default=4,
            help="Keep weekly backups for N weeks (default: 4)",
        )
        parser.add_argument(
            "--monthly-retention",
            dest="monthly_retention",
            type=int,
            default=12,
            help="Keep monthly backups for N months (default: 12)",
        )
        parser.add_argument(
            "--rollback-retention",
            dest="rollback_retention",
            type=int,
            default=7,
            help="Keep rollback backups for N days (default: 7)",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force cleanup without confirmation",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be deleted without making changes",
        )
        parser.add_argument(
            "--schema",
            dest="schema",
            help="Clean up backups for specific schema only",
        )

    def handle(self, *args, **options):
        self.backup_dir = Path(options.get("backup_dir") or (Path(settings.BASE_DIR) / "backups"))

        if not self.backup_dir.exists():
            self.stdout.write("No backup directory found.")
            return

        # Apply retention policy settings
        retention_settings = self.get_retention_settings(options)

        # Analyze what needs to be cleaned up
        cleanup_plan = self.create_cleanup_plan(retention_settings, options)

        if not cleanup_plan["to_delete"]:
            self.stdout.write(self.style.SUCCESS("✅ No cleanup needed. All backups are within retention policy."))
            return

        # Show cleanup plan
        self.show_cleanup_plan(cleanup_plan, options)

        if options["dry_run"]:
            return

        # Confirm cleanup
        if not options["force"]:
            self.confirm_cleanup(cleanup_plan)

        # Execute cleanup
        self.execute_cleanup(cleanup_plan, options)

        self.stdout.write(
            self.style.SUCCESS(f"🧹 Cleanup completed! Removed {len(cleanup_plan['to_delete'])} items, freed {self.format_file_size(cleanup_plan['total_size_freed'])}")
        )

    def get_retention_settings(self, options):
        """Get retention settings based on policy"""
        policy = options["retention_policy"]

        if policy == "aggressive":
            return {
                "daily_retention": 3,
                "weekly_retention": 2,
                "monthly_retention": 6,
                "rollback_retention": 3,
            }
        elif policy == "conservative":
            return {
                "daily_retention": 14,
                "weekly_retention": 8,
                "monthly_retention": 24,
                "rollback_retention": 14,
            }
        elif policy == "custom":
            return {
                "daily_retention": options["daily_retention"],
                "weekly_retention": options["weekly_retention"],
                "monthly_retention": options["monthly_retention"],
                "rollback_retention": options["rollback_retention"],
            }
        else:  # default
            return {
                "daily_retention": 7,
                "weekly_retention": 4,
                "monthly_retention": 12,
                "rollback_retention": 7,
            }

    def create_cleanup_plan(self, retention_settings, options):
        """Create a plan for which backups to delete"""
        plan = {
            "to_delete": [],
            "to_keep": [],
            "total_size_freed": 0,
            "categories": {
                "expired_daily": [],
                "expired_weekly": [],
                "expired_monthly": [],
                "expired_rollback": [],
                "corrupted": [],
                "orphaned": []
            }
        }

        now = datetime.datetime.now()

        # Analyze manifests
        manifests_dir = self.backup_dir / "manifests"
        if manifests_dir.exists():
            self.analyze_manifest_backups(manifests_dir, retention_settings, plan, now, options)

        # Analyze standalone files
        data_dir = self.backup_dir / "data"
        if data_dir.exists():
            self.analyze_standalone_backups(data_dir, retention_settings, plan, now, options)

        # Analyze media backups
        media_dir = self.backup_dir / "media"
        if media_dir.exists():
            self.analyze_media_backups(media_dir, retention_settings, plan, now, options)

        # Analyze rollback backups
        rollback_dir = self.backup_dir / "rollback"
        if rollback_dir.exists():
            self.analyze_rollback_backups(rollback_dir, retention_settings, plan, now, options)

        return plan

    def analyze_manifest_backups(self, manifests_dir, retention_settings, plan, now, options):
        """Analyze manifest-based backups"""
        manifests = []

        for manifest_file in manifests_dir.glob("backup_manifest_*.json"):
            if manifest_file.name == "latest_manifest.json":
                continue

            try:
                with manifest_file.open() as f:
                    manifest = json.load(f)

                backup_time = datetime.datetime.fromisoformat(manifest.get("timestamp", ""))
                manifest_info = {
                    "file": manifest_file,
                    "timestamp": backup_time,
                    "type": manifest.get("backup_type", "full"),
                    "schemas": manifest.get("schemas", []),
                    "size": manifest_file.stat().st_size
                }

                # Add size of associated backup files
                for schema_info in manifest.get("schemas", []):
                    backup_file_path = Path(schema_info.get("filepath", ""))
                    if backup_file_path.exists():
                        manifest_info["size"] += backup_file_path.stat().st_size

                manifests.append(manifest_info)

            except Exception as e:
                # Corrupted manifest
                plan["categories"]["corrupted"].append({
                    "file": manifest_file,
                    "reason": f"Corrupted manifest: {e}",
                    "size": manifest_file.stat().st_size
                })

        # Sort by timestamp
        manifests.sort(key=lambda x: x["timestamp"])

        # Apply retention logic
        self.apply_retention_to_manifests(manifests, retention_settings, plan, now, options)

    def apply_retention_to_manifests(self, manifests, retention_settings, plan, now, options):
        """Apply retention policy to manifest backups"""
        # Group by backup type and apply retention
        daily_cutoff = now - datetime.timedelta(days=retention_settings["daily_retention"])
        weekly_cutoff = now - datetime.timedelta(weeks=retention_settings["weekly_retention"])
        monthly_cutoff = now - datetime.timedelta(days=retention_settings["monthly_retention"] * 30)

        for manifest in manifests:
            age = now - manifest["timestamp"]
            backup_type = manifest["type"]

            # Filter by schema if specified
            if options.get("schema"):
                schema_names = [s.get("schema", "") for s in manifest["schemas"]]
                if options["schema"] not in schema_names:
                    continue

            should_delete = False
            category = None

            if backup_type == "full":
                if manifest["timestamp"] < monthly_cutoff:
                    should_delete = True
                    category = "expired_monthly"
                elif manifest["timestamp"] < weekly_cutoff and age.days > retention_settings["weekly_retention"] * 7:
                    # Keep one full backup per week
                    week_number = manifest["timestamp"].isocalendar()[1]
                    existing_weekly = any(
                        m["timestamp"].isocalendar()[1] == week_number and
                        m["timestamp"] > manifest["timestamp"]
                        for m in manifests
                        if m["type"] == "full" and m["timestamp"] >= weekly_cutoff
                    )
                    if existing_weekly:
                        should_delete = True
                        category = "expired_weekly"

            elif backup_type == "incremental":
                if manifest["timestamp"] < daily_cutoff:
                    should_delete = True
                    category = "expired_daily"

            elif backup_type == "baseline":
                # Keep all baselines unless very old
                if age.days > 365:  # Keep baselines for 1 year
                    should_delete = True
                    category = "expired_monthly"

            if should_delete:
                deletion_item = {
                    "manifest": manifest["file"],
                    "files": [manifest["file"]],
                    "category": category,
                    "size": manifest["size"],
                    "timestamp": manifest["timestamp"]
                }

                # Add associated backup files
                for schema_info in manifest["schemas"]:
                    backup_file_path = Path(schema_info.get("filepath", ""))
                    if backup_file_path.exists():
                        deletion_item["files"].append(backup_file_path)

                    # Add media backup if exists
                    media_backup = schema_info.get("media_backup")
                    if media_backup and Path(media_backup).exists():
                        deletion_item["files"].append(Path(media_backup))
                        deletion_item["size"] += Path(media_backup).stat().st_size

                plan["categories"][category].append(deletion_item)
                plan["to_delete"].append(deletion_item)
                plan["total_size_freed"] += deletion_item["size"]
            else:
                plan["to_keep"].append(manifest)

    def analyze_standalone_backups(self, data_dir, retention_settings, plan, now, options):
        """Analyze standalone backup files"""
        for backup_file in data_dir.glob("*.sql*"):
            # Check if this file is part of a manifest
            is_orphaned = True
            manifest_files = set()

            manifests_dir = self.backup_dir / "manifests"
            if manifests_dir.exists():
                for manifest_file in manifests_dir.glob("backup_manifest_*.json"):
                    try:
                        with manifest_file.open() as f:
                            manifest = json.load(f)
                        for schema_info in manifest.get("schemas", []):
                            manifest_files.add(Path(schema_info.get("filepath", "")).name)
                            manifest_files.add(schema_info.get("filename", ""))
                    except:
                        continue

            if backup_file.name in manifest_files:
                is_orphaned = False

            if is_orphaned:
                # Apply retention based on file age
                file_age = now - datetime.datetime.fromtimestamp(backup_file.stat().st_mtime)
                if file_age.days > retention_settings["daily_retention"]:
                    deletion_item = {
                        "files": [backup_file],
                        "category": "orphaned",
                        "size": backup_file.stat().st_size,
                        "timestamp": datetime.datetime.fromtimestamp(backup_file.stat().st_mtime)
                    }
                    plan["categories"]["orphaned"].append(deletion_item)
                    plan["to_delete"].append(deletion_item)
                    plan["total_size_freed"] += deletion_item["size"]

    def analyze_media_backups(self, media_dir, retention_settings, plan, now, options):
        """Analyze media backup files"""
        # Similar logic to standalone backups
        for media_file in media_dir.iterdir():
            if media_file.is_file() or media_file.is_dir():
                file_age = now - datetime.datetime.fromtimestamp(media_file.stat().st_mtime)
                if file_age.days > retention_settings["daily_retention"]:
                    size = self.get_path_size(media_file)
                    deletion_item = {
                        "files": [media_file],
                        "category": "orphaned",
                        "size": size,
                        "timestamp": datetime.datetime.fromtimestamp(media_file.stat().st_mtime)
                    }
                    plan["categories"]["orphaned"].append(deletion_item)
                    plan["to_delete"].append(deletion_item)
                    plan["total_size_freed"] += size

    def analyze_rollback_backups(self, rollback_dir, retention_settings, plan, now, options):
        """Analyze rollback backups"""
        rollback_cutoff = now - datetime.timedelta(days=retention_settings["rollback_retention"])

        for item in rollback_dir.rglob("*"):
            if item.is_file():
                item_time = datetime.datetime.fromtimestamp(item.stat().st_mtime)
                if item_time < rollback_cutoff:
                    deletion_item = {
                        "files": [item],
                        "category": "expired_rollback",
                        "size": item.stat().st_size,
                        "timestamp": item_time
                    }
                    plan["categories"]["expired_rollback"].append(deletion_item)
                    plan["to_delete"].append(deletion_item)
                    plan["total_size_freed"] += deletion_item["size"]

    def show_cleanup_plan(self, plan, options):
        """Show what will be cleaned up"""
        if options["dry_run"]:
            self.stdout.write(self.style.NOTICE("🔍 Dry Run - Cleanup Plan:"))
        else:
            self.stdout.write(self.style.WARNING("🗑️  Cleanup Plan:"))

        self.stdout.write("")

        for category, items in plan["categories"].items():
            if not items:
                continue

            category_size = sum(item["size"] for item in items)
            self.stdout.write(f"{category.replace('_', ' ').title()}: {len(items)} items ({self.format_file_size(category_size)})")

            for item in items[:5]:  # Show first 5 items
                timestamp = item["timestamp"].strftime("%Y-%m-%d %H:%M")
                size = self.format_file_size(item["size"])
                if "manifest" in item:
                    self.stdout.write(f"  • {item['manifest'].name} ({size}) - {timestamp}")
                else:
                    file_names = [f.name for f in item["files"]]
                    self.stdout.write(f"  • {', '.join(file_names)} ({size}) - {timestamp}")

            if len(items) > 5:
                self.stdout.write(f"  ... and {len(items) - 5} more items")

            self.stdout.write("")

        self.stdout.write(f"Total to delete: {len(plan['to_delete'])} items")
        self.stdout.write(f"Space to free: {self.format_file_size(plan['total_size_freed'])}")

    def confirm_cleanup(self, plan):
        """Confirm cleanup operation with user"""
        self.stdout.write(self.style.WARNING("⚠️ CLEANUP OPERATION"))
        self.stdout.write("")
        self.stdout.write(f"This will permanently delete {len(plan['to_delete'])} backup items")
        self.stdout.write(f"and free {self.format_file_size(plan['total_size_freed'])} of disk space.")
        self.stdout.write("")

        response = input("Are you sure you want to continue? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            raise SystemExit("Cleanup cancelled by user")

    def execute_cleanup(self, plan, options):
        """Execute the cleanup plan"""
        deleted_count = 0

        for deletion_item in plan["to_delete"]:
            try:
                for file_path in deletion_item["files"]:
                    if file_path.is_dir():
                        shutil.rmtree(file_path)
                    else:
                        file_path.unlink()

                deleted_count += 1

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"❌ Failed to delete {file_path}: {e}")
                )

        self.stdout.write(f"🗑️  Deleted {deleted_count} items")

    def get_path_size(self, path):
        """Get total size of a path (file or directory)"""
        if path.is_file():
            return path.stat().st_size
        elif path.is_dir():
            return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
        return 0

    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"