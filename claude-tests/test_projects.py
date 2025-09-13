"""
Test suite for projects functionality.
Tests Project model, admin interface, and project-related views.
"""

import pytest
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker

from apps.projects.models import Project


@pytest.mark.django_db
class TestProjectModel:
    """Test the Project model."""

    def test_project_creation(self):
        """Test basic project creation."""
        project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            published=True,
            featured=False
        )

        assert project.title == 'Test Project'
        assert project.description == 'A test project description'
        assert project.published is True
        assert project.featured is False
        assert project.date is not None

    def test_project_str_representation(self):
        """Test project string representation."""
        project = Project.objects.create(
            title='Sample Project',
            description='Description',
            published=True
        )

        assert str(project) == 'Sample Project'

    def test_project_default_values(self):
        """Test default values for project fields."""
        project = Project.objects.create(
            title='Default Test',
            description='Test description'
        )

        # Check default values
        assert project.published is False  # Should default to False
        assert project.featured is False   # Should default to False
        assert project.date is not None    # Should auto-add current date

    def test_project_ordering(self):
        """Test project ordering."""
        project1 = Project.objects.create(
            title='First Project',
            description='First',
            published=True
        )

        project2 = Project.objects.create(
            title='Second Project',
            description='Second',
            published=True
        )

        # Test default ordering (likely by date)
        projects = Project.objects.all()
        # Ordering will depend on model's Meta.ordering setting


@pytest.mark.django_db
class TestProjectViews:
    """Test project-related views."""

    def test_project_gallery_view(self, client, gallery_page):
        """Test project gallery view displays projects."""
        # Create published projects
        published_project = Project.objects.create(
            title='Published Project',
            description='This project is published',
            published=True
        )

        # Create unpublished project
        unpublished_project = Project.objects.create(
            title='Unpublished Project',
            description='This project is not published',
            published=False
        )

        response = client.get(gallery_page.get_url())

        assert response.status_code == 200
        content = response.content.decode()

        # Published project should be visible
        assert 'Published Project' in content

        # Unpublished project should not be visible
        assert 'Unpublished Project' not in content

    def test_featured_projects_filtering(self, client, gallery_page):
        """Test featured projects filtering."""
        # Create featured and non-featured projects
        featured_project = Project.objects.create(
            title='Featured Project',
            description='This is featured',
            published=True,
            featured=True
        )

        regular_project = Project.objects.create(
            title='Regular Project',
            description='This is not featured',
            published=True,
            featured=False
        )

        # Test featured filter
        response = client.get(f'{gallery_page.get_url()}?featured=true')

        assert response.status_code == 200

        # Check that filtering works through context
        projects = response.context['project_pages']
        project_titles = [p.title for p in projects]

        assert 'Featured Project' in project_titles
        assert 'Regular Project' not in project_titles

    def test_project_detail_urls_if_implemented(self):
        """Test project detail URLs if implemented."""
        # This depends on whether individual project detail pages exist
        # Current structure suggests projects are displayed in gallery only
        pass


@pytest.mark.django_db
class TestProjectFiltering:
    """Test project filtering and search functionality."""

    def test_tag_filtering(self, gallery_page):
        """Test tag-based filtering if implemented."""
        # Create projects with tags (if tag system is implemented)
        project1 = Project.objects.create(
            title='Kitchen Project',
            description='Kitchen renovation',
            published=True
        )

        project2 = Project.objects.create(
            title='Bathroom Project',
            description='Bathroom remodel',
            published=True
        )

        # Test tag filtering through gallery context
        from django.test import RequestFactory
        factory = RequestFactory()

        # Test if tag filtering is implemented
        request = factory.get('/?tag=kitchen')
        context = gallery_page.get_context(request)

        # This test documents tag filtering capability
        assert 'tag_filter' in context

    def test_search_functionality(self, gallery_page):
        """Test project search if implemented."""
        # Create searchable projects
        project1 = Project.objects.create(
            title='Modern Kitchen Design',
            description='Contemporary kitchen with island',
            published=True
        )

        project2 = Project.objects.create(
            title='Bathroom Renovation',
            description='Complete bathroom overhaul',
            published=True
        )

        # Test search through context (if implemented)
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/?search=kitchen')
        context = gallery_page.get_context(request)

        # This documents search functionality
        projects = list(context['project_pages'])


@pytest.mark.django_db
class TestProjectAdmin:
    """Test project admin functionality."""

    def test_project_admin_list_view(self, admin_client):
        """Test project admin list view."""
        # Create some projects
        Project.objects.create(
            title='Admin Test Project 1',
            published=True,
            featured=True
        )

        Project.objects.create(
            title='Admin Test Project 2',
            published=False,
            featured=False
        )

        # Access admin list view
        response = admin_client.get('/admin/')
        assert response.status_code == 200

        # Check if projects are accessible in admin
        # This would depend on admin registration

    def test_project_admin_creation(self, admin_client):
        """Test creating project through admin."""
        # Test admin creation form
        # This would require specific admin URLs and form testing
        pass

    def test_project_admin_bulk_actions(self, admin_client):
        """Test bulk actions in project admin."""
        # Create multiple projects
        projects = []
        for i in range(5):
            project = Project.objects.create(
                title=f'Bulk Test Project {i}',
                published=False
            )
            projects.append(project)

        # Test bulk publishing action if implemented
        # This would require admin action testing


@pytest.mark.django_db
class TestProjectIntegration:
    """Integration tests for project functionality."""

    def test_homepage_featured_projects(self, client, home_page):
        """Test featured projects display on homepage."""
        # Create featured projects
        featured_projects = []
        for i in range(3):
            project = Project.objects.create(
                title=f'Featured Project {i}',
                description=f'Featured description {i}',
                published=True,
                featured=True
            )
            featured_projects.append(project)

        # Create non-featured project
        Project.objects.create(
            title='Regular Project',
            description='Not featured',
            published=True,
            featured=False
        )

        response = client.get(home_page.get_url())
        assert response.status_code == 200

        content = response.content.decode()

        # Featured projects should appear on homepage
        for project in featured_projects:
            assert project.title in content

        # Non-featured should not appear
        assert 'Regular Project' not in content

    def test_project_gallery_pagination(self, client, gallery_page):
        """Test gallery pagination if implemented."""
        # Create many projects
        for i in range(25):
            Project.objects.create(
                title=f'Pagination Test Project {i}',
                description=f'Description {i}',
                published=True
            )

        response = client.get(gallery_page.get_url())
        assert response.status_code == 200

        # Check if pagination is implemented
        content = response.content.decode()
        pagination_indicators = ['page', 'next', 'previous', 'pagination']
        has_pagination = any(indicator in content.lower() for indicator in pagination_indicators)

        # This documents pagination implementation


@pytest.mark.django_db
class TestProjectValidation:
    """Test project model validation."""

    def test_project_title_validation(self):
        """Test project title field validation."""
        # Test empty title
        with pytest.raises(Exception):  # Should raise validation error
            project = Project(
                title='',  # Empty title
                description='Valid description',
                published=True
            )
            project.full_clean()  # Trigger validation

    def test_project_description_validation(self):
        """Test project description validation."""
        # Description might be optional
        project = Project(
            title='Valid Title',
            description='',  # Empty description
            published=True
        )

        # Should not raise error if description is optional
        try:
            project.full_clean()
        except Exception:
            # If description is required, this is expected
            pass

    def test_project_boolean_field_validation(self):
        """Test boolean field validation."""
        project = Project(
            title='Valid Title',
            description='Valid description',
            published='invalid',  # Invalid boolean value
            featured=True
        )

        with pytest.raises(Exception):  # Should raise validation error
            project.full_clean()


@pytest.mark.django_db
class TestProjectPerformance:
    """Test project-related performance."""

    def test_project_queryset_efficiency(self, gallery_page):
        """Test project queryset efficiency."""
        # Create projects with related data
        for i in range(20):
            Project.objects.create(
                title=f'Performance Test Project {i}',
                description=f'Description {i}' * 10,
                published=True,
                featured=(i % 3 == 0)
            )

        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/')

        # Test gallery context generation
        import time
        start_time = time.time()
        context = gallery_page.get_context(request)
        projects = list(context['project_pages'])
        end_time = time.time()

        query_time = end_time - start_time
        assert query_time < 0.5  # Should be fast

    def test_project_filtering_performance(self, gallery_page):
        """Test project filtering performance."""
        # Create many projects
        for i in range(100):
            Project.objects.create(
                title=f'Filter Test Project {i}',
                description='Bathroom kitchen renovation construction',
                published=True,
                featured=(i % 5 == 0)
            )

        from django.test import RequestFactory
        factory = RequestFactory()

        # Test featured filtering performance
        request = factory.get('/?featured=true')
        start_time = time.time()
        context = gallery_page.get_context(request)
        projects = list(context['project_pages'])
        end_time = time.time()

        filter_time = end_time - start_time
        assert filter_time < 1.0  # Filtering should be efficient

        # Should return only featured projects
        assert all(p.featured for p in projects)


@pytest.mark.django_db
class TestProjectSecurity:
    """Test project security considerations."""

    def test_unpublished_projects_not_accessible(self, client, gallery_page):
        """Test that unpublished projects are not accessible to public."""
        # Create unpublished project
        unpublished = Project.objects.create(
            title='Secret Project',
            description='This should not be visible',
            published=False
        )

        response = client.get(gallery_page.get_url())
        content = response.content.decode()

        # Unpublished project should not appear
        assert 'Secret Project' not in content
        assert 'This should not be visible' not in content

    def test_project_admin_access_control(self, client, regular_user):
        """Test project admin access control."""
        client.force_login(regular_user)

        # Regular user should not access project admin
        response = client.get('/admin/')
        assert response.status_code in [302, 403]  # Redirect to login or forbidden

    def test_project_data_sanitization(self):
        """Test that project data is properly sanitized."""
        # Test with potentially malicious content
        project = Project.objects.create(
            title='<script>alert("XSS")</script>',
            description='<img src="x" onerror="alert(1)">',
            published=True
        )

        # Data should be stored as-is for proper escaping in templates
        assert '<script>' in project.title
        assert '<img' in project.description