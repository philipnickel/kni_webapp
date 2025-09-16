from .base import *
import os

# Development-specific settings
DEBUG = True

# Derive ALLOWED_HOSTS automatically
_default_hosts = ["localhost", "127.0.0.1", "0.0.0.0"]
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

# Development tools
INTERNAL_IPS = ["127.0.0.1", "::1"]

# Development-specific apps
INSTALLED_APPS += [
    "debug_toolbar",
]

# Development middleware - insert debug toolbar after GZip middleware
MIDDLEWARE.insert(3, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "mailhog")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "1025"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False").lower() == "true"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "dev@localhost")

# Wagtail admin URL for development
WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "http://localhost:8000")

# Local media/static paths
MEDIA_ROOT = os.getenv("MEDIA_ROOT", BASE_DIR / "media")
STATIC_ROOT = os.getenv("STATIC_ROOT", BASE_DIR / "staticfiles")

# Development-specific database settings
DATABASES["default"]["CONN_MAX_AGE"] = 0  # Disable connection pooling in development

# Development logging - use console only to avoid file permission issues
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'wagtail': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# WhiteNoise settings for development
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
WHITENOISE_MAX_AGE = 0

# Disable cache in development
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

# Use database sessions in development
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Security settings for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_REFERRER_POLICY = None
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None
X_FRAME_OPTIONS = "SAMEORIGIN"

# Disable Wagtail cache in development
WAGTAIL_CACHE = False
