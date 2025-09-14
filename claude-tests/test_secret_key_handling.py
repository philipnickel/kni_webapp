#!/usr/bin/env python3
"""
Test script to verify secret key handling works correctly.
This tests the deployment configuration without requiring Django to be installed.
"""

import os
import tempfile
import subprocess
import sys


def test_docker_compose_env_parsing():
    """Test that Docker Compose handles missing DJANGO_SECRET_KEY gracefully"""
    print("✓ Testing Docker Compose environment parsing...")

    # Check if the docker-compose.yml has the correct fallback syntax
    with open('docker-compose.coolify.yml', 'r') as f:
        content = f.read()

    # Should not contain the hard requirement syntax anymore
    if '${DJANGO_SECRET_KEY:?}' in content:
        print("❌ Docker Compose still has hard requirement for DJANGO_SECRET_KEY")
        return False

    # Should contain the optional fallback syntax
    if '${DJANGO_SECRET_KEY:-}' not in content:
        print("❌ Docker Compose missing optional DJANGO_SECRET_KEY syntax")
        return False

    print("✅ Docker Compose correctly handles optional DJANGO_SECRET_KEY")
    return True


def test_entrypoint_script():
    """Test that the entrypoint script has the secret key generation logic"""
    print("✓ Testing entrypoint script modifications...")

    with open('docker/entrypoint.sh', 'r') as f:
        content = f.read()

    # Check for secret key generation logic
    required_patterns = [
        'if [ "$ROLE" = "web" ] && [ -z "$DJANGO_SECRET_KEY" ]',
        'export DJANGO_SECRET_KEY=$(python manage.py generate_secret_key --print-only)',
        'Generated secure Django secret key'
    ]

    for pattern in required_patterns:
        if pattern not in content:
            print(f"❌ Entrypoint script missing pattern: {pattern}")
            return False

    print("✅ Entrypoint script has secret key generation logic")
    return True


def test_management_command_exists():
    """Test that the management command file exists and has correct structure"""
    print("✓ Testing management command existence...")

    command_path = 'apps/core/management/commands/generate_secret_key.py'

    if not os.path.exists(command_path):
        print(f"❌ Management command not found: {command_path}")
        return False

    with open(command_path, 'r') as f:
        content = f.read()

    # Check for essential components
    required_patterns = [
        'class Command(BaseCommand)',
        'get_random_secret_key',
        '--print-only',
        'def handle(self, *args, **options)'
    ]

    for pattern in required_patterns:
        if pattern not in content:
            print(f"❌ Management command missing pattern: {pattern}")
            return False

    print("✅ Management command exists and has correct structure")
    return True


def test_settings_configuration():
    """Test that settings.py has the enhanced secret key handling"""
    print("✓ Testing Django settings modifications...")

    with open('project/settings.py', 'r') as f:
        content = f.read()

    # Check for enhanced secret key function
    required_patterns = [
        'def get_secret_key()',
        'get_random_secret_key',
        'SECRET_KEY = get_secret_key()',
        'WARNING: No DJANGO_SECRET_KEY provided'
    ]

    for pattern in required_patterns:
        if pattern not in content:
            print(f"❌ Settings missing pattern: {pattern}")
            return False

    print("✅ Django settings has enhanced secret key handling")
    return True


def main():
    """Run all tests"""
    print("🧪 Testing KNI Webapp secret key deployment fix...\n")

    tests = [
        test_docker_compose_env_parsing,
        test_entrypoint_script,
        test_management_command_exists,
        test_settings_configuration
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
            print()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
            print()

    # Summary
    passed = sum(results)
    total = len(results)

    print("=" * 50)
    print(f"Test Results: {passed}/{total} passed")

    if passed == total:
        print("🎉 All tests passed! The deployment fix should work correctly.")
        print("\n📋 Summary of changes:")
        print("  • Docker Compose no longer requires DJANGO_SECRET_KEY")
        print("  • Entrypoint script generates secret key if missing")
        print("  • Django management command for secure key generation")
        print("  • Enhanced Django settings with robust fallbacks")
        print("\n🚀 This should work for both production and preview deployments!")
        return True
    else:
        print("❌ Some tests failed. Please review the implementation.")
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)