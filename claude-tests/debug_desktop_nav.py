"""
Debug script to check desktop navigation visibility
"""

import asyncio
from playwright.async_api import async_playwright

async def debug_desktop_nav():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Set desktop viewport
        await page.set_viewport_size({"width": 1920, "height": 1080})

        await page.goto("http://localhost:8001")
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(3000)  # Wait longer for JavaScript

        # Check navigation menu
        nav_menu = await page.query_selector('#hs-navbar-collapse-nav')
        if nav_menu:
            classes = await nav_menu.get_attribute('class')
            style = await nav_menu.get_attribute('style')
            computed_display = await page.evaluate("el => window.getComputedStyle(el).display", nav_menu)
            computed_visibility = await page.evaluate("el => window.getComputedStyle(el).visibility", nav_menu)
            is_visible = await nav_menu.is_visible()

            print(f"Navigation menu:")
            print(f"  Classes: {classes}")
            print(f"  Style: {style}")
            print(f"  Computed display: {computed_display}")
            print(f"  Computed visibility: {computed_visibility}")
            print(f"  Playwright is_visible: {is_visible}")

            # Check first navigation link
            first_link = await page.query_selector('#hs-navbar-collapse-nav a')
            if first_link:
                link_visible = await first_link.is_visible()
                link_bbox = await first_link.bounding_box()
                print(f"  First link visible: {link_visible}")
                print(f"  First link bbox: {link_bbox}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_desktop_nav())