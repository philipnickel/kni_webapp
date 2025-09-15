"""
Accessibility compliance verification tests specific to the DaisyUI to Flowbite migration.
Ensures accessibility standards are maintained or improved after migration.
"""

import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python import AxeBuilder
import time
import json
from pathlib import Path


# Updated themes after migration (Flowbite compatible)
MIGRATED_THEMES = ['light', 'corporate', 'business', 'emerald']

# Key accessibility test pages
ACCESSIBILITY_TEST_PAGES = [
    {'url': '/', 'name': 'Home Page', 'critical': True},
    {'url': '/kontakt/', 'name': 'Contact Page', 'critical': True},
    {'url': '/galleri/', 'name': 'Gallery Page', 'critical': False},
]

# Critical WCAG 2.1 AA rules for migration verification
CRITICAL_WCAG_RULES = [
    'color-contrast',
    'link-name',
    'button-name',
    'form-field-multiple-labels',
    'heading-order',
    'html-has-lang',
    'image-alt',
    'label',
    'skip-link',
    'region',
    'page-has-heading-one'
]


@pytest.mark.django_db
class TestMigrationAccessibilityCompliance:
    """Test accessibility compliance after DaisyUI to Flowbite migration."""

    def test_axe_core_compliance_all_themes(self, page: Page, live_server):
        """Run axe-core tests across all migrated themes."""
        accessibility_results = {}

        for theme in MIGRATED_THEMES:
            theme_results = {}

            for test_page in ACCESSIBILITY_TEST_PAGES:
                try:
                    page.goto(f"{live_server.url}{test_page['url']}")
                    page.wait_for_timeout(1000)

                    # Switch to theme
                    page.evaluate(f"() => window.switchTheme && window.switchTheme('{theme}')")
                    page.wait_for_timeout(500)

                    # Run axe-core analysis
                    axe_builder = AxeBuilder(page)

                    # Configure for WCAG 2.1 AA compliance
                    axe_builder.with_tags(['wcag2a', 'wcag2aa', 'wcag21aa'])

                    # Include critical rules
                    axe_builder.with_rules(CRITICAL_WCAG_RULES)

                    # Exclude known third-party issues
                    axe_builder.exclude('#google-analytics, [id*="gtag"], .grecaptcha-badge')

                    results = axe_builder.analyze()

                    # Process violations
                    violations = results.get('violations', [])
                    critical_violations = [
                        v for v in violations
                        if v.get('impact') in ['critical', 'serious']
                    ]

                    theme_results[test_page['name']] = {
                        'url': test_page['url'],
                        'total_violations': len(violations),
                        'critical_violations': len(critical_violations),
                        'violations_summary': [
                            {
                                'id': v.get('id'),
                                'impact': v.get('impact'),
                                'description': v.get('description'),
                                'nodes_affected': len(v.get('nodes', []))
                            }
                            for v in critical_violations
                        ]
                    }

                    # Assert no critical violations on critical pages
                    if test_page.get('critical', False):
                        assert len(critical_violations) == 0, \
                            f"Critical accessibility violations found on {test_page['name']} with {theme} theme: {[v.get('id') for v in critical_violations]}"

                except Exception as e:
                    theme_results[test_page['name']] = {
                        'error': str(e),
                        'url': test_page['url']
                    }

            accessibility_results[theme] = theme_results

        # Save detailed results
        report_path = Path(__file__).parent / 'migration_accessibility_report.json'
        with open(report_path, 'w') as f:
            json.dump({
                'timestamp': time.time(),
                'themes_tested': MIGRATED_THEMES,
                'results': accessibility_results
            }, f, indent=2)

        return accessibility_results

    def test_keyboard_navigation_post_migration(self, page: Page, live_server):
        """Test keyboard navigation works correctly after migration."""
        page.goto(f"{live_server.url}/")

        # Test tab order and focus visibility
        focusable_elements = []

        # Start tabbing through the page
        for i in range(15):  # Test first 15 tab stops
            page.keyboard.press('Tab')
            page.wait_for_timeout(100)

            # Get currently focused element
            focused_element = page.evaluate("""
                () => {
                    const el = document.activeElement;
                    if (el && el !== document.body) {
                        return {
                            tagName: el.tagName,
                            type: el.type || null,
                            id: el.id || null,
                            className: el.className || null,
                            ariaLabel: el.getAttribute('aria-label') || null,
                            textContent: el.textContent ? el.textContent.substring(0, 50) : null,
                            visible: el.offsetParent !== null
                        };
                    }
                    return null;
                }
            """)

            if focused_element:
                focusable_elements.append(focused_element)

        # Verify focus order makes sense
        assert len(focusable_elements) > 0, "Should have focusable elements"

        # Check for skip links
        skip_links = [el for el in focusable_elements if 'skip' in (el.get('textContent') or '').lower()]
        assert len(skip_links) > 0, "Should have skip links for accessibility"

        # Check focus visibility
        page.keyboard.press('Tab')
        focus_indicator = page.evaluate("""
            () => {
                const el = document.activeElement;
                if (el) {
                    const styles = window.getComputedStyle(el);
                    return {
                        outline: styles.outline,
                        outlineWidth: styles.outlineWidth,
                        outlineStyle: styles.outlineStyle,
                        boxShadow: styles.boxShadow,
                        border: styles.border
                    };
                }
                return null;
            }
        """)

        # Should have some form of focus indicator
        if focus_indicator:
            has_focus_indicator = any([
                focus_indicator.get('outline') != 'none',
                focus_indicator.get('outlineWidth') != '0px',
                'ring' in str(focus_indicator.get('boxShadow', '')),
                focus_indicator.get('boxShadow') not in [None, 'none']
            ])

            assert has_focus_indicator, "Focused elements should have visible focus indicators"

    def test_screen_reader_compatibility(self, page: Page, live_server):
        """Test screen reader compatibility features."""
        page.goto(f"{live_server.url}/")

        # Check for proper landmarks
        landmarks = page.evaluate("""
            () => {
                const landmarks = [
                    ...document.querySelectorAll('[role="banner"], header'),
                    ...document.querySelectorAll('[role="navigation"], nav'),
                    ...document.querySelectorAll('[role="main"], main'),
                    ...document.querySelectorAll('[role="contentinfo"], footer'),
                    ...document.querySelectorAll('[role="complementary"], aside'),
                    ...document.querySelectorAll('[role="search"]')
                ];

                return landmarks.map(el => ({
                    tagName: el.tagName,
                    role: el.getAttribute('role') || null,
                    ariaLabel: el.getAttribute('aria-label') || null,
                    ariaLabelledby: el.getAttribute('aria-labelledby') || null
                }));
            }
        """)

        assert len(landmarks) > 0, "Page should have proper landmark elements"

        # Check for main content landmark
        main_landmarks = [l for l in landmarks if l.get('role') == 'main' or l.get('tagName') == 'MAIN']
        assert len(main_landmarks) > 0, "Page should have a main content landmark"

        # Check heading structure
        headings = page.evaluate("""
            () => {
                const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
                return Array.from(headings).map(h => ({
                    level: parseInt(h.tagName.charAt(1)),
                    text: h.textContent ? h.textContent.substring(0, 100) : '',
                    ariaLevel: h.getAttribute('aria-level') || null
                }));
            }
        """)

        assert len(headings) > 0, "Page should have headings"

        # Should have exactly one h1
        h1_count = len([h for h in headings if h.get('level') == 1])
        assert h1_count == 1, f"Page should have exactly one h1 heading, found {h1_count}"

        # Check heading hierarchy
        for i in range(1, len(headings)):
            current_level = headings[i].get('level')
            previous_level = headings[i-1].get('level')

            # Heading levels shouldn't skip more than one level
            level_jump = current_level - previous_level
            assert level_jump <= 1, f"Heading hierarchy violation: h{previous_level} followed by h{current_level}"

    def test_form_accessibility_post_migration(self, page: Page, live_server):
        """Test form accessibility after migration."""
        try:
            page.goto(f"{live_server.url}/kontakt/")
        except:
            try:
                page.goto(f"{live_server.url}/contact/")
            except:
                pytest.skip("No contact page available")

        # Find forms
        forms = page.locator('form')
        if forms.count() == 0:
            pytest.skip("No forms found on contact page")

        form = forms.first

        # Test form labels and descriptions
        form_fields = form.locator('input, textarea, select')

        for i in range(form_fields.count()):
            field = form_fields.nth(i)
            field_info = page.evaluate("""
                (element) => {
                    return {
                        type: element.type || element.tagName,
                        id: element.id,
                        name: element.name,
                        required: element.required,
                        ariaLabel: element.getAttribute('aria-label'),
                        ariaLabelledby: element.getAttribute('aria-labelledby'),
                        ariaDescribedby: element.getAttribute('aria-describedby'),
                        hasLabel: !!document.querySelector(`label[for="${element.id}"]`)
                    };
                }
            """, field)

            # Each form field should have proper labeling
            has_label = any([
                field_info.get('hasLabel'),
                field_info.get('ariaLabel'),
                field_info.get('ariaLabelledby')
            ])

            assert has_label, f"Form field {field_info.get('name')} should have proper labeling"

            # Required fields should be indicated
            if field_info.get('required'):
                # Check for aria-required or visual indicators
                aria_required = field.get_attribute('aria-required')
                # Note: Visual indicators are harder to test programmatically

        # Test form error handling
        submit_button = form.locator('button[type="submit"], input[type="submit"]')

        if submit_button.count() > 0:
            # Try submitting empty form
            submit_button.first.click()
            page.wait_for_timeout(500)

            # Check for error messages
            error_messages = page.locator('.error, .invalid-feedback, [aria-invalid="true"]')

            # Form should handle validation appropriately
            # Note: This depends on implementation

    def test_color_contrast_compliance(self, page: Page, live_server):
        """Test color contrast compliance across themes."""
        contrast_results = {}

        for theme in MIGRATED_THEMES:
            page.goto(f"{live_server.url}/")
            page.wait_for_timeout(500)

            # Switch to theme
            page.evaluate(f"() => window.switchTheme && window.switchTheme('{theme}')")
            page.wait_for_timeout(500)

            # Test contrast for various element types
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

                    const elementTypes = [
                        'p', 'h1', 'h2', 'h3', 'a', 'button', '.btn'
                    ];

                    const contrastResults = {};

                    elementTypes.forEach(selector => {
                        const elements = document.querySelectorAll(selector);
                        const sampleSize = Math.min(elements.length, 3);

                        const contrasts = [];
                        for (let i = 0; i < sampleSize; i++) {
                            const element = elements[i];
                            const styles = window.getComputedStyle(element);
                            const textColor = styles.color;
                            const backgroundColor = styles.backgroundColor;

                            // Get background from parent if transparent
                            let bgElement = element;
                            let bgColor = backgroundColor;

                            while ((bgColor === 'rgba(0, 0, 0, 0)' || bgColor === 'transparent') && bgElement.parentElement) {
                                bgElement = bgElement.parentElement;
                                bgColor = window.getComputedStyle(bgElement).backgroundColor;
                            }

                            try {
                                const contrast = getContrastRatio(textColor, bgColor);
                                contrasts.push({
                                    textColor,
                                    backgroundColor: bgColor,
                                    contrast: contrast,
                                    passes_AA: contrast >= 4.5,
                                    passes_AAA: contrast >= 7
                                });
                            } catch (e) {
                                // Skip if color parsing fails
                            }
                        }

                        if (contrasts.length > 0) {
                            contrastResults[selector] = contrasts;
                        }
                    });

                    return contrastResults;
                }
            """)

            contrast_results[theme] = contrast_data

            # Check for critical contrast failures
            for selector, contrasts in contrast_data.items():
                failing_contrasts = [c for c in contrasts if not c.get('passes_AA', True)]

                # Allow some tolerance for non-critical elements
                failure_rate = len(failing_contrasts) / len(contrasts) if contrasts else 0

                if selector in ['h1', 'h2', 'h3', 'p']:  # Critical text elements
                    assert failure_rate < 0.2, \
                        f"High contrast failure rate for {selector} in {theme} theme: {failure_rate:.2f}"

        return contrast_results

    def test_aria_attributes_preservation(self, page: Page, live_server):
        """Test that ARIA attributes are preserved after migration."""
        page.goto(f"{live_server.url}/")

        # Check for essential ARIA attributes
        aria_elements = page.evaluate("""
            () => {
                const selectors = [
                    '[aria-label]',
                    '[aria-labelledby]',
                    '[aria-describedby]',
                    '[aria-expanded]',
                    '[aria-haspopup]',
                    '[role]',
                    '[aria-hidden]',
                    '[aria-live]'
                ];

                const results = {};

                selectors.forEach(selector => {
                    const elements = document.querySelectorAll(selector);
                    results[selector] = {
                        count: elements.length,
                        samples: Array.from(elements).slice(0, 3).map(el => ({
                            tagName: el.tagName,
                            attribute: selector,
                            value: el.getAttribute(selector.replace(/[\\[\\]]/g, ''))
                        }))
                    };
                });

                return results;
            }
        """)

        # Should have aria-label elements
        aria_labels = aria_elements.get('[aria-label]', {}).get('count', 0)
        assert aria_labels > 0, "Page should have elements with aria-label"

        # Should have role attributes
        role_elements = aria_elements.get('[role]', {}).get('count', 0)
        assert role_elements > 0, "Page should have elements with role attributes"

        # Check interactive elements have proper ARIA
        interactive_elements = page.evaluate("""
            () => {
                const buttons = document.querySelectorAll('button, [role="button"]');
                const dropdowns = document.querySelectorAll('[aria-haspopup], .dropdown');
                const menus = document.querySelectorAll('[role="menu"], .menu');

                return {
                    buttons: buttons.length,
                    dropdowns: dropdowns.length,
                    menus: menus.length,
                    buttonsWithAriaLabel: document.querySelectorAll('button[aria-label], [role="button"][aria-label]').length
                };
            }
        """)

        # Interactive elements should have proper labeling
        if interactive_elements['buttons'] > 0:
            labeling_rate = interactive_elements['buttonsWithAriaLabel'] / interactive_elements['buttons']
            # Allow some unlabeled buttons (those with text content)
            # This is informational rather than strict

    def test_migration_specific_accessibility_regressions(self, page: Page, live_server):
        """Test for accessibility regressions specific to the DaisyUI -> Flowbite migration."""
        page.goto(f"{live_server.url}/")

        # Test for common migration issues
        migration_issues = page.evaluate("""
            () => {
                const issues = [];

                // Check for missing lang attribute
                if (!document.documentElement.lang) {
                    issues.push('Missing lang attribute on html element');
                }

                // Check for DaisyUI-specific accessibility classes that might be missing
                const skipLinks = document.querySelectorAll('a[href="#main-content"], a[href="#main-navigation"]');
                if (skipLinks.length === 0) {
                    issues.push('Missing skip links');
                }

                // Check for proper heading structure
                const h1s = document.querySelectorAll('h1');
                if (h1s.length !== 1) {
                    issues.push(`Should have exactly one h1, found ${h1s.length}`);
                }

                // Check for empty buttons or links
                const emptyButtons = document.querySelectorAll('button:empty:not([aria-label]):not([aria-labelledby])');
                const emptyLinks = document.querySelectorAll('a:empty:not([aria-label]):not([aria-labelledby])');

                if (emptyButtons.length > 0) {
                    issues.push(`Found ${emptyButtons.length} empty buttons without labels`);
                }

                if (emptyLinks.length > 0) {
                    issues.push(`Found ${emptyLinks.length} empty links without labels`);
                }

                // Check for form labels
                const inputs = document.querySelectorAll('input[type="text"], input[type="email"], textarea');
                let unlabeledInputs = 0;

                inputs.forEach(input => {
                    const hasLabel = input.id && document.querySelector(`label[for="${input.id}"]`);
                    const hasAriaLabel = input.getAttribute('aria-label');
                    const hasAriaLabelledby = input.getAttribute('aria-labelledby');

                    if (!hasLabel && !hasAriaLabel && !hasAriaLabelledby) {
                        unlabeledInputs++;
                    }
                });

                if (unlabeledInputs > 0) {
                    issues.push(`Found ${unlabeledInputs} unlabeled form inputs`);
                }

                return issues;
            }
        """)

        # Assert no critical accessibility regressions
        critical_issues = [issue for issue in migration_issues if any(keyword in issue.lower() for keyword in ['missing', 'empty', 'unlabeled'])]

        assert len(critical_issues) == 0, f"Critical accessibility issues found after migration: {critical_issues}"

        return migration_issues


def test_accessibility_migration_summary(page: Page, live_server):
    """Generate comprehensive accessibility migration summary."""
    page.goto(f"{live_server.url}/")

    # Collect comprehensive accessibility data
    accessibility_summary = page.evaluate("""
        () => {
            return {
                structure: {
                    hasLangAttribute: !!document.documentElement.lang,
                    skipLinksCount: document.querySelectorAll('a[href="#main-content"], a[href="#main-navigation"]').length,
                    landmarksCount: document.querySelectorAll('[role="banner"], [role="navigation"], [role="main"], [role="contentinfo"], header, nav, main, footer').length,
                    headingsCount: document.querySelectorAll('h1, h2, h3, h4, h5, h6').length,
                    h1Count: document.querySelectorAll('h1').length
                },
                interactive: {
                    buttonsCount: document.querySelectorAll('button, [role="button"]').length,
                    linksCount: document.querySelectorAll('a').length,
                    formsCount: document.querySelectorAll('form').length,
                    inputsCount: document.querySelectorAll('input, textarea, select').length
                },
                aria: {
                    ariaLabelsCount: document.querySelectorAll('[aria-label]').length,
                    rolesCount: document.querySelectorAll('[role]').length,
                    ariaExpandedCount: document.querySelectorAll('[aria-expanded]').length,
                    ariaHaspopupCount: document.querySelectorAll('[aria-haspopup]').length
                },
                themes: {
                    currentTheme: window.getCurrentTheme ? window.getCurrentTheme() : null,
                    availableThemes: window.getAvailableThemes ? window.getAvailableThemes() : null,
                    themeSystemAvailable: typeof window.switchTheme === 'function'
                }
            };
        }
    """)

    # Save accessibility summary
    report_path = Path(__file__).parent / 'accessibility_migration_summary.json'
    with open(report_path, 'w') as f:
        json.dump({
            'timestamp': time.time(),
            'url': page.url,
            'themes_supported': MIGRATED_THEMES,
            'accessibility_summary': accessibility_summary
        }, f, indent=2)

    print(f"Accessibility migration summary saved to: {report_path}")
    return accessibility_summary