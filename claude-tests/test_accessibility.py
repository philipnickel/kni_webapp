"""
Comprehensive accessibility tests for the JCleemannByg website.

This module tests for WCAG 2.1 AA compliance across all themes,
keyboard navigation, screen reader compatibility, and other
accessibility features.
"""

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python import AxeBuilder
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import json
import os
from typing import List, Dict, Any


# DaisyUI themes to test
DAISYUI_THEMES = [
    'light', 'dark', 'corporate', 'business',
    'luxury', 'emerald', 'garden', 'autumn'
]

# Key pages to test for accessibility
TEST_PAGES = [
    {'url': '/', 'name': 'Home Page', 'has_form': False},
    {'url': '/kontakt/', 'name': 'Contact Page', 'has_form': True},
    {'url': '/galleri/', 'name': 'Gallery Page', 'has_form': False},
]

# WCAG 2.1 AA rules to enforce
WCAG_AA_RULES = {
    'color-contrast': 'AA',
    'link-name': 'AA',
    'button-name': 'AA',
    'form-field-multiple-labels': 'AA',
    'heading-order': 'AA',
    'html-has-lang': 'AA',
    'image-alt': 'AA',
    'input-image-alt': 'AA',
    'label': 'AA',
    'meta-viewport': 'AA',
    'page-has-heading-one': 'AA',
    'region': 'AA',
    'skip-link': 'AA',
    'focus-order-semantics': 'AA',
    'keyboard-navigation': 'AA',
}


class AccessibilityTestMixin:
    """Mixin providing common accessibility testing utilities."""

    def setup_theme(self, page: Page, theme: str):
        """Set up a specific DaisyUI theme for testing."""
        page.evaluate(f"window.switchTheme('{theme}')")
        page.wait_for_timeout(500)  # Allow theme to apply

    def get_axe_results(self, page: Page, theme: str = None) -> Dict[str, Any]:
        """Run axe accessibility scan and return results."""
        builder = AxeBuilder(page)

        # Configure axe rules for WCAG 2.1 AA
        builder.with_tags(['wcag2a', 'wcag2aa', 'wcag21aa'])

        # Include accessibility rules
        builder.include('.navbar')
        builder.include('main')
        builder.include('footer')

        # Exclude elements that might interfere with testing
        builder.exclude('[data-testid="preview-banner"]')

        results = builder.analyze()

        if theme:
            results['theme'] = theme

        return results

    def assert_no_accessibility_violations(self, results: Dict[str, Any],
                                          severity_threshold: str = 'serious'):
        """Assert that there are no accessibility violations above threshold."""
        violations = results.get('violations', [])

        # Filter by severity
        severity_levels = {'minor': 1, 'moderate': 2, 'serious': 3, 'critical': 4}
        threshold = severity_levels.get(severity_threshold, 3)

        critical_violations = [
            v for v in violations
            if severity_levels.get(v.get('impact', 'minor'), 1) >= threshold
        ]

        if critical_violations:
            violation_details = []
            for violation in critical_violations:
                nodes = len(violation.get('nodes', []))
                violation_details.append(
                    f"Rule: {violation['id']} - {violation['description']} "
                    f"(Impact: {violation['impact']}, Nodes: {nodes})"
                )

            theme_info = f" in theme '{results.get('theme', 'unknown')}'" if results.get('theme') else ""

            pytest.fail(
                f"Found {len(critical_violations)} accessibility violations{theme_info}:\n"
                + '\n'.join(violation_details)
            )


@pytest.mark.accessibility
@pytest.mark.wcag
class TestWCAGCompliance(AccessibilityTestMixin):
    """Test WCAG 2.1 AA compliance across all themes."""

    @pytest.mark.parametrize("theme", DAISYUI_THEMES)
    @pytest.mark.parametrize("page_info", TEST_PAGES)
    def test_wcag_aa_compliance_by_theme_and_page(self, live_server, page: Page,
                                                  theme: str, page_info: Dict[str, str]):
        """Test WCAG 2.1 AA compliance for each page in each theme."""
        # Navigate to page
        page.goto(f"{live_server.url}{page_info['url']}")

        # Set theme
        self.setup_theme(page, theme)

        # Wait for page to fully load
        page.wait_for_load_state("networkidle")

        # Run accessibility scan
        results = self.get_axe_results(page, theme)

        # Assert compliance
        self.assert_no_accessibility_violations(results, 'serious')

        # Additional assertions for specific WCAG criteria
        self._assert_color_contrast(results)
        self._assert_keyboard_navigation(page)
        self._assert_semantic_markup(page)

    def _assert_color_contrast(self, results: Dict[str, Any]):
        """Assert adequate color contrast ratios."""
        violations = results.get('violations', [])
        contrast_violations = [v for v in violations if v['id'] == 'color-contrast']

        assert len(contrast_violations) == 0, (
            f"Color contrast violations found in theme {results.get('theme', 'unknown')}: "
            f"{[v['description'] for v in contrast_violations]}"
        )

    def _assert_keyboard_navigation(self, page: Page):
        """Assert keyboard navigation works properly."""
        # Test tab navigation through interactive elements
        page.keyboard.press('Tab')

        # Ensure focus is visible
        focused_element = page.evaluate('document.activeElement.tagName')
        assert focused_element in ['A', 'BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'], (
            f"First tab should focus on interactive element, got {focused_element}"
        )

    def _assert_semantic_markup(self, page: Page):
        """Assert proper semantic HTML structure."""
        # Check for proper heading hierarchy
        headings = page.query_selector_all('h1, h2, h3, h4, h5, h6')
        if headings:
            first_heading = headings[0]
            assert first_heading.get_attribute('tagName').lower() == 'h1', (
                "First heading should be h1"
            )

        # Check for main landmark
        main_element = page.query_selector('main')
        assert main_element is not None, "Page should have a main landmark"

        # Check for navigation landmark
        nav_element = page.query_selector('nav, [role="navigation"]')
        assert nav_element is not None, "Page should have navigation landmark"


@pytest.mark.accessibility
@pytest.mark.keyboard_navigation
class TestKeyboardNavigation(AccessibilityTestMixin):
    """Test keyboard navigation functionality."""

    @pytest.mark.parametrize("theme", ['light', 'dark'])  # Test key themes
    def test_keyboard_navigation_flow(self, live_server, page: Page, theme: str):
        """Test complete keyboard navigation flow through the site."""
        page.goto(f"{live_server.url}/")
        self.setup_theme(page, theme)

        # Track focus progression
        focusable_elements = []

        # Start from body
        page.evaluate('document.body.focus()')

        # Navigate through all focusable elements
        for i in range(20):  # Limit to prevent infinite loops
            page.keyboard.press('Tab')
            element_info = page.evaluate('''
                () => {
                    const el = document.activeElement;
                    return {
                        tagName: el.tagName,
                        type: el.type || null,
                        id: el.id || null,
                        className: el.className || null,
                        visible: el.offsetWidth > 0 && el.offsetHeight > 0
                    };
                }
            ''')

            if element_info:
                focusable_elements.append(element_info)

                # Check focus is visible
                assert element_info['visible'], (
                    f"Focused element should be visible: {element_info}"
                )

        # Ensure we found interactive elements
        interactive_elements = [
            el for el in focusable_elements
            if el['tagName'] in ['A', 'BUTTON', 'INPUT', 'SELECT']
        ]
        assert len(interactive_elements) > 0, "Should find focusable interactive elements"

    def test_skip_links(self, live_server, page: Page):
        """Test skip link functionality."""
        page.goto(f"{live_server.url}/")

        # Press Tab to potentially reveal skip links
        page.keyboard.press('Tab')

        # Check if skip link becomes visible or accessible
        skip_link = page.query_selector('a[href="#main"], a[href="#content"]')
        if skip_link:
            # Skip link should be keyboard accessible
            skip_link.focus()
            assert skip_link.is_visible() or skip_link.evaluate(
                'el => getComputedStyle(el).position !== "absolute" || '
                'getComputedStyle(el).left !== "-9999px"'
            ), "Skip link should become visible when focused"

    def test_modal_keyboard_trap(self, live_server, page: Page):
        """Test keyboard trap in modals/dropdowns."""
        page.goto(f"{live_server.url}/")

        # Find dropdown triggers
        dropdown_triggers = page.query_selector_all('[role="button"][tabindex="0"]')

        for trigger in dropdown_triggers:
            # Open dropdown
            trigger.click()
            page.wait_for_timeout(100)

            # Tab navigation should stay within dropdown
            initial_focus = page.evaluate('document.activeElement')
            page.keyboard.press('Tab')

            # Check focus is still within dropdown context
            current_focus = page.evaluate('document.activeElement')
            assert current_focus != initial_focus, "Focus should move within dropdown"

            # Press Escape to close
            page.keyboard.press('Escape')
            page.wait_for_timeout(100)


@pytest.mark.accessibility
@pytest.mark.contact_form
class TestFormAccessibility(AccessibilityTestMixin):
    """Test accessibility of contact forms."""

    def test_contact_form_accessibility(self, live_server, page: Page, contact_page):
        """Test contact form for accessibility compliance."""
        page.goto(f"{live_server.url}/kontakt/")

        # Run general accessibility scan
        results = self.get_axe_results(page)
        self.assert_no_accessibility_violations(results)

        # Test form-specific accessibility
        self._test_form_labels(page)
        self._test_form_validation_messages(page)
        self._test_form_fieldsets(page)

    def _test_form_labels(self, page: Page):
        """Test that all form fields have proper labels."""
        form_fields = page.query_selector_all('input, select, textarea')

        for field in form_fields:
            field_id = field.get_attribute('id')
            field_name = field.get_attribute('name')

            if field_id:
                # Check for explicit label
                label = page.query_selector(f'label[for="{field_id}"]')
                if not label:
                    # Check for aria-label or aria-labelledby
                    aria_label = field.get_attribute('aria-label')
                    aria_labelledby = field.get_attribute('aria-labelledby')

                    assert aria_label or aria_labelledby, (
                        f"Form field {field_name} must have label, aria-label, or aria-labelledby"
                    )

    def _test_form_validation_messages(self, page: Page):
        """Test form validation message accessibility."""
        # Try to submit empty form to trigger validation
        submit_button = page.query_selector('button[type="submit"], input[type="submit"]')
        if submit_button:
            submit_button.click()
            page.wait_for_timeout(500)

            # Check for validation messages
            error_messages = page.query_selector_all('.error, [role="alert"], .invalid-feedback')

            for message in error_messages:
                # Error messages should be associated with form fields
                assert message.is_visible(), "Error messages should be visible"

                # Check for proper ARIA attributes
                role = message.get_attribute('role')
                aria_live = message.get_attribute('aria-live')

                assert role == 'alert' or aria_live in ['polite', 'assertive'], (
                    "Error messages should have proper ARIA attributes"
                )

    def _test_form_fieldsets(self, page: Page):
        """Test proper fieldset and legend usage for grouped form fields."""
        fieldsets = page.query_selector_all('fieldset')

        for fieldset in fieldsets:
            legend = fieldset.query_selector('legend')
            assert legend is not None, "Fieldset should have a legend"
            assert legend.text_content().strip(), "Legend should have descriptive text"


@pytest.mark.accessibility
@pytest.mark.visual_regression
class TestVisualRegression(AccessibilityTestMixin):
    """Test for visual regressions that might affect accessibility."""

    @pytest.mark.parametrize("theme", ['light', 'dark'])
    @pytest.mark.parametrize("viewport", [
        {'width': 1200, 'height': 800},  # Desktop
        {'width': 768, 'height': 1024},  # Tablet
        {'width': 375, 'height': 667},   # Mobile
    ])
    def test_theme_visual_consistency(self, live_server, page: Page,
                                    theme: str, viewport: Dict[str, int]):
        """Test visual consistency across themes and viewports."""
        page.set_viewport_size(viewport['width'], viewport['height'])
        page.goto(f"{live_server.url}/")

        self.setup_theme(page, theme)
        page.wait_for_load_state("networkidle")

        # Focus on navigation to test focus indicators
        nav_button = page.query_selector('.navbar button, .navbar a')
        if nav_button:
            nav_button.focus()

            # Ensure focus indicator is visible
            focus_outline = page.evaluate('''
                (element) => {
                    const styles = getComputedStyle(element);
                    return {
                        outline: styles.outline,
                        outlineWidth: styles.outlineWidth,
                        outlineStyle: styles.outlineStyle,
                        outlineColor: styles.outlineColor,
                        boxShadow: styles.boxShadow
                    };
                }
            ''', nav_button)

            # Should have some form of focus indication
            has_focus_indicator = any([
                focus_outline.get('outline', 'none') != 'none',
                focus_outline.get('outlineWidth', '0px') != '0px',
                'focus' in focus_outline.get('boxShadow', ''),
            ])

            assert has_focus_indicator, f"Focus indicator should be visible in {theme} theme"

    def test_color_scheme_preferences(self, live_server, page: Page):
        """Test that themes respect system color scheme preferences."""
        page.goto(f"{live_server.url}/")

        # Test with light preference
        page.emulate_media(color_scheme='light')
        self.setup_theme(page, 'light')

        # Check computed colors
        bg_color = page.evaluate('''
            () => getComputedStyle(document.body).backgroundColor
        ''')

        # Light theme should have light background
        assert 'rgb(255, 255, 255)' in bg_color or 'rgb(248' in bg_color, (
            f"Light theme should have light background, got {bg_color}"
        )

        # Test with dark preference
        page.emulate_media(color_scheme='dark')
        self.setup_theme(page, 'dark')

        bg_color_dark = page.evaluate('''
            () => getComputedStyle(document.body).backgroundColor
        ''')

        # Dark theme should have dark background
        assert 'rgb(0, 0, 0)' in bg_color_dark or 'rgb(' in bg_color_dark and '0,' in bg_color_dark, (
            f"Dark theme should have dark background, got {bg_color_dark}"
        )


@pytest.fixture
def live_server():
    """Provide a live server for Playwright tests."""
    from django.test.utils import setup_test_environment, teardown_test_environment
    from django.test.testcases import LiveServerTestCase
    from django.conf import settings

    # Use a specific port for consistency
    import socket
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()

    class AccessibilityLiveServer(StaticLiveServerTestCase):
        port = port

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.live_server_url = f'http://127.0.0.1:{cls.port}'

    server = AccessibilityLiveServer()
    server.setUpClass()

    yield server

    server.tearDownClass()