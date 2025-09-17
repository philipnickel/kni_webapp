"""
Comprehensive Playwright tests for the new mega menu header implementation.

Tests the new header structure including:
- Modern Preline mega menu design
- Main navigation: Logo, "Kontakt", "Galleri"
- "Flere Sider" mega menu dropdown containing all other pages
- Search, theme toggle, and CTA buttons
- Mobile responsive collapse behavior
- Dynamic loading of pages in mega menu
- Cross-device responsive behavior
"""

import asyncio
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
import json
import time
from datetime import datetime


class MegaMenuHeaderTests:
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

    async def test_header_loading_structure(self):
        """Test that the new mega menu header loads correctly with proper structure"""
        test_name = "Header Loading & Structure"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Check for header element with Preline classes
            header = await page.query_selector('header')
            if not header:
                self.log_result(test_name, "FAIL", "Header element not found")
                return

            # Check header classes for Preline styling
            header_classes = await header.get_attribute('class')
            expected_classes = ['sticky', 'flex', 'flex-wrap', 'lg:justify-start', 'z-50', 'bg-white', 'dark:bg-neutral-900']
            preline_classes_found = sum(1 for cls in expected_classes if cls in header_classes)

            # Check for key header components
            components = {
                "logo": "a[aria-label*='Brand'], a[href='/']",
                "navigation_container": "#hs-navbar-collapse-nav",
                "button_group": ".lg\\:order-3",
                "mobile_toggle": ".lg\\:hidden button[data-hs-collapse]",
                "mega_menu_trigger": "#hs-dropdown-mega-menu",
            }

            details = {"preline_classes": f"{preline_classes_found}/{len(expected_classes)} found"}
            for component_name, selector in components.items():
                element = await page.query_selector(selector)
                details[component_name] = "Found" if element else "Missing"

            # Check for navigation structure
            nav_element = await page.query_selector('nav[role="navigation"]')
            has_proper_nav = nav_element is not None
            details["navigation_role"] = "Found" if has_proper_nav else "Missing"

            all_components_found = all(details[key] == "Found" for key in components.keys())
            if all_components_found and preline_classes_found >= len(expected_classes) // 2:
                self.log_result(test_name, "PASS", "Header structure loaded correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Header missing required components", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_main_navigation_links(self):
        """Test main navigation links (Kontakt & Galleri)"""
        test_name = "Main Navigation Links"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find main navigation links (should be direct links, not in mega menu)
            nav_container = await page.query_selector('#hs-navbar-collapse-nav')
            if not nav_container:
                self.log_result(test_name, "FAIL", "Navigation container not found")
                await page.close()
                return

            # Look for direct navigation links (excluding mega menu items)
            direct_links = await page.query_selector_all('#hs-navbar-collapse-nav > div > div > a')

            details = {
                "total_direct_links": len(direct_links),
                "working_links": 0,
                "kontakt_found": False,
                "galleri_found": False,
                "link_details": []
            }

            for link in direct_links:
                try:
                    href = await link.get_attribute('href')
                    text_content = await link.text_content()
                    is_visible = await link.is_visible()
                    is_enabled = await link.is_enabled()

                    link_info = {
                        "text": text_content.strip(),
                        "href": href,
                        "visible": is_visible,
                        "enabled": is_enabled
                    }
                    details["link_details"].append(link_info)

                    if is_visible and is_enabled and href and href != '#':
                        details["working_links"] += 1

                        # Check for specific navigation items
                        if "kontakt" in text_content.lower():
                            details["kontakt_found"] = True
                        if "galleri" in text_content.lower():
                            details["galleri_found"] = True

                except Exception as e:
                    print(f"Error checking link: {e}")

            # Test clicking one of the main nav links
            if direct_links:
                try:
                    first_link = direct_links[0]
                    href = await first_link.get_attribute('href')
                    if href and href != '#' and not href.startswith('mailto:') and not href.startswith('tel:'):
                        await first_link.click()
                        await page.wait_for_timeout(1000)
                        current_url = page.url
                        details["click_test"] = f"Successfully navigated to {current_url}"
                    else:
                        details["click_test"] = "No suitable link found for click test"
                except Exception as e:
                    details["click_test"] = f"Click test failed: {e}"

            success_criteria = (
                details["working_links"] >= 2 and
                (details["kontakt_found"] or details["galleri_found"])
            )

            if success_criteria:
                self.log_result(test_name, "PASS", "Main navigation links working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Issues with main navigation links", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_mega_menu_functionality(self):
        """Test 'Flere Sider' mega menu dropdown functionality"""
        test_name = "Mega Menu Functionality"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find mega menu trigger
            mega_menu_trigger = await page.query_selector('#hs-dropdown-mega-menu')
            if not mega_menu_trigger:
                self.log_result(test_name, "FAIL", "Mega menu trigger not found")
                await page.close()
                return

            # Check trigger text
            trigger_text = await mega_menu_trigger.text_content()
            has_correct_text = "flere sider" in trigger_text.lower()

            # Find mega menu dropdown
            mega_menu_dropdown = await page.query_selector('.hs-dropdown-menu')
            if not mega_menu_dropdown:
                self.log_result(test_name, "FAIL", "Mega menu dropdown not found")
                await page.close()
                return

            # Check initial state (should be hidden)
            dropdown_classes = await mega_menu_dropdown.get_attribute('class')
            initially_hidden = 'hidden' in dropdown_classes or 'opacity-0' in dropdown_classes

            # Test hover functionality (for desktop)
            await mega_menu_trigger.hover()
            await page.wait_for_timeout(500)

            # Test click functionality
            await mega_menu_trigger.click()
            await page.wait_for_timeout(1000)

            # Check if dropdown is now visible
            dropdown_classes_after = await mega_menu_dropdown.get_attribute('class')
            visible_after_interaction = (
                'hs-dropdown-open:opacity-100' in dropdown_classes_after or
                'opacity-100' in dropdown_classes_after or
                'hidden' not in dropdown_classes_after
            )

            # Check dropdown arrow rotation
            dropdown_arrow = await page.query_selector('#hs-dropdown-mega-menu svg')
            arrow_classes = await dropdown_arrow.get_attribute('class') if dropdown_arrow else ""
            has_rotation_classes = 'hs-dropdown-open:-rotate-180' in arrow_classes

            details = {
                "trigger_found": True,
                "trigger_text_correct": has_correct_text,
                "trigger_text": trigger_text.strip(),
                "dropdown_found": True,
                "initially_hidden": initially_hidden,
                "visible_after_interaction": visible_after_interaction,
                "has_rotation_animation": has_rotation_classes,
                "dropdown_classes": dropdown_classes_after
            }

            success_criteria = (
                has_correct_text and
                initially_hidden and
                visible_after_interaction
            )

            if success_criteria:
                self.log_result(test_name, "PASS", "Mega menu functionality working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Mega menu functionality not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_mega_menu_content(self):
        """Test mega menu content and dynamic loading of pages"""
        test_name = "Mega Menu Content"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Open mega menu
            mega_menu_trigger = await page.query_selector('#hs-dropdown-mega-menu')
            if not mega_menu_trigger:
                self.log_result(test_name, "FAIL", "Mega menu trigger not found")
                await page.close()
                return

            await mega_menu_trigger.click()
            await page.wait_for_timeout(1000)

            # Check for grid layout
            grid_container = await page.query_selector('.hs-dropdown-menu .grid')
            has_grid_layout = grid_container is not None

            # Check for column headers
            column_headers = await page.query_selector_all('.hs-dropdown-menu h3')
            header_texts = []
            for header in column_headers:
                text = await header.text_content()
                header_texts.append(text.strip())

            # Find mega menu items
            mega_menu_items = await page.query_selector_all('.hs-dropdown-menu a[href]')

            details = {
                "grid_layout": "Found" if has_grid_layout else "Missing",
                "column_headers": header_texts,
                "total_menu_items": len(mega_menu_items),
                "working_items": 0,
                "items_with_icons": 0,
                "items_with_descriptions": 0,
                "item_details": []
            }

            # Analyze each menu item
            for i, item in enumerate(mega_menu_items[:8]):  # Test first 8 to avoid long test times
                try:
                    href = await item.get_attribute('href')
                    text_content = await item.text_content()
                    is_visible = await item.is_visible()
                    is_enabled = await item.is_enabled()

                    # Check for icon
                    icon = await item.query_selector('svg')
                    has_icon = icon is not None
                    if has_icon:
                        details["items_with_icons"] += 1

                    # Check for description
                    description = await item.query_selector('p.text-sm')
                    has_description = description is not None
                    if has_description:
                        details["items_with_descriptions"] += 1

                    if is_visible and is_enabled and href and href != '#':
                        details["working_items"] += 1

                    item_info = {
                        "text": text_content.strip()[:50],  # Truncate for readability
                        "href": href,
                        "has_icon": has_icon,
                        "has_description": has_description,
                        "visible": is_visible,
                        "enabled": is_enabled
                    }
                    details["item_details"].append(item_info)

                except Exception as e:
                    print(f"Error analyzing menu item {i}: {e}")

            # Test clicking a menu item
            if mega_menu_items:
                try:
                    first_item = mega_menu_items[0]
                    href = await first_item.get_attribute('href')
                    if href and href != '#' and not href.startswith('mailto:') and not href.startswith('tel:'):
                        await first_item.click()
                        await page.wait_for_timeout(1500)
                        current_url = page.url
                        details["navigation_test"] = f"Successfully navigated to {current_url}"
                    else:
                        details["navigation_test"] = "No suitable item found for navigation test"
                except Exception as e:
                    details["navigation_test"] = f"Navigation test failed: {e}"

            success_criteria = (
                has_grid_layout and
                details["total_menu_items"] >= 3 and
                details["working_items"] >= 2 and
                len(header_texts) >= 1
            )

            if success_criteria:
                self.log_result(test_name, "PASS", "Mega menu content loaded correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Issues with mega menu content", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_mobile_navigation_behavior(self):
        """Test mobile responsive collapse behavior"""
        test_name = "Mobile Navigation Behavior"
        try:
            page = await self.context.new_page()

            # Set mobile viewport
            await page.set_viewport_size({"width": 375, "height": 667})
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find mobile menu toggle
            mobile_toggle = await page.query_selector('.lg\\:hidden button[data-hs-collapse]')
            if not mobile_toggle:
                self.log_result(test_name, "FAIL", "Mobile menu toggle not found")
                await page.close()
                return

            # Check toggle button has correct attributes
            toggle_target = await mobile_toggle.get_attribute('data-hs-collapse')
            has_correct_target = toggle_target == '#hs-navbar-collapse-nav'

            # Find navigation menu
            nav_menu = await page.query_selector('#hs-navbar-collapse-nav')
            if not nav_menu:
                self.log_result(test_name, "FAIL", "Navigation menu not found")
                await page.close()
                return

            # Check initial state (should be hidden on mobile)
            initial_classes = await nav_menu.get_attribute('class')
            initially_hidden = 'hidden' in initial_classes

            # Check that navigation is not visible initially on mobile
            nav_computed_display = await page.evaluate("el => window.getComputedStyle(el).display", nav_menu)
            nav_initially_hidden = nav_computed_display == 'none' or initially_hidden

            # Click mobile toggle to open menu
            await mobile_toggle.click()
            await page.wait_for_timeout(1000)

            # Check if menu is now visible
            after_click_classes = await nav_menu.get_attribute('class')
            nav_after_display = await page.evaluate("el => window.getComputedStyle(el).display", nav_menu)
            nav_visible_after_click = (
                'hidden' not in after_click_classes and
                nav_after_display != 'none'
            )

            # Check hamburger icon animation
            hamburger_icons = await page.query_selector_all('.hs-collapse-toggle svg')
            icon_animation_working = len(hamburger_icons) >= 2  # Should have open and close icons

            # Test mega menu in mobile
            mega_menu_trigger = await page.query_selector('#hs-dropdown-mega-menu')
            mega_menu_mobile_working = False
            if mega_menu_trigger:
                is_mega_trigger_visible = await mega_menu_trigger.is_visible()
                if is_mega_trigger_visible:
                    await mega_menu_trigger.click()
                    await page.wait_for_timeout(500)
                    mega_dropdown = await page.query_selector('.hs-dropdown-menu')
                    if mega_dropdown:
                        mega_dropdown_visible = await mega_dropdown.is_visible()
                        mega_menu_mobile_working = mega_dropdown_visible

            # Click toggle again to close menu
            await mobile_toggle.click()
            await page.wait_for_timeout(1000)

            final_classes = await nav_menu.get_attribute('class')
            nav_hidden_after_close = 'hidden' in final_classes

            details = {
                "mobile_toggle_found": True,
                "toggle_target_correct": has_correct_target,
                "nav_initially_hidden": nav_initially_hidden,
                "nav_visible_after_open": nav_visible_after_click,
                "nav_hidden_after_close": nav_hidden_after_close,
                "icon_animation": icon_animation_working,
                "mega_menu_mobile": mega_menu_mobile_working,
                "initial_display": nav_computed_display,
                "after_click_display": nav_after_display
            }

            success_criteria = (
                has_correct_target and
                nav_initially_hidden and
                nav_visible_after_click and
                nav_hidden_after_close
            )

            if success_criteria:
                self.log_result(test_name, "PASS", "Mobile navigation behavior working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Mobile navigation behavior not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_search_functionality(self):
        """Test search modal functionality"""
        test_name = "Search Functionality"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find search button in header
            search_button = await page.query_selector('button[data-hs-overlay="#search-modal"]')
            if not search_button:
                self.log_result(test_name, "FAIL", "Search button not found in header")
                await page.close()
                return

            # Check search modal exists
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
            await page.wait_for_timeout(1000)

            # Check if modal is now visible
            modal_classes_after = await search_modal.get_attribute('class')
            is_visible_after_click = (
                'hs-overlay-open' in modal_classes_after or
                'hidden' not in modal_classes_after
            )

            # Check search form elements
            search_input = await page.query_selector('#search-modal input[name="q"]')
            search_form = await page.query_selector('#search-modal form')
            search_submit = await page.query_selector('#search-modal button[type="submit"]')
            modal_close = await page.query_selector('#search-modal button[data-hs-overlay]')

            # Test search input functionality
            search_input_working = False
            if search_input:
                await search_input.fill("test search")
                input_value = await search_input.input_value()
                search_input_working = input_value == "test search"

            # Test modal close functionality
            modal_close_working = False
            if modal_close:
                await modal_close.click()
                await page.wait_for_timeout(500)
                modal_classes_closed = await search_modal.get_attribute('class')
                modal_close_working = 'hidden' in modal_classes_closed

            details = {
                "search_button_found": True,
                "search_modal_found": True,
                "initially_hidden": is_initially_hidden,
                "visible_after_click": is_visible_after_click,
                "search_input_found": search_input is not None,
                "search_form_found": search_form is not None,
                "search_submit_found": search_submit is not None,
                "modal_close_found": modal_close is not None,
                "search_input_working": search_input_working,
                "modal_close_working": modal_close_working
            }

            success_criteria = (
                is_initially_hidden and
                is_visible_after_click and
                search_input is not None and
                search_form is not None and
                search_input_working
            )

            if success_criteria:
                self.log_result(test_name, "PASS", "Search functionality working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Search functionality not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_theme_toggle(self):
        """Test dark/light mode theme toggle functionality"""
        test_name = "Theme Toggle"
        try:
            page = await self.context.new_page()
            await page.goto(self.base_url)
            await page.wait_for_load_state('networkidle')

            # Find theme toggle buttons
            dark_mode_button = await page.query_selector('button[data-hs-theme-click-value="dark"]')
            light_mode_button = await page.query_selector('button[data-hs-theme-click-value="light"]')

            if not dark_mode_button:
                self.log_result(test_name, "FAIL", "Dark mode button not found")
                await page.close()
                return

            # Check initial theme state
            html_element = await page.query_selector('html')
            initial_classes = await html_element.get_attribute('class')
            initial_theme = "dark" if "dark" in initial_classes else "light"

            # Test dark mode
            await dark_mode_button.click()
            await page.wait_for_timeout(1000)

            after_dark_classes = await html_element.get_attribute('class')
            dark_applied = "dark" in after_dark_classes

            # Test header theme change
            header = await page.query_selector('header')
            header_classes_dark = await header.get_attribute('class')
            header_dark_theme = "dark:bg-neutral-900" in header_classes_dark

            # Test light mode if button exists
            light_applied = None
            if light_mode_button:
                await light_mode_button.click()
                await page.wait_for_timeout(1000)
                after_light_classes = await html_element.get_attribute('class')
                light_applied = "dark" not in after_light_classes

            # Check if buttons have proper visibility states
            dark_button_classes = await dark_mode_button.get_attribute('class')
            light_button_classes = await light_mode_button.get_attribute('class') if light_mode_button else ""

            has_visibility_toggle = (
                "hs-dark-mode-active:hidden" in dark_button_classes and
                "hs-dark-mode-active:inline-flex" in light_button_classes
            )

            details = {
                "dark_mode_button_found": True,
                "light_mode_button_found": light_mode_button is not None,
                "initial_theme": initial_theme,
                "dark_mode_applied": dark_applied,
                "light_mode_applied": light_applied if light_applied is not None else "Not tested",
                "header_theme_support": header_dark_theme,
                "button_visibility_toggle": has_visibility_toggle
            }

            success_criteria = dark_applied and header_dark_theme

            if success_criteria:
                self.log_result(test_name, "PASS", "Theme toggle working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Theme toggle not working properly", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def test_responsive_behavior(self):
        """Test responsive behavior across desktop/tablet/mobile"""
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
                await page.wait_for_timeout(500)

                # Check header visibility
                header = await page.query_selector('header')
                header_visible = await header.is_visible() if header else False

                # Check mobile toggle visibility
                mobile_toggle = await page.query_selector('.lg\\:hidden button[data-hs-collapse]')
                mobile_toggle_visible = await mobile_toggle.is_visible() if mobile_toggle else False

                # Check desktop navigation visibility
                desktop_nav = await page.query_selector('#hs-navbar-collapse-nav')
                desktop_nav_visible = False
                if desktop_nav:
                    computed_display = await page.evaluate("el => window.getComputedStyle(el).display", desktop_nav)
                    has_hidden_class = 'hidden' in (await desktop_nav.get_attribute('class') or '')
                    desktop_nav_visible = computed_display != 'none' and not has_hidden_class

                # Check mega menu behavior
                mega_menu_trigger = await page.query_selector('#hs-dropdown-mega-menu')
                mega_menu_accessible = await mega_menu_trigger.is_visible() if mega_menu_trigger else False

                # Check button group layout
                button_group = await page.query_selector('.lg\\:order-3')
                button_group_visible = await button_group.is_visible() if button_group else False

                results[viewport["name"]] = {
                    "header_visible": header_visible,
                    "mobile_toggle_visible": mobile_toggle_visible,
                    "desktop_nav_visible": desktop_nav_visible,
                    "mega_menu_accessible": mega_menu_accessible,
                    "button_group_visible": button_group_visible,
                    "viewport_size": f"{viewport['width']}x{viewport['height']}"
                }

            # Evaluate responsive behavior
            mobile_correct = (
                results["Mobile"]["mobile_toggle_visible"] and
                not results["Mobile"]["desktop_nav_visible"]
            )

            desktop_correct = (
                not results["Desktop"]["mobile_toggle_visible"] and
                results["Desktop"]["desktop_nav_visible"]
            )

            tablet_reasonable = (
                results["Tablet"]["header_visible"] and
                results["Tablet"]["button_group_visible"]
            )

            all_headers_visible = all(results[vp]["header_visible"] for vp in results)
            mega_menu_always_accessible = all(results[vp]["mega_menu_accessible"] for vp in results)

            success_criteria = (
                mobile_correct and
                desktop_correct and
                tablet_reasonable and
                all_headers_visible
            )

            details = {
                "mobile_behavior_correct": mobile_correct,
                "desktop_behavior_correct": desktop_correct,
                "tablet_behavior_reasonable": tablet_reasonable,
                "all_headers_visible": all_headers_visible,
                "mega_menu_always_accessible": mega_menu_always_accessible,
                "viewport_results": results
            }

            if success_criteria:
                self.log_result(test_name, "PASS", "Responsive behavior working correctly", details)
            else:
                self.log_result(test_name, "FAIL", "Responsive behavior issues detected", details)

            await page.close()

        except Exception as e:
            self.log_result(test_name, "FAIL", f"Exception occurred: {str(e)}")

    async def run_all_tests(self):
        """Run all mega menu header tests"""
        print(f"\n🚀 Starting Mega Menu Header Tests for {self.base_url}\n")

        await self.setup()

        try:
            # Run all tests in order
            await self.test_header_loading_structure()
            await self.test_main_navigation_links()
            await self.test_mega_menu_functionality()
            await self.test_mega_menu_content()
            await self.test_mobile_navigation_behavior()
            await self.test_search_functionality()
            await self.test_theme_toggle()
            await self.test_responsive_behavior()

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

    def save_results(self, filename="mega_menu_test_results.json"):
        """Save test results to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "base_url": self.base_url,
                "test_type": "mega_menu_header",
                "results": self.test_results
            }, f, indent=2)
        print(f"\n💾 Results saved to {filename}")


async def main():
    """Main function to run the tests"""
    tester = MegaMenuHeaderTests()
    results = await tester.run_all_tests()
    tester.save_results()
    return results


if __name__ == "__main__":
    asyncio.run(main())