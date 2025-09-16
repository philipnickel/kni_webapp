# =============================================================================
# Django Settings - Main Entry Point
# This file imports the appropriate settings based on the environment
# =============================================================================

import os

# Determine which settings to use based on DJANGO_SETTINGS_MODULE
settings_module = os.getenv("DJANGO_SETTINGS_MODULE", "project.settings.production")

if settings_module.endswith(".dev"):
    from .settings.dev import *
elif settings_module.endswith(".production"):
    from .settings.production import *
else:
    # Fallback to production for backward compatibility
    from .settings.production import *