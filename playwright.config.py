"""
Playwright configuration for accessibility testing.
"""

from playwright.sync_api import sync_playwright
import os

# Playwright configuration for accessibility tests
PLAYWRIGHT_CONFIG = {
    'headless': True,
    'slow_mo': 0,
    'timeout': 30000,
    'browsers': ['chromium'],  # Focus on Chromium for consistent results
    'viewport': {'width': 1200, 'height': 800},
    'ignore_https_errors': True,
    'screenshot': 'only-on-failure',
    'video': 'retain-on-failure',
    'trace': 'retain-on-failure',
}

# Browser context configuration for accessibility
BROWSER_CONTEXT_CONFIG = {
    'locale': 'da-DK',
    'timezone_id': 'Europe/Copenhagen',
    'color_scheme': 'light',
    'reduced_motion': 'no-preference',
    'forced_colors': 'none',
    'permissions': ['clipboard-read', 'clipboard-write'],
}

# Accessibility testing specific configuration
ACCESSIBILITY_CONFIG = {
    'wait_for_load_state': 'networkidle',
    'stabilization_timeout': 500,
    'screenshot_full_page': True,
    'axe_timeout': 10000,
}