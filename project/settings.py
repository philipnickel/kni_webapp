import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key")
DEBUG = True
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if h.strip()]

# Django-tenants configuration
SHARED_APPS = [
    # Django-tenants must be first
    "django_tenants",
    
    # Django core apps - PUBLIC SCHEMA ONLY (Super Admin)
    "django.contrib.admin",      # Django admin for super admin
    "django.contrib.auth", 
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    
    # Essential Wagtail core for middleware (shared across all schemas)
    "wagtail",
    "wagtail.sites",
    "wagtail.contrib.redirects",
    
    # Third-party shared
    "django_htmx",
    
    # Tenant management app (shared) - SUPER ADMIN ONLY
    "apps.tenants",
]

TENANT_APPS = [
    # Django core for tenant schemas
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Full Wagtail stack - TENANT SCHEMAS ONLY
    "wagtail.contrib.redirects",
    "wagtail.users",
    "wagtail.admin",                # Wagtail admin for tenants
    "wagtail",
    "wagtail.sites",
    "wagtail.images",
    "wagtail.documents", 
    "wagtail.contrib.settings",
    "wagtail.snippets",
    "modelcluster",
    "taggit",
    
    # Local tenant-specific apps
    "apps.core",
    "apps.pages", 
    "apps.projects",
    "apps.contacts",
]

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    # Django-tenants middleware must be first
    "django_tenants.middleware.TenantMainMiddleware",
    
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"

SITE_ID = 1

# Database - django-tenants requires PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/kni_webapp")
parsed = urlparse(DATABASE_URL)

DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",  # Use django-tenants backend
        "NAME": parsed.path.lstrip("/"),
        "USER": parsed.username,
        "PASSWORD": parsed.password,
        "HOST": parsed.hostname,
        "PORT": parsed.port or "5432",
    }
}

DATABASE_ROUTERS = (
    "django_tenants.routers.TenantSyncRouter",
)

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "da"
TIME_ZONE = "Europe/Copenhagen"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Wagtail
WAGTAIL_SITE_NAME = "JCleemannByg"
WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "http://localhost:8000")
WAGTAILIMAGES_IMAGE_MODEL = "wagtailimages.Image"

# Wagtail admin settings

# Customize admin interface  
WAGTAIL_USAGE_COUNT_ENABLED = True

# Disable moderation and workflows for Johann's simple setup
WAGTAIL_WORKFLOW_ENABLED = False
WAGTAIL_MODERATION_ENABLED = False

# Security
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "false").lower() == "true"
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 0 if DEBUG else 60 * 60 * 24 * 30

# Django-tenants settings
TENANT_MODEL = "tenants.Client"
TENANT_DOMAIN_MODEL = "tenants.Domain" 
PUBLIC_SCHEMA_NAME = "public"
PUBLIC_SCHEMA_URLCONF = "project.urls_public"  # We'll create this

# Allow wildcard domains for development
ALLOWED_HOSTS = ["*"] if DEBUG else ALLOWED_HOSTS

