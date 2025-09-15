#!/usr/bin/env python
"""
Accessibility test runner for JCleemannByg website.

This script runs the accessibility test suite and generates reports.
"""

import os
import sys
import django
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_test')
django.setup()

def run_accessibility_tests():
    """Run accessibility tests with proper configuration."""
    import pytest

    # Test arguments
    test_args = [
        'claude-tests/',  # Test directory
        '-v',  # Verbose output
        '--tb=short',  # Short traceback
        '-m', 'accessibility',  # Only accessibility tests
        '--strict-markers',  # Strict marker validation
        '--html=claude-tests/accessibility_report.html',  # HTML report
        '--self-contained-html',  # Self-contained HTML
    ]

    # Add coverage if requested
    if '--coverage' in sys.argv:
        test_args.extend([
            '--cov=apps',
            '--cov-report=html:claude-tests/accessibility_coverage',
            '--cov-report=term-missing'
        ])

    # Add specific test markers if requested
    if '--wcag' in sys.argv:
        test_args.extend(['-m', 'wcag'])
    elif '--visual' in sys.argv:
        test_args.extend(['-m', 'visual_regression'])
    elif '--keyboard' in sys.argv:
        test_args.extend(['-m', 'keyboard_navigation'])

    print("Running accessibility tests...")
    print(f"Test arguments: {' '.join(test_args)}")

    # Run tests
    exit_code = pytest.main(test_args)

    print(f"\nAccessibility tests completed with exit code: {exit_code}")

    if exit_code == 0:
        print("✅ All accessibility tests passed!")
    else:
        print("❌ Some accessibility tests failed. Check the report for details.")

    return exit_code


def run_theme_tests():
    """Run tests for the Frostbite carpenter theme."""
    themes = ['light', 'dark', 'corporate', 'business', 'emerald']

    print("Running theme-specific accessibility tests...")

    for theme in themes:
        print(f"\nTesting theme: {theme}")
        test_args = [
            'claude-tests/test_accessibility.py::TestWCAGCompliance::test_wcag_aa_compliance_by_theme_and_page',
            '-v',
            '--tb=short',
            '-k', f'theme_{theme}',
        ]

        exit_code = pytest.main(test_args)
        if exit_code != 0:
            print(f"❌ Theme {theme} failed accessibility tests")
            return exit_code
        else:
            print(f"✅ Theme {theme} passed accessibility tests")

    return 0


def generate_baseline_screenshots():
    """Generate baseline screenshots for visual regression testing."""
    print("Generating baseline screenshots...")

    test_args = [
        'claude-tests/test_visual_regression.py',
        '-v',
        '--tb=short',
        '-m', 'visual_regression'
    ]

    # Set environment variable to update baselines
    os.environ['UPDATE_BASELINES'] = '1'

    exit_code = pytest.main(test_args)

    # Clean up environment
    if 'UPDATE_BASELINES' in os.environ:
        del os.environ['UPDATE_BASELINES']

    if exit_code == 0:
        print("✅ Baseline screenshots generated successfully")
    else:
        print("❌ Failed to generate baseline screenshots")

    return exit_code


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python run_accessibility_tests.py [command] [options]")
        print("Commands:")
        print("  run         - Run all accessibility tests")
        print("  themes      - Run theme-specific tests")
        print("  baselines   - Generate baseline screenshots")
        print("  wcag        - Run only WCAG compliance tests")
        print("  visual      - Run only visual regression tests")
        print("  keyboard    - Run only keyboard navigation tests")
        print("\nOptions:")
        print("  --coverage  - Include coverage reporting")
        return 1

    command = sys.argv[1]

    try:
        if command == 'run':
            return run_accessibility_tests()
        elif command == 'themes':
            return run_theme_tests()
        elif command == 'baselines':
            return generate_baseline_screenshots()
        elif command in ['wcag', 'visual', 'keyboard']:
            sys.argv.insert(1, f'--{command}')
            return run_accessibility_tests()
        else:
            print(f"Unknown command: {command}")
            return 1
    except KeyboardInterrupt:
        print("\n⚠️  Tests interrupted by user")
        return 1
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)