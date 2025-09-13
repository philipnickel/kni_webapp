"""
Test suite for page functionality and navigation.
Tests Wagtail pages, URL routing, and site navigation.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import Http404
from wagtail.models import Page, Site
from wagtail.test.utils import WagtailPageTestCase

from apps.pages.models import HomePage, ContactPage, GalleryPage, ModularPage
from apps.projects.models import Project


@pytest.mark.pages
@pytest.mark.django_db
class TestPageModels:
    """Test Wagtail page models."""

    def test_homepage_creation(self, root_page):
        """Test HomePage can be created and configured."""
        home_page = HomePage(
            title='Test Home',
            slug='home',
            intro='Welcome to our site'
        )
        root_page.add_child(instance=home_page)

        assert home_page.title == 'Test Home'
        assert home_page.slug == 'home'
        assert home_page.intro == 'Welcome to our site'
        assert home_page.get_parent() == root_page

    def test_homepage_context_with_featured_projects(self, home_page, sample_project):
        """Test HomePage context includes featured projects."""
        # Create a mock request
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/')

        context = home_page.get_context(request)

        assert 'featured_projects' in context
        # Should include our featured project
        featured = list(context['featured_projects'])
        assert sample_project in featured

    def test_contact_page_creation(self, root_page):
        """Test ContactPage creation and configuration."""
        contact_page = ContactPage(
            title='Contact Us',
            slug='contact',
            intro='Get in touch',
            show_contact_form=True,
            contact_form_title='Send Message',
            contact_form_intro='We want to hear from you'
        )
        root_page.add_child(instance=contact_page)

        assert contact_page.title == 'Contact Us'
        assert contact_page.show_contact_form is True
        assert contact_page.contact_form_title == 'Send Message'

    def test_gallery_page_creation(self, root_page):
        """Test GalleryPage creation."""
        gallery_page = GalleryPage(
            title='Our Projects',
            slug='projects',
            intro='View our work'
        )
        root_page.add_child(instance=gallery_page)

        assert gallery_page.title == 'Our Projects'
        assert gallery_page.intro == 'View our work'

    def test_gallery_page_context_with_projects(self, gallery_page, sample_project):
        """Test GalleryPage context includes projects."""
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/')

        context = gallery_page.get_context(request)

        assert 'project_pages' in context
        projects = list(context['project_pages'])
        assert sample_project in projects

    def test_gallery_page_filtering(self, gallery_page):
        """Test GalleryPage filtering functionality."""
        # Create projects with different attributes
        featured_project = Project.objects.create(
            title='Featured Project',
            description='A featured project',
            published=True,
            featured=True
        )

        regular_project = Project.objects.create(
            title='Regular Project',
            description='A regular project',
            published=True,
            featured=False
        )

        from django.test import RequestFactory
        factory = RequestFactory()

        # Test featured filter
        request = factory.get('/?featured=true')
        context = gallery_page.get_context(request)
        projects = list(context['project_pages'])

        assert featured_project in projects
        assert regular_project not in projects
        assert context['featured_filter'] == 'true'

    def test_modular_page_creation(self, root_page):
        """Test ModularPage creation."""
        modular_page = ModularPage(
            title='About Us',
            slug='about',
            intro='Learn more about us'
        )
        root_page.add_child(instance=modular_page)

        assert modular_page.title == 'About Us'
        assert modular_page.intro == 'Learn more about us'


@pytest.mark.pages
@pytest.mark.django_db
class TestPageRouting:
    """Test URL routing and page access."""

    def test_homepage_routing(self, client, home_page):
        """Test home page is accessible."""
        response = client.get('/')
        assert response.status_code == 200

    def test_contact_page_routing(self, client, contact_page):
        """Test contact page routing."""
        url = contact_page.get_url()
        response = client.get(url)
        assert response.status_code == 200

    def test_gallery_page_routing(self, client, gallery_page):
        """Test gallery page routing."""
        url = gallery_page.get_url()
        response = client.get(url)
        assert response.status_code == 200

    def test_404_page_handling(self, client):
        """Test 404 error handling."""
        response = client.get('/non-existent-page/')
        assert response.status_code == 404

    def test_page_slugs_are_unique_per_parent(self, root_page):
        """Test that page slugs are unique within same parent."""
        page1 = HomePage(title='Page 1', slug='test-page')
        root_page.add_child(instance=page1)

        # Attempting to create another page with same slug should raise error
        page2 = HomePage(title='Page 2', slug='test-page')

        with pytest.raises(Exception):  # Django will raise validation error
            root_page.add_child(instance=page2)


@pytest.mark.navigation
@pytest.mark.django_db
class TestSiteNavigation:
    """Test site navigation functionality."""

    def test_main_navigation_links(self, client, home_page, contact_page, gallery_page):
        """Test main navigation contains expected links."""
        response = client.get('/')
        content = response.content.decode()

        # Check navigation contains links to main pages
        assert contact_page.get_url() in content or 'contact' in content.lower()
        assert gallery_page.get_url() in content or 'project' in content.lower()

    def test_breadcrumb_navigation(self, client, gallery_page):
        """Test breadcrumb navigation if implemented."""
        response = client.get(gallery_page.get_url())
        # Implementation depends on breadcrumb template structure
        assert response.status_code == 200

    def test_mobile_navigation_accessibility(self, client, home_page):
        """Test mobile navigation is accessible."""
        response = client.get('/')
        content = response.content.decode()

        # Look for mobile navigation indicators
        mobile_indicators = ['mobile', 'hamburger', 'menu-toggle', 'navbar-toggle']
        has_mobile_nav = any(indicator in content.lower() for indicator in mobile_indicators)

        # This test documents mobile navigation presence
        # Actual assertion depends on implementation

    def test_navigation_active_states(self, client, contact_page):
        """Test navigation shows active page states."""
        response = client.get(contact_page.get_url())
        content = response.content.decode()

        # Look for active state indicators
        active_indicators = ['active', 'current', 'selected']
        # Implementation specific - would need to check actual template

    def test_footer_navigation(self, client, home_page):
        """Test footer contains navigation elements."""
        response = client.get('/')
        content = response.content.decode()

        # Check for footer section
        assert 'footer' in content.lower()


@pytest.mark.pages
@pytest.mark.django_db
class TestPageSearch:
    """Test page search functionality."""

    def test_page_search_fields_configured(self, home_page):
        """Test that pages have search fields configured."""
        # HomePage should have search fields
        search_fields = home_page.search_fields
        assert len(search_fields) > 0

        # Check specific search field types
        field_names = [field.field_name for field in search_fields if hasattr(field, 'field_name')]
        assert 'title' in field_names or any('title' in str(field) for field in search_fields)

    def test_search_functionality(self, client, home_page):
        """Test search functionality if available."""
        # This would test search views if implemented
        # Currently documenting search capability
        pass


@pytest.mark.pages
@pytest.mark.integration
@pytest.mark.django_db
class TestPageIntegration:
    """Integration tests for page functionality."""

    def test_complete_site_navigation_flow(self, client, home_page, contact_page, gallery_page):
        """Test complete user navigation flow."""
        # Start at home page
        response = client.get('/')
        assert response.status_code == 200

        # Navigate to gallery
        gallery_url = gallery_page.get_url()
        response = client.get(gallery_url)
        assert response.status_code == 200

        # Navigate to contact page
        contact_url = contact_page.get_url()
        response = client.get(contact_url)
        assert response.status_code == 200

        # Return to home
        response = client.get('/')
        assert response.status_code == 200

    def test_page_hierarchy_consistency(self, root_page, home_page, contact_page):
        """Test page hierarchy is consistent."""
        # Check parent-child relationships
        assert contact_page.get_parent() == root_page
        assert home_page.get_parent() == root_page

        # Check page tree structure
        children = root_page.get_children().live()
        child_titles = [child.title for child in children]
        assert home_page.title in child_titles
        assert contact_page.title in child_titles

    def test_page_templates_exist(self, client, home_page, contact_page, gallery_page):
        """Test that page templates render without errors."""
        pages = [home_page, contact_page, gallery_page]

        for page in pages:
            response = client.get(page.get_url())
            assert response.status_code == 200
            # Check that basic HTML structure exists
            content = response.content.decode()
            assert '<html' in content or '<!DOCTYPE' in content

    def test_page_seo_fields(self, home_page):
        """Test that pages support SEO fields."""
        # Test basic meta fields exist
        assert hasattr(home_page, 'title')
        assert hasattr(home_page, 'search_description') or hasattr(home_page, 'seo_title')

    def test_page_social_sharing_meta(self, client, home_page):
        """Test social sharing meta tags if implemented."""
        response = client.get(home_page.get_url())
        content = response.content.decode()

        # Look for Open Graph or Twitter Card meta tags
        social_tags = ['og:', 'twitter:', 'property="og', 'name="twitter']
        has_social_meta = any(tag in content for tag in social_tags)

        # This documents social sharing capability


@pytest.mark.pages
@pytest.mark.performance
@pytest.mark.django_db
class TestPagePerformance:
    """Test page performance characteristics."""

    def test_page_load_times(self, client, home_page):
        """Test page load times are reasonable."""
        import time

        start_time = time.time()
        response = client.get(home_page.get_url())
        end_time = time.time()

        load_time = end_time - start_time

        assert response.status_code == 200
        assert load_time < 1.0  # Should load within 1 second

    def test_database_query_efficiency(self, client, gallery_page, django_assert_num_queries):
        """Test that pages don't generate excessive database queries."""
        # Create multiple projects to test N+1 query issues
        for i in range(10):
            Project.objects.create(
                title=f'Project {i}',
                description=f'Description {i}',
                published=True
            )

        # Gallery page should not generate excessive queries
        with django_assert_num_queries(10):  # Adjust based on actual implementation
            response = client.get(gallery_page.get_url())
            assert response.status_code == 200


@pytest.mark.pages
@pytest.mark.wagtail
@pytest.mark.django_db
class TestWagtailAdmin:
    """Test Wagtail admin functionality for pages."""

    def test_wagtail_admin_accessible(self, admin_client):
        """Test Wagtail admin is accessible to admin users."""
        response = admin_client.get('/admin/')
        assert response.status_code == 200

    def test_page_creation_in_admin(self, admin_client, root_page):
        """Test creating pages through Wagtail admin."""
        # This would test the admin interface
        # Implementation depends on specific admin views
        pass

    def test_page_editing_permissions(self, client, regular_user, home_page):
        """Test page editing permissions."""
        client.force_login(regular_user)

        # Regular user should not access admin
        response = client.get('/admin/')
        # Should redirect to login or show permission denied
        assert response.status_code in [302, 403]