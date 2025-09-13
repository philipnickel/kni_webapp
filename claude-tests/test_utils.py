"""
Test utilities and helper functions for the JCleemannByg test suite.
"""

import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from wagtail.models import Site, Page
import tempfile
import os
from PIL import Image
import io

User = get_user_model()


class TestDataFactory:
    """Factory for creating test data."""

    @staticmethod
    def create_test_image(filename='test_image.jpg', format='JPEG', size=(100, 100)):
        """Create a test image file."""
        image = Image.new('RGB', size, color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix=f'.{format.lower()}', delete=False)
        image.save(temp_file, format=format)
        temp_file.seek(0)
        return temp_file

    @staticmethod
    def create_large_text(length=1000):
        """Create large text for testing."""
        return 'Test text content. ' * (length // 18)

    @staticmethod
    def create_contact_form_data(**overrides):
        """Create valid contact form data with optional overrides."""
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '12345678',
            'message': 'This is a test message',
            'consent': True,
            'honeypot': ''
        }
        data.update(overrides)
        return data


class TestAssertions:
    """Custom assertions for tests."""

    @staticmethod
    def assertContainsText(response, text, msg_prefix=''):
        """Assert response contains specific text."""
        content = response.content.decode()
        assert text in content, f"{msg_prefix}Expected '{text}' in response content"

    @staticmethod
    def assertNotContainsText(response, text, msg_prefix=''):
        """Assert response does not contain specific text."""
        content = response.content.decode()
        assert text not in content, f"{msg_prefix}Expected '{text}' not in response content"

    @staticmethod
    def assertResponseTime(response_time, max_time, msg_prefix=''):
        """Assert response time is within acceptable limit."""
        assert response_time <= max_time, \
            f"{msg_prefix}Response time {response_time:.3f}s exceeds limit {max_time}s"

    @staticmethod
    def assertValidHTML(response, msg_prefix=''):
        """Assert response contains valid HTML structure."""
        content = response.content.decode()
        # Basic HTML validation
        assert '<html' in content or '<!DOCTYPE' in content, \
            f"{msg_prefix}Response does not contain valid HTML structure"

    @staticmethod
    def assertNoSQLErrors(func, msg_prefix=''):
        """Assert function doesn't cause SQL errors."""
        try:
            result = func()
            return result
        except Exception as e:
            if 'sql' in str(e).lower() or 'database' in str(e).lower():
                pytest.fail(f"{msg_prefix}SQL/Database error occurred: {e}")
            raise


class MockObjects:
    """Mock objects for testing."""

    @staticmethod
    def mock_request(user=None, method='GET', path='/', data=None):
        """Create a mock request object."""
        from django.test import RequestFactory
        from django.contrib.auth.models import AnonymousUser

        factory = RequestFactory()

        if method.upper() == 'POST':
            request = factory.post(path, data or {})
        else:
            request = factory.get(path)

        request.user = user or AnonymousUser()
        return request

    @staticmethod
    def mock_wagtail_site():
        """Create a mock Wagtail site."""
        site, created = Site.objects.get_or_create(
            hostname='testserver',
            defaults={
                'port': 80,
                'site_name': 'Test Site',
                'is_default_site': True
            }
        )
        return site


class PerformanceTimer:
    """Context manager for timing operations."""

    def __init__(self, max_time=None):
        self.max_time = max_time
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        import time
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed_time = time.time() - self.start_time

        if self.max_time and self.elapsed_time > self.max_time:
            pytest.fail(f"Operation took {self.elapsed_time:.3f}s, "
                       f"exceeding limit of {self.max_time}s")

    def get_elapsed_time(self):
        """Get elapsed time in seconds."""
        return self.elapsed_time


class DatabaseAssertions:
    """Database-specific assertions."""

    @staticmethod
    def assertRecordCount(model_class, expected_count, msg_prefix=''):
        """Assert database record count."""
        actual_count = model_class.objects.count()
        assert actual_count == expected_count, \
            f"{msg_prefix}Expected {expected_count} records, got {actual_count}"

    @staticmethod
    def assertRecordExists(model_class, **filters):
        """Assert record exists with given filters."""
        exists = model_class.objects.filter(**filters).exists()
        assert exists, f"No {model_class.__name__} record found with filters {filters}"

    @staticmethod
    def assertRecordDoesNotExist(model_class, **filters):
        """Assert record does not exist with given filters."""
        exists = model_class.objects.filter(**filters).exists()
        assert not exists, f"{model_class.__name__} record found with filters {filters}"


class SecurityTestHelpers:
    """Helpers for security testing."""

    @staticmethod
    def get_xss_payloads():
        """Get common XSS payloads for testing."""
        return [
            '<script>alert("XSS")</script>',
            '<img src="x" onerror="alert(1)">',
            'javascript:alert("XSS")',
            '<svg onload="alert(1)">',
            '"><script>alert("XSS")</script>',
        ]

    @staticmethod
    def get_sql_injection_payloads():
        """Get common SQL injection payloads for testing."""
        return [
            "'; DROP TABLE users; --",
            "1' OR '1'='1",
            "admin'--",
            "' UNION SELECT * FROM users--",
            "1; SELECT * FROM information_schema.tables",
        ]

    @staticmethod
    def get_path_traversal_payloads():
        """Get path traversal payloads for testing."""
        return [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32\\config\\sam',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2f',
            '....//....//....//etc/passwd',
        ]


class EmailTestHelpers:
    """Helpers for email testing."""

    @staticmethod
    def assert_email_sent(expected_count=1):
        """Assert that emails were sent."""
        from django.core import mail
        assert len(mail.outbox) == expected_count, \
            f"Expected {expected_count} emails, got {len(mail.outbox)}"

    @staticmethod
    def assert_email_contains(text, email_index=0):
        """Assert that email contains specific text."""
        from django.core import mail
        if not mail.outbox:
            pytest.fail("No emails sent")

        email = mail.outbox[email_index]
        assert text in email.body, f"Email does not contain '{text}'"

    @staticmethod
    def clear_email_outbox():
        """Clear the email outbox."""
        from django.core import mail
        mail.outbox = []


class FormTestHelpers:
    """Helpers for form testing."""

    @staticmethod
    def submit_form(client, url, data, follow=False):
        """Submit form and return response with timing."""
        with PerformanceTimer(max_time=5.0) as timer:
            response = client.post(url, data=data, follow=follow)

        return response, timer.get_elapsed_time()

    @staticmethod
    def assert_form_error(response, field_name, error_text=None):
        """Assert form has error on specific field."""
        assert 'form' in response.context, "No form in response context"
        form = response.context['form']

        assert not form.is_valid(), "Form should not be valid"
        assert field_name in form.errors, f"No error on field '{field_name}'"

        if error_text:
            field_errors = form.errors[field_name]
            assert any(error_text in str(error) for error in field_errors), \
                f"Error text '{error_text}' not found in field errors: {field_errors}"


class WagtailTestHelpers:
    """Helpers for Wagtail-specific testing."""

    @staticmethod
    def create_test_page(parent, page_class, **kwargs):
        """Create a test page under given parent."""
        defaults = {
            'title': f'Test {page_class.__name__}',
            'slug': f'test-{page_class.__name__.lower()}',
        }
        defaults.update(kwargs)

        page = page_class(**defaults)
        parent.add_child(instance=page)
        return page

    @staticmethod
    def assert_page_published(page):
        """Assert page is published (live)."""
        assert page.live, f"Page '{page.title}' should be published"

    @staticmethod
    def assert_page_accessible(client, page):
        """Assert page is accessible via HTTP."""
        url = page.get_url()
        response = client.get(url)
        assert response.status_code == 200, \
            f"Page '{page.title}' at '{url}' returned status {response.status_code}"


class TestCase:
    """Base test case with useful methods."""

    def setUp(self):
        """Set up test data."""
        self.assertions = TestAssertions()
        self.db_assertions = DatabaseAssertions()
        self.security = SecurityTestHelpers()
        self.email_helpers = EmailTestHelpers()
        self.form_helpers = FormTestHelpers()
        self.wagtail_helpers = WagtailTestHelpers()

    def create_test_user(self, username='testuser', **kwargs):
        """Create a test user."""
        defaults = {
            'email': f'{username}@test.com',
            'first_name': 'Test',
            'last_name': 'User',
        }
        defaults.update(kwargs)

        return User.objects.create_user(username=username, **defaults)

    def create_admin_user(self, username='admin', **kwargs):
        """Create an admin user."""
        defaults = {
            'email': f'{username}@test.com',
            'is_staff': True,
            'is_superuser': True,
        }
        defaults.update(kwargs)

        return User.objects.create_user(username=username, **defaults)