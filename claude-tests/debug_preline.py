"""
Debug script to check Preline initialization and functionality
"""

import asyncio
from playwright.async_api import async_playwright

async def debug_preline():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Enable console logging
        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))

        await page.goto("http://localhost:8001")
        await page.wait_for_load_state('networkidle')

        # Wait a bit for everything to load
        await page.wait_for_timeout(2000)

        # Check if Preline is available
        preline_available = await page.evaluate("typeof HSStaticMethods !== 'undefined'")
        print(f"Preline available: {preline_available}")

        # Check specific components
        overlay_available = await page.evaluate("typeof window.HSOverlay !== 'undefined'")
        collapse_available = await page.evaluate("typeof window.HSCollapse !== 'undefined'")
        print(f"HSOverlay available: {overlay_available}")
        print(f"HSCollapse available: {collapse_available}")

        # Check search button and modal
        search_button = await page.query_selector('[data-hs-overlay="#search-modal"]')
        search_modal = await page.query_selector('#search-modal')
        print(f"Search button found: {search_button is not None}")
        print(f"Search modal found: {search_modal is not None}")

        if search_button and search_modal:
            # Try clicking the search button
            print("Clicking search button...")
            await search_button.click()
            await page.wait_for_timeout(1000)

            # Check if modal is visible
            modal_classes = await search_modal.get_attribute('class')
            print(f"Modal classes after click: {modal_classes}")
            is_visible = 'hidden' not in modal_classes
            print(f"Modal visible: {is_visible}")

        # Check mobile navigation
        mobile_toggle = await page.query_selector('[data-hs-collapse="#hs-navbar-collapse-nav"]')
        nav_menu = await page.query_selector('#hs-navbar-collapse-nav')
        print(f"Mobile toggle found: {mobile_toggle is not None}")
        print(f"Nav menu found: {nav_menu is not None}")

        if mobile_toggle and nav_menu:
            # Set mobile viewport
            await page.set_viewport_size({"width": 375, "height": 667})
            await page.wait_for_timeout(500)

            # Check initial state
            initial_classes = await nav_menu.get_attribute('class')
            print(f"Nav menu initial classes: {initial_classes}")

            # Try clicking the mobile toggle
            print("Clicking mobile toggle...")
            await mobile_toggle.click()
            await page.wait_for_timeout(1000)

            # Check state after click
            after_classes = await nav_menu.get_attribute('class')
            print(f"Nav menu classes after click: {after_classes}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_preline())