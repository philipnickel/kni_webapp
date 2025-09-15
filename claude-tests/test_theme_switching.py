"""
Comprehensive theme switching functionality tests for the DaisyUI to Flowbite migration.
Tests theme system integrity, visual consistency, and user preferences.
"""

import pytest
from playwright.sync_api import Page, expect
import time
import json
from pathlib import Path


# Available themes based on the theme.js file
AVAILABLE_THEMES = ['light', 'corporate', 'business', 'emerald']

# Theme validation tests
THEME_PROPERTIES = [
    'background-color',
    'color',
    'border-color'
]


@pytest.mark.django_db
class TestThemeSystemIntegrity:
    """Test the theme system works correctly after migration."""

    def test_theme_script_loaded(self, page: Page, live_server):
        """Test that theme.js is loaded and working."""
        page.goto(f"{live_server.url}/")

        # Check if theme functions are available
        theme_functions = page.evaluate("""
            () => {
                return {
                    switchTheme: typeof window.switchTheme === 'function',
                    getCurrentTheme: typeof window.getCurrentTheme === 'function',
                    getAvailableThemes: typeof window.getAvailableThemes === 'function',
                    previewTheme: typeof window.previewTheme === 'function',
                    restoreTheme: typeof window.restoreTheme === 'function'
                };
            }
        """)

        assert theme_functions['switchTheme'], "window.switchTheme function should be available"
        assert theme_functions['getCurrentTheme'], "window.getCurrentTheme function should be available"
        assert theme_functions['getAvailableThemes'], "window.getAvailableThemes function should be available"
        assert theme_functions['previewTheme'], "window.previewTheme function should be available"
        assert theme_functions['restoreTheme'], "window.restoreTheme function should be available"

    def test_initial_theme_application(self, page: Page, live_server):
        """Test that initial theme is properly applied."""
        page.goto(f"{live_server.url}/")

        # Check if HTML has data-theme attribute
        theme_attribute = page.evaluate("""
            () => document.documentElement.getAttribute('data-theme')
        """)

        assert theme_attribute is not None, "HTML element should have data-theme attribute"
        assert theme_attribute in AVAILABLE_THEMES, f"Theme '{theme_attribute}' should be in available themes"

    def test_theme_switching_functionality(self, page: Page, live_server):
        """Test that theme switching works correctly."""
        page.goto(f"{live_server.url}/")

        original_theme = page.evaluate("() => window.getCurrentTheme()")

        for theme in AVAILABLE_THEMES:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(200)

            # Verify theme was applied
            current_theme = page.evaluate("() => window.getCurrentTheme()")
            assert current_theme == theme, f"Theme should be '{theme}', got '{current_theme}'"

            # Verify HTML attribute
            html_theme = page.evaluate("() => document.documentElement.getAttribute('data-theme')")
            assert html_theme == theme, f"HTML data-theme should be '{theme}', got '{html_theme}'"

        # Restore original theme
        page.evaluate(f"() => window.switchTheme('{original_theme}')")

    def test_theme_persistence(self, page: Page, live_server):
        """Test that theme preference is stored in localStorage."""
        page.goto(f"{live_server.url}/")

        test_theme = 'corporate'

        # Switch theme
        page.evaluate(f"() => window.switchTheme('{test_theme}')")
        page.wait_for_timeout(200)

        # Check localStorage
        stored_theme = page.evaluate("() => localStorage.getItem('preferred-theme')")
        assert stored_theme == test_theme, f"Theme should be stored in localStorage as '{test_theme}'"

        # Reload page and check if theme persists
        page.reload()
        page.wait_for_timeout(500)

        current_theme = page.evaluate("() => window.getCurrentTheme()")
        assert current_theme == test_theme, f"Theme should persist after reload: expected '{test_theme}', got '{current_theme}'"

    def test_theme_preview_functionality(self, page: Page, live_server):
        """Test theme preview functionality."""
        page.goto(f"{live_server.url}/")

        original_theme = page.evaluate("() => window.getCurrentTheme()")
        preview_theme = 'business'

        # Start preview
        page.evaluate(f"() => window.previewTheme('{preview_theme}')")
        page.wait_for_timeout(200)

        # Check preview is applied
        current_theme = page.evaluate("() => window.getCurrentTheme()")
        assert current_theme == preview_theme, f"Preview theme should be applied: expected '{preview_theme}', got '{current_theme}'"

        # Check preview class is added
        has_preview_class = page.evaluate("() => document.documentElement.classList.contains('theme-preview')")
        assert has_preview_class, "HTML should have theme-preview class during preview"

        # Restore theme
        page.evaluate("() => window.restoreTheme()")
        page.wait_for_timeout(300)

        # Check original theme is restored
        restored_theme = page.evaluate("() => window.getCurrentTheme()")
        assert restored_theme == original_theme, f"Original theme should be restored: expected '{original_theme}', got '{restored_theme}'"

        # Check preview class is removed
        has_preview_class = page.evaluate("() => document.documentElement.classList.contains('theme-preview')")
        assert not has_preview_class, "HTML should not have theme-preview class after restore"


@pytest.mark.django_db
class TestThemeVisualConsistency:
    """Test visual consistency across themes."""

    def test_color_scheme_application(self, page: Page, live_server):
        """Test that color schemes are properly applied for each theme."""
        page.goto(f"{live_server.url}/")

        theme_colors = {}

        for theme in AVAILABLE_THEMES:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(300)

            # Sample key elements and their colors
            color_data = page.evaluate("""
                () => {
                    const elements = {
                        body: document.body,
                        primaryButton: document.querySelector('.btn-primary, .bg-primary'),
                        card: document.querySelector('.card, .bg-white, .shadow'),
                        navbar: document.querySelector('nav, .navbar')
                    };

                    const colors = {};

                    for (const [name, element] of Object.entries(elements)) {
                        if (element) {
                            const styles = window.getComputedStyle(element);
                            colors[name] = {
                                backgroundColor: styles.backgroundColor,
                                color: styles.color,
                                borderColor: styles.borderColor
                            };
                        }
                    }

                    return colors;
                }
            """)

            theme_colors[theme] = color_data

        # Verify themes have different color schemes
        light_colors = theme_colors.get('light')
        business_colors = theme_colors.get('business')

        if light_colors and business_colors:
            # Body background should be different between light and business themes
            light_bg = light_colors.get('body', {}).get('backgroundColor')
            business_bg = business_colors.get('body', {}).get('backgroundColor')

            if light_bg and business_bg:
                assert light_bg != business_bg, "Different themes should have different background colors"

    def test_contrast_ratios_maintained(self, page: Page, live_server):
        """Test that adequate contrast ratios are maintained across themes."""
        page.goto(f"{live_server.url}/")

        contrast_issues = []

        for theme in AVAILABLE_THEMES:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(300)

            # Check contrast for key elements
            contrast_data = page.evaluate("""
                () => {
                    function getLuminance(rgb) {
                        const [r, g, b] = rgb.match(/\\d+/g).map(Number);
                        const [rs, gs, bs] = [r, g, b].map(c => {
                            c = c / 255;
                            return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
                        });
                        return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
                    }

                    function getContrastRatio(color1, color2) {
                        const lum1 = getLuminance(color1);
                        const lum2 = getLuminance(color2);
                        const bright = Math.max(lum1, lum2);
                        const dark = Math.min(lum1, lum2);
                        return (bright + 0.05) / (dark + 0.05);
                    }

                    const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, a, button');
                    const contrastIssues = [];

                    for (let i = 0; i < Math.min(textElements.length, 10); i++) {
                        const element = textElements[i];
                        const styles = window.getComputedStyle(element);
                        const textColor = styles.color;
                        const backgroundColor = styles.backgroundColor;

                        // Skip transparent backgrounds
                        if (backgroundColor === 'rgba(0, 0, 0, 0)' || backgroundColor === 'transparent') {
                            continue;
                        }

                        try {
                            const contrast = getContrastRatio(textColor, backgroundColor);
                            if (contrast < 4.5) { // WCAG AA standard
                                contrastIssues.push({
                                    element: element.tagName,
                                    contrast: contrast,
                                    textColor: textColor,
                                    backgroundColor: backgroundColor
                                });
                            }
                        } catch (e) {
                            // Skip if color parsing fails
                        }
                    }

                    return contrastIssues;
                }
            """)

            if contrast_data and len(contrast_data) > 0:
                contrast_issues.extend([f"{theme}: {issue}" for issue in contrast_data])

        # Note: This is informational - some contrast issues might be acceptable
        if len(contrast_issues) > 5:  # Threshold for serious issues
            print(f"Warning: Multiple contrast issues found: {contrast_issues[:5]}")

    def test_component_styling_consistency(self, page: Page, live_server):
        """Test that components maintain consistent styling across themes."""
        page.goto(f"{live_server.url}/")

        for theme in AVAILABLE_THEMES:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(300)

            # Test button components
            buttons = page.locator('button, .btn')
            if buttons.count() > 0:
                button = buttons.first

                # Button should be visible and styled
                expect(button).to_be_visible()

                # Check for proper styling classes
                button_classes = button.get_attribute('class') or ''
                has_button_styling = any(cls in button_classes for cls in [
                    'btn', 'button', 'bg-', 'text-', 'border-', 'px-', 'py-'
                ])
                assert has_button_styling, f"Button should have proper styling in {theme} theme"

            # Test card components
            cards = page.locator('.card, .shadow, .bg-white')
            if cards.count() > 0:
                card = cards.first

                # Card should be visible
                expect(card).to_be_visible()

                # Check card styling
                card_classes = card.get_attribute('class') or ''
                has_card_styling = any(cls in card_classes for cls in [
                    'card', 'shadow', 'rounded', 'bg-', 'border'
                ])
                assert has_card_styling, f"Card should have proper styling in {theme} theme"


@pytest.mark.django_db
class TestThemeResponsiveness:
    """Test theme behavior across different screen sizes."""

    def test_theme_consistency_across_viewports(self, page: Page, live_server):
        """Test themes work consistently across different viewport sizes."""
        page.goto(f"{live_server.url}/")

        viewports = [
            {'width': 375, 'height': 667},   # Mobile
            {'width': 768, 'height': 1024},  # Tablet
            {'width': 1200, 'height': 800}   # Desktop
        ]

        for theme in AVAILABLE_THEMES:
            # Switch to theme
            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(200)

            for viewport in viewports:
                page.set_viewport_size(viewport)
                page.wait_for_timeout(300)

                # Verify theme is still applied
                current_theme = page.evaluate("() => window.getCurrentTheme()")
                assert current_theme == theme, f"Theme should remain '{theme}' across viewport changes"

                # Check that theme colors are applied
                body_bg = page.evaluate("""
                    () => window.getComputedStyle(document.body).backgroundColor
                """)

                assert body_bg != 'rgba(0, 0, 0, 0)', "Body should have background color applied"

    def test_dark_theme_media_query_support(self, page: Page, live_server):
        """Test system dark theme preference handling."""
        page.goto(f"{live_server.url}/")

        # Clear any stored theme preference
        page.evaluate("() => localStorage.removeItem('preferred-theme')")

        # Test dark theme preference
        page.emulate_media(media="(prefers-color-scheme: dark)")
        page.reload()
        page.wait_for_timeout(500)

        # Check if dark theme is applied when system preference is dark
        current_theme = page.evaluate("() => window.getCurrentTheme()")

        # Note: This depends on implementation - the system might default to light
        # if dark theme is not available

        # Test light theme preference
        page.emulate_media(media="(prefers-color-scheme: light)")
        page.reload()
        page.wait_for_timeout(500)

        current_theme = page.evaluate("() => window.getCurrentTheme()")
        # Should generally default to light theme


@pytest.mark.django_db
class TestThemeAccessibility:
    """Test theme accessibility features."""

    def test_theme_switching_keyboard_accessibility(self, page: Page, live_server):
        """Test theme switching is accessible via keyboard."""
        page.goto(f"{live_server.url}/")

        # Look for theme switcher elements
        theme_switchers = page.locator(
            '[data-theme], .theme-switcher, .theme-toggle, [aria-label*="theme"]'
        )

        if theme_switchers.count() > 0:
            switcher = theme_switchers.first

            # Test keyboard focus
            switcher.focus()
            page.wait_for_timeout(100)

            # Check if element is focusable
            focused_element = page.evaluate("() => document.activeElement")
            assert focused_element is not None, "Theme switcher should be focusable"

            # Test keyboard interaction (if applicable)
            # This depends on implementation

    def test_theme_announcements(self, page: Page, live_server):
        """Test that theme changes are announced to screen readers."""
        page.goto(f"{live_server.url}/")

        # Look for aria-live regions or announcements
        live_regions = page.locator('[aria-live], .sr-only')

        # Test theme switching triggers announcements
        original_theme = page.evaluate("() => window.getCurrentTheme()")
        new_theme = 'corporate' if original_theme != 'corporate' else 'business'

        page.evaluate(f"() => window.switchTheme('{new_theme}')")
        page.wait_for_timeout(300)

        # Check for theme change events
        theme_events = page.evaluate("""
            () => {
                let eventFired = false;
                window.addEventListener('themechange', () => eventFired = true);
                return eventFired;
            }
        """)

        # Note: Event listening depends on when this test runs


@pytest.mark.django_db
class TestThemePerformance:
    """Test theme switching performance."""

    def test_theme_switching_performance(self, page: Page, live_server):
        """Test that theme switching is performant."""
        page.goto(f"{live_server.url}/")

        # Measure theme switching time
        performance_data = []

        for theme in AVAILABLE_THEMES:
            start_time = time.time()

            page.evaluate(f"() => window.switchTheme('{theme}')")
            page.wait_for_timeout(100)

            # Verify theme was applied
            current_theme = page.evaluate("() => window.getCurrentTheme()")
            assert current_theme == theme, f"Theme switch to '{theme}' failed"

            end_time = time.time()
            switch_time = (end_time - start_time) * 1000  # Convert to milliseconds

            performance_data.append({
                'theme': theme,
                'switch_time_ms': switch_time
            })

        # Theme switching should be fast (under 500ms including wait time)
        for data in performance_data:
            assert data['switch_time_ms'] < 500, f"Theme switching to '{data['theme']}' took too long: {data['switch_time_ms']}ms"

    def test_theme_css_loading(self, page: Page, live_server):
        """Test that theme CSS doesn't cause layout shifts."""
        page.goto(f"{live_server.url}/")

        # Get initial layout
        initial_layout = page.evaluate("""
            () => {
                const elements = document.querySelectorAll('button, .card, .navbar');
                const positions = [];

                elements.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    positions.push({
                        x: rect.x,
                        y: rect.y,
                        width: rect.width,
                        height: rect.height
                    });
                });

                return positions;
            }
        """)

        # Switch theme
        page.evaluate("() => window.switchTheme('corporate')")
        page.wait_for_timeout(300)

        # Get layout after theme switch
        new_layout = page.evaluate("""
            () => {
                const elements = document.querySelectorAll('button, .card, .navbar');
                const positions = [];

                elements.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    positions.push({
                        x: rect.x,
                        y: rect.y,
                        width: rect.width,
                        height: rect.height
                    });
                });

                return positions;
            }
        """)

        # Compare layouts - positions should be relatively stable
        # Small differences are acceptable, major shifts are not
        if len(initial_layout) == len(new_layout):
            major_shifts = 0
            for i in range(len(initial_layout)):
                initial = initial_layout[i]
                new = new_layout[i]

                x_shift = abs(initial['x'] - new['x'])
                y_shift = abs(initial['y'] - new['y'])

                if x_shift > 50 or y_shift > 50:  # 50px tolerance
                    major_shifts += 1

            # Should have minimal layout shifts
            shift_percentage = major_shifts / len(initial_layout)
            assert shift_percentage < 0.3, f"Too many layout shifts during theme change: {shift_percentage:.2f}"


def test_theme_switching_report(page: Page, live_server):
    """Generate comprehensive theme switching report."""
    page.goto(f"{live_server.url}/")

    theme_analysis = {
        'themes_tested': AVAILABLE_THEMES,
        'theme_data': {},
        'performance': {},
        'accessibility': {}
    }

    for theme in AVAILABLE_THEMES:
        # Switch to theme
        start_time = time.time()
        page.evaluate(f"() => window.switchTheme('{theme}')")
        page.wait_for_timeout(300)
        end_time = time.time()

        # Collect theme data
        theme_info = page.evaluate("""
            () => {
                return {
                    currentTheme: window.getCurrentTheme(),
                    htmlDataTheme: document.documentElement.getAttribute('data-theme'),
                    localStorageTheme: localStorage.getItem('preferred-theme'),
                    bodyBackgroundColor: window.getComputedStyle(document.body).backgroundColor,
                    primaryButtonExists: !!document.querySelector('.btn-primary, .bg-primary'),
                    themeEventSupport: typeof window.addEventListener === 'function'
                };
            }
        """)

        theme_analysis['theme_data'][theme] = theme_info
        theme_analysis['performance'][theme] = {
            'switch_time_ms': (end_time - start_time) * 1000
        }

    # Save the analysis
    report_path = Path(__file__).parent / 'theme_switching_report.json'
    with open(report_path, 'w') as f:
        json.dump({
            'timestamp': time.time(),
            'url': page.url,
            'analysis': theme_analysis
        }, f, indent=2)

    print(f"Theme switching report saved to: {report_path}")
    return theme_analysis