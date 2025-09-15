import os
import json
import datetime
import subprocess
from pathlib import Path
import shutil
import hashlib

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import connection


class Command(BaseCommand):
    help = "Create schema-aware backups for multi-tenant customer data protection"

    def add_arguments(self, parser):
        parser.add_argument(
            "--schema",
            dest="schema",
            help="Specific schema to backup (default: current/all)",
        )
        parser.add_argument(
            "--tenant",
            dest="tenant",
            help="Tenant identifier for backup naming",
        )
        parser.add_argument(
            "--backup-type",
            dest="backup_type",
            choices=["full", "incremental", "baseline"],
            default="full",
            help="Type of backup to create (default: full)",
        )
        parser.add_argument(
            "--include-media",
            action="store_true",
            help="Include media files in the backup",
        )
        parser.add_argument(
            "--output-dir",
            dest="output_dir",
            help="Output directory for backups (default: backups/)",
        )
        parser.add_argument(
            "--retention-days",
            dest="retention_days",
            type=int,
            default=30,
            help="Retention period in days (default: 30)",
        )
        parser.add_argument(
            "--name",
            dest="backup_name",
            help="Custom name for the backup (e.g., 'baseline', 'before-update')",
        )
        parser.add_argument(
            "--compress",
            action="store_true",
            help="Compress backup files with gzip",
        )

    def handle(self, *args, **options):
        # Initialize backup system
        self.setup_backup_environment(options)

        # Determine schemas to backup
        schemas = self.get_schemas_to_backup(options)

        # Create backup for each schema
        backup_manifest = {
            "timestamp": datetime.datetime.now().isoformat(),
            "backup_type": options["backup_type"],
            "schemas": [],
            "retention_days": options["retention_days"],
            "include_media": options["include_media"],
            "compressed": options["compress"]
        }

        for schema in schemas:
            try:
                backup_info = self.backup_schema(schema, options)
                backup_manifest["schemas"].append(backup_info)
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Schema '{schema}' backed up successfully")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"❌ Failed to backup schema '{schema}': {e}")
                )
                if len(schemas) == 1:
                    raise CommandError(f"Backup failed: {e}")

        # Save backup manifest
        self.save_backup_manifest(backup_manifest, options)

        # Apply retention policy
        self.apply_retention_policy(options)

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Backup completed! {len(backup_manifest['schemas'])} schemas backed up"
            )
        )

    def setup_backup_environment(self, options):
        """Initialize backup directories and environment"""
        self.backup_dir = Path(options.get("output_dir") or (Path(settings.BASE_DIR) / "backups"))
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        self.data_dir = self.backup_dir / "data"
        self.media_dir = self.backup_dir / "media"
        self.manifests_dir = self.backup_dir / "manifests"

        for directory in [self.data_dir, self.media_dir, self.manifests_dir]:
            directory.mkdir(parents=True, exist_ok=True)

        # Find pg_dump executable
        self.pg_dump_path = self.find_pg_dump()

    def find_pg_dump(self):
        """Find pg_dump executable"""
        pg_dump_paths = [
            "/usr/bin/pg_dump",  # Linux container path
            "/opt/homebrew/Cellar/postgresql@15/15.14/bin/pg_dump",
            "/opt/homebrew/bin/pg_dump",
            "/usr/local/bin/pg_dump",
            "pg_dump"  # In PATH
        ]

        for path in pg_dump_paths:
            try:
                result = subprocess.run([path, "--version"],
                                       check=True, capture_output=True, text=True)
                return path
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue

        raise CommandError("pg_dump not found. Please install PostgreSQL client tools.")

    def get_schemas_to_backup(self, options):
        """Determine which schemas to backup"""
        if options.get("schema"):
            return [options["schema"]]

        # Auto-detect tenant schemas
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT schema_name
                FROM information_schema.schemata
                WHERE schema_name NOT IN ('public', 'information_schema', 'pg_catalog', 'pg_toast')
                ORDER BY schema_name
            """)
            tenant_schemas = [row[0] for row in cursor.fetchall()]

        # Always include public schema for core data
        schemas = ["public"]
        schemas.extend(tenant_schemas)

        return schemas

    def backup_schema(self, schema, options):
        """Backup a specific database schema"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        tenant = options.get("tenant") or schema
        backup_type = options["backup_type"]

        # Generate filename
        backup_name = options.get("backup_name")

        if backup_name:
            # Custom named backup
            filename = f"{backup_name}_{schema}_{timestamp}.sql"
        elif backup_type == "baseline":
            filename = f"baseline_{schema}.sql"
        else:
            filename = f"{tenant}_{schema}_{backup_type}_{timestamp}.sql"

        if options["compress"]:
            filename += ".gz"

        output_file = self.data_dir / filename

        # Get database configuration
        db = settings.DATABASES.get("default", {})
        name = db.get("NAME")
        user = db.get("USER")
        password = db.get("PASSWORD", "")
        host = db.get("HOST") or "localhost"
        port = str(db.get("PORT") or "5432")

        # Set up environment
        env = os.environ.copy()
        env.update({
            "PGHOST": host,
            "PGPORT": port,
        })
        if user:
            env["PGUSER"] = user
        if password:
            env["PGPASSWORD"] = password

        # Build pg_dump command
        cmd = [
            self.pg_dump_path,
            "--schema", schema,
            "--clean",
            "--if-exists",
            "--no-owner",
            "--no-privileges",
            "--verbose",
            "--no-password",
        ]

        # Add incremental options for non-baseline backups
        if backup_type == "incremental":
            cmd.extend(["--data-only"])

        cmd.append(name)

        self.stdout.write(f"🔄 Backing up schema '{schema}' to {output_file}")

        # Execute backup
        if options["compress"]:
            # Use gzip compression
            pg_process = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            with output_file.open("wb") as f:
                gzip_process = subprocess.Popen(["gzip"], stdin=pg_process.stdout, stdout=f)
                pg_process.stdout.close()
                gzip_process.wait()

            returncode = pg_process.wait()
            if returncode != 0:
                stderr = pg_process.stderr.read().decode()
                raise CommandError(f"pg_dump failed: {stderr}")
        else:
            # Direct output to file
            with output_file.open("w") as f:
                try:
                    result = subprocess.run(
                        cmd,
                        env=env,
                        stdout=f,
                        stderr=subprocess.PIPE,
                        text=True,
                        check=True
                    )
                except subprocess.CalledProcessError as e:
                    error_msg = e.stderr if e.stderr else str(e)
                    raise CommandError(f"pg_dump failed: {error_msg}")

        # Calculate file hash for integrity checking
        file_hash = self.calculate_file_hash(output_file)

        # Backup media files for this schema if requested
        media_backup_path = None
        if options["include_media"] and schema != "public":
            media_backup_path = self.backup_schema_media(schema, tenant, timestamp, options)

        return {
            "schema": schema,
            "tenant": tenant,
            "filename": filename,
            "filepath": str(output_file),
            "size": output_file.stat().st_size,
            "hash": file_hash,
            "media_backup": media_backup_path,
            "timestamp": timestamp,
            "type": backup_type
        }

    def backup_schema_media(self, schema, tenant, timestamp, options):
        """Backup media files for a specific schema/tenant"""
        media_root = Path(settings.MEDIA_ROOT)
        if not media_root.exists():
            return None

        # Create tenant-specific media backup directory
        media_backup_name = f"{tenant}_media_{timestamp}"
        if options["compress"]:
            media_backup_name += ".tar.gz"

        media_backup_path = self.media_dir / media_backup_name

        try:
            if options["compress"]:
                # Create compressed tar archive
                subprocess.run([
                    "tar", "czf", str(media_backup_path),
                    "-C", str(media_root.parent), media_root.name
                ], check=True)
            else:
                # Copy directory
                shutil.copytree(media_root, media_backup_path, dirs_exist_ok=True)

            self.stdout.write(f"📁 Media files backed up to {media_backup_path}")
            return str(media_backup_path)
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f"⚠️ Failed to backup media files: {e}")
            )
            return None

    def calculate_file_hash(self, filepath):
        """Calculate SHA256 hash of a file for integrity checking"""
        sha256_hash = hashlib.sha256()
        with filepath.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    def save_backup_manifest(self, manifest, options):
        """Save backup manifest with metadata"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        manifest_file = self.manifests_dir / f"backup_manifest_{timestamp}.json"

        with manifest_file.open("w") as f:
            json.dump(manifest, f, indent=2, default=str)

        # Also create/update latest manifest symlink
        latest_manifest = self.manifests_dir / "latest_manifest.json"
        if latest_manifest.exists():
            latest_manifest.unlink()
        latest_manifest.symlink_to(manifest_file.name)

        self.stdout.write(f"📋 Backup manifest saved: {manifest_file}")

    def apply_retention_policy(self, options):
        """Apply retention policy to old backups"""
        retention_days = options["retention_days"]
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=retention_days)

        deleted_count = 0

        # Clean up old data files
        for backup_file in self.data_dir.iterdir():
            if backup_file.is_file() and backup_file.stat().st_mtime < cutoff_date.timestamp():
                backup_file.unlink()
                deleted_count += 1

        # Clean up old media files
        for media_backup in self.media_dir.iterdir():
            if media_backup.is_file() and media_backup.stat().st_mtime < cutoff_date.timestamp():
                if media_backup.is_dir():
                    shutil.rmtree(media_backup)
                else:
                    media_backup.unlink()
                deleted_count += 1

        # Clean up old manifests
        for manifest in self.manifests_dir.iterdir():
            if manifest.name != "latest_manifest.json" and manifest.is_file():
                if manifest.stat().st_mtime < cutoff_date.timestamp():
                    manifest.unlink()
                    deleted_count += 1

        if deleted_count > 0:
            self.stdout.write(
                self.style.NOTICE(f"🧹 Cleaned up {deleted_count} old backup files")
            )