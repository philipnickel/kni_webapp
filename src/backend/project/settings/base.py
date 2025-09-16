import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Secret Key Configuration
def get_secret_key():
    """
    Get Django secret key with multiple fallback strategies.
    Priority:
    1. DJANGO_SECRET_KEY environment variable
    2. Generate and cache a secure key for the current deployment
    3. Development fallback (only in DEBUG mode)
    """
    secret_key = os.getenv("DJANGO_SECRET_KEY", "").strip()

    if secret_key:
        return secret_key

    # Generate a secure key if none provided
    from django.core.management.utils import get_random_secret_key
    generated_key = get_random_secret_key()

    # In production, warn about using a generated key
    debug_mode = os.getenv("DEBUG", "True").lower() == "true"
    if not debug_mode:
        import sys
        print(f"WARNING: No DJANGO_SECRET_KEY provided. Generated temporary key: {generated_key[:10]}...", file=sys.stderr)
        print("WARNING: For production use, set DJANGO_SECRET_KEY environment variable.", file=sys.stderr)

    return generated_key

SECRET_KEY = get_secret_key()

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
                # Handle malformed URLs like "domain://domain"
                if '://' in url:
                    # Split on :// and take the last part (handles "domain://domain" format)
                    url = url.split('://')[-1]
                # Remove any remaining scheme prefixes
                url = url.replace('https://', '').replace('http://', '')
                # Remove port if present
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
    "django.middleware.gzip.GZipMiddleware",
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
                "apps.core.context_processors.settings",
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
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "connect_timeout": 10,
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        },
    }
}

# Enforce SSL for database connections in production-like environments
_local_db_hosts = {"localhost", "127.0.0.1", "db"}
if parsed.hostname:
    if any(pattern in parsed.hostname for pattern in ["knipostgres", "postgres", "database", "kni-webapp-db"]):
        _local_db_hosts.add(parsed.hostname)

# Only require SSL for truly remote databases, not Docker internal networks
# Skip SSL requirement if DATABASE_URL explicitly contains sslmode parameter
if (parsed.hostname and
    parsed.hostname not in _local_db_hosts and
    "sslmode" not in DATABASE_URL.lower()):
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
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "frontend_static",
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Wagtail settings
WAGTAIL_SITE_NAME = "KNI Webapp"
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

# Redis Configuration
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
if REDIS_URL.startswith("redis://"):
    redis_parsed = urlparse(REDIS_URL)
    REDIS_CONFIG = {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 50,
                "retry_on_timeout": True,
                "socket_keepalive": True,
                "socket_keepalive_options": {},
                "health_check_interval": 30,
            },
            "SERIALIZER": "django_redis.serializers.pickle.PickleSerializer",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        },
        "TIMEOUT": 300,
        "KEY_PREFIX": "kni_webapp",
    }
else:
    # Fallback to dummy cache if Redis is not available
    REDIS_CONFIG = {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }

# Cache Configuration - use Redis when available, fallback to dummy
if REDIS_URL.startswith("redis://"):
    CACHES = {
        "default": REDIS_CONFIG,
        "sessions": dict(REDIS_CONFIG, **{
            "KEY_PREFIX": "kni_webapp_sessions",
            "TIMEOUT": 86400,  # 24 hours
        }),
        "pages": dict(REDIS_CONFIG, **{
            "KEY_PREFIX": "kni_webapp_pages",
            "TIMEOUT": 3600,  # 1 hour
        }),
    }
else:
    # Fallback to dummy cache when Redis is not available
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },
        "sessions": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },
        "pages": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },
    }

# Session Configuration - use cache sessions when Redis is available
if REDIS_URL.startswith("redis://"):
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
else:
    SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_CACHE_ALIAS = "sessions"
SESSION_COOKIE_AGE = 86400  # 24 hours
SESSION_SAVE_EVERY_REQUEST = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "maxBytes": 10 * 1024 * 1024,  # 10 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
        "security": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "security.log",
            "maxBytes": 10 * 1024 * 1024,  # 10 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["security", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "wagtail": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "apps": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Create logs directory if it doesn't exist
os.makedirs(BASE_DIR / "logs", exist_ok=True)

# Performance and Compression Settings
USE_ETAGS = True
GZIP_COMPRESSION_LEVEL = 6

# WhiteNoise Configuration for Static Files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_USE_FINDERS = False
WHITENOISE_AUTOREFRESH = False
WHITENOISE_MAX_AGE = 31536000  # 1 year for production

# Wagtail Cache Settings
if "pages" in CACHES:
    WAGTAIL_CACHE = True
    WAGTAIL_CACHE_BACKEND = "pages"
    WAGTAILFRONTENDCACHE = {
        "default": {
            "BACKEND": "wagtail.contrib.frontend_cache.backends.HTTPBackend",
            "LOCATION": "http://localhost:8000",
        }
    }

# Data Upload Settings
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB
