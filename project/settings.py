import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

def get_domains_from_coolify():
    """Extract domains from Coolify environment variables"""
    domains = []
    
    # Try COOLIFY_FQDN first (strip https:// scheme)
    coolify_fqdn = os.getenv("COOLIFY_FQDN", "")
    if coolify_fqdn:
        # Strip scheme and split multiple domains
        for domain in coolify_fqdn.split(','):
            domain = domain.strip()
            # Remove scheme (https:// or http://)
            domain = domain.replace('https://', '').replace('http://', '')
            # Remove port if present
            domain = domain.split(':')[0]
            if domain:
                domains.append(domain)
    
    # Fallback to COOLIFY_URL 
    if not domains:
        coolify_url = os.getenv("COOLIFY_URL", "")
        if coolify_url:
            for url in coolify_url.split(','):
                url = url.strip()
                url = url.replace('https://', '').replace('http://', '')
                url = url.split(':')[0]
                if url:
                    domains.append(url)
    
    return domains

# Domain configuration with Coolify auto-detection
PRIMARY_DOMAIN = os.getenv("PRIMARY_DOMAIN", "").strip()
EXTRA_DOMAINS = [d.strip() for d in os.getenv("EXTRA_DOMAINS", "").split(",") if d.strip()]

# Auto-detect from Coolify if no PRIMARY_DOMAIN is set
if not PRIMARY_DOMAIN:
    coolify_domains = get_domains_from_coolify()
    if coolify_domains:
        PRIMARY_DOMAIN = coolify_domains[0]  # Use first as primary
        EXTRA_DOMAINS.extend(coolify_domains[1:])  # Rest as extras

# Derive ALLOWED_HOSTS automatically
_default_hosts = ["localhost", "127.0.0.1"]
if PRIMARY_DOMAIN:
    ALLOWED_HOSTS = [PRIMARY_DOMAIN, f"www.{PRIMARY_DOMAIN}"] + EXTRA_DOMAINS
else:
    ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", ",".join(_default_hosts)).split(",") if h.strip()]

# Derive CSRF_TRUSTED_ORIGINS automatically
if PRIMARY_DOMAIN:
    _origins = [f"https://{PRIMARY_DOMAIN}", f"https://www.{PRIMARY_DOMAIN}"]
    CSRF_TRUSTED_ORIGINS = _origins + [o if o.startswith("http") else f"https://{o}" for o in EXTRA_DOMAINS]
else:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    
    # Wagtail apps
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.sitemaps",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "wagtail.contrib.settings",
    
    "modelcluster",
    "taggit",
    
    # Third-party apps
    "django_htmx",
    
    # Local apps
    "apps.core",
    "apps.pages",
    "apps.projects",
    "apps.contacts",
]

MIDDLEWARE = [
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
                # "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

SITE_ID = 1

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost:5432/kni_webapp_dev")
parsed = urlparse(DATABASE_URL)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": parsed.path.lstrip("/"),
        "USER": parsed.username or "",
        "PASSWORD": parsed.password or "",
        "HOST": parsed.hostname or "",
        "PORT": parsed.port or "5432",
    }
}

# Enforce SSL for database connections in production-like environments
_local_db_hosts = {"localhost", "127.0.0.1", "db"}
if not DEBUG and (parsed.hostname and parsed.hostname not in _local_db_hosts):
    DATABASES["default"].setdefault("OPTIONS", {})
    DATABASES["default"]["OPTIONS"].setdefault("sslmode", "require")

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

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Wagtail settings
WAGTAIL_SITE_NAME = "KNI Webapp"
if PRIMARY_DOMAIN:
    WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", f"https://{PRIMARY_DOMAIN}")
else:
    WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "http://localhost:8000")
WAGTAILIMAGES_IMAGE_MODEL = "wagtailimages.Image"
WAGTAILSETTINGS_CONTEXT_USE_DEFAULT_SITE = True

# Wagtail admin settings
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAIL_WORKFLOW_ENABLED = False
WAGTAIL_MODERATION_ENABLED = False

# Rich text editor
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': [
                'bold', 'italic', 'link', 'ol', 'ul', 
                'document-link', 'image', 'code'
            ]
        }
    },
}

WAGTAIL_AUTO_UPDATE_PREVIEW = True
WAGTAIL_ENABLE_UPDATE_CHECK = False

# Search configuration
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
        'AUTO_UPDATE': True,
    }
}

# Security settings
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False").lower() == "true"
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_REFERRER_POLICY = "same-origin"
    SESSION_COOKIE_SAMESITE = "Lax"
    CSRF_COOKIE_SAMESITE = "Lax"
    X_FRAME_OPTIONS = "DENY"

# Rely on Wagtail's built-in default-site fallback for settings via
# WAGTAILSETTINGS_CONTEXT_USE_DEFAULT_SITE rather than monkey-patching
