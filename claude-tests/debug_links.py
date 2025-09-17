"""
Debug script to check navigation link clickability
"""

import asyncio
from playwright.async_api import async_playwright

async def debug_links():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("http://localhost:8001")
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(2000)

        # Find navigation links
        nav_links = await page.query_selector_all('#hs-navbar-collapse-nav a')
        print(f"Found {len(nav_links)} navigation links")

        for i, link in enumerate(nav_links[:4]):
            try:
                # Get link properties
                href = await link.get_attribute('href')
                text = await link.inner_text()
                classes = await link.get_attribute('class')
                is_visible = await link.is_visible()
                is_enabled = await link.is_enabled()

                # Check bounding box
                bbox = await link.bounding_box()

                print(f"\nLink {i+1}:")
                print(f"  Text: {text}")
                print(f"  Href: {href}")
                print(f"  Classes: {classes}")
                print(f"  Visible: {is_visible}")
                print(f"  Enabled: {is_enabled}")
                print(f"  Bounding box: {bbox}")

                # Try to click the link
                if is_visible and is_enabled and bbox:
                    try:
                        await link.click(timeout=1000)
                        print(f"  Click: SUCCESS")
                        # Go back
                        await page.go_back()
                        await page.wait_for_load_state('networkidle')
                    except Exception as e:
                        print(f"  Click: FAILED - {e}")
                else:
                    print(f"  Click: SKIPPED - not clickable")

            except Exception as e:
                print(f"Error testing link {i}: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_links())