import os
import datetime
import subprocess
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Create a SQL backup of the current development database used by 'make run' (PostgreSQL only)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            dest="output",
            help="Output file path for the SQL dump (default: backups/dev-YYYYmmdd_HHMMSS.sql)",
        )

    def handle(self, *args, **options):
        db = settings.DATABASES.get("default", {})
        engine = db.get("ENGINE", "")
        if "postgresql" not in engine:
            raise CommandError(
                f"Unsupported database engine for dev_backup: {engine}. Only PostgreSQL is supported."
            )

        name = db.get("NAME")
        user = db.get("USER")
        password = db.get("PASSWORD", "")
        host = db.get("HOST") or "localhost"
        port = str(db.get("PORT") or "5432")

        if not name:
            raise CommandError("DATABASES['default'] must define NAME for PostgreSQL.")

        # Ensure pg_dump exists
        try:
            subprocess.run(["pg_dump", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception:
            raise CommandError("pg_dump not found. Please install PostgreSQL client tools (psql/pg_dump).")

        backups_dir = Path(settings.BASE_DIR) / "backups"
        backups_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output = options.get("output") or backups_dir / f"dev-{ts}.sql"
        output = Path(output)

        env = os.environ.copy()
        env.update({
            "PGHOST": host,
            "PGPORT": port,
        })
        if user:
            env["PGUSER"] = user
        if password:
            env["PGPASSWORD"] = password

        cmd = [
            "pg_dump",
            "-d",
            name,
        ]

        self.stdout.write(self.style.NOTICE(f"Backing up PostgreSQL database '{name}' to {output} ..."))
        with output.open("wb") as f:
            proc = subprocess.run(cmd, env=env, stdout=f, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            raise CommandError(f"pg_dump failed: {proc.stderr.decode('utf-8', errors='ignore')}")

        self.stdout.write(self.style.SUCCESS(f"Backup written to {output}"))
