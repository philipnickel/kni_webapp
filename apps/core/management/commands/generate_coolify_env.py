import os
import secrets
from typing import List

from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Generate a ready-to-paste Coolify environment block for a given domain"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("domain", help="Primary domain, e.g. example.com")
        parser.add_argument(
            "--extra-domains",
            default="",
            help="Comma-separated extra domains without scheme (e.g. api.example.com,admin.example.com)",
        )
        parser.add_argument(
            "--database-url",
            default="",
            help="Optional DATABASE_URL to include (e.g. postgresql://user:pass@host:5432/db?sslmode=require)",
        )
        parser.add_argument(
            "--redis-url",
            default="",
            help="Optional REDIS_URL to include (e.g. redis://:password@redis:6379/0)",
        )

    def handle(self, *args, **options):
        domain: str = options["domain"].strip()
        extra_domains_raw: str = options.get("extra_domains", "")
        extra_domains: List[str] = [d.strip() for d in extra_domains_raw.split(",") if d.strip()]
        database_url: str = options.get("database_url", "").strip()
        redis_url: str = options.get("redis_url", "").strip()

        if not domain or "," in domain or domain.startswith("http"):
            self.stderr.write(
                self.style.ERROR("Provide a bare primary domain without scheme or commas, e.g. example.com")
            )
            return

        secret = secrets.token_urlsafe(64)

        lines: List[str] = []
        lines.append("DJANGO_SETTINGS_MODULE=project.settings")
        lines.append("DEBUG=false")
        lines.append(f"DJANGO_SECRET_KEY={secret}")
        lines.append(f"PRIMARY_DOMAIN={domain}")
        if extra_domains:
            lines.append(f"EXTRA_DOMAINS={','.join(extra_domains)}")
        else:
            lines.append("EXTRA_DOMAINS=")
        lines.append("SECURE_SSL_REDIRECT=true")

        if database_url:
            lines.append(f"DATABASE_URL={database_url}")
        else:
            lines.append("# DATABASE_URL=postgresql://user:pass@host:5432/db?sslmode=require")

        if redis_url:
            lines.append(f"REDIS_URL={redis_url}")
        else:
            lines.append("# REDIS_URL=redis://:strongpassword@redis:6379/0")

        lines.append("# Optional tenant/seed flags")
        lines.append("SEED_TENANT_DATA=false")
        lines.append("TENANT_SCHEMA=")
        lines.append("TENANT_HOSTNAME=")
        lines.append("TENANT_PORT=443")
        lines.append("TENANT_ADMIN_USER=")
        lines.append("TENANT_ADMIN_PASSWORD=")
        lines.append("TENANT_ADMIN_EMAIL=")

        block = "\n".join(lines) + "\n"
        self.stdout.write(self.style.SUCCESS("# Coolify environment (paste into Environment tab)"))
        self.stdout.write(block)

