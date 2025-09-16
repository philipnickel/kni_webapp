from .base import *
import os

# Production-specific settings
DEBUG = False

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

# Wagtail admin URL for production
if PRIMARY_DOMAIN:
    WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", f"https://{PRIMARY_DOMAIN}")
else:
    WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "http://localhost:8000")

# Email Configuration for Production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@jcleemannbyg.dk")

# S3 Configuration (if enabled)
USE_S3 = os.getenv("USE_S3", "False").lower() == "true"
if USE_S3:
    INSTALLED_APPS += ["storages"]
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
    
    # AWS S3 settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "us-east-1")
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")
    AWS_S3_USE_SSL = os.getenv("AWS_S3_USE_SSL", "True").lower() == "true"
    AWS_S3_VERIFY = os.getenv("AWS_S3_VERIFY", "True").lower() == "true"
    AWS_DEFAULT_ACL = None
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }

# Security settings
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False").lower() == "true"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

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

# Additional Security Headers
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
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

# Content Security Policy (CSP) Headers
CSP_DEFAULT_SRC = "'self'"
CSP_SCRIPT_SRC = "'self' 'unsafe-inline' 'unsafe-eval'"
CSP_STYLE_SRC = "'self' 'unsafe-inline'"
CSP_IMG_SRC = "'self' data: https:"
CSP_FONT_SRC = "'self' https:"
CSP_CONNECT_SRC = "'self'"
CSP_FRAME_ANCESTORS = "'none'"

# Production logging
LOGGING["handlers"]["console"]["formatter"] = "json"
LOGGING["loggers"]["django"]["handlers"] = ["console", "file"]
LOGGING["loggers"]["apps"]["handlers"] = ["console", "file"]

# WhiteNoise settings for production
WHITENOISE_USE_FINDERS = False
WHITENOISE_AUTOREFRESH = False
WHITENOISE_MAX_AGE = 31536000  # 1 year

# Enable Wagtail cache in production
if "pages" in CACHES:
    WAGTAIL_CACHE = True
    WAGTAIL_CACHE_BACKEND = "pages"
