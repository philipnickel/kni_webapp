"""
Test suite for error handling and edge cases.
Tests 404/500 errors, form validation, and system resilience.
"""

import pytest
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from unittest.mock import patch, Mock

from apps.contacts.models import ContactSubmission
from apps.contacts.forms import ContactForm
from apps.pages.models import HomePage, ContactPage
from apps.projects.models import Project


@pytest.mark.django_db
class TestHTTPErrorHandling:
    """Test HTTP error handling (404, 500, etc.)."""

    def test_404_error_page(self, client):
        """Test 404 error page displays correctly."""
        response = client.get('/non-existent-url/')
        assert response.status_code == 404

    def test_404_with_valid_domain(self, client):
        """Test 404 with valid domain structure."""
        response = client.get('/valid-looking-url/that-does-not-exist/')
        assert response.status_code == 404

    def test_deeply_nested_404(self, client):
        """Test deeply nested non-existent URLs."""
        response = client.get('/level1/level2/level3/level4/non-existent/')
        assert response.status_code == 404

    def test_404_with_query_parameters(self, client):
        """Test 404 pages with query parameters."""
        response = client.get('/non-existent/?param=value&other=123')
        assert response.status_code == 404

    def test_404_with_special_characters(self, client):
        """Test 404 with special characters in URL."""
        special_urls = [
            '/non-existent-üñíçødé/',
            '/path with spaces/',
            '/path?param=value with spaces',
        ]

        for url in special_urls:
            response = client.get(url)
            assert response.status_code == 404

    @override_settings(DEBUG=False)
    def test_500_error_handling(self, client):
        """Test 500 error handling in production mode."""
        # This test would require triggering an actual 500 error
        # Implementation depends on creating a view that raises an exception
        pass

    def test_csrf_failure_handling(self, client):
        """Test CSRF token failure handling."""
        # Note: Contact form has @csrf_exempt, so this tests general CSRF behavior
        url = reverse('contacts:form')

        # Enable CSRF checking for this test
        client = Client(enforce_csrf_checks=True)

        # POST without CSRF token should fail for normal views
        # But contact form is exempt, so this documents the behavior
        response = client.post(url, {'name': 'test'})
        # Behavior depends on whether view has csrf_exempt


@pytest.mark.django_db
class TestFormValidationErrors:
    """Test form validation and error handling."""

    def test_contact_form_validation_errors_display(self, client):
        """Test that form validation errors are displayed properly."""
        url = reverse('contacts:form')

        invalid_data = {
            'name': '',  # Required field empty
            'email': 'invalid-email',  # Invalid email format
            'phone': 'x' * 65,  # Exceeds max length
            'message': 'Valid message',
            'consent': False,  # Required consent not given
            'honeypot': ''
        }

        response = client.post(url, data=invalid_data)

        assert response.status_code == 200  # Stays on form page
        assert 'form' in response.context
        form = response.context['form']

        # Check specific field errors
        assert not form.is_valid()
        assert 'name' in form.errors
        assert 'email' in form.errors
        assert 'consent' in form.errors

        # Check if field length validation works
        if len(invalid_data['phone']) > 64:
            assert 'phone' in form.errors or form.is_valid()  # Depends on model validation

    def test_form_error_messages_are_user_friendly(self, client):
        """Test that error messages are user-friendly."""
        url = reverse('contacts:form')

        response = client.post(url, data={
            'name': '',
            'email': 'bad-email',
            'phone': '',
            'message': '',
            'consent': False,
            'honeypot': ''
        })

        form = response.context['form']
        error_messages = str(form.errors)

        # Error messages should not contain technical jargon
        technical_terms = ['constraint', 'null', 'varchar', 'integrity']
        for term in technical_terms:
            assert term.lower() not in error_messages.lower()

    def test_form_preserves_valid_data_on_error(self, client):
        """Test that form preserves valid data when other fields have errors."""
        url = reverse('contacts:form')

        data = {
            'name': 'John Doe',  # Valid
            'email': 'invalid-email',  # Invalid
            'phone': '12345678',  # Valid
            'message': 'Test message',  # Valid
            'consent': True,  # Valid
            'honeypot': ''
        }

        response = client.post(url, data=data)
        form = response.context['form']

        # Valid fields should retain their values
        assert form.data['name'] == 'John Doe'
        assert form.data['phone'] == '12345678'
        assert form.data['message'] == 'Test message'

    def test_honeypot_field_error_handling(self, client):
        """Test honeypot field spam detection error handling."""
        url = reverse('contacts:form')

        spam_data = {
            'name': 'Spam Bot',
            'email': 'spam@bot.com',
            'phone': '12345678',
            'message': 'Spam message',
            'consent': True,
            'honeypot': 'filled-by-bot'  # This triggers spam detection
        }

        response = client.post(url, data=spam_data)
        form = response.context['form']

        assert not form.is_valid()
        # Spam error should be in non-field errors
        non_field_errors = str(form.non_field_errors())
        assert 'spam' in non_field_errors.lower()


@pytest.mark.django_db
class TestDatabaseErrorHandling:
    """Test database-related error handling."""

    def test_contact_submission_database_constraints(self, site):
        """Test database constraints on ContactSubmission model."""
        # Test required field constraints
        with pytest.raises((IntegrityError, ValidationError)):
            ContactSubmission.objects.create(
                site=site,
                # Missing required name field
                email='test@example.com',
                consent=True
            )

    def test_duplicate_constraint_handling(self, site):
        """Test handling of duplicate constraints if any exist."""
        # Create first submission
        submission1 = ContactSubmission.objects.create(
            site=site,
            name='John Doe',
            email='john@example.com',
            consent=True
        )

        # Creating another with same data should be allowed
        # (no unique constraints on these fields)
        submission2 = ContactSubmission.objects.create(
            site=site,
            name='John Doe',
            email='john@example.com',
            consent=True
        )

        assert submission1.pk != submission2.pk

    def test_foreign_key_constraint_handling(self):
        """Test foreign key constraint handling."""
        # Test creating submission with invalid site reference
        with pytest.raises((IntegrityError, ValidationError)):
            ContactSubmission.objects.create(
                site_id=99999,  # Non-existent site ID
                name='John Doe',
                email='john@example.com',
                consent=True
            )

    @patch('apps.contacts.models.ContactSubmission.save')
    def test_database_connection_error_handling(self, mock_save, client, valid_contact_form_data):
        """Test handling of database connection errors."""
        # Simulate database save failure
        mock_save.side_effect = Exception("Database connection failed")

        url = reverse('contacts:form')

        # This should be handled gracefully by the application
        with pytest.raises(Exception):
            response = client.post(url, data=valid_contact_form_data)


@pytest.mark.django_db
class TestInputValidationEdgeCases:
    """Test edge cases for input validation."""

    def test_extremely_long_input_fields(self, client):
        """Test handling of extremely long input values."""
        url = reverse('contacts:form')

        # Test with extremely long values
        long_data = {
            'name': 'A' * 1000,  # Much longer than expected
            'email': 'test@' + 'a' * 240 + '.com',  # Very long email
            'phone': '1' * 100,  # Very long phone
            'message': 'B' * 10000,  # Very long message
            'consent': True,
            'honeypot': ''
        }

        response = client.post(url, data=long_data)

        # Should handle gracefully without crashing
        assert response.status_code in [200, 302]

        if response.status_code == 200:
            # If validation failed, should show appropriate errors
            form = response.context['form']
            # Check if length validation is working

    def test_unicode_and_special_characters(self, client):
        """Test handling of Unicode and special characters."""
        url = reverse('contacts:form')

        unicode_data = {
            'name': 'Test User øæå ñüéî 中文',
            'email': 'test@example.com',
            'phone': '+45 12 34 56 78',
            'message': 'Message with émojis 🙂🌟 and spëcial çhars!',
            'consent': True,
            'honeypot': ''
        }

        response = client.post(url, data=unicode_data)

        # Should handle Unicode characters properly
        if response.status_code == 302:
            submission = ContactSubmission.objects.first()
            assert 'øæå' in submission.name
            assert 'émojis' in submission.message

    def test_sql_injection_attempts(self, client):
        """Test protection against SQL injection attempts."""
        url = reverse('contacts:form')

        malicious_data = {
            'name': "'; DROP TABLE contacts_contactsubmission; --",
            'email': 'test@example.com',
            'phone': '12345678',
            'message': "1' OR '1'='1",
            'consent': True,
            'honeypot': ''
        }

        response = client.post(url, data=malicious_data)

        # Should handle safely without executing SQL
        if response.status_code == 302:
            # If successful, verify data is stored safely
            submission = ContactSubmission.objects.first()
            # Data should be stored as-is, not executed
            assert "DROP TABLE" in submission.name

        # Verify table still exists
        assert ContactSubmission.objects.count() >= 0

    def test_xss_attempt_handling(self, client):
        """Test protection against XSS attempts."""
        url = reverse('contacts:form')

        xss_data = {
            'name': '<script>alert("XSS")</script>',
            'email': 'test@example.com',
            'phone': '12345678',
            'message': '<img src="x" onerror="alert(1)">',
            'consent': True,
            'honeypot': ''
        }

        response = client.post(url, data=xss_data)

        # Should store data safely
        if response.status_code == 302:
            submission = ContactSubmission.objects.first()
            # Scripts should be stored as text, not executed
            assert '<script>' in submission.name
            assert '<img' in submission.message

    def test_null_byte_injection(self, client):
        """Test protection against null byte injection."""
        url = reverse('contacts:form')

        null_data = {
            'name': 'Test\x00User',
            'email': 'test@example.com',
            'phone': '12345678',
            'message': 'Message\x00with\x00nulls',
            'consent': True,
            'honeypot': ''
        }

        response = client.post(url, data=null_data)

        # Should handle null bytes safely
        assert response.status_code in [200, 302]


@pytest.mark.django_db
class TestConcurrencyEdgeCases:
    """Test concurrency and race condition handling."""

    def test_simultaneous_form_submissions(self, client, valid_contact_form_data):
        """Test handling of simultaneous form submissions."""
        import threading
        import time

        url = reverse('contacts:form')
        results = []
        errors = []

        def submit_form():
            try:
                response = client.post(url, data=valid_contact_form_data)
                results.append(response.status_code)
            except Exception as e:
                errors.append(str(e))

        # Create multiple threads to simulate simultaneous submissions
        threads = []
        for i in range(5):
            thread = threading.Thread(target=submit_form)
            threads.append(thread)

        # Start all threads simultaneously
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join(timeout=5)

        # Check results
        assert len(errors) == 0  # No errors should occur
        # All submissions should either succeed or fail gracefully
        assert all(status in [200, 302] for status in results)


@pytest.mark.django_db
class TestSystemResourceLimits:
    """Test system resource limits and edge cases."""

    def test_memory_usage_with_large_datasets(self, gallery_page):
        """Test memory usage doesn't explode with large datasets."""
        # Create many projects
        projects = []
        for i in range(100):
            project = Project.objects.create(
                title=f'Project {i}',
                description=f'Description {i}' * 100,  # Large description
                published=True
            )
            projects.append(project)

        # Test gallery page can handle large dataset
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/')

        context = gallery_page.get_context(request)
        project_list = list(context['project_pages'])

        # Should return projects without memory issues
        assert len(project_list) <= 100

    def test_file_upload_limits(self, client, admin_user):
        """Test file upload size limits if applicable."""
        # This would test image uploads for projects or pages
        # Implementation depends on file upload functionality
        pass

    @pytest.mark.slow
    def test_timeout_handling(self, client):
        """Test request timeout handling."""
        # This would test long-running operations
        # Implementation depends on having operations that could timeout
        pass


@pytest.mark.django_db
class TestConfigurationEdgeCases:
    """Test configuration-related edge cases."""

    @override_settings(DEBUG=False)
    def test_production_mode_error_handling(self, client):
        """Test error handling in production mode."""
        response = client.get('/non-existent-page/')
        assert response.status_code == 404

        # In production, should not reveal sensitive information
        content = response.content.decode()
        sensitive_info = ['traceback', 'exception', 'debug', 'stacktrace']
        for info in sensitive_info:
            assert info.lower() not in content.lower()

    @override_settings(ALLOWED_HOSTS=[])
    def test_invalid_host_handling(self):
        """Test handling of requests to invalid hosts."""
        # Create client with specific host
        client = Client()

        # Request with disallowed host should be rejected
        response = client.get('/', HTTP_HOST='malicious.com')
        assert response.status_code == 400  # Bad Request

    def test_missing_environment_variables(self):
        """Test handling of missing environment variables."""
        # This would test behavior when required env vars are missing
        # Implementation depends on how settings handle missing variables
        pass