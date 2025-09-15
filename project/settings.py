import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

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

# Derive ALLOWED_HOSTS automatically
_default_hosts = ["localhost", "127.0.0.1"]
if PRIMARY_DOMAIN:
    ALLOWED_HOSTS = [PRIMARY_DOMAIN, f"www.{PRIMARY_DOMAIN}"] + EXTRA_DOMAINS + _default_hosts
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
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# Add cache middleware for page caching in production
# TODO: Fix cache serialization issue and re-enable
# if not DEBUG:
#     MIDDLEWARE.insert(2, "django.middleware.cache.UpdateCacheMiddleware")
#     MIDDLEWARE.append("django.middleware.cache.FetchFromCacheMiddleware")
#
#     # Cache middleware settings
#     CACHE_MIDDLEWARE_ALIAS = "pages"
#     CACHE_MIDDLEWARE_SECONDS = 3600  # 1 hour
#     CACHE_MIDDLEWARE_KEY_PREFIX = "kni_webapp_page"

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
        "CONN_MAX_AGE": 60 if not DEBUG else 0,  # Connection pooling
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
# Include Dokploy internal hostnames to allow non-SSL connections
_local_db_hosts = {"localhost", "127.0.0.1", "db"}
# Add common Dokploy internal hostname patterns
if parsed.hostname:
    if any(pattern in parsed.hostname for pattern in ["knipostgres", "postgres", "database"]):
        _local_db_hosts.add(parsed.hostname)

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
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

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

# Redis caching is properly configured above (lines 324-335)

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
        } if not DEBUG else {
            "format": "{levelname} {asctime} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "json" if not DEBUG else "simple",
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
            "handlers": ["console", "file"] if not DEBUG else ["console"],
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
            "handlers": ["console", "file"] if not DEBUG else ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Create logs directory if it doesn't exist
os.makedirs(BASE_DIR / "logs", exist_ok=True)

# Email Configuration for Production
if not DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
    DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@jcleemannbyg.dk")
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Performance and Compression Settings
USE_ETAGS = True
GZIP_COMPRESSION_LEVEL = 6

# WhiteNoise Configuration for Static Files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_USE_FINDERS = DEBUG
WHITENOISE_AUTOREFRESH = DEBUG
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0  # 1 year for production

# Wagtail Cache Settings
if not DEBUG and "pages" in CACHES:
    WAGTAIL_CACHE = True
    WAGTAIL_CACHE_BACKEND = "pages"
    WAGTAILFRONTENDCACHE = {
        "default": {
            "BACKEND": "wagtail.contrib.frontend_cache.backends.HTTPBackend",
            "LOCATION": "http://localhost:8000",
        }
    }

# Content Security Policy (CSP) Headers
if not DEBUG:
    CSP_DEFAULT_SRC = "'self'"
    CSP_SCRIPT_SRC = "'self' 'unsafe-inline' 'unsafe-eval'"
    CSP_STYLE_SRC = "'self' 'unsafe-inline'"
    CSP_IMG_SRC = "'self' data: https:"
    CSP_FONT_SRC = "'self' https:"
    CSP_CONNECT_SRC = "'self'"
    CSP_FRAME_ANCESTORS = "'none'"

# Additional Security Settings for Production
if not DEBUG:
    # HTTPS redirect - controlled by environment variable (default False for initial deployment)
    # Note: SECURE_SSL_REDIRECT already set above, don't override it here
    pass  # SECURE_SSL_REDIRECT is already configured above
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # HSTS Settings
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Content Security
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

    # Cookie Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SAMESITE = "Lax"

    # Frame Options
    X_FRAME_OPTIONS = "DENY"

    # Additional Security Headers (will be added via middleware)
    SECURE_PERMISSIONS_POLICY = {
        "accelerometer": [],
        "camera": [],
        "geolocation": [],
        "gyroscope": [],
        "magnetometer": [],
        "microphone": [],
        "payment": [],
        "usb": [],
    }

# Data Upload Settings
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB

# Rely on Wagtail's built-in default-site fallback for settings via
# WAGTAILSETTINGS_CONTEXT_USE_DEFAULT_SITE rather than monkey-patching
