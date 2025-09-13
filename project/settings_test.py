"""
Test settings for the JCleemannByg Django/Wagtail application.
Optimized for fast test execution and isolation.
"""

from .settings import *
import tempfile

# Use in-memory SQLite for faster tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'OPTIONS': {
            'timeout': 20,
        }
    }
}

# Test-specific settings
DEBUG = False
TESTING = True

# Disable migrations for faster test runs
class DisableMigrations:
    def __contains__(self, item):
        return True
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Use a temporary directory for media files during tests
MEDIA_ROOT = tempfile.mkdtemp()

# Disable password validators for test users
AUTH_PASSWORD_VALIDATORS = []

# Use console email backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Fast password hashing for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable security features that slow down tests
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Logging configuration for tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# Static files for tests
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Test-specific Wagtail settings
WAGTAIL_AUTO_UPDATE_PREVIEW = False
WAGTAIL_ENABLE_UPDATE_CHECK = False
WAGTAIL_USAGE_COUNT_ENABLED = False

# Faster search backend for tests
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.dummy',
    }
}