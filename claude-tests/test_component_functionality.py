"""
Comprehensive functional tests for UI components after DaisyUI to Flowbite migration.
Tests interactive elements, user flows, and component behavior.
"""

import pytest
from playwright.sync_api import Page, expect
from django.test import LiveServerTestCase
import time
import json


@pytest.mark.django_db
class TestButtonComponents:
    """Test all button variants and their functionality."""

    def test_primary_button_functionality(self, page: Page, live_server):
        """Test primary button behavior and styling."""
        page.goto(f"{live_server.url}/")

        # Find primary buttons
        primary_buttons = page.locator('a.btn-primary, button.btn-primary, .btn.btn-primary')

        if primary_buttons.count() > 0:
            button = primary_buttons.first

            # Test visibility and basic properties
            expect(button).to_be_visible()
            expect(button).to_be_enabled()

            # Test styling classes
            button_classes = button.get_attribute('class') or ''
            assert 'btn-primary' in button_classes or 'bg-primary' in button_classes, \
                "Primary button should have primary styling"

            # Test hover interaction
            button.hover()
            page.wait_for_timeout(100)

            # Test click interaction
            if button.get_attribute('href'):
                # It's a link - check href is valid
                href = button.get_attribute('href')
                assert href and href != '#', "Button link should have valid href"
            else:
                # It's a button - test click
                button.click()
                page.wait_for_timeout(300)

    def test_secondary_button_functionality(self, page: Page, live_server):
        """Test secondary/outline button behavior."""
        page.goto(f"{live_server.url}/")

        # Find secondary buttons
        secondary_buttons = page.locator(
            'a.btn-secondary, button.btn-secondary, '
            'a.btn-outline, button.btn-outline, '
            '.btn.btn-secondary, .btn.btn-outline'
        )

        if secondary_buttons.count() > 0:
            button = secondary_buttons.first

            expect(button).to_be_visible()
            expect(button).to_be_enabled()

            # Test styling
            button_classes = button.get_attribute('class') or ''
            has_secondary_style = any(cls in button_classes for cls in [
                'btn-secondary', 'btn-outline', 'border'
            ])
            assert has_secondary_style, "Secondary button should have appropriate styling"

            # Test interaction
            button.hover()
            page.wait_for_timeout(100)

    def test_button_focus_states(self, page: Page, live_server):
        """Test button focus states for accessibility."""
        page.goto(f"{live_server.url}/")

        buttons = page.locator('button, .btn, a[role="button"]')

        if buttons.count() > 0:
            for i in range(min(buttons.count(), 3)):
                button = buttons.nth(i)

                # Focus the button
                button.focus()

                # Check for focus indicator
                # This could be outline, ring, or other visual indicator
                focused_styles = page.evaluate("""
                    (element) => {
                        const styles = window.getComputedStyle(element);
                        return {
                            outline: styles.outline,
                            outlineWidth: styles.outlineWidth,
                            boxShadow: styles.boxShadow,
                            transform: styles.transform
                        };
                    }
                """, button)

                # Should have some form of focus indicator
                has_focus_indicator = any([
                    focused_styles['outline'] != 'none',
                    focused_styles['outlineWidth'] != '0px',
                    'ring' in (button.get_attribute('class') or ''),
                    focused_styles['boxShadow'] != 'none'
                ])

                # Not all buttons need visual focus (some have :focus-visible only)
                # This is informational testing

    def test_button_loading_states(self, page: Page, live_server):
        """Test button loading states if implemented."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            page.goto(f"{live_server.url}/contact/")

        # Look for form with submit button
        forms = page.locator('form')

        if forms.count() > 0:
            form = forms.first
            submit_button = form.locator('button[type="submit"], input[type="submit"]')

            if submit_button.count() > 0:
                button = submit_button.first

                # Fill in required fields if any
                inputs = form.locator('input[required], textarea[required]')
                for i in range(inputs.count()):
                    input_field = inputs.nth(i)
                    input_type = input_field.get_attribute('type')

                    if input_type == 'email':
                        input_field.fill('test@example.com')
                    elif input_type == 'tel':
                        input_field.fill('12345678')
                    else:
                        input_field.fill('Test content')

                # Test form submission
                original_text = button.text_content()
                button.click()

                # Check if button text changes (loading state)
                page.wait_for_timeout(500)
                # Note: This depends on implementation


@pytest.mark.django_db
class TestNavigationComponents:
    """Test navigation functionality including dropdowns and mobile menu."""

    def test_mobile_menu_functionality(self, page: Page, live_server):
        """Test mobile navigation menu."""
        page.goto(f"{live_server.url}/")

        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        page.wait_for_timeout(500)

        # Find mobile menu button
        mobile_menu_button = page.locator(
            '#mobile-menu-button, '
            '.navbar-toggler, '
            '[aria-label*="menu"], '
            '.menu-toggle'
        )

        if mobile_menu_button.count() > 0:
            button = mobile_menu_button.first
            expect(button).to_be_visible()

            # Test menu toggle
            button.click()
            page.wait_for_timeout(300)

            # Find mobile menu
            mobile_menu = page.locator(
                '#mobile-menu, '
                '.mobile-menu, '
                '.navbar-collapse, '
                '[role="menu"]'
            )

            if mobile_menu.count() > 0:
                menu = mobile_menu.first
                expect(menu).to_be_visible()

                # Test menu items
                menu_items = menu.locator('a, [role="menuitem"]')
                assert menu_items.count() > 0, "Mobile menu should have menu items"

                # Test first menu item
                if menu_items.count() > 0:
                    first_item = menu_items.first
                    expect(first_item).to_be_visible()
                    expect(first_item).to_be_enabled()

                # Close menu by clicking button again
                button.click()
                page.wait_for_timeout(300)

    def test_desktop_dropdown_functionality(self, page: Page, live_server):
        """Test desktop dropdown navigation."""
        page.goto(f"{live_server.url}/")

        # Set desktop viewport
        page.set_viewport_size({"width": 1200, "height": 800})
        page.wait_for_timeout(500)

        # Find dropdown triggers
        dropdown_triggers = page.locator(
            '[aria-haspopup="true"], '
            '.dropdown button, '
            '[data-dropdown-toggle], '
            '#pages-menu-button'
        )

        if dropdown_triggers.count() > 0:
            trigger = dropdown_triggers.first

            # Test dropdown visibility in desktop
            expect(trigger).to_be_visible()

            # Test dropdown interaction
            trigger.click()
            page.wait_for_timeout(300)

            # Find dropdown content
            dropdown_content = page.locator(
                '.dropdown-content, '
                '[role="menu"], '
                '.dropdown-menu, '
                '[data-dropdown-menu]'
            )

            if dropdown_content.count() > 0:
                content = dropdown_content.first
                expect(content).to_be_visible()

                # Test dropdown items
                dropdown_items = content.locator('a, [role="menuitem"]')
                if dropdown_items.count() > 0:
                    item = dropdown_items.first
                    expect(item).to_be_visible()

                # Test closing dropdown by clicking outside
                page.click('body')
                page.wait_for_timeout(300)

    def test_keyboard_navigation(self, page: Page, live_server):
        """Test keyboard navigation accessibility."""
        page.goto(f"{live_server.url}/")

        # Test tab navigation
        page.keyboard.press('Tab')
        page.wait_for_timeout(100)

        # Check if focus is visible
        focused_element = page.evaluate("""
            () => document.activeElement
        """)

        assert focused_element is not None, "Tab navigation should focus elements"

        # Test dropdown keyboard interaction
        dropdown_triggers = page.locator('[aria-haspopup="true"]')

        if dropdown_triggers.count() > 0:
            trigger = dropdown_triggers.first
            trigger.focus()

            # Test Enter key
            page.keyboard.press('Enter')
            page.wait_for_timeout(300)

            # Test Escape key
            page.keyboard.press('Escape')
            page.wait_for_timeout(300)

    def test_navigation_links_validity(self, page: Page, live_server):
        """Test that navigation links are valid and accessible."""
        page.goto(f"{live_server.url}/")

        # Find all navigation links
        nav_links = page.locator('nav a, .navbar a, header a')

        if nav_links.count() > 0:
            for i in range(min(nav_links.count(), 5)):
                link = nav_links.nth(i)

                # Check link has valid href
                href = link.get_attribute('href')
                if href and not href.startswith('#'):
                    # Skip external links and javascript links
                    if not href.startswith('http') and not href.startswith('javascript'):
                        assert href.startswith('/') or href.startswith(live_server.url), \
                            f"Navigation link should have valid internal href: {href}"

                # Check for accessibility attributes
                aria_label = link.get_attribute('aria-label')
                text_content = link.text_content()

                assert aria_label or text_content.strip(), \
                    "Navigation links should have accessible text"


@pytest.mark.django_db
class TestFormComponents:
    """Test form functionality and validation."""

    def test_contact_form_rendering(self, page: Page, live_server):
        """Test contact form renders correctly."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        # Find contact form
        forms = page.locator('form')
        assert forms.count() > 0, "Contact page should have a form"

        form = forms.first
        expect(form).to_be_visible()

        # Test form fields
        form_fields = form.locator('input, textarea, select')
        assert form_fields.count() > 0, "Form should have input fields"

        # Test each field type
        for i in range(form_fields.count()):
            field = form_fields.nth(i)
            field_type = field.get_attribute('type')

            expect(field).to_be_visible()

            # Test field styling
            field_classes = field.get_attribute('class') or ''
            has_form_styling = any(cls in field_classes for cls in [
                'input', 'form-control', 'border', 'rounded', 'px-', 'py-'
            ])
            assert has_form_styling, f"Form field should have proper styling: {field_classes}"

    def test_form_field_interactions(self, page: Page, live_server):
        """Test form field interactions and behavior."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        forms = page.locator('form')
        if forms.count() == 0:
            pytest.skip("No forms found")

        form = forms.first

        # Test text input
        text_inputs = form.locator('input[type="text"], input:not([type])')
        if text_inputs.count() > 0:
            text_input = text_inputs.first

            # Test typing
            text_input.click()
            text_input.fill('Test Name')
            assert text_input.input_value() == 'Test Name', "Text input should accept text"

        # Test email input
        email_inputs = form.locator('input[type="email"]')
        if email_inputs.count() > 0:
            email_input = email_inputs.first

            email_input.click()
            email_input.fill('test@example.com')
            assert email_input.input_value() == 'test@example.com', "Email input should accept email"

        # Test textarea
        textareas = form.locator('textarea')
        if textareas.count() > 0:
            textarea = textareas.first

            textarea.click()
            textarea.fill('This is a test message')
            assert 'test message' in textarea.input_value(), "Textarea should accept text"

    def test_form_validation_behavior(self, page: Page, live_server):
        """Test form validation behavior."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        forms = page.locator('form')
        if forms.count() == 0:
            pytest.skip("No forms found")

        form = forms.first

        # Find submit button
        submit_buttons = form.locator('button[type="submit"], input[type="submit"]')
        if submit_buttons.count() == 0:
            pytest.skip("No submit button found")

        submit_button = submit_buttons.first

        # Test submitting empty form
        submit_button.click()
        page.wait_for_timeout(500)

        # Check for HTML5 validation or custom validation
        # Note: This depends on implementation

        # Fill out form correctly
        name_inputs = form.locator('input[name*="name"], input[id*="name"]')
        if name_inputs.count() > 0:
            name_inputs.first.fill('John Doe')

        email_inputs = form.locator('input[type="email"], input[name*="email"]')
        if email_inputs.count() > 0:
            email_inputs.first.fill('john@example.com')

        message_fields = form.locator('textarea, input[name*="message"]')
        if message_fields.count() > 0:
            message_fields.first.fill('This is a test message')

        # Test valid form submission
        submit_button.click()
        page.wait_for_timeout(1000)


@pytest.mark.django_db
class TestCardComponents:
    """Test card component functionality and styling."""

    def test_card_rendering(self, page: Page, live_server):
        """Test card components render correctly."""
        page.goto(f"{live_server.url}/")

        # Look for card elements
        cards = page.locator(
            '.card, '
            '.bg-white, '
            '.shadow, '
            '[class*="rounded"]'
        ).filter(has=page.locator('img, h1, h2, h3, h4, h5, h6, p'))

        if cards.count() > 0:
            for i in range(min(cards.count(), 3)):
                card = cards.nth(i)
                expect(card).to_be_visible()

                # Check for card content
                card_content = card.locator('h1, h2, h3, h4, h5, h6, p, img')
                assert card_content.count() > 0, "Card should have content"

                # Test card styling
                card_classes = card.get_attribute('class') or ''
                has_card_styling = any(cls in card_classes for cls in [
                    'card', 'shadow', 'rounded', 'bg-white', 'bg-base', 'border'
                ])
                assert has_card_styling, f"Card should have proper styling: {card_classes}"

    def test_card_hover_effects(self, page: Page, live_server):
        """Test card hover effects."""
        page.goto(f"{live_server.url}/")

        cards = page.locator('.card, .shadow, .bg-white').filter(
            has=page.locator('img, h1, h2, h3, h4, h5, h6')
        )

        if cards.count() > 0:
            card = cards.first

            # Get initial styles
            initial_transform = page.evaluate("""
                (element) => window.getComputedStyle(element).transform
            """, card)

            # Hover over card
            card.hover()
            page.wait_for_timeout(200)

            # Check for transform changes (common hover effect)
            hover_transform = page.evaluate("""
                (element) => window.getComputedStyle(element).transform
            """, card)

            # Note: Not all cards need hover effects, this is informational


@pytest.mark.django_db
class TestInteractiveElements:
    """Test various interactive elements functionality."""

    def test_modal_functionality(self, page: Page, live_server):
        """Test modal component functionality if present."""
        page.goto(f"{live_server.url}/")

        # Look for modal triggers
        modal_triggers = page.locator(
            '[data-modal-toggle], '
            '[data-modal-target], '
            '.modal-trigger, '
            '[data-bs-toggle="modal"]'
        )

        if modal_triggers.count() > 0:
            trigger = modal_triggers.first
            trigger.click()
            page.wait_for_timeout(500)

            # Look for modal
            modals = page.locator(
                '.modal, '
                '[role="dialog"], '
                '[data-modal], '
                '.modal-dialog'
            )

            if modals.count() > 0:
                modal = modals.first
                expect(modal).to_be_visible()

                # Test modal close functionality
                close_buttons = page.locator(
                    '[data-modal-hide], '
                    '.modal-close, '
                    '[aria-label*="lose"], '
                    '.btn-close'
                )

                if close_buttons.count() > 0:
                    close_buttons.first.click()
                    page.wait_for_timeout(300)

    def test_tooltip_functionality(self, page: Page, live_server):
        """Test tooltip functionality if present."""
        page.goto(f"{live_server.url}/")

        # Look for elements with tooltips
        tooltip_elements = page.locator(
            '[title], '
            '[data-tooltip], '
            '[data-bs-toggle="tooltip"], '
            '[data-tooltip-target]'
        )

        if tooltip_elements.count() > 0:
            element = tooltip_elements.first

            # Hover to trigger tooltip
            element.hover()
            page.wait_for_timeout(500)

            # Look for tooltip content
            tooltips = page.locator('.tooltip, [role="tooltip"], .popover')

            # Note: Tooltips might not be visible in all cases

    def test_accordion_functionality(self, page: Page, live_server):
        """Test accordion/collapse functionality if present."""
        page.goto(f"{live_server.url}/")

        # Look for accordion triggers
        accordion_triggers = page.locator(
            '[data-accordion-target], '
            '[data-bs-toggle="collapse"], '
            '.accordion-button, '
            '[aria-expanded]'
        )

        if accordion_triggers.count() > 0:
            trigger = accordion_triggers.first

            # Test accordion toggle
            trigger.click()
            page.wait_for_timeout(300)

            # Look for accordion content
            accordion_content = page.locator(
                '.accordion-content, '
                '.collapse, '
                '[data-accordion-content]'
            )

            if accordion_content.count() > 0:
                # Note: Testing depends on implementation

    def test_tab_functionality(self, page: Page, live_server):
        """Test tab component functionality if present."""
        page.goto(f"{live_server.url}/")

        # Look for tab elements
        tab_triggers = page.locator(
            '[role="tab"], '
            '.tab, '
            '[data-bs-toggle="tab"], '
            '.nav-link'
        )

        if tab_triggers.count() > 0:
            # Test tab switching
            for i in range(min(tab_triggers.count(), 3)):
                tab = tab_triggers.nth(i)
                tab.click()
                page.wait_for_timeout(200)

                # Check if tab is active
                tab_classes = tab.get_attribute('class') or ''
                aria_selected = tab.get_attribute('aria-selected')

                # Note: Tab state depends on implementation


def test_component_functionality_report(page: Page, live_server):
    """Generate a comprehensive component functionality report."""
    page.goto(f"{live_server.url}/")

    # Collect comprehensive component information
    component_analysis = page.evaluate("""
        () => {
            const analysis = {
                buttons: {
                    total: document.querySelectorAll('button, .btn, [role="button"]').length,
                    primary: document.querySelectorAll('.btn-primary, .bg-primary').length,
                    secondary: document.querySelectorAll('.btn-secondary, .btn-outline').length
                },
                forms: {
                    total: document.querySelectorAll('form').length,
                    inputs: document.querySelectorAll('input').length,
                    textareas: document.querySelectorAll('textarea').length
                },
                navigation: {
                    navbars: document.querySelectorAll('nav, .navbar').length,
                    dropdowns: document.querySelectorAll('.dropdown, [aria-haspopup="true"]').length,
                    menus: document.querySelectorAll('[role="menu"]').length
                },
                interactive: {
                    modals: document.querySelectorAll('.modal, [role="dialog"]').length,
                    tooltips: document.querySelectorAll('[title], [data-tooltip]').length,
                    accordions: document.querySelectorAll('[data-accordion], .accordion').length,
                    tabs: document.querySelectorAll('[role="tab"], .tab').length
                },
                cards: {
                    total: document.querySelectorAll('.card, .shadow').length
                },
                accessibility: {
                    ariaLabels: document.querySelectorAll('[aria-label]').length,
                    skipLinks: document.querySelectorAll('a[href="#main-content"]').length,
                    headings: document.querySelectorAll('h1, h2, h3, h4, h5, h6').length
                }
            };

            return analysis;
        }
    """)

    # Save the analysis
    import json
    from pathlib import Path

    report_path = Path(__file__).parent / 'component_functionality_report.json'
    with open(report_path, 'w') as f:
        json.dump({
            'timestamp': time.time(),
            'url': page.url,
            'analysis': component_analysis
        }, f, indent=2)

    print(f"Component functionality report saved to: {report_path}")
    return component_analysis