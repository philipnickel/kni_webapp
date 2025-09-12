import os
import datetime
import subprocess
from pathlib import Path
import shutil

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Create a PostgreSQL backup of the current database that can be restored reliably."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            dest="output",
            help="Output file path for the SQL dump (default: backups/baseline.sql)",
        )
        parser.add_argument(
            "--baseline",
            action="store_true",
            help="Create baseline.sql (the default for Docker containers)",
        )
        parser.add_argument(
            "--include-media",
            action="store_true",
            help="Include media files in the backup (copies to backups/media/)",
        )

    def handle(self, *args, **options):
        db = settings.DATABASES.get("default", {})
        engine = db.get("ENGINE", "")
        if "postgresql" not in engine:
            raise CommandError(
                f"Unsupported database engine: {engine}. Only PostgreSQL is supported."
            )

        name = db.get("NAME")
        user = db.get("USER")
        password = db.get("PASSWORD", "")
        host = db.get("HOST") or "localhost"
        port = str(db.get("PORT") or "5432")

        if not name:
            raise CommandError("DATABASES['default'] must define NAME for PostgreSQL.")

        # Find pg_dump
        pg_dump_paths = [
            "/opt/homebrew/Cellar/postgresql@15/15.14/bin/pg_dump",
            "/opt/homebrew/bin/pg_dump",
            "/usr/local/bin/pg_dump",
            "pg_dump"  # In PATH
        ]
        
        pg_dump_path = None
        for path in pg_dump_paths:
            try:
                result = subprocess.run([path, "--version"], 
                                       check=True, capture_output=True, text=True)
                pg_dump_path = path
                break
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
                
        if not pg_dump_path:
            raise CommandError("pg_dump not found. Please install PostgreSQL client tools.")

        backups_dir = Path(settings.BASE_DIR) / "backups"
        backups_dir.mkdir(parents=True, exist_ok=True)

        # Determine output file
        if options.get("baseline"):
            output = backups_dir / "baseline.sql"
        elif options.get("output"):
            output = Path(options.get("output"))
        else:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output = backups_dir / f"postgres-dev-{ts}.sql"

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

        # pg_dump command with options for clean restore
        cmd = [
            pg_dump_path,
            "--clean",                    # Include DROP statements
            "--if-exists",               # Use IF EXISTS in DROP statements  
            "--no-owner",                # Don't include ownership commands
            "--no-privileges",           # Don't include privilege commands
            "--verbose",                 # Verbose output
            "--no-password",             # Don't prompt for password
            name
        ]

        self.stdout.write(self.style.NOTICE(f"Creating PostgreSQL backup of '{name}' to {output} ..."))
        
        # Run pg_dump
        with output.open("w") as f:
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

        # Optionally backup media files
        if options.get("include_media"):
            media_backup_dir = backups_dir / "media"
            if media_backup_dir.exists():
                shutil.rmtree(media_backup_dir)
            
            media_root = Path(settings.MEDIA_ROOT)
            if media_root.exists():
                self.stdout.write(f"Backing up media files to {media_backup_dir}")
                try:
                    shutil.copytree(media_root, media_backup_dir, dirs_exist_ok=True)
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"Error backing up media: {e}")
                    )

        self.stdout.write(
            self.style.SUCCESS(f"PostgreSQL backup completed: {output}")
        )
        
        if options.get("baseline"):
            self.stdout.write(
                self.style.NOTICE("This baseline will be used by Docker containers.")
            )