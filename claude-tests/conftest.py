"""
Pytest configuration and shared fixtures for the JCleemannByg test suite.
"""

import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from wagtail.models import Site, Page
from wagtail.test.utils import WagtailPageTestCase
from model_bakery import baker
import tempfile
import os
from pathlib import Path

from apps.pages.models import HomePage, ContactPage, GalleryPage
from apps.contacts.models import ContactSubmission
from apps.projects.models import Project

# Import accessibility testing utilities (conditional for backward compatibility)
try:
    from .accessibility_config import AccessibilityConfig, AccessibilityReportGenerator
except ImportError:
    # For when running tests from project root
    try:
        import sys
        sys.path.append(os.path.dirname(__file__))
        from accessibility_config import AccessibilityConfig, AccessibilityReportGenerator
    except ImportError:
        # Fallback - create dummy classes
        class AccessibilityConfig:
            pass
        class AccessibilityReportGenerator:
            pass

User = get_user_model()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    """Set up the test database with initial data."""
    with django_db_blocker.unblock():
        # Create default site and pages
        call_command('migrate', '--run-syncdb')


@pytest.fixture
def client():
    """Django test client."""
    return Client()


@pytest.fixture
def admin_client(admin_user):
    """Django test client logged in as admin."""
    client = Client()
    client.force_login(admin_user)
    return client


@pytest.fixture
def admin_user():
    """Create a superuser for admin tests."""
    return baker.make(
        User,
        is_staff=True,
        is_superuser=True,
        username='testadmin',
        email='admin@test.com'
    )


@pytest.fixture
def regular_user():
    """Create a regular user."""
    return baker.make(
        User,
        username='testuser',
        email='user@test.com'
    )


@pytest.fixture
def site():
    """Create a test site."""
    site, created = Site.objects.get_or_create(
        hostname='testserver',
        defaults={
            'port': 80,
            'site_name': 'Test Site',
            'root_page_id': 1,
            'is_default_site': True
        }
    )
    return site


@pytest.fixture
def root_page():
    """Get the root page."""
    return Page.objects.get(depth=1)


@pytest.fixture
def home_page(site, root_page):
    """Create a test home page."""
    home_page = HomePage(
        title='Test Home',
        slug='test-home',
        intro='Welcome to our test home page'
    )
    root_page.add_child(instance=home_page)
    site.root_page = home_page
    site.save()
    return home_page


@pytest.fixture
def contact_page(root_page):
    """Create a test contact page."""
    contact_page = ContactPage(
        title='Contact Us',
        slug='contact',
        intro='Contact us for more information',
        show_contact_form=True,
        contact_form_title='Get in Touch',
        contact_form_intro='Send us a message'
    )
    root_page.add_child(instance=contact_page)
    return contact_page


@pytest.fixture
def gallery_page(root_page):
    """Create a test gallery page."""
    gallery_page = GalleryPage(
        title='Our Projects',
        slug='projects',
        intro='View our completed projects'
    )
    root_page.add_child(instance=gallery_page)
    return gallery_page


@pytest.fixture
def sample_project():
    """Create a sample project."""
    return baker.make(
        Project,
        title='Test Project',
        description='A test project',
        published=True,
        featured=True
    )


@pytest.fixture
def contact_submission(site):
    """Create a sample contact submission."""
    return baker.make(
        ContactSubmission,
        site=site,
        name='John Doe',
        email='john@example.com',
        phone='12345678',
        message='Test message',
        consent=True,
        status='new'
    )


@pytest.fixture
def valid_contact_form_data():
    """Valid contact form data."""
    return {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '12345678',
        'message': 'This is a test message',
        'consent': True,
        'honeypot': ''  # Anti-spam field should be empty
    }


@pytest.fixture
def invalid_contact_form_data():
    """Invalid contact form data."""
    return {
        'name': '',  # Required field empty
        'email': 'invalid-email',  # Invalid email
        'phone': '12345678',
        'message': 'Test message',
        'consent': False,  # Consent not given
        'honeypot': ''
    }


@pytest.fixture
def spam_contact_form_data():
    """Spam contact form data (honeypot filled)."""
    return {
        'name': 'Spam Bot',
        'email': 'spam@example.com',
        'phone': '12345678',
        'message': 'This is spam',
        'consent': True,
        'honeypot': 'filled-by-bot'  # Anti-spam honeypot filled
    }


@pytest.fixture
def media_root():
    """Create a temporary media root for tests."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Cleanup after test
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)


class WagtailTestCase(WagtailPageTestCase):
    """Base test case class that provides Wagtail-specific assertions."""

    def setUp(self):
        super().setUp()
        # Set up any common test data here

    def assertPagePublished(self, page):
        """Assert that a page is published (live)."""
        self.assertTrue(page.live, f"Page '{page.title}' should be published")

    def assertPageNotPublished(self, page):
        """Assert that a page is not published."""
        self.assertFalse(page.live, f"Page '{page.title}' should not be published")

    def assertPageHasUrl(self, page, expected_url):
        """Assert that a page has the expected URL."""
        actual_url = page.get_url()
        self.assertEqual(actual_url, expected_url,
                        f"Expected URL '{expected_url}', got '{actual_url}'")


# Custom markers for different test types
pytestmark = [
    pytest.mark.django_db,
]


# Accessibility testing fixtures
@pytest.fixture(scope='session')
def accessibility_config():
    """Provide accessibility testing configuration."""
    return AccessibilityConfig()


@pytest.fixture
def accessibility_reporter():
    """Provide accessibility report generator."""
    return AccessibilityReportGenerator()


@pytest.fixture(scope='session')
def live_server():
    """Provide a live server for Playwright accessibility tests."""
    from django.test.utils import setup_test_environment, teardown_test_environment
    from django.conf import settings
    import socket

    # Find an available port
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()

    class AccessibilityLiveServer(StaticLiveServerTestCase):
        port = port
        host = '127.0.0.1'

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.live_server_url = f'http://{cls.host}:{cls.port}'

    server = AccessibilityLiveServer()
    server.setUpClass()

    yield server

    server.tearDownClass()


@pytest.fixture
def browser_context_args():
    """Configure browser context for accessibility testing."""
    return {
        'viewport': {'width': 1200, 'height': 800},
        'ignore_https_errors': True,
        'java_script_enabled': True,
        'locale': 'da-DK',
        'timezone_id': 'Europe/Copenhagen',
        'color_scheme': 'light',
        'reduced_motion': 'no-preference',
        'forced_colors': 'none',
    }


@pytest.fixture
def accessibility_test_data():
    """Provide test data for accessibility testing."""
    from .accessibility_config import generate_test_form_data
    return generate_test_form_data()


# Utility fixtures for accessibility testing
@pytest.fixture
def theme_switcher():
    """Fixture to switch themes during testing."""
    def switch_theme(page, theme_name):
        """Switch to the Frostbite carpenter theme."""
        page.evaluate(f"window.switchTheme('{theme_name}')")
        page.wait_for_timeout(500)  # Allow theme to apply
        return page.evaluate("window.getCurrentTheme()")

    return switch_theme


@pytest.fixture
def axe_builder():
    """Fixture for configuring axe accessibility testing."""
    def create_axe_builder(page, config=None):
        """Create and configure axe builder."""
        from axe_playwright_python import AxeBuilder

        builder = AxeBuilder(page)

        if config:
            if 'rules' in config:
                for rule, settings in config['rules'].items():
                    if settings.get('enabled', True):
                        builder.with_rules([rule])
                    else:
                        builder.disable_rules([rule])

            if 'tags' in config:
                builder.with_tags(config['tags'])

        return builder

    return create_axe_builder


@pytest.fixture
def screenshot_manager():
    """Fixture for managing test screenshots."""
    def take_screenshot(page, name, theme=None, viewport=None):
        """Take and save a screenshot with metadata."""
        screenshots_dir = Path(__file__).parent / 'screenshots'
        screenshots_dir.mkdir(exist_ok=True)

        filename_parts = [name]
        if theme:
            filename_parts.append(theme)
        if viewport:
            filename_parts.append(viewport)

        filename = '_'.join(filename_parts) + '.png'
        screenshot_path = screenshots_dir / filename

        page.screenshot(path=str(screenshot_path), full_page=True)
        return screenshot_path

    return take_screenshot