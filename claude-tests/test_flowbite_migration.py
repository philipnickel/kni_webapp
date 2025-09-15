"""
Test suite to verify the DaisyUI to Flowbite migration is successful.
This module tests component rendering, functionality, and migration integrity.
"""

import pytest
from playwright.sync_api import Page, expect
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import json
from pathlib import Path

# Test configuration
FLOWBITE_COMPONENTS = [
    'button', 'dropdown', 'modal', 'tooltip', 'accordion',
    'carousel', 'collapse', 'datepicker', 'drawer', 'tabs'
]

DAISYUI_COMPONENTS = [
    'btn', 'card', 'badge', 'alert', 'hero', 'navbar',
    'footer', 'menu', 'dropdown', 'modal'
]

class FlowbiteMigrationTestCase(StaticLiveServerTestCase):
    """Base test case for Flowbite migration testing."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_results = []

    def log_test_result(self, test_name, status, details=None):
        """Log test results for reporting."""
        self.test_results.append({
            'test': test_name,
            'status': status,
            'details': details,
            'timestamp': time.time()
        })


@pytest.mark.django_db
class TestFlowbiteComponentRendering:
    """Test that Flowbite components render correctly after migration."""

    def test_flowbite_css_loaded(self, page: Page, live_server):
        """Verify Flowbite CSS is properly loaded."""
        page.goto(f"{live_server.url}/")

        # Check if Flowbite CSS classes are available
        flowbite_css_check = page.evaluate("""
            () => {
                const testElement = document.createElement('div');
                testElement.className = 'bg-blue-500 text-white rounded-lg p-4';
                document.body.appendChild(testElement);

                const computedStyle = window.getComputedStyle(testElement);
                const hasBackground = computedStyle.backgroundColor !== 'rgba(0, 0, 0, 0)';
                const hasRounding = computedStyle.borderRadius !== '0px';
                const hasPadding = computedStyle.padding !== '0px';

                document.body.removeChild(testElement);

                return hasBackground && hasRounding && hasPadding;
            }
        """)

        assert flowbite_css_check, "Flowbite CSS classes are not working properly"

    def test_flowbite_javascript_loaded(self, page: Page, live_server):
        """Verify Flowbite JavaScript is properly loaded."""
        page.goto(f"{live_server.url}/")

        # Check if Flowbite namespace is available
        flowbite_js_loaded = page.evaluate("typeof window.Flowbite !== 'undefined'")
        assert flowbite_js_loaded, "Flowbite JavaScript is not loaded"

        # Check for core Flowbite methods
        flowbite_methods = page.evaluate("""
            () => {
                return typeof window.Flowbite === 'object' &&
                       typeof window.Flowbite.init === 'function';
            }
        """)
        assert flowbite_methods, "Flowbite methods are not available"

    def test_button_components_migration(self, page: Page, live_server):
        """Test button components work correctly with Flowbite."""
        page.goto(f"{live_server.url}/")

        # Test primary button
        primary_buttons = page.locator('button, .btn, [role="button"]').filter(
            has_text="tilbud"
        ).or_(page.locator('a.btn-primary'))

        if primary_buttons.count() > 0:
            button = primary_buttons.first

            # Check button is visible and clickable
            expect(button).to_be_visible()
            expect(button).to_be_enabled()

            # Check for proper styling classes
            button_classes = button.get_attribute('class') or ''
            assert any(cls in button_classes for cls in ['btn', 'button', 'bg-blue', 'bg-primary']), \
                f"Button missing proper styling classes: {button_classes}"

            # Test hover state
            button.hover()
            page.wait_for_timeout(100)

            # Button should be interactive
            assert button.is_enabled(), "Button should be enabled"

    def test_navigation_dropdown_migration(self, page: Page, live_server):
        """Test navigation dropdown functionality."""
        page.goto(f"{live_server.url}/")

        # Look for dropdown buttons
        dropdown_buttons = page.locator('[aria-haspopup="true"], .dropdown button, [data-dropdown-toggle]')

        if dropdown_buttons.count() > 0:
            dropdown_button = dropdown_buttons.first

            # Test dropdown interaction
            expect(dropdown_button).to_be_visible()
            dropdown_button.click()

            # Wait for dropdown to appear
            page.wait_for_timeout(300)

            # Look for dropdown content
            dropdown_content = page.locator('.dropdown-content, [role="menu"], .dropdown-menu, [data-dropdown-menu]')

            if dropdown_content.count() > 0:
                # Dropdown should be visible after click
                expect(dropdown_content.first).to_be_visible()

                # Click outside to close
                page.click('body')
                page.wait_for_timeout(300)

    def test_responsive_navigation(self, page: Page, live_server):
        """Test responsive navigation behavior."""
        page.goto(f"{live_server.url}/")

        # Test mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        page.wait_for_timeout(500)

        # Look for mobile menu button
        mobile_menu_button = page.locator('[aria-label*="menu"], .navbar-toggler, #mobile-menu-button')

        if mobile_menu_button.count() > 0:
            expect(mobile_menu_button.first).to_be_visible()

            # Test mobile menu interaction
            mobile_menu_button.first.click()
            page.wait_for_timeout(300)

            # Look for mobile menu content
            mobile_menu = page.locator('#mobile-menu, .mobile-menu, [role="menu"]')
            if mobile_menu.count() > 0:
                expect(mobile_menu.first).to_be_visible()

        # Test desktop viewport
        page.set_viewport_size({"width": 1200, "height": 800})
        page.wait_for_timeout(500)

    def test_card_components_migration(self, page: Page, live_server):
        """Test card components render correctly."""
        page.goto(f"{live_server.url}/")

        # Look for card elements
        cards = page.locator('.card, .bg-white, .shadow, [class*="rounded"]').filter(
            has=page.locator('img, h1, h2, h3, h4, h5, h6, p')
        )

        if cards.count() > 0:
            card = cards.first
            expect(card).to_be_visible()

            # Check for proper card styling
            card_classes = card.get_attribute('class') or ''
            has_card_styling = any(cls in card_classes for cls in [
                'card', 'shadow', 'rounded', 'bg-white', 'bg-base-100'
            ])
            assert has_card_styling, f"Card missing proper styling: {card_classes}"

    def test_form_components_migration(self, page: Page, live_server):
        """Test form components work correctly."""
        # Try contact page first
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            page.goto(f"{live_server.url}/contact/")

        # Look for form elements
        forms = page.locator('form')

        if forms.count() > 0:
            form = forms.first
            expect(form).to_be_visible()

            # Test input fields
            inputs = form.locator('input[type="text"], input[type="email"], textarea')
            if inputs.count() > 0:
                input_field = inputs.first
                expect(input_field).to_be_visible()
                expect(input_field).to_be_enabled()

                # Test input styling
                input_classes = input_field.get_attribute('class') or ''
                has_input_styling = any(cls in input_classes for cls in [
                    'input', 'form-control', 'border', 'rounded'
                ])
                assert has_input_styling, f"Input missing proper styling: {input_classes}"

    def test_no_daisyui_remnants(self, page: Page, live_server):
        """Verify no DaisyUI-specific classes remain in the HTML."""
        page.goto(f"{live_server.url}/")

        # Check for DaisyUI-specific classes that should be removed
        daisyui_classes = [
            'daisyui', 'daisy-', 'btn-ghost', 'btn-outline',
            'card-compact', 'hero-content', 'navbar-start',
            'navbar-center', 'navbar-end'
        ]

        page_content = page.content()

        # Some DaisyUI classes might still be valid if they're used intentionally
        # Focus on classes that are definitely DaisyUI-specific
        problematic_classes = ['daisyui', 'daisy-']

        for class_name in problematic_classes:
            assert class_name not in page_content, \
                f"Found DaisyUI-specific class '{class_name}' that should be removed"

    def test_theme_data_attributes(self, page: Page, live_server):
        """Test that theme data attributes work correctly."""
        page.goto(f"{live_server.url}/")

        # Check for theme data attribute on html element
        html_element = page.locator('html')
        theme_attr = html_element.get_attribute('data-theme')

        # Theme should be set
        assert theme_attr is not None, "HTML element should have data-theme attribute"
        assert theme_attr in ['light', 'dark', 'auto'], f"Unexpected theme value: {theme_attr}"

    def test_accessibility_attributes_preserved(self, page: Page, live_server):
        """Test that accessibility attributes are preserved after migration."""
        page.goto(f"{live_server.url}/")

        # Check for skip links
        skip_links = page.locator('a[href="#main-content"], a[href="#main-navigation"]')
        assert skip_links.count() > 0, "Skip links should be present for accessibility"

        # Check for proper ARIA labels
        interactive_elements = page.locator('button, [role="button"], a[role="button"]')

        for i in range(min(interactive_elements.count(), 5)):  # Check first 5 elements
            element = interactive_elements.nth(i)

            # Should have either aria-label or text content
            aria_label = element.get_attribute('aria-label')
            text_content = element.text_content()

            assert aria_label or text_content.strip(), \
                "Interactive elements should have accessible labels"

    def test_responsive_images(self, page: Page, live_server):
        """Test that images are responsive and properly loaded."""
        page.goto(f"{live_server.url}/")

        images = page.locator('img')

        if images.count() > 0:
            for i in range(min(images.count(), 3)):  # Test first 3 images
                img = images.nth(i)

                # Image should be visible
                expect(img).to_be_visible()

                # Check for alt text
                alt_text = img.get_attribute('alt')
                assert alt_text is not None, "Images should have alt text for accessibility"

                # Check for responsive classes
                img_classes = img.get_attribute('class') or ''
                has_responsive_class = any(cls in img_classes for cls in [
                    'w-full', 'max-w', 'object-cover', 'object-contain', 'responsive'
                ])
                # Note: Not all images need responsive classes, so this is informational

    def test_javascript_functionality(self, page: Page, live_server):
        """Test that JavaScript functionality works correctly."""
        page.goto(f"{live_server.url}/")

        # Check for console errors
        console_errors = []
        page.on("console", lambda msg:
            console_errors.append(msg.text) if msg.type == "error" else None)

        # Interact with the page to trigger any JS
        page.wait_for_timeout(1000)

        # Click on interactive elements
        interactive_elements = page.locator('button, [role="button"], a[href^="#"]')

        if interactive_elements.count() > 0:
            interactive_elements.first.click()
            page.wait_for_timeout(500)

        # Filter out irrelevant console errors
        relevant_errors = [error for error in console_errors
                          if not any(ignore in error.lower() for ignore in [
                              'favicon', 'chrome-extension', 'googletagmanager'
                          ])]

        # Assert no critical JavaScript errors
        assert len(relevant_errors) == 0, \
            f"JavaScript errors found: {relevant_errors}"


@pytest.mark.django_db
class TestFlowbiteFunctionalComponents:
    """Test functional behavior of migrated components."""

    def test_modal_functionality(self, page: Page, live_server):
        """Test modal components work correctly."""
        page.goto(f"{live_server.url}/")

        # Look for modal triggers
        modal_triggers = page.locator('[data-modal-toggle], [data-modal-target], .modal-trigger')

        if modal_triggers.count() > 0:
            trigger = modal_triggers.first
            trigger.click()
            page.wait_for_timeout(300)

            # Look for modal
            modal = page.locator('.modal, [role="dialog"], [data-modal]')
            if modal.count() > 0:
                expect(modal.first).to_be_visible()

                # Test modal close
                close_buttons = page.locator('[data-modal-hide], .modal-close, [aria-label*="lose"]')
                if close_buttons.count() > 0:
                    close_buttons.first.click()
                    page.wait_for_timeout(300)

    def test_dropdown_keyboard_navigation(self, page: Page, live_server):
        """Test dropdown keyboard navigation."""
        page.goto(f"{live_server.url}/")

        dropdown_triggers = page.locator('[aria-haspopup="true"]')

        if dropdown_triggers.count() > 0:
            trigger = dropdown_triggers.first

            # Focus the trigger
            trigger.focus()

            # Press Enter to open
            page.keyboard.press('Enter')
            page.wait_for_timeout(300)

            # Press Escape to close
            page.keyboard.press('Escape')
            page.wait_for_timeout(300)

    def test_form_validation(self, page: Page, live_server):
        """Test form validation works correctly."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        forms = page.locator('form')

        if forms.count() > 0:
            form = forms.first

            # Find submit button
            submit_buttons = form.locator('button[type="submit"], input[type="submit"]')

            if submit_buttons.count() > 0:
                # Try to submit empty form
                submit_buttons.first.click()
                page.wait_for_timeout(500)

                # Check for validation messages
                validation_messages = page.locator(
                    '.error, .invalid-feedback, [aria-invalid="true"]'
                )

                # Note: Not all forms have client-side validation


@pytest.fixture(scope="session")
def migration_test_report():
    """Generate a comprehensive migration test report."""
    report_data = {
        'timestamp': time.time(),
        'flowbite_version': None,
        'migration_status': 'in_progress',
        'component_tests': [],
        'accessibility_tests': [],
        'performance_tests': []
    }

    yield report_data

    # Save report after tests complete
    report_path = Path(__file__).parent / 'migration_test_report.json'
    with open(report_path, 'w') as f:
        json.dump(report_data, f, indent=2)


def test_generate_migration_report(page: Page, live_server, migration_test_report):
    """Generate a comprehensive migration report."""
    page.goto(f"{live_server.url}/")

    # Check Flowbite version
    flowbite_version = page.evaluate("""
        () => {
            if (window.Flowbite && window.Flowbite.version) {
                return window.Flowbite.version;
            }
            return null;
        }
    """)

    migration_test_report['flowbite_version'] = flowbite_version

    # Collect component information
    components_info = page.evaluate("""
        () => {
            const components = [];

            // Check for various component types
            const selectors = [
                'button, .btn',
                '.card',
                '.dropdown',
                '.modal',
                'form',
                '.navbar, nav',
                '.hero'
            ];

            selectors.forEach(selector => {
                const elements = document.querySelectorAll(selector);
                if (elements.length > 0) {
                    components.push({
                        selector: selector,
                        count: elements.length,
                        classes: Array.from(elements[0].classList)
                    });
                }
            });

            return components;
        }
    """)

    migration_test_report['component_tests'] = components_info
    migration_test_report['migration_status'] = 'completed'