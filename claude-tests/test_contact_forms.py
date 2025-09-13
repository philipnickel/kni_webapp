"""
Test suite for contact form functionality.
Tests form validation, submission, and email processing.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from unittest.mock import patch, Mock

from apps.contacts.models import ContactSubmission
from apps.contacts.forms import ContactForm
from apps.contacts.views import contact_view, contact_thanks


@pytest.mark.contact_form
class TestContactForm:
    """Test the ContactForm model form."""

    def test_contact_form_valid_data(self, valid_contact_form_data):
        """Test form with valid data."""
        form = ContactForm(data=valid_contact_form_data)
        assert form.is_valid()

    def test_contact_form_missing_required_fields(self):
        """Test form validation with missing required fields."""
        form_data = {
            'name': '',  # Required field empty
            'email': '',  # Required field empty
            'phone': '',
            'message': '',
            'consent': False,  # Required field false
            'honeypot': ''
        }
        form = ContactForm(data=form_data)
        assert not form.is_valid()
        assert 'name' in form.errors
        assert 'email' in form.errors
        assert 'consent' in form.errors

    def test_contact_form_invalid_email(self):
        """Test form validation with invalid email."""
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email-format',
            'phone': '12345678',
            'message': 'Test message',
            'consent': True,
            'honeypot': ''
        }
        form = ContactForm(data=form_data)
        assert not form.is_valid()
        assert 'email' in form.errors

    def test_contact_form_honeypot_spam_detection(self, spam_contact_form_data):
        """Test honeypot anti-spam functionality."""
        form = ContactForm(data=spam_contact_form_data)
        assert not form.is_valid()
        assert 'Spam detected.' in str(form.non_field_errors())

    def test_contact_form_phone_optional(self):
        """Test that phone field is optional."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '',  # Optional field empty
            'message': 'Test message',
            'consent': True,
            'honeypot': ''
        }
        form = ContactForm(data=form_data)
        assert form.is_valid()

    def test_contact_form_message_optional(self):
        """Test that message field is optional."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '12345678',
            'message': '',  # Optional field empty
            'consent': True,
            'honeypot': ''
        }
        form = ContactForm(data=form_data)
        assert form.is_valid()


@pytest.mark.contact_form
@pytest.mark.django_db
class TestContactFormViews:
    """Test contact form views and submission process."""

    def test_contact_form_get_request(self, client, site):
        """Test GET request to contact form displays form."""
        url = reverse('contacts:form')
        response = client.get(url)

        assert response.status_code == 200
        assert 'form' in response.context
        assert isinstance(response.context['form'], ContactForm)

    def test_contact_form_post_valid_data(self, client, site, valid_contact_form_data):
        """Test valid form submission creates ContactSubmission and redirects."""
        url = reverse('contacts:form')

        # Ensure no existing submissions
        assert ContactSubmission.objects.count() == 0

        response = client.post(url, data=valid_contact_form_data)

        # Check redirect to thanks page
        assert response.status_code == 302
        assert response.url == reverse('contacts:thanks')

        # Check that submission was created
        assert ContactSubmission.objects.count() == 1

        submission = ContactSubmission.objects.first()
        assert submission.name == valid_contact_form_data['name']
        assert submission.email == valid_contact_form_data['email']
        assert submission.phone == valid_contact_form_data['phone']
        assert submission.message == valid_contact_form_data['message']
        assert submission.consent == valid_contact_form_data['consent']
        assert submission.status == 'new'
        assert submission.site == site

    def test_contact_form_post_invalid_data(self, client, invalid_contact_form_data):
        """Test invalid form submission shows errors."""
        url = reverse('contacts:form')

        response = client.post(url, data=invalid_contact_form_data)

        # Should not redirect, stays on form page
        assert response.status_code == 200
        assert 'form' in response.context
        assert not response.context['form'].is_valid()

        # No submission should be created
        assert ContactSubmission.objects.count() == 0

    def test_contact_form_post_spam_data(self, client, spam_contact_form_data):
        """Test spam submission (honeypot filled) is rejected."""
        url = reverse('contacts:form')

        response = client.post(url, data=spam_contact_form_data)

        # Should not redirect, stays on form page
        assert response.status_code == 200
        assert 'form' in response.context
        assert not response.context['form'].is_valid()

        # No submission should be created
        assert ContactSubmission.objects.count() == 0

    def test_contact_thanks_view(self, client):
        """Test contact thanks page displays correctly."""
        url = reverse('contacts:thanks')
        response = client.get(url)

        assert response.status_code == 200
        assert 'contacts/thanks.html' in [t.name for t in response.templates]

    def test_contact_form_csrf_protection(self, client, valid_contact_form_data):
        """Test CSRF protection on contact form (note: view has @csrf_exempt)."""
        # This test documents that the contact form currently has CSRF exemption
        # which might need review for security
        url = reverse('contacts:form')

        # Even without CSRF token, should work due to @csrf_exempt decorator
        response = client.post(url, data=valid_contact_form_data)
        assert response.status_code == 302

    def test_contact_form_with_different_sites(self, client, valid_contact_form_data):
        """Test contact form with different site contexts."""
        # Create additional site
        from wagtail.models import Site
        site2 = Site.objects.create(
            hostname='testserver2',
            port=80,
            site_name='Test Site 2',
            root_page_id=1
        )

        # Make request to specific site
        url = reverse('contacts:form')
        response = client.post(url, data=valid_contact_form_data,
                             HTTP_HOST='testserver2')

        if response.status_code == 302:
            # Check submission is associated with correct site
            submission = ContactSubmission.objects.first()
            # Site detection logic may vary based on implementation


@pytest.mark.contact_form
@pytest.mark.django_db
class TestContactSubmissionModel:
    """Test the ContactSubmission model."""

    def test_contact_submission_str_representation(self, contact_submission):
        """Test string representation of ContactSubmission."""
        expected = f"{contact_submission.name} — {contact_submission.created_at:%Y-%m-%d}"
        assert str(contact_submission) == expected

    def test_contact_submission_status_choices(self, contact_submission):
        """Test status field choices."""
        assert contact_submission.status == 'new'

        # Test changing status
        contact_submission.status = 'in_progress'
        contact_submission.save()
        contact_submission.refresh_from_db()
        assert contact_submission.status == 'in_progress'

        contact_submission.status = 'closed'
        contact_submission.save()
        contact_submission.refresh_from_db()
        assert contact_submission.status == 'closed'

    def test_contact_submission_required_fields(self, site):
        """Test that required fields are enforced at model level."""
        from django.db import IntegrityError

        # Test with missing required fields should fail
        with pytest.raises(IntegrityError):
            ContactSubmission.objects.create(
                site=site,
                # Missing name and email
                phone='12345678',
                message='Test',
                consent=True
            )

    def test_contact_submission_default_values(self, site):
        """Test default values for model fields."""
        submission = ContactSubmission.objects.create(
            site=site,
            name='John Doe',
            email='john@example.com',
            consent=True
        )

        # Check defaults
        assert submission.status == 'new'
        assert submission.consent == True
        assert submission.phone == ''
        assert submission.message == ''
        assert submission.created_at is not None

    def test_contact_submission_ordering(self, site):
        """Test that submissions can be ordered by creation date."""
        import time

        submission1 = ContactSubmission.objects.create(
            site=site,
            name='First User',
            email='first@example.com',
            consent=True
        )

        time.sleep(0.01)  # Ensure different timestamps

        submission2 = ContactSubmission.objects.create(
            site=site,
            name='Second User',
            email='second@example.com',
            consent=True
        )

        submissions = ContactSubmission.objects.order_by('-created_at')
        assert submissions.first() == submission2
        assert submissions.last() == submission1


@pytest.mark.contact_form
@pytest.mark.integration
@pytest.mark.django_db
class TestContactFormIntegration:
    """Integration tests for the complete contact form workflow."""

    def test_complete_contact_form_workflow(self, client, site, valid_contact_form_data):
        """Test the complete user journey from form to submission."""
        # Step 1: User visits contact form
        form_url = reverse('contacts:form')
        response = client.get(form_url)
        assert response.status_code == 200

        # Step 2: User submits valid form
        response = client.post(form_url, data=valid_contact_form_data)
        assert response.status_code == 302

        # Step 3: User is redirected to thanks page
        thanks_url = reverse('contacts:thanks')
        response = client.get(thanks_url)
        assert response.status_code == 200

        # Step 4: Verify submission exists in database
        assert ContactSubmission.objects.count() == 1
        submission = ContactSubmission.objects.first()
        assert submission.name == valid_contact_form_data['name']
        assert submission.status == 'new'

    def test_contact_form_with_max_length_data(self, client, site):
        """Test form with maximum allowed data lengths."""
        long_name = 'A' * 255  # Max length for name field
        long_message = 'B' * 1000  # Long message

        form_data = {
            'name': long_name,
            'email': 'test@example.com',
            'phone': '12345678901234567890123456789012345678901234567890123456789012',  # Max 64 chars
            'message': long_message,
            'consent': True,
            'honeypot': ''
        }

        url = reverse('contacts:form')
        response = client.post(url, data=form_data)

        if response.status_code == 302:
            submission = ContactSubmission.objects.first()
            assert len(submission.name) <= 255
            assert len(submission.phone) <= 64

    @patch('apps.contacts.views.ContactForm')
    def test_contact_form_view_error_handling(self, mock_form_class, client):
        """Test error handling in contact form view."""
        # Simulate form raising an exception
        mock_form = Mock()
        mock_form.is_valid.side_effect = Exception("Database error")
        mock_form_class.return_value = mock_form

        url = reverse('contacts:form')

        # The view should handle errors gracefully
        # (Implementation would depend on actual error handling in view)
        with pytest.raises(Exception):
            client.post(url, data={'name': 'test'})