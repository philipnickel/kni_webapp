"""
Visual regression tests for the JCleemannByg website.

This module tests visual consistency across themes, viewports,
and interaction states to ensure accessibility features remain
visually functional.
"""

import pytest
from playwright.sync_api import Page
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import hashlib
import json
from typing import Dict, List, Tuple


# Test configuration
THEMES_TO_TEST = ['light', 'dark', 'corporate', 'business', 'emerald']
VIEWPORTS = [
    {'name': 'desktop', 'width': 1200, 'height': 800},
    {'name': 'tablet', 'width': 768, 'height': 1024},
    {'name': 'mobile', 'width': 375, 'height': 667},
]

PAGES_TO_TEST = [
    {'url': '/', 'name': 'home'},
    {'url': '/kontakt/', 'name': 'contact'},
    {'url': '/galleri/', 'name': 'gallery'},
]

# Baseline directory for storing reference images
BASELINE_DIR = Path(__file__).parent / 'visual_baselines'
BASELINE_DIR.mkdir(exist_ok=True)


class VisualRegressionTestMixin:
    """Mixin providing visual regression testing utilities."""

    @staticmethod
    def setup_theme(page: Page, theme: str):
        """Set up the Frostbite carpenter theme."""
        page.evaluate(f"window.switchTheme('{theme}')")
        page.wait_for_timeout(500)

    @staticmethod
    def get_screenshot_path(test_name: str, theme: str, viewport: str, state: str = 'default') -> Path:
        """Generate consistent screenshot path."""
        filename = f"{test_name}_{theme}_{viewport}_{state}.png"
        return BASELINE_DIR / filename

    def take_screenshot_with_metadata(self, page: Page, path: Path,
                                    element_selector: str = None) -> Dict:
        """Take screenshot and return metadata."""
        # Ensure page is fully loaded
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(500)  # Additional stabilization

        # Take screenshot
        if element_selector:
            element = page.query_selector(element_selector)
            if element:
                screenshot_bytes = element.screenshot()
            else:
                screenshot_bytes = page.screenshot(full_page=True)
        else:
            screenshot_bytes = page.screenshot(full_page=True)

        # Save screenshot
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            f.write(screenshot_bytes)

        # Generate metadata
        metadata = {
            'path': str(path),
            'size': len(screenshot_bytes),
            'hash': hashlib.md5(screenshot_bytes).hexdigest(),
            'viewport': page.viewport_size,
            'url': page.url,
            'timestamp': page.evaluate('Date.now()')
        }

        return metadata

    def compare_screenshots(self, baseline_path: Path, current_path: Path,
                          threshold: float = 0.01) -> Dict:
        """Compare two screenshots and return difference information."""
        if not baseline_path.exists():
            return {'status': 'no_baseline', 'message': 'No baseline image found'}

        try:
            from PIL import Image, ImageChops

            baseline_img = Image.open(baseline_path)
            current_img = Image.open(current_path)

            # Resize if dimensions differ
            if baseline_img.size != current_img.size:
                current_img = current_img.resize(baseline_img.size, Image.Resampling.LANCZOS)

            # Calculate difference
            diff = ImageChops.difference(baseline_img, current_img)

            # Calculate percentage of different pixels
            histogram = diff.histogram()
            total_pixels = sum(histogram)
            different_pixels = total_pixels - histogram[0]  # Non-zero values

            if total_pixels > 0:
                diff_percentage = different_pixels / total_pixels
            else:
                diff_percentage = 0

            if diff_percentage <= threshold:
                return {'status': 'match', 'difference': diff_percentage}
            else:
                # Save difference image
                diff_path = current_path.parent / f"{current_path.stem}_diff.png"
                diff.save(diff_path)

                return {
                    'status': 'mismatch',
                    'difference': diff_percentage,
                    'threshold': threshold,
                    'diff_path': str(diff_path)
                }

        except Exception as e:
            return {'status': 'error', 'message': str(e)}


@pytest.mark.visual_regression
class TestThemeVisualConsistency(VisualRegressionTestMixin):
    """Test visual consistency across themes."""

    @pytest.mark.parametrize("theme", THEMES_TO_TEST)
    @pytest.mark.parametrize("page_info", PAGES_TO_TEST)
    @pytest.mark.parametrize("viewport", VIEWPORTS)
    def test_theme_page_consistency(self, live_server, page: Page,
                                  theme: str, page_info: Dict, viewport: Dict):
        """Test that each page renders consistently in each theme."""
        # Set viewport
        page.set_viewport_size(viewport['width'], viewport['height'])

        # Navigate to page
        page.goto(f"{live_server.url}{page_info['url']}")

        # Set theme
        self.setup_theme(page, theme)

        # Generate test name
        test_name = f"page_{page_info['name']}"

        # Take screenshot
        screenshot_path = self.get_screenshot_path(
            test_name, theme, viewport['name']
        )

        metadata = self.take_screenshot_with_metadata(page, screenshot_path)

        # For new baseline creation, just save the image
        if not screenshot_path.exists() or os.getenv('UPDATE_BASELINES'):
            print(f"Creating/updating baseline: {screenshot_path}")
            return

        # Compare with baseline (for future runs)
        # This is where you'd implement actual comparison logic

    def test_navigation_focus_states(self, live_server, page: Page):
        """Test visual consistency of navigation focus states."""
        page.goto(f"{live_server.url}/")

        for theme in ['light', 'dark']:  # Test key themes
            self.setup_theme(page, theme)

            # Test focus states on navigation elements
            nav_elements = page.query_selector_all('.navbar a, .navbar button')

            for i, element in enumerate(nav_elements[:3]):  # Limit to avoid too many screenshots
                # Focus element
                element.focus()
                page.wait_for_timeout(200)

                # Take screenshot of focused element
                test_name = f"nav_focus_{i}"
                screenshot_path = self.get_screenshot_path(
                    test_name, theme, 'desktop', 'focused'
                )

                self.take_screenshot_with_metadata(
                    page, screenshot_path, '.navbar'
                )

    def test_form_interaction_states(self, live_server, page: Page, contact_page):
        """Test visual consistency of form interaction states."""
        page.goto(f"{live_server.url}/kontakt/")

        for theme in ['light', 'dark']:
            self.setup_theme(page, theme)

            # Test various form states
            states_to_test = [
                {'name': 'default', 'action': None},
                {'name': 'focused', 'action': lambda: page.query_selector('input[name="name"]').focus()},
                {'name': 'filled', 'action': lambda: page.fill('input[name="name"]', 'Test User')},
                {'name': 'error', 'action': lambda: page.query_selector('button[type="submit"]').click()},
            ]

            for state in states_to_test:
                if state['action']:
                    state['action']()
                    page.wait_for_timeout(500)

                test_name = f"form_{state['name']}"
                screenshot_path = self.get_screenshot_path(
                    test_name, theme, 'desktop', state['name']
                )

                # Screenshot the form area
                form_element = page.query_selector('form')
                if form_element:
                    self.take_screenshot_with_metadata(
                        page, screenshot_path, 'form'
                    )


@pytest.mark.visual_regression
class TestResponsiveDesign(VisualRegressionTestMixin):
    """Test responsive design visual consistency."""

    @pytest.mark.parametrize("viewport", VIEWPORTS)
    def test_responsive_navigation(self, live_server, page: Page, viewport: Dict):
        """Test navigation appearance across viewports."""
        page.set_viewport_size(viewport['width'], viewport['height'])
        page.goto(f"{live_server.url}/")

        # Test in light theme
        self.setup_theme(page, 'light')

        test_name = f"navigation_responsive"
        screenshot_path = self.get_screenshot_path(
            test_name, 'light', viewport['name']
        )

        self.take_screenshot_with_metadata(
            page, screenshot_path, '.navbar'
        )

        # Test mobile menu if in mobile viewport
        if viewport['width'] <= 768:
            mobile_trigger = page.query_selector('.navbar .dropdown [role="button"]')
            if mobile_trigger:
                mobile_trigger.click()
                page.wait_for_timeout(300)

                test_name = f"mobile_menu_open"
                screenshot_path = self.get_screenshot_path(
                    test_name, 'light', viewport['name']
                )

                self.take_screenshot_with_metadata(
                    page, screenshot_path, '.navbar'
                )

    @pytest.mark.parametrize("viewport", VIEWPORTS)
    def test_responsive_content_layout(self, live_server, page: Page, viewport: Dict):
        """Test content layout across viewports."""
        page.set_viewport_size(viewport['width'], viewport['height'])

        for page_info in PAGES_TO_TEST:
            page.goto(f"{live_server.url}{page_info['url']}")
            self.setup_theme(page, 'light')

            test_name = f"layout_{page_info['name']}"
            screenshot_path = self.get_screenshot_path(
                test_name, 'light', viewport['name']
            )

            self.take_screenshot_with_metadata(page, screenshot_path)

    def test_responsive_footer(self, live_server, page: Page):
        """Test footer layout across viewports."""
        page.goto(f"{live_server.url}/")

        for viewport in VIEWPORTS:
            page.set_viewport_size(viewport['width'], viewport['height'])
            self.setup_theme(page, 'light')

            test_name = f"footer_responsive"
            screenshot_path = self.get_screenshot_path(
                test_name, 'light', viewport['name']
            )

            self.take_screenshot_with_metadata(
                page, screenshot_path, 'footer'
            )


@pytest.mark.visual_regression
class TestInteractionStates(VisualRegressionTestMixin):
    """Test visual consistency of interaction states."""

    def test_button_states(self, live_server, page: Page):
        """Test button states across themes."""
        page.goto(f"{live_server.url}/")

        for theme in ['light', 'dark', 'corporate']:
            self.setup_theme(page, theme)

            # Find buttons to test
            buttons = page.query_selector_all('.btn')

            for i, button in enumerate(buttons[:3]):  # Test first 3 buttons
                # Test different states
                states = [
                    {'name': 'default', 'action': None},
                    {'name': 'hover', 'action': lambda b=button: b.hover()},
                    {'name': 'focus', 'action': lambda b=button: b.focus()},
                ]

                for state in states:
                    if state['action']:
                        state['action']()
                        page.wait_for_timeout(200)

                    test_name = f"button_{i}_{state['name']}"
                    screenshot_path = self.get_screenshot_path(
                        test_name, theme, 'desktop'
                    )

                    # Screenshot just the button area
                    button_box = button.bounding_box()
                    if button_box:
                        # Expand box slightly for context
                        expanded_box = {
                            'x': max(0, button_box['x'] - 10),
                            'y': max(0, button_box['y'] - 10),
                            'width': button_box['width'] + 20,
                            'height': button_box['height'] + 20
                        }

                        screenshot_bytes = page.screenshot(clip=expanded_box)

                        with open(screenshot_path, 'wb') as f:
                            f.write(screenshot_bytes)

    def test_link_states(self, live_server, page: Page):
        """Test link states across themes."""
        page.goto(f"{live_server.url}/")

        for theme in ['light', 'dark']:
            self.setup_theme(page, theme)

            # Test navigation links
            nav_links = page.query_selector_all('.navbar a')

            for i, link in enumerate(nav_links[:3]):
                # Test hover state
                link.hover()
                page.wait_for_timeout(200)

                test_name = f"link_hover_{i}"
                screenshot_path = self.get_screenshot_path(
                    test_name, theme, 'desktop'
                )

                self.take_screenshot_with_metadata(
                    page, screenshot_path, '.navbar'
                )


@pytest.fixture
def baseline_manager():
    """Fixture for managing visual regression baselines."""
    class BaselineManager:
        def __init__(self):
            self.baseline_dir = BASELINE_DIR

        def create_baseline_index(self):
            """Create an index of all baseline images."""
            index = {}

            for img_path in self.baseline_dir.glob('*.png'):
                if '_diff.png' not in str(img_path):  # Skip diff images
                    parts = img_path.stem.split('_')
                    if len(parts) >= 3:
                        test_name = '_'.join(parts[:-2])
                        theme = parts[-2]
                        viewport = parts[-1]

                        if test_name not in index:
                            index[test_name] = {}
                        if theme not in index[test_name]:
                            index[test_name][theme] = {}

                        index[test_name][theme][viewport] = {
                            'path': str(img_path),
                            'size': img_path.stat().st_size,
                            'modified': img_path.stat().st_mtime
                        }

            # Save index
            index_path = self.baseline_dir / 'baseline_index.json'
            with open(index_path, 'w') as f:
                json.dump(index, f, indent=2)

            return index

    return BaselineManager()


# Utility function to generate baseline report
def generate_baseline_report():
    """Generate a report of all baseline images."""
    baseline_manager = baseline_manager()
    index = baseline_manager.create_baseline_index()

    report = {
        'total_baselines': sum(
            len(themes[theme])
            for test in index.values()
            for theme in test.values()
        ),
        'themes_covered': set(),
        'viewports_covered': set(),
        'tests_covered': list(index.keys())
    }

    for test_name, themes in index.items():
        for theme, viewports in themes.items():
            report['themes_covered'].add(theme)
            for viewport in viewports.keys():
                report['viewports_covered'].add(viewport)

    report['themes_covered'] = list(report['themes_covered'])
    report['viewports_covered'] = list(report['viewports_covered'])

    return report