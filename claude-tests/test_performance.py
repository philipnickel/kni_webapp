"""
Test suite for performance and responsiveness.
Tests load times, database query optimization, and mobile responsiveness.
"""

import pytest
import time
from django.test import TestCase, Client
from django.test.utils import override_settings
from django.core.management import call_command
from django.db import connections
from django.test import RequestFactory
from unittest.mock import patch

from apps.pages.models import HomePage, GalleryPage
from apps.projects.models import Project
from apps.contacts.models import ContactSubmission


@pytest.mark.performance
@pytest.mark.django_db
class TestPageLoadTimes:
    """Test page load performance."""

    def test_homepage_load_time(self, client, home_page):
        """Test homepage loads within acceptable time limit."""
        start_time = time.time()
        response = client.get(home_page.get_url())
        end_time = time.time()

        load_time = end_time - start_time

        assert response.status_code == 200
        assert load_time < 2.0  # Should load within 2 seconds
        print(f"Homepage load time: {load_time:.3f} seconds")

    def test_gallery_page_load_time(self, client, gallery_page):
        """Test gallery page loads within acceptable time limit."""
        # Create some projects to make test realistic
        for i in range(10):
            Project.objects.create(
                title=f'Project {i}',
                description=f'Description for project {i}',
                published=True,
                featured=(i % 3 == 0)
            )

        start_time = time.time()
        response = client.get(gallery_page.get_url())
        end_time = time.time()

        load_time = end_time - start_time

        assert response.status_code == 200
        assert load_time < 3.0  # Gallery with projects should load within 3 seconds
        print(f"Gallery page load time: {load_time:.3f} seconds")

    def test_contact_form_load_time(self, client, contact_page):
        """Test contact form page loads quickly."""
        start_time = time.time()
        response = client.get(contact_page.get_url())
        end_time = time.time()

        load_time = end_time - start_time

        assert response.status_code == 200
        assert load_time < 1.5  # Contact form should be fast
        print(f"Contact page load time: {load_time:.3f} seconds")

    @pytest.mark.slow
    def test_page_load_with_large_dataset(self, client, gallery_page):
        """Test page performance with large dataset."""
        # Create many projects
        projects = []
        for i in range(100):
            project = Project.objects.create(
                title=f'Large Dataset Project {i}',
                description=f'Description {i}' * 50,  # Larger description
                published=True,
                featured=(i % 5 == 0)
            )
            projects.append(project)

        start_time = time.time()
        response = client.get(gallery_page.get_url())
        end_time = time.time()

        load_time = end_time - start_time

        assert response.status_code == 200
        assert load_time < 5.0  # Even with 100 projects, should load within 5 seconds
        print(f"Gallery with 100 projects load time: {load_time:.3f} seconds")


@pytest.mark.performance
@pytest.mark.django_db
class TestDatabaseQueryOptimization:
    """Test database query efficiency to prevent N+1 problems."""

    def test_homepage_query_count(self, client, home_page, django_assert_num_queries):
        """Test homepage doesn't generate excessive database queries."""
        # Create featured projects
        for i in range(5):
            Project.objects.create(
                title=f'Featured Project {i}',
                description=f'Description {i}',
                published=True,
                featured=True
            )

        # Homepage should not generate too many queries
        with django_assert_num_queries(15):  # Adjust based on actual requirements
            response = client.get(home_page.get_url())
            assert response.status_code == 200

    def test_gallery_page_query_efficiency(self, client, gallery_page, django_assert_num_queries):
        """Test gallery page query efficiency with multiple projects."""
        # Create projects with relationships
        for i in range(20):
            Project.objects.create(
                title=f'Query Test Project {i}',
                description=f'Description {i}',
                published=True,
                featured=(i % 4 == 0)
            )

        # Gallery page should use efficient queries (select_related, prefetch_related)
        with django_assert_num_queries(10):  # Adjust based on optimization
            response = client.get(gallery_page.get_url())
            assert response.status_code == 200

    def test_contact_form_submission_query_count(self, client, site, valid_contact_form_data, django_assert_num_queries):
        """Test contact form submission doesn't generate excessive queries."""
        url = '/fa-tilbud/'  # Direct URL instead of reverse for consistency

        # Form submission should be efficient
        with django_assert_num_queries(5):  # INSERT + basic queries
            response = client.post(url, data=valid_contact_form_data)
            assert response.status_code == 302

    def test_wagtail_page_tree_query_efficiency(self, client, django_assert_num_queries):
        """Test Wagtail page tree queries are efficient."""
        # Test basic page routing doesn't cause query explosion
        with django_assert_num_queries(8):  # Adjust based on Wagtail requirements
            response = client.get('/')
            assert response.status_code == 200

    def test_search_query_performance(self, gallery_page):
        """Test search functionality performance if implemented."""
        # Create searchable content
        for i in range(50):
            Project.objects.create(
                title=f'Searchable Project {i}',
                description='Kitchen renovation bathroom remodel construction',
                published=True
            )

        from django.test import RequestFactory
        factory = RequestFactory()

        # Test filtered requests
        request = factory.get('/?tag=kitchen')
        start_time = time.time()
        context = gallery_page.get_context(request)
        end_time = time.time()

        search_time = end_time - start_time
        assert search_time < 1.0  # Search should be fast
        print(f"Search query time: {search_time:.3f} seconds")


@pytest.mark.performance
@pytest.mark.django_db
class TestCachingPerformance:
    """Test caching mechanisms and their performance impact."""

    @override_settings(
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            }
        }
    )
    def test_page_caching_effectiveness(self, client, home_page):
        """Test page caching improves performance."""
        # First request (not cached)
        start_time = time.time()
        response1 = client.get(home_page.get_url())
        first_load_time = time.time() - start_time

        # Second request (should be faster if cached)
        start_time = time.time()
        response2 = client.get(home_page.get_url())
        second_load_time = time.time() - start_time

        assert response1.status_code == 200
        assert response2.status_code == 200

        # Second request should be faster (if caching is implemented)
        # Note: This test documents caching behavior
        print(f"First load: {first_load_time:.3f}s, Second load: {second_load_time:.3f}s")

    def test_database_query_caching(self, client, gallery_page):
        """Test database query result caching."""
        # Create projects
        for i in range(10):
            Project.objects.create(
                title=f'Cache Test Project {i}',
                published=True
            )

        # First request
        start_time = time.time()
        response1 = client.get(gallery_page.get_url())
        first_time = time.time() - start_time

        # Second identical request
        start_time = time.time()
        response2 = client.get(gallery_page.get_url())
        second_time = time.time() - start_time

        assert response1.status_code == 200
        assert response2.status_code == 200

        print(f"Query cache test - First: {first_time:.3f}s, Second: {second_time:.3f}s")


@pytest.mark.performance
@pytest.mark.django_db
class TestResponsiveDesign:
    """Test responsive design performance and functionality."""

    def test_mobile_viewport_rendering(self, client, home_page):
        """Test page renders correctly on mobile viewport."""
        # Simulate mobile request
        response = client.get(
            home_page.get_url(),
            HTTP_USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)'
        )

        assert response.status_code == 200
        content = response.content.decode()

        # Check for mobile-responsive meta tags
        assert 'viewport' in content
        assert 'width=device-width' in content

    def test_responsive_images_optimization(self, client, gallery_page):
        """Test responsive image optimization."""
        response = client.get(gallery_page.get_url())
        content = response.content.decode()

        # Look for responsive image techniques
        responsive_indicators = [
            'srcset',
            'sizes',
            'picture',
            'loading="lazy"',
            'responsive'
        ]

        # Check if any responsive image techniques are used
        has_responsive_images = any(indicator in content for indicator in responsive_indicators)
        # This test documents responsive image usage

    def test_mobile_navigation_performance(self, client, home_page):
        """Test mobile navigation performance."""
        # Test with mobile user agent
        response = client.get(
            home_page.get_url(),
            HTTP_USER_AGENT='Mozilla/5.0 (Android 10; Mobile; rv:81.0)'
        )

        assert response.status_code == 200
        content = response.content.decode()

        # Mobile navigation should be present
        mobile_nav_indicators = ['mobile', 'hamburger', 'menu-toggle', 'navbar-toggle']
        has_mobile_nav = any(indicator in content.lower() for indicator in mobile_nav_indicators)

    def test_touch_friendly_interface_elements(self, client, contact_page):
        """Test touch-friendly interface elements."""
        response = client.get(contact_page.get_url())
        content = response.content.decode()

        # Look for touch-friendly CSS classes or attributes
        touch_indicators = [
            'btn-lg',  # Large buttons
            'form-control',  # Larger form controls
            'touch-friendly',
            'mobile-friendly'
        ]

        # This test documents touch-friendly design


@pytest.mark.performance
@pytest.mark.django_db
class TestStaticAssetPerformance:
    """Test static asset loading and optimization."""

    def test_css_loading_performance(self, client, home_page):
        """Test CSS assets load efficiently."""
        response = client.get(home_page.get_url())
        content = response.content.decode()

        # Count CSS files
        css_links = content.count('<link')
        print(f"Number of CSS links: {css_links}")

        # Should not have excessive CSS files
        assert css_links < 10  # Reasonable limit

    def test_javascript_loading_performance(self, client, home_page):
        """Test JavaScript assets load efficiently."""
        response = client.get(home_page.get_url())
        content = response.content.decode()

        # Count JS files
        js_scripts = content.count('<script')
        print(f"Number of script tags: {js_scripts}")

        # Should not have excessive JS files
        assert js_scripts < 15  # Reasonable limit

    def test_image_optimization_hints(self, client, gallery_page):
        """Test image optimization implementation."""
        # Create project with image (mock)
        project = Project.objects.create(
            title='Image Test Project',
            description='Project with images',
            published=True
        )

        response = client.get(gallery_page.get_url())
        content = response.content.decode()

        # Look for image optimization attributes
        optimization_attrs = [
            'loading="lazy"',
            'decoding="async"',
            'sizes=',
            'srcset='
        ]

        # This test documents image optimization techniques


@pytest.mark.performance
@pytest.mark.slow
@pytest.mark.django_db
class TestLoadTesting:
    """Basic load testing to identify performance bottlenecks."""

    def test_concurrent_homepage_requests(self, client, home_page):
        """Test homepage handles concurrent requests."""
        import threading
        import statistics

        results = []
        errors = []

        def make_request():
            try:
                start_time = time.time()
                response = client.get(home_page.get_url())
                end_time = time.time()

                results.append({
                    'status_code': response.status_code,
                    'load_time': end_time - start_time
                })
            except Exception as e:
                errors.append(str(e))

        # Create multiple threads for concurrent requests
        threads = []
        num_threads = 10

        for _ in range(num_threads):
            thread = threading.Thread(target=make_request)
            threads.append(thread)

        # Start all threads
        start_time = time.time()
        for thread in threads:
            thread.start()

        # Wait for completion
        for thread in threads:
            thread.join(timeout=10)

        total_time = time.time() - start_time

        # Analyze results
        assert len(errors) == 0, f"Errors occurred: {errors}"
        assert len(results) == num_threads

        load_times = [r['load_time'] for r in results]
        avg_load_time = statistics.mean(load_times)
        max_load_time = max(load_times)

        print(f"Concurrent requests test:")
        print(f"  Threads: {num_threads}")
        print(f"  Total time: {total_time:.3f}s")
        print(f"  Average load time: {avg_load_time:.3f}s")
        print(f"  Max load time: {max_load_time:.3f}s")

        # Performance assertions
        assert avg_load_time < 2.0  # Average should be reasonable
        assert max_load_time < 5.0  # No request should take too long

    def test_memory_usage_under_load(self, client, gallery_page):
        """Test memory usage doesn't grow excessively under load."""
        import psutil
        import os

        # Get current process
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Create many projects
        for i in range(50):
            Project.objects.create(
                title=f'Memory Test Project {i}',
                description='Description ' * 100,  # Larger content
                published=True
            )

        # Make multiple requests
        for i in range(20):
            response = client.get(gallery_page.get_url())
            assert response.status_code == 200

        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory

        print(f"Memory usage test:")
        print(f"  Initial memory: {initial_memory / 1024 / 1024:.1f} MB")
        print(f"  Final memory: {final_memory / 1024 / 1024:.1f} MB")
        print(f"  Memory increase: {memory_increase / 1024 / 1024:.1f} MB")

        # Memory increase should be reasonable
        assert memory_increase < 100 * 1024 * 1024  # Less than 100MB increase


@pytest.mark.performance
@pytest.mark.django_db
class TestPerformanceRegression:
    """Test to catch performance regressions."""

    def test_baseline_performance_metrics(self, client, home_page, gallery_page, contact_page):
        """Establish baseline performance metrics."""
        pages_to_test = [
            ('Homepage', home_page),
            ('Gallery', gallery_page),
            ('Contact', contact_page),
        ]

        performance_results = {}

        for page_name, page in pages_to_test:
            start_time = time.time()
            response = client.get(page.get_url())
            end_time = time.time()

            load_time = end_time - start_time

            assert response.status_code == 200

            performance_results[page_name] = {
                'load_time': load_time,
                'status_code': response.status_code,
                'content_length': len(response.content)
            }

        # Print results for baseline establishment
        print("\nPerformance Baseline Metrics:")
        for page_name, metrics in performance_results.items():
            print(f"{page_name}:")
            print(f"  Load time: {metrics['load_time']:.3f}s")
            print(f"  Content length: {metrics['content_length']} bytes")

        # Store these metrics for comparison in future test runs
        # In a real scenario, these would be stored in a performance database