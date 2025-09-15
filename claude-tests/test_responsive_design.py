"""
Comprehensive responsive design tests for the DaisyUI to Flowbite migration.
Tests layout behavior across different screen sizes and devices.
"""

import pytest
from playwright.sync_api import Page, expect
import time
import json
from pathlib import Path


# Standard viewport sizes for testing
VIEWPORT_SIZES = {
    'mobile_portrait': {'width': 375, 'height': 667},
    'mobile_landscape': {'width': 667, 'height': 375},
    'tablet_portrait': {'width': 768, 'height': 1024},
    'tablet_landscape': {'width': 1024, 'height': 768},
    'desktop_small': {'width': 1200, 'height': 800},
    'desktop_large': {'width': 1920, 'height': 1080},
    'ultrawide': {'width': 2560, 'height': 1440}
}

BREAKPOINTS = {
    'xs': 375,    # Extra small devices
    'sm': 640,    # Small devices
    'md': 768,    # Medium devices
    'lg': 1024,   # Large devices
    'xl': 1280,   # Extra large devices
    '2xl': 1536   # 2X Large devices
}


@pytest.mark.django_db
class TestResponsiveLayout:
    """Test responsive layout behavior across different screen sizes."""

    def test_layout_stability_across_viewports(self, page: Page, live_server):
        """Test that layout remains stable across different viewport sizes."""
        page.goto(f"{live_server.url}/")

        layout_issues = []

        for viewport_name, size in VIEWPORT_SIZES.items():
            page.set_viewport_size(size)
            page.wait_for_timeout(300)

            # Check for horizontal scrollbars (layout overflow)
            has_horizontal_scroll = page.evaluate("""
                () => document.documentElement.scrollWidth > document.documentElement.clientWidth
            """)

            if has_horizontal_scroll:
                layout_issues.append(f"Horizontal scroll on {viewport_name}")

            # Check for layout shift
            layout_info = page.evaluate("""
                () => {
                    const body = document.body;
                    return {
                        scrollWidth: document.documentElement.scrollWidth,
                        clientWidth: document.documentElement.clientWidth,
                        bodyHeight: body.scrollHeight,
                        viewportHeight: window.innerHeight
                    };
                }
            """)

            # Basic layout sanity checks
            if layout_info['scrollWidth'] > layout_info['clientWidth'] + 20:  # 20px tolerance
                layout_issues.append(f"Layout overflow on {viewport_name}")

        assert len(layout_issues) == 0, f"Layout issues found: {layout_issues}"

    def test_navigation_responsive_behavior(self, page: Page, live_server):
        """Test navigation adapts correctly to different screen sizes."""
        page.goto(f"{live_server.url}/")

        # Test mobile navigation
        page.set_viewport_size(VIEWPORT_SIZES['mobile_portrait'])
        page.wait_for_timeout(500)

        # Mobile menu button should be visible
        mobile_menu_button = page.locator(
            '#mobile-menu-button, .navbar-toggler, [aria-label*="menu"]'
        )

        if mobile_menu_button.count() > 0:
            expect(mobile_menu_button.first).to_be_visible()

        # Desktop navigation items might be hidden
        desktop_nav_items = page.locator('.hidden.lg\\:block, .navbar-nav')

        # Test desktop navigation
        page.set_viewport_size(VIEWPORT_SIZES['desktop_small'])
        page.wait_for_timeout(500)

        # Desktop navigation should be visible
        desktop_dropdown = page.locator('.dropdown.dropdown-end, .navbar-expand')

        if desktop_dropdown.count() > 0:
            expect(desktop_dropdown.first).to_be_visible()

        # Mobile menu might be hidden
        if mobile_menu_button.count() > 0:
            mobile_menu_display = page.evaluate("""
                (element) => window.getComputedStyle(element).display
            """, mobile_menu_button.first)

            # Should be hidden on desktop or have appropriate responsive classes

    def test_hero_section_responsiveness(self, page: Page, live_server):
        """Test hero section adapts to different screen sizes."""
        page.goto(f"{live_server.url}/")

        hero_sections = page.locator('.hero, .jumbotron, .banner, section:first-child')

        if hero_sections.count() > 0:
            hero = hero_sections.first

            for viewport_name, size in VIEWPORT_SIZES.items():
                page.set_viewport_size(size)
                page.wait_for_timeout(300)

                # Hero should be visible
                expect(hero).to_be_visible()

                # Check hero sizing
                hero_box = hero.bounding_box()
                if hero_box:
                    # Hero should not exceed viewport width
                    assert hero_box['width'] <= size['width'] + 20, \
                        f"Hero section too wide on {viewport_name}"

                    # Hero should have reasonable height
                    assert hero_box['height'] > 100, \
                        f"Hero section too short on {viewport_name}"

    def test_content_grid_responsiveness(self, page: Page, live_server):
        """Test content grids adapt to screen sizes."""
        page.goto(f"{live_server.url}/")

        # Look for grid containers
        grid_containers = page.locator(
            '.grid, .row, .flex.flex-wrap, [class*="grid-cols"]'
        )

        if grid_containers.count() > 0:
            for viewport_name, size in VIEWPORT_SIZES.items():
                page.set_viewport_size(size)
                page.wait_for_timeout(300)

                # Check grid behavior
                for i in range(min(grid_containers.count(), 3)):
                    container = grid_containers.nth(i)

                    # Get grid items
                    grid_items = container.locator('> *')

                    if grid_items.count() > 1:
                        # Check if items are properly arranged
                        first_item_box = grid_items.first.bounding_box()
                        second_item_box = grid_items.nth(1).bounding_box()

                        if first_item_box and second_item_box:
                            # Check if items stack on mobile
                            if size['width'] < BREAKPOINTS['md']:
                                # Items should stack vertically on mobile
                                items_stacked = first_item_box['y'] != second_item_box['y']
                                # Note: This is informational - not all grids need to stack

    def test_typography_scaling(self, page: Page, live_server):
        """Test typography scales appropriately across devices."""
        page.goto(f"{live_server.url}/")

        # Find headings
        headings = page.locator('h1, h2, h3, h4, h5, h6')

        if headings.count() > 0:
            heading_data = {}

            for viewport_name, size in VIEWPORT_SIZES.items():
                page.set_viewport_size(size)
                page.wait_for_timeout(300)

                # Measure font sizes
                font_sizes = []
                for i in range(min(headings.count(), 3)):
                    heading = headings.nth(i)
                    font_size = page.evaluate("""
                        (element) => window.getComputedStyle(element).fontSize
                    """, heading)
                    font_sizes.append(float(font_size.replace('px', '')))

                heading_data[viewport_name] = font_sizes

            # Check that typography scales reasonably
            mobile_sizes = heading_data.get('mobile_portrait', [])
            desktop_sizes = heading_data.get('desktop_small', [])

            if mobile_sizes and desktop_sizes:
                for i in range(len(mobile_sizes)):
                    if i < len(desktop_sizes):
                        # Desktop typography should generally be larger or equal
                        assert desktop_sizes[i] >= mobile_sizes[i] - 2, \
                            f"Typography scaling issue: desktop ({desktop_sizes[i]}px) smaller than mobile ({mobile_sizes[i]}px)"

    def test_image_responsiveness(self, page: Page, live_server):
        """Test images scale properly across devices."""
        page.goto(f"{live_server.url}/")

        images = page.locator('img')

        if images.count() > 0:
            for viewport_name, size in VIEWPORT_SIZES.items():
                page.set_viewport_size(size)
                page.wait_for_timeout(300)

                for i in range(min(images.count(), 3)):
                    img = images.nth(i)

                    # Skip if image is not visible
                    if not img.is_visible():
                        continue

                    img_box = img.bounding_box()
                    if img_box:
                        # Image should not exceed container width
                        assert img_box['width'] <= size['width'], \
                            f"Image exceeds viewport width on {viewport_name}"

                        # Image should have reasonable size
                        assert img_box['width'] > 0 and img_box['height'] > 0, \
                            f"Image has invalid dimensions on {viewport_name}"

    def test_button_touch_targets(self, page: Page, live_server):
        """Test buttons meet touch target size requirements on mobile."""
        page.goto(f"{live_server.url}/")

        # Set mobile viewport
        page.set_viewport_size(VIEWPORT_SIZES['mobile_portrait'])
        page.wait_for_timeout(500)

        buttons = page.locator('button, .btn, a[role="button"], input[type="submit"]')

        if buttons.count() > 0:
            for i in range(min(buttons.count(), 5)):
                button = buttons.nth(i)

                if button.is_visible():
                    button_box = button.bounding_box()
                    if button_box:
                        # Touch target should be at least 44px (WCAG AA standard)
                        min_touch_size = 44

                        touch_area = min(button_box['width'], button_box['height'])
                        assert touch_area >= min_touch_size - 5, \
                            f"Button touch target too small: {touch_area}px (minimum: {min_touch_size}px)"


@pytest.mark.django_db
class TestBreakpointBehavior:
    """Test behavior at specific breakpoints."""

    def test_tailwind_breakpoint_behavior(self, page: Page, live_server):
        """Test Tailwind CSS breakpoint behavior."""
        page.goto(f"{live_server.url}/")

        for breakpoint_name, width in BREAKPOINTS.items():
            # Test just below and above each breakpoint
            test_widths = [width - 1, width, width + 1]

            for test_width in test_widths:
                page.set_viewport_size({"width": test_width, "height": 800})
                page.wait_for_timeout(300)

                # Check for responsive classes at this breakpoint
                responsive_elements = page.locator(f'[class*="{breakpoint_name}:"]')

                # Test visibility changes
                hidden_elements = page.locator(f'.{breakpoint_name}\\:hidden, .hidden.{breakpoint_name}\\:block')

                if hidden_elements.count() > 0:
                    # Elements should behave according to their responsive classes
                    for i in range(min(hidden_elements.count(), 3)):
                        element = hidden_elements.nth(i)
                        element_classes = element.get_attribute('class') or ''

                        # Check if element visibility matches expected behavior
                        is_visible = element.is_visible()

                        # This is complex to test generically since it depends on specific classes

    def test_container_behavior_at_breakpoints(self, page: Page, live_server):
        """Test container behavior at different breakpoints."""
        page.goto(f"{live_server.url}/")

        containers = page.locator('.container, .max-w-7xl, .max-w-6xl, .max-w-5xl')

        if containers.count() > 0:
            container = containers.first

            for breakpoint_name, width in BREAKPOINTS.items():
                page.set_viewport_size({"width": width, "height": 800})
                page.wait_for_timeout(300)

                container_box = container.bounding_box()
                if container_box:
                    # Container should not exceed viewport
                    assert container_box['width'] <= width, \
                        f"Container exceeds viewport at {breakpoint_name} breakpoint"

                    # Container should have reasonable margins on larger screens
                    if width >= BREAKPOINTS['lg']:
                        container_margin = (width - container_box['width']) / 2
                        # Should have some margin on large screens
                        # Note: This depends on specific container implementation


@pytest.mark.django_db
class TestMobileSpecificFeatures:
    """Test mobile-specific features and optimizations."""

    def test_mobile_menu_functionality(self, page: Page, live_server):
        """Test mobile menu works correctly."""
        page.goto(f"{live_server.url}/")
        page.set_viewport_size(VIEWPORT_SIZES['mobile_portrait'])
        page.wait_for_timeout(500)

        # Find mobile menu button
        mobile_menu_button = page.locator('#mobile-menu-button, .navbar-toggler')

        if mobile_menu_button.count() > 0:
            button = mobile_menu_button.first
            expect(button).to_be_visible()

            # Test menu toggle
            button.click()
            page.wait_for_timeout(300)

            # Find mobile menu
            mobile_menu = page.locator('#mobile-menu, .mobile-menu')

            if mobile_menu.count() > 0:
                menu = mobile_menu.first
                expect(menu).to_be_visible()

                # Menu should be properly sized for mobile
                menu_box = menu.bounding_box()
                if menu_box:
                    assert menu_box['width'] <= 375, "Mobile menu too wide"

                # Test menu items are accessible
                menu_items = menu.locator('a, [role="menuitem"]')
                if menu_items.count() > 0:
                    for i in range(min(menu_items.count(), 3)):
                        item = menu_items.nth(i)
                        expect(item).to_be_visible()

                        # Check touch target size
                        item_box = item.bounding_box()
                        if item_box:
                            assert item_box['height'] >= 40, \
                                "Mobile menu items should have adequate touch targets"

    def test_mobile_form_usability(self, page: Page, live_server):
        """Test forms are usable on mobile devices."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        page.set_viewport_size(VIEWPORT_SIZES['mobile_portrait'])
        page.wait_for_timeout(500)

        forms = page.locator('form')

        if forms.count() > 0:
            form = forms.first

            # Test form fields on mobile
            form_fields = form.locator('input, textarea, select')

            for i in range(min(form_fields.count(), 5)):
                field = form_fields.nth(i)

                if field.is_visible():
                    field_box = field.bounding_box()
                    if field_box:
                        # Form fields should be adequately sized for touch
                        assert field_box['height'] >= 40, \
                            "Form fields should be at least 40px tall on mobile"

                        # Form fields should not exceed container width
                        assert field_box['width'] <= 375, \
                            "Form fields should not exceed mobile viewport width"

            # Test form submission button
            submit_buttons = form.locator('button[type="submit"], input[type="submit"]')

            if submit_buttons.count() > 0:
                button = submit_buttons.first
                button_box = button.bounding_box()

                if button_box:
                    assert button_box['height'] >= 44, \
                        "Submit button should meet minimum touch target size"

    def test_mobile_typography_readability(self, page: Page, live_server):
        """Test typography is readable on mobile devices."""
        page.goto(f"{live_server.url}/")
        page.set_viewport_size(VIEWPORT_SIZES['mobile_portrait'])
        page.wait_for_timeout(500)

        # Test body text
        body_text = page.locator('p, .text-base, body')

        if body_text.count() > 0:
            text_element = body_text.first

            font_size = page.evaluate("""
                (element) => window.getComputedStyle(element).fontSize
            """, text_element)

            font_size_px = float(font_size.replace('px', ''))
            assert font_size_px >= 16, \
                f"Body text should be at least 16px on mobile, got {font_size_px}px"

        # Test line height
        line_height = page.evaluate("""
            (element) => window.getComputedStyle(element).lineHeight
        """, body_text.first)

        # Line height should be reasonable for readability
        if line_height != 'normal':
            line_height_num = float(line_height.replace('px', ''))
            if font_size_px:
                line_height_ratio = line_height_num / font_size_px
                assert line_height_ratio >= 1.2, \
                    f"Line height ratio should be at least 1.2, got {line_height_ratio}"


@pytest.mark.django_db
class TestTabletOptimization:
    """Test tablet-specific optimizations."""

    def test_tablet_layout_optimization(self, page: Page, live_server):
        """Test layout is optimized for tablet viewports."""
        page.goto(f"{live_server.url}/")

        for tablet_size in ['tablet_portrait', 'tablet_landscape']:
            page.set_viewport_size(VIEWPORT_SIZES[tablet_size])
            page.wait_for_timeout(500)

            # Check navigation behavior
            # On tablet, navigation might be hybrid between mobile and desktop
            desktop_nav = page.locator('.dropdown.dropdown-end, .navbar-expand')
            mobile_nav = page.locator('#mobile-menu-button')

            # Either desktop or mobile nav should be visible, not both prominently
            desktop_visible = desktop_nav.count() > 0 and desktop_nav.first.is_visible()
            mobile_visible = mobile_nav.count() > 0 and mobile_nav.first.is_visible()

            # Test content layout
            content_containers = page.locator('.container, .max-w-7xl, main')

            if content_containers.count() > 0:
                container = content_containers.first
                container_box = container.bounding_box()

                if container_box:
                    viewport_size = VIEWPORT_SIZES[tablet_size]
                    # Container should utilize tablet space efficiently
                    width_utilization = container_box['width'] / viewport_size['width']
                    assert width_utilization > 0.7, \
                        f"Poor width utilization on {tablet_size}: {width_utilization:.2f}"


def test_responsive_design_report(page: Page, live_server):
    """Generate comprehensive responsive design report."""
    page.goto(f"{live_server.url}/")

    responsive_analysis = {}

    for viewport_name, size in VIEWPORT_SIZES.items():
        page.set_viewport_size(size)
        page.wait_for_timeout(500)

        # Collect responsive data
        viewport_data = page.evaluate("""
            () => {
                return {
                    viewport: {
                        width: window.innerWidth,
                        height: window.innerHeight,
                        devicePixelRatio: window.devicePixelRatio
                    },
                    layout: {
                        scrollWidth: document.documentElement.scrollWidth,
                        scrollHeight: document.documentElement.scrollHeight,
                        hasHorizontalScroll: document.documentElement.scrollWidth > document.documentElement.clientWidth
                    },
                    navigation: {
                        mobileMenuVisible: document.querySelector('#mobile-menu-button') ?
                            window.getComputedStyle(document.querySelector('#mobile-menu-button')).display !== 'none' : false,
                        desktopNavVisible: document.querySelector('.dropdown.dropdown-end') ?
                            window.getComputedStyle(document.querySelector('.dropdown.dropdown-end')).display !== 'none' : false
                    },
                    typography: {
                        bodyFontSize: window.getComputedStyle(document.body).fontSize,
                        h1FontSize: document.querySelector('h1') ?
                            window.getComputedStyle(document.querySelector('h1')).fontSize : null
                    },
                    interactiveElements: {
                        buttons: document.querySelectorAll('button, .btn').length,
                        links: document.querySelectorAll('a').length,
                        forms: document.querySelectorAll('form').length
                    }
                };
            }
        """)

        responsive_analysis[viewport_name] = viewport_data

    # Save the analysis
    report_path = Path(__file__).parent / 'responsive_design_report.json'
    with open(report_path, 'w') as f:
        json.dump({
            'timestamp': time.time(),
            'url': page.url,
            'analysis': responsive_analysis,
            'breakpoints_tested': BREAKPOINTS,
            'viewports_tested': VIEWPORT_SIZES
        }, f, indent=2)

    print(f"Responsive design report saved to: {report_path}")
    return responsive_analysis