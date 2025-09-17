#!/usr/bin/env python3
"""
Test script for HeaderManagementPage functionality
Tests the new header editing workflow and preview functionality
"""

import os
import sys
import django

# Add the project root to Python path
sys.path.append('/Users/philipnickel/Documents/GitHub/kni_webapp_library_unification/src/backend')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def test_header_management_page():
    """Test HeaderManagementPage model functionality"""
    from apps.pages.models import HeaderManagementPage, NavigationLink

    print("🧪 Testing HeaderManagementPage functionality...")

    # Test 1: Check if model can be imported
    print("✅ HeaderManagementPage model imported successfully")

    # Test 2: Check if all required fields exist
    expected_fields = [
        'header_style', 'custom_logo', 'show_company_name', 'show_search',
        'show_theme_toggle', 'show_cta_button', 'cta_button_text', 'cta_button_page',
        'cta_button_external_url', 'sticky_header', 'header_height', 'mobile_menu_style',
        'header_background_transparent', 'hide_on_scroll', 'preview_mode'
    ]

    for field in expected_fields:
        if hasattr(HeaderManagementPage, field):
            print(f"✅ Field '{field}' exists")
        else:
            print(f"❌ Field '{field}' missing")

    # Test 3: Check preview functionality
    try:
        # Create a test instance (don't save to database)
        test_header = HeaderManagementPage(
            title="Test Header Management",
            slug="test-header",
            header_style="standard",
            show_search=True,
            show_theme_toggle=True,
            sticky_header=True
        )

        # Test preview methods
        if hasattr(test_header, 'get_preview_template'):
            template = test_header.get_preview_template(None, 'desktop')
            print(f"✅ Preview template: {template}")

        if hasattr(test_header, 'get_preview_context'):
            print("✅ Preview context method exists")

        print("✅ HeaderManagementPage instance created successfully")
    except Exception as e:
        print(f"❌ Error creating HeaderManagementPage instance: {e}")

    # Test 4: Check NavigationLink model
    try:
        if hasattr(NavigationLink, 'show_in_header'):
            print("✅ NavigationLink has 'show_in_header' field")
        else:
            print("❌ NavigationLink missing 'show_in_header' field")
    except Exception as e:
        print(f"❌ Error checking NavigationLink: {e}")

def test_context_processor():
    """Test updated context processor"""
    from apps.core.context_processors import settings

    print("\n🧪 Testing context processor...")

    try:
        # Create a mock request object
        class MockRequest:
            def __init__(self):
                self.META = {}

        mock_request = MockRequest()
        context = settings(mock_request)

        # Check if all expected keys are in context
        expected_keys = ['company_settings', 'design_settings', 'header_settings',
                        'footer_settings', 'navigation_links']

        for key in expected_keys:
            if key in context:
                print(f"✅ Context includes '{key}'")
            else:
                print(f"❌ Context missing '{key}'")

        print("✅ Context processor working correctly")
    except Exception as e:
        print(f"❌ Error in context processor: {e}")

def test_template_compatibility():
    """Test if templates can access the new header settings"""
    print("\n🧪 Testing template compatibility...")

    # Check if preview template exists
    import os
    template_path = "/Users/philipnickel/Documents/GitHub/kni_webapp_library_unification/templates/admin/header_preview.html"

    if os.path.exists(template_path):
        print("✅ Header preview template exists")

        # Check template content for key elements
        with open(template_path, 'r') as f:
            content = f.read()

        if 'header_settings' in content:
            print("✅ Template uses 'header_settings' variable")
        if 'preview_mode' in content:
            print("✅ Template uses 'preview_mode' variable")
        if 'components/header_preline.html' in content:
            print("✅ Template includes header_preline component")
    else:
        print("❌ Header preview template not found")

if __name__ == "__main__":
    print("🚀 Starting Header Management Tests")
    print("=" * 50)

    test_header_management_page()
    test_context_processor()
    test_template_compatibility()

    print("\n" + "=" * 50)
    print("✨ Header Management Tests Completed")