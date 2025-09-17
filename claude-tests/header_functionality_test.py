"""
Comprehensive Playwright tests for header functionality using Preline UI components.

Tests include:
- Preline-compliant header loading
- Search button functionality (opens modal)
- Dark mode toggle functionality
- Mobile navigation (hamburger menu)
- Responsive behavior across different screen sizes
- Navigation links functionality and active states
- Sticky header behavior when scrolling
"""

import asyncio
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
import json
import time
from datetime import datetime


class HeaderFunctionalityTests:
    def __init__(self, base_url="http://localhost:8001"):
        self.base_url = base_url
        self.test_results = []
        self.browser = None
        self.context = None

    async def setup(self):
        """Initialize Playwright browser and context"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()

    async def teardown(self):
        """Clean up Playwright resources"""
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    def log_result(self, test_name, status, message, details=None):
        """Log test result"""
        result = {
            "test": test_name,
            "status": status,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        self.test_results.append(result)
        status_symbol = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{status_symbol} {test_name}: {message}")
        if details:
            for key, value in details.items():
                print(f"   {key}: {value}")

    async def test_header_loading(self):
        """Test that the Preline-compliant header loads correctly"""
        test_name = "Header Loading"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)

            # Wait for page to load
            await page.wait_for_load_state('networkidle')

            # Check for header element
            header = await page.query_selector('header')
            if not header:
                self.log_result(test_name, "FAIL", "Header element not found")
                return

            # Check for key header components
            components = {
                "logo": "a[aria-label*='Brand'], a[href='/']",
                "navigation": "nav[role='navigation']",
                "button_group": ".lg\\:order-3", # Button group with search/theme toggle
            }

            details = {}
            for component_name, selector in components.items():
                element = await page.query_selector(selector)
                details[component_name] = "Found" if element else "Missing"

            # Check for Preline-specific classes
            preline_classes = [
                "sticky", "flex", "flex-wrap", "lg:justify-start",
                "lg:flex-nowrap", "z-50", "bg-white", "dark:bg-neutral-900"
            ]

            header_classes = await header.get_attribute('class')
            preline_found = sum(1 for cls in preline_classes if cls in header_classes)
            details["preline_classes"] = f"{preline_found}/{len(preline_classes)} found"

            all_components_found = all(details[key] == "Found" for key in components.keys())
            if all_components_found and preline_found >= len(preline_classes) // 2:
                self.log_result(test_name, "PASS", "Header loaded successfully with Preline components", details)
            else:
                self.log_result(test_name, "FAIL", "Header missing required components", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_search_functionality(self):
        """Test search button functionality (should open modal)"""
        test_name = "Search Functionality"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find search button
            search_button = await page.query_selector('[data-hs-overlay="#search-modal"]')
            if not search_button:
                self.log_result(test_name, "FAIL", "Search button not found")
                await page.close()
                return

            # Check if search modal exists
            search_modal = await page.query_selector('#search-modal')
            if not search_modal:
                self.log_result(test_name, "FAIL", "Search modal not found")
                await page.close()
                return

            # Check modal initial state
            modal_classes = await search_modal.get_attribute('class')
            is_initially_hidden = 'hidden' in modal_classes

            # Click search button
            await search_button.click()

            # Wait longer for Preline to process the click and open modal
            await page.wait_for_timeout(1000)

            # Check if modal is now visible (Preline should add 'open' class)
            modal_classes_after = await search_modal.get_attribute('class')
            is_visible_after_click = 'open' in modal_classes_after

            # Check for search form elements
            search_input = await page.query_selector('#search-modal input[name="q"]')
            search_form = await page.query_selector('#search-modal form')

            details = {
                "search_button": "Found",
                "search_modal": "Found",
                "initially_hidden": is_initially_hidden,
                "visible_after_click": is_visible_after_click,
                "search_input": "Found" if search_input else "Missing",
                "search_form": "Found" if search_form else "Missing"
            }

            if is_initially_hidden and is_visible_after_click and search_input and search_form:
                self.log_result(test_name, "PASS", "Search functionality working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Search functionality not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_dark_mode_toggle(self):
        """Test dark mode toggle functionality"""
        test_name = "Dark Mode Toggle"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find dark mode toggle buttons
            dark_mode_button = await page.query_selector('[data-hs-theme-click-value="dark"]')
            light_mode_button = await page.query_selector('[data-hs-theme-click-value="light"]')

            if not dark_mode_button:
                self.log_result(test_name, "FAIL", "Dark mode button not found")
                await page.close()
                return

            # Check initial theme state
            html_element = await page.query_selector('html')
            initial_classes = await html_element.get_attribute('class')
            initial_theme = "dark" if "dark" in initial_classes else "light"

            # Click dark mode button
            await dark_mode_button.click()
            await page.wait_for_timeout(500)

            # Check if dark mode was applied
            after_dark_classes = await html_element.get_attribute('class')
            dark_applied = "dark" in after_dark_classes

            # Test light mode if light button exists
            light_applied = None
            if light_mode_button:
                await light_mode_button.click()
                await page.wait_for_timeout(500)
                after_light_classes = await html_element.get_attribute('class')
                light_applied = "dark" not in after_light_classes

            details = {
                "dark_mode_button": "Found",
                "light_mode_button": "Found" if light_mode_button else "Missing",
                "initial_theme": initial_theme,
                "dark_mode_applied": dark_applied,
                "light_mode_applied": light_applied if light_applied is not None else "Not tested"
            }

            if dark_applied:
                self.log_result(test_name, "PASS", "Dark mode toggle working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Dark mode toggle not working", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_mobile_navigation(self):
        """Test mobile navigation (hamburger menu)"""
        test_name = "Mobile Navigation"
        try:
            page = await self.context.new_page()

            # Set mobile viewport
            await page.set_viewport_size({"width": 375, "height": 667})
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find mobile menu toggle
            mobile_toggle = await page.query_selector('[data-hs-collapse="#hs-navbar-collapse-nav"]')
            if not mobile_toggle:
                self.log_result(test_name, "FAIL", "Mobile menu toggle not found")
                await page.close()
                return

            # Find navigation menu
            nav_menu = await page.query_selector('#hs-navbar-collapse-nav')
            if not nav_menu:
                self.log_result(test_name, "FAIL", "Navigation menu not found")
                await page.close()
                return

            # Check initial state (should be hidden on mobile)
            initial_classes = await nav_menu.get_attribute('class')
            initially_hidden = 'hidden' in initial_classes

            # Click mobile toggle
            await mobile_toggle.click()
            await page.wait_for_timeout(1000)

            # Check if menu is now visible (Preline should add 'open' class and remove 'hidden')
            after_click_classes = await nav_menu.get_attribute('class')
            visible_after_click = 'open' in after_click_classes or 'hidden' not in after_click_classes

            # Check for hamburger icon changes
            hamburger_icons = await page.query_selector_all('.hs-collapse-toggle svg')
            icon_count = len(hamburger_icons)

            details = {
                "mobile_toggle": "Found",
                "nav_menu": "Found",
                "initially_hidden": initially_hidden,
                "visible_after_click": visible_after_click,
                "hamburger_icons": icon_count
            }

            if initially_hidden and visible_after_click:
                self.log_result(test_name, "PASS", "Mobile navigation working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Mobile navigation not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_responsive_behavior(self):
        """Test responsive behavior across different screen sizes"""
        test_name = "Responsive Behavior"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Test different screen sizes
            viewports = [
                {"name": "Mobile", "width": 375, "height": 667},
                {"name": "Tablet", "width": 768, "height": 1024},
                {"name": "Desktop", "width": 1920, "height": 1080}
            ]

            results = {}

            for viewport in viewports:
                await page.set_viewport_size({"width": viewport["width"], "height": viewport["height"]})
                await page.wait_for_timeout(300)

                # Check header visibility and layout
                header = await page.query_selector('header')
                header_visible = await header.is_visible() if header else False

                # Check mobile toggle visibility (should only be visible on mobile/tablet)
                mobile_toggle = await page.query_selector('.lg\\:hidden')
                mobile_toggle_visible = await mobile_toggle.is_visible() if mobile_toggle else False

                # Check desktop navigation visibility (considering our custom JavaScript)
                desktop_nav = await page.query_selector('#hs-navbar-collapse-nav')
                if desktop_nav:
                    # Check if it's visible through CSS display property or lack of hidden class
                    computed_display = await page.evaluate("el => window.getComputedStyle(el).display", desktop_nav)
                    has_hidden_class = 'hidden' in (await desktop_nav.get_attribute('class') or '')
                    desktop_nav_visible = computed_display != 'none' and not has_hidden_class
                else:
                    desktop_nav_visible = False

                results[viewport["name"]] = {
                    "header_visible": header_visible,
                    "mobile_toggle_visible": mobile_toggle_visible,
                    "desktop_nav_visible": desktop_nav_visible
                }

            # Evaluate results
            mobile_correct = results["Mobile"]["mobile_toggle_visible"] and not results["Mobile"]["desktop_nav_visible"]
            desktop_correct = not results["Desktop"]["mobile_toggle_visible"] and results["Desktop"]["desktop_nav_visible"]
            all_headers_visible = all(results[vp]["header_visible"] for vp in results)

            if mobile_correct and desktop_correct and all_headers_visible:
                self.log_result(test_name, "PASS", "Responsive behavior working correctly", results)
            else:
                self.log_result(test_name, "FAIL", "Responsive behavior issues detected", results)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_navigation_links(self):
        """Test navigation links functionality and active states"""
        test_name = "Navigation Links"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find navigation links
            nav_links = await page.query_selector_all('#hs-navbar-collapse-nav a')

            if not nav_links:
                self.log_result(test_name, "FAIL", "No navigation links found")
                await page.close()
                return

            details = {
                "total_links": len(nav_links),
                "links_tested": 0,
                "clickable_links": 0,
                "active_states": 0
            }

            for i, link in enumerate(nav_links[:3]):  # Test first 3 links to avoid long test times
                try:
                    # Wait for link to be available
                    await page.wait_for_timeout(200)

                    # Check if link is visible and clickable
                    is_visible = await link.is_visible()
                    is_enabled = await link.is_enabled()

                    # Additional check for href attribute
                    href = await link.get_attribute('href')
                    has_href = href and href != '#'

                    if is_visible and is_enabled and has_href:
                        details["clickable_links"] += 1

                        # Check for active state classes
                        link_classes = await link.get_attribute('class')
                        has_active_state = any(cls in link_classes for cls in ['bg-primary', 'before:bg-primary', 'text-primary', 'before:bg-yellow-400'])

                        if has_active_state:
                            details["active_states"] += 1

                    details["links_tested"] += 1

                except Exception as e:
                    print(f"Error testing link {i}: {e}")

            # Evaluate results
            success_rate = details["clickable_links"] / details["links_tested"] if details["links_tested"] > 0 else 0

            if success_rate >= 0.8 and details["clickable_links"] > 0:
                self.log_result(test_name, "PASS", "Navigation links working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Issues with navigation links", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_sticky_header(self):
        """Test sticky header behavior when scrolling"""
        test_name = "Sticky Header"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Check if header has sticky classes
            header = await page.query_selector('header')
            if not header:
                self.log_result(test_name, "FAIL", "Header not found")
                await page.close()
                return

            header_classes = await header.get_attribute('class')
            has_sticky_class = 'sticky' in header_classes or 'fixed' in header_classes

            # Get initial header position
            initial_bbox = await header.bounding_box()
            initial_top = initial_bbox['y'] if initial_bbox else None

            # Scroll down the page
            await page.evaluate("window.scrollTo(0, 500)")
            await page.wait_for_timeout(300)

            # Get header position after scroll
            after_scroll_bbox = await header.bounding_box()
            after_scroll_top = after_scroll_bbox['y'] if after_scroll_bbox else None

            # Check if header is still visible after scroll
            header_visible_after_scroll = await header.is_visible()

            details = {
                "has_sticky_class": has_sticky_class,
                "initial_position": initial_top,
                "position_after_scroll": after_scroll_top,
                "visible_after_scroll": header_visible_after_scroll,
                "position_maintained": abs(initial_top - after_scroll_top) < 10 if initial_top and after_scroll_top else False
            }

            if has_sticky_class and header_visible_after_scroll:
                self.log_result(test_name, "PASS", "Sticky header working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Sticky header not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def run_all_tests(self):
        """Run all header functionality tests"""
        print(f"\n🚀 Starting Header Functionality Tests for {self.base_url}\n")

        await self.setup()

        try:
            # Run all tests
            await self.test_header_loading()
            await self.test_search_functionality()
            await self.test_dark_mode_toggle()
            await self.test_mobile_navigation()
            await self.test_responsive_behavior()
            await self.test_navigation_links()
            await self.test_sticky_header()

        finally:
            await self.teardown()

        # Generate summary
        passed = len([r for r in self.test_results if r["status"] == "PASS"])
        failed = len([r for r in self.test_results if r["status"] == "FAIL"])
        total = len(self.test_results)

        print(f"\n📊 Test Summary:")
        print(f"   Total Tests: {total}")
        print(f"   Passed: {passed} ✅")
        print(f"   Failed: {failed} ❌")
        print(f"   Success Rate: {(passed/total)*100:.1f}%")

        return self.test_results

    def save_results(self, filename="header_test_results.json"):
        """Save test results to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "base_url": self.base_url,
                "results": self.test_results
            }, f, indent=2)
        print(f"\n💾 Results saved to {filename}")


async def main():
    """Main function to run the tests"""
    tester = HeaderFunctionalityTests()
    results = await tester.run_all_tests()
    tester.save_results()
    return results


if __name__ == "__main__":
    asyncio.run(main())