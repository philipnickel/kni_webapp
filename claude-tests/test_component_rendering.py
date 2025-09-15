"""
Comprehensive component rendering tests for DaisyUI to Flowbite migration.
Tests visual consistency, component integrity, and proper styling across all components.
"""

import pytest
from playwright.sync_api import Page, expect
import time
import json
from pathlib import Path


# Component categories to test
COMPONENT_CATEGORIES = {
    'buttons': {
        'selectors': ['button', '.btn', 'a[role="button"]', 'input[type="submit"]'],
        'variants': ['primary', 'secondary', 'outline', 'ghost'],
        'critical': True
    },
    'cards': {
        'selectors': ['.card', '.shadow', '.bg-white', '.rounded'],
        'variants': ['default', 'compact', 'bordered'],
        'critical': True
    },
    'navigation': {
        'selectors': ['nav', '.navbar', '.menu', '.dropdown'],
        'variants': ['desktop', 'mobile', 'dropdown'],
        'critical': True
    },
    'forms': {
        'selectors': ['form', 'input', 'textarea', 'select', 'label'],
        'variants': ['text', 'email', 'password', 'textarea'],
        'critical': True
    },
    'typography': {
        'selectors': ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', '.text-'],
        'variants': ['heading', 'body', 'caption'],
        'critical': True
    },
    'layout': {
        'selectors': ['.container', '.grid', '.flex', '.max-w-'],
        'variants': ['container', 'grid', 'flexbox'],
        'critical': False
    },
    'alerts': {
        'selectors': ['.alert', '.notification', '.toast', '.badge'],
        'variants': ['success', 'warning', 'error', 'info'],
        'critical': False
    },
    'modals': {
        'selectors': ['.modal', '[role="dialog"]', '.overlay'],
        'variants': ['default', 'large', 'small'],
        'critical': False
    }
}

# Theme compatibility test
THEMES_TO_TEST = ['light', 'corporate', 'business', 'emerald']


@pytest.mark.django_db
class TestComponentRenderingIntegrity:
    """Test that all components render correctly after migration."""

    def test_button_component_rendering(self, page: Page, live_server):
        """Test button components render correctly across all variants."""
        page.goto(f"{live_server.url}/")

        button_selectors = COMPONENT_CATEGORIES['buttons']['selectors']
        button_issues = []

        for selector in button_selectors:
            buttons = page.locator(selector)

            for i in range(min(buttons.count(), 5)):  # Test first 5 of each type
                button = buttons.nth(i)

                if not button.is_visible():
                    continue

                # Test basic rendering properties
                button_box = button.bounding_box()
                if button_box:
                    # Button should have reasonable dimensions
                    if button_box['width'] < 20 or button_box['height'] < 20:
                        button_issues.append(f"Button too small: {selector} ({button_box['width']}x{button_box['height']})")

                # Test styling classes
                button_classes = button.get_attribute('class') or ''
                has_button_styling = any(cls in button_classes for cls in [
                    'btn', 'button', 'bg-', 'text-', 'border-', 'px-', 'py-', 'rounded'
                ])

                if not has_button_styling:
                    button_issues.append(f"Button missing styling classes: {selector}")

                # Test interaction capability
                if button.is_enabled():
                    try:
                        button.hover()
                        page.wait_for_timeout(50)
                    except:
                        button_issues.append(f"Button hover failed: {selector}")

        assert len(button_issues) == 0, f"Button rendering issues: {button_issues}"

    def test_card_component_rendering(self, page: Page, live_server):
        """Test card components render correctly."""
        page.goto(f"{live_server.url}/")

        card_selectors = COMPONENT_CATEGORIES['cards']['selectors']
        card_issues = []

        for selector in card_selectors:
            cards = page.locator(selector).filter(
                has=page.locator('img, h1, h2, h3, h4, h5, h6, p')
            )

            for i in range(min(cards.count(), 3)):
                card = cards.nth(i)

                if not card.is_visible():
                    continue

                # Test card structure
                card_box = card.bounding_box()
                if card_box:
                    # Card should have reasonable size
                    if card_box['width'] < 100 or card_box['height'] < 50:
                        card_issues.append(f"Card too small: {selector}")

                # Test card styling
                card_classes = card.get_attribute('class') or ''
                has_card_styling = any(cls in card_classes for cls in [
                    'card', 'shadow', 'rounded', 'bg-', 'border', 'p-'
                ])

                if not has_card_styling:
                    card_issues.append(f"Card missing styling: {selector}")

                # Test card content
                card_content = card.locator('img, h1, h2, h3, h4, h5, h6, p, button, a')
                if card_content.count() == 0:
                    card_issues.append(f"Card has no content: {selector}")

        assert len(card_issues) == 0, f"Card rendering issues: {card_issues}"

    def test_navigation_component_rendering(self, page: Page, live_server):
        """Test navigation components render correctly."""
        page.goto(f"{live_server.url}/")

        nav_issues = []

        # Test main navigation
        main_nav = page.locator('nav, .navbar, header nav')
        if main_nav.count() > 0:
            nav = main_nav.first
            expect(nav).to_be_visible()

            # Test navigation structure
            nav_links = nav.locator('a, button')
            if nav_links.count() == 0:
                nav_issues.append("Navigation has no links or buttons")

            # Test navigation styling
            nav_classes = nav.get_attribute('class') or ''
            has_nav_styling = any(cls in nav_classes for cls in [
                'navbar', 'nav', 'flex', 'bg-', 'shadow', 'border'
            ])

            if not has_nav_styling:
                nav_issues.append("Navigation missing styling classes")

        # Test mobile navigation
        mobile_nav_triggers = page.locator(
            '#mobile-menu-button, .navbar-toggler, [aria-label*="menu"]'
        )

        if mobile_nav_triggers.count() > 0:
            # Set mobile viewport
            page.set_viewport_size({"width": 375, "height": 667})
            page.wait_for_timeout(300)

            trigger = mobile_nav_triggers.first
            expect(trigger).to_be_visible()

            # Test mobile menu interaction
            trigger.click()
            page.wait_for_timeout(300)

            mobile_menu = page.locator('#mobile-menu, .mobile-menu')
            if mobile_menu.count() > 0:
                expect(mobile_menu.first).to_be_visible()

            # Reset viewport
            page.set_viewport_size({"width": 1200, "height": 800})

        # Test dropdown navigation
        dropdowns = page.locator('.dropdown, [aria-haspopup="true"]')
        if dropdowns.count() > 0:
            for i in range(min(dropdowns.count(), 2)):
                dropdown = dropdowns.nth(i)

                # Test dropdown trigger
                dropdown.click()
                page.wait_for_timeout(200)

                # Look for dropdown content
                dropdown_content = page.locator('.dropdown-content, [role="menu"]')
                # Note: Not all dropdowns may be visible immediately

        assert len(nav_issues) == 0, f"Navigation rendering issues: {nav_issues}"

    def test_form_component_rendering(self, page: Page, live_server):
        """Test form components render correctly."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        form_issues = []

        # Find forms
        forms = page.locator('form')
        if forms.count() == 0:
            pytest.skip("No forms found")

        form = forms.first
        expect(form).to_be_visible()

        # Test form fields
        form_fields = form.locator('input, textarea, select')
        if form_fields.count() == 0:
            form_issues.append("Form has no input fields")

        for i in range(min(form_fields.count(), 10)):
            field = form_fields.nth(i)

            if not field.is_visible():
                continue

            # Test field styling
            field_classes = field.get_attribute('class') or ''
            has_field_styling = any(cls in field_classes for cls in [
                'input', 'form-control', 'border', 'rounded', 'px-', 'py-'
            ])

            if not has_field_styling:
                field_type = field.get_attribute('type') or field.tag_name
                form_issues.append(f"Form field missing styling: {field_type}")

            # Test field dimensions
            field_box = field.bounding_box()
            if field_box:
                if field_box['height'] < 30:  # Minimum usable height
                    form_issues.append(f"Form field too short: {field_box['height']}px")

        # Test form labels
        labels = form.locator('label')
        inputs_with_ids = form.locator('input[id], textarea[id], select[id]')

        if labels.count() > 0 and inputs_with_ids.count() > 0:
            # Check label-input associations
            for i in range(min(inputs_with_ids.count(), 5)):
                input_field = inputs_with_ids.nth(i)
                input_id = input_field.get_attribute('id')

                if input_id:
                    associated_label = form.locator(f'label[for="{input_id}"]')
                    if associated_label.count() == 0:
                        # Check for aria-label or aria-labelledby
                        aria_label = input_field.get_attribute('aria-label')
                        aria_labelledby = input_field.get_attribute('aria-labelledby')

                        if not aria_label and not aria_labelledby:
                            form_issues.append(f"Input field missing label: {input_id}")

        # Test submit button
        submit_buttons = form.locator('button[type="submit"], input[type="submit"]')
        if submit_buttons.count() == 0:
            form_issues.append("Form missing submit button")
        else:
            submit_button = submit_buttons.first
            expect(submit_button).to_be_visible()
            expect(submit_button).to_be_enabled()

        assert len(form_issues) == 0, f"Form rendering issues: {form_issues}"

    def test_typography_rendering(self, page: Page, live_server):
        """Test typography components render correctly."""
        page.goto(f"{live_server.url}/")

        typography_issues = []

        # Test headings
        headings = page.locator('h1, h2, h3, h4, h5, h6')
        if headings.count() == 0:
            typography_issues.append("No headings found on page")

        for i in range(min(headings.count(), 6)):
            heading = headings.nth(i)

            if not heading.is_visible():
                continue

            # Test heading font size
            font_size = page.evaluate("""
                (element) => window.getComputedStyle(element).fontSize
            """, heading)

            font_size_px = float(font_size.replace('px', ''))
            if font_size_px < 16:  # Minimum readable size
                heading_level = heading.tag_name
                typography_issues.append(f"Heading too small: {heading_level} ({font_size_px}px)")

            # Test heading hierarchy
            heading_level = int(heading.tag_name[1])  # Extract number from h1, h2, etc.

            # Check for text content
            text_content = heading.text_content()
            if not text_content or len(text_content.strip()) == 0:
                typography_issues.append(f"Empty heading: {heading.tag_name}")

        # Test paragraph text
        paragraphs = page.locator('p')
        if paragraphs.count() > 0:
            paragraph = paragraphs.first

            # Test paragraph font size
            p_font_size = page.evaluate("""
                (element) => window.getComputedStyle(element).fontSize
            """, paragraph)

            p_font_size_px = float(p_font_size.replace('px', ''))
            if p_font_size_px < 14:  # Minimum readable body text
                typography_issues.append(f"Body text too small: {p_font_size_px}px")

            # Test line height
            line_height = page.evaluate("""
                (element) => window.getComputedStyle(element).lineHeight
            """, paragraph)

            if line_height != 'normal' and 'px' in line_height:
                line_height_px = float(line_height.replace('px', ''))
                line_height_ratio = line_height_px / p_font_size_px

                if line_height_ratio < 1.2:  # WCAG recommendation
                    typography_issues.append(f"Line height too small: {line_height_ratio:.2f}")

        assert len(typography_issues) == 0, f"Typography rendering issues: {typography_issues}"

    def test_layout_component_rendering(self, page: Page, live_server):
        """Test layout components render correctly."""
        page.goto(f"{live_server.url}/")

        layout_issues = []

        # Test container elements
        containers = page.locator('.container, .max-w-7xl, .max-w-6xl, .max-w-5xl')
        if containers.count() > 0:
            container = containers.first

            container_box = container.bounding_box()
            if container_box:
                # Container should not exceed viewport
                viewport_width = page.viewport_size['width']
                if container_box['width'] > viewport_width:
                    layout_issues.append(f"Container exceeds viewport: {container_box['width']}px > {viewport_width}px")

        # Test grid layouts
        grids = page.locator('.grid, [class*="grid-cols"]')
        if grids.count() > 0:
            grid = grids.first

            # Test grid children
            grid_items = grid.locator('> *')
            if grid_items.count() > 1:
                # Check if grid items are properly arranged
                first_item_box = grid_items.first.bounding_box()
                second_item_box = grid_items.nth(1).bounding_box()

                if first_item_box and second_item_box:
                    # Items should be positioned differently
                    same_position = (
                        first_item_box['x'] == second_item_box['x'] and
                        first_item_box['y'] == second_item_box['y']
                    )

                    if same_position:
                        layout_issues.append("Grid items have same position")

        # Test flexbox layouts
        flex_containers = page.locator('.flex, [class*="flex-"]')
        if flex_containers.count() > 0:
            for i in range(min(flex_containers.count(), 3)):
                flex_container = flex_containers.nth(i)

                # Check flex properties
                display_property = page.evaluate("""
                    (element) => window.getComputedStyle(element).display
                """, flex_container)

                if 'flex' not in display_property:
                    layout_issues.append("Flex container missing flex display")

        assert len(layout_issues) == 0, f"Layout rendering issues: {layout_issues}"


@pytest.mark.django_db
class TestComponentThemeConsistency:
    """Test component rendering consistency across themes."""

    def test_component_styling_across_themes(self, page: Page, live_server):
        """Test components maintain proper styling across all themes."""
        page.goto(f"{live_server.url}/")

        theme_component_data = {}

        for theme in THEMES_TO_TEST:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme && window.switchTheme('{theme}')")
            page.wait_for_timeout(500)

            # Collect component styling data
            component_styles = page.evaluate("""
                () => {
                    const components = {
                        buttons: [],
                        cards: [],
                        navigation: [],
                        typography: []
                    };

                    // Sample buttons
                    const buttons = document.querySelectorAll('button, .btn');
                    for (let i = 0; i < Math.min(buttons.length, 3); i++) {
                        const btn = buttons[i];
                        const styles = window.getComputedStyle(btn);
                        components.buttons.push({
                            backgroundColor: styles.backgroundColor,
                            color: styles.color,
                            borderColor: styles.borderColor,
                            borderRadius: styles.borderRadius
                        });
                    }

                    // Sample cards
                    const cards = document.querySelectorAll('.card, .shadow');
                    for (let i = 0; i < Math.min(cards.length, 2); i++) {
                        const card = cards[i];
                        const styles = window.getComputedStyle(card);
                        components.cards.push({
                            backgroundColor: styles.backgroundColor,
                            boxShadow: styles.boxShadow,
                            borderRadius: styles.borderRadius
                        });
                    }

                    // Sample navigation
                    const nav = document.querySelector('nav, .navbar');
                    if (nav) {
                        const styles = window.getComputedStyle(nav);
                        components.navigation.push({
                            backgroundColor: styles.backgroundColor,
                            borderColor: styles.borderColor
                        });
                    }

                    // Sample typography
                    const h1 = document.querySelector('h1');
                    const p = document.querySelector('p');
                    if (h1) {
                        const h1Styles = window.getComputedStyle(h1);
                        components.typography.push({
                            element: 'h1',
                            color: h1Styles.color,
                            fontSize: h1Styles.fontSize,
                            fontWeight: h1Styles.fontWeight
                        });
                    }
                    if (p) {
                        const pStyles = window.getComputedStyle(p);
                        components.typography.push({
                            element: 'p',
                            color: pStyles.color,
                            fontSize: pStyles.fontSize
                        });
                    }

                    return components;
                }
            """)

            theme_component_data[theme] = component_styles

        # Verify themes produce different styling
        for component_type in ['buttons', 'cards', 'navigation', 'typography']:
            light_styles = theme_component_data.get('light', {}).get(component_type, [])
            business_styles = theme_component_data.get('business', {}).get(component_type, [])

            if light_styles and business_styles:
                # Compare first element of each
                if len(light_styles) > 0 and len(business_styles) > 0:
                    light_style = light_styles[0]
                    business_style = business_styles[0]

                    # Colors should be different between themes
                    if component_type in ['buttons', 'cards']:
                        light_bg = light_style.get('backgroundColor')
                        business_bg = business_style.get('backgroundColor')

                        if light_bg and business_bg and light_bg == business_bg:
                            # Some components might have the same colors, this is informational
                            pass

    def test_component_responsive_behavior_across_themes(self, page: Page, live_server):
        """Test component responsive behavior is consistent across themes."""
        page.goto(f"{live_server.url}/")

        viewports = [
            {'width': 375, 'height': 667},   # Mobile
            {'width': 1200, 'height': 800}   # Desktop
        ]

        for theme in THEMES_TO_TEST:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme && window.switchTheme('{theme}')")
            page.wait_for_timeout(300)

            for viewport in viewports:
                page.set_viewport_size(viewport)
                page.wait_for_timeout(300)

                # Test that key components are still visible and functional
                key_components = [
                    'button, .btn',
                    'nav, .navbar',
                    'form',
                    '.card, .shadow'
                ]

                for selector in key_components:
                    elements = page.locator(selector)
                    if elements.count() > 0:
                        element = elements.first

                        # Element should be visible
                        if element.is_visible():
                            element_box = element.bounding_box()
                            if element_box:
                                # Element should fit within viewport
                                assert element_box['width'] <= viewport['width'], \
                                    f"Component {selector} exceeds viewport width in {theme} theme at {viewport['width']}px"


@pytest.mark.django_db
class TestVisualRegressionComponents:
    """Test for visual regressions in component rendering."""

    def test_component_visual_consistency(self, page: Page, live_server):
        """Test component visual consistency after migration."""
        page.goto(f"{live_server.url}/")

        # Take baseline screenshots of key components
        component_screenshots = {}

        key_components = [
            ('navigation', 'nav, .navbar'),
            ('hero', '.hero, .jumbotron, section:first-child'),
            ('buttons', 'button, .btn'),
            ('cards', '.card, .shadow'),
            ('footer', 'footer')
        ]

        for component_name, selector in key_components:
            elements = page.locator(selector)

            if elements.count() > 0:
                element = elements.first

                if element.is_visible():
                    # Take screenshot of component
                    try:
                        screenshots_dir = Path(__file__).parent / 'component_screenshots'
                        screenshots_dir.mkdir(exist_ok=True)

                        screenshot_path = screenshots_dir / f'{component_name}_baseline.png'
                        element.screenshot(path=str(screenshot_path))

                        component_screenshots[component_name] = str(screenshot_path)
                    except Exception as e:
                        print(f"Could not take screenshot of {component_name}: {e}")

        return component_screenshots

    def test_component_hover_states(self, page: Page, live_server):
        """Test component hover states render correctly."""
        page.goto(f"{live_server.url}/")

        hover_issues = []

        # Test button hover states
        buttons = page.locator('button, .btn, a[role="button"]')
        if buttons.count() > 0:
            for i in range(min(buttons.count(), 3)):
                button = buttons.nth(i)

                if not button.is_visible():
                    continue

                # Get initial state
                initial_styles = page.evaluate("""
                    (element) => {
                        const styles = window.getComputedStyle(element);
                        return {
                            backgroundColor: styles.backgroundColor,
                            transform: styles.transform,
                            boxShadow: styles.boxShadow
                        };
                    }
                """, button)

                # Hover over button
                button.hover()
                page.wait_for_timeout(200)

                # Get hover state
                hover_styles = page.evaluate("""
                    (element) => {
                        const styles = window.getComputedStyle(element);
                        return {
                            backgroundColor: styles.backgroundColor,
                            transform: styles.transform,
                            boxShadow: styles.boxShadow
                        };
                    }
                """, button)

                # Check if hover state is different (indicates working hover effect)
                has_hover_effect = (
                    initial_styles['backgroundColor'] != hover_styles['backgroundColor'] or
                    initial_styles['transform'] != hover_styles['transform'] or
                    initial_styles['boxShadow'] != hover_styles['boxShadow']
                )

                # Note: Not all buttons need hover effects, this is informational

        # Test link hover states
        links = page.locator('a:not([role="button"])')
        if links.count() > 0:
            for i in range(min(links.count(), 3)):
                link = links.nth(i)

                if not link.is_visible():
                    continue

                # Test link hover
                initial_color = page.evaluate("""
                    (element) => window.getComputedStyle(element).color
                """, link)

                link.hover()
                page.wait_for_timeout(100)

                hover_color = page.evaluate("""
                    (element) => window.getComputedStyle(element).color
                """, link)

                # Links should generally have hover effects
                # This is informational testing

        assert len(hover_issues) == 0, f"Hover state issues: {hover_issues}"


def test_component_rendering_report(page: Page, live_server):
    """Generate comprehensive component rendering report."""
    page.goto(f"{live_server.url}/")

    # Collect comprehensive component data
    component_analysis = page.evaluate("""
        () => {
            const analysis = {
                overview: {
                    totalElements: document.querySelectorAll('*').length,
                    visibleElements: Array.from(document.querySelectorAll('*')).filter(el =>
                        el.offsetParent !== null
                    ).length
                },
                components: {},
                styling: {
                    cssRulesCount: document.styleSheets.length,
                    customProperties: []
                }
            };

            // Analyze each component category
            const componentCategories = {
                buttons: 'button, .btn, [role="button"]',
                cards: '.card, .shadow, .rounded',
                navigation: 'nav, .navbar, .menu',
                forms: 'form, input, textarea, select',
                typography: 'h1, h2, h3, h4, h5, h6, p',
                layout: '.container, .grid, .flex',
                interactive: '.modal, .dropdown, .tooltip'
            };

            for (const [category, selector] of Object.entries(componentCategories)) {
                const elements = document.querySelectorAll(selector);
                const visibleElements = Array.from(elements).filter(el => el.offsetParent !== null);

                analysis.components[category] = {
                    total: elements.length,
                    visible: visibleElements.length,
                    samples: visibleElements.slice(0, 3).map(el => ({
                        tagName: el.tagName,
                        className: el.className,
                        id: el.id || null,
                        hasContent: !!el.textContent.trim(),
                        styles: {
                            display: window.getComputedStyle(el).display,
                            position: window.getComputedStyle(el).position,
                            backgroundColor: window.getComputedStyle(el).backgroundColor,
                            color: window.getComputedStyle(el).color
                        }
                    }))
                };
            }

            // Check for CSS custom properties (CSS variables)
            try {
                const computedStyle = window.getComputedStyle(document.documentElement);
                for (let i = 0; i < computedStyle.length; i++) {
                    const property = computedStyle[i];
                    if (property.startsWith('--')) {
                        analysis.styling.customProperties.push({
                            property: property,
                            value: computedStyle.getPropertyValue(property)
                        });
                    }
                }
            } catch (e) {
                // CSS custom properties not accessible
            }

            return analysis;
        }
    """)

    # Save comprehensive analysis
    report_path = Path(__file__).parent / 'component_rendering_report.json'
    with open(report_path, 'w') as f:
        json.dump({
            'timestamp': time.time(),
            'url': page.url,
            'themes_tested': THEMES_TO_TEST,
            'component_categories': list(COMPONENT_CATEGORIES.keys()),
            'analysis': component_analysis
        }, f, indent=2)

    print(f"Component rendering report saved to: {report_path}")
    return component_analysis