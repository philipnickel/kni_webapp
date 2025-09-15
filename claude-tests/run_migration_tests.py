"""
Comprehensive test runner for DaisyUI to Flowbite migration verification.
Runs all migration-related tests and generates detailed reports.
"""

import pytest
import sys
import os
import json
import time
from pathlib import Path
from typing import Dict, List, Any


# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Test modules to run
MIGRATION_TEST_MODULES = [
    'test_flowbite_migration',
    'test_component_functionality',
    'test_responsive_design',
    'test_theme_switching',
    'test_migration_accessibility',
    'test_component_rendering'
]

# Test categories and their importance
TEST_CATEGORIES = {
    'critical': [
        'test_flowbite_migration',
        'test_component_functionality',
        'test_migration_accessibility'
    ],
    'important': [
        'test_responsive_design',
        'test_theme_switching',
        'test_component_rendering'
    ],
    'informational': []
}


class MigrationTestRunner:
    """Comprehensive test runner for migration verification."""

    def __init__(self):
        self.test_results = {}
        self.reports_dir = Path(__file__).parent / 'migration_reports'
        self.reports_dir.mkdir(exist_ok=True)
        self.start_time = time.time()

    def run_migration_tests(self, verbose: bool = True) -> Dict[str, Any]:
        """Run all migration tests and collect results."""
        print("🚀 Starting DaisyUI to Flowbite Migration Test Suite")
        print("=" * 60)

        overall_results = {
            'timestamp': self.start_time,
            'test_modules': {},
            'summary': {
                'total_modules': len(MIGRATION_TEST_MODULES),
                'passed_modules': 0,
                'failed_modules': 0,
                'skipped_modules': 0
            },
            'issues_found': [],
            'recommendations': []
        }

        for module_name in MIGRATION_TEST_MODULES:
            print(f"\n📋 Running {module_name}...")

            try:
                # Run pytest for specific module
                test_file = Path(__file__).parent / f"{module_name}.py"

                if not test_file.exists():
                    print(f"❌ Test file not found: {test_file}")
                    overall_results['test_modules'][module_name] = {
                        'status': 'error',
                        'error': 'Test file not found'
                    }
                    overall_results['summary']['failed_modules'] += 1
                    continue

                # Configure pytest args
                pytest_args = [
                    str(test_file),
                    '-v' if verbose else '-q',
                    '--tb=short',
                    '--disable-warnings',
                    f'--junitxml={self.reports_dir}/{module_name}_results.xml'
                ]

                # Run pytest programmatically
                exit_code = pytest.main(pytest_args)

                if exit_code == 0:
                    print(f"✅ {module_name} - PASSED")
                    overall_results['test_modules'][module_name] = {'status': 'passed'}
                    overall_results['summary']['passed_modules'] += 1
                elif exit_code == 5:  # No tests collected
                    print(f"⚠️  {module_name} - SKIPPED (No tests collected)")
                    overall_results['test_modules'][module_name] = {'status': 'skipped'}
                    overall_results['summary']['skipped_modules'] += 1
                else:
                    print(f"❌ {module_name} - FAILED (exit code: {exit_code})")
                    overall_results['test_modules'][module_name] = {
                        'status': 'failed',
                        'exit_code': exit_code
                    }
                    overall_results['summary']['failed_modules'] += 1

            except Exception as e:
                print(f"❌ {module_name} - ERROR: {str(e)}")
                overall_results['test_modules'][module_name] = {
                    'status': 'error',
                    'error': str(e)
                }
                overall_results['summary']['failed_modules'] += 1

        # Generate summary report
        self.generate_summary_report(overall_results)

        return overall_results

    def generate_summary_report(self, results: Dict[str, Any]) -> None:
        """Generate comprehensive summary report."""
        print("\n" + "=" * 60)
        print("📊 MIGRATION TEST SUMMARY")
        print("=" * 60)

        # Test execution summary
        summary = results['summary']
        total = summary['total_modules']
        passed = summary['passed_modules']
        failed = summary['failed_modules']
        skipped = summary['skipped_modules']

        print(f"Total Test Modules: {total}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"⚠️  Skipped: {skipped}")

        success_rate = (passed / total) * 100 if total > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")

        # Categorize results
        critical_passed = 0
        critical_total = 0

        for module in TEST_CATEGORIES['critical']:
            critical_total += 1
            if results['test_modules'].get(module, {}).get('status') == 'passed':
                critical_passed += 1

        critical_success_rate = (critical_passed / critical_total) * 100 if critical_total > 0 else 0

        print(f"\n🔴 Critical Tests: {critical_passed}/{critical_total} passed ({critical_success_rate:.1f}%)")

        # Migration status assessment
        print(f"\n🔍 MIGRATION STATUS ASSESSMENT")
        print("-" * 40)

        if critical_success_rate >= 100:
            print("🟢 MIGRATION STATUS: EXCELLENT")
            print("All critical tests passed. Migration appears successful.")
        elif critical_success_rate >= 80:
            print("🟡 MIGRATION STATUS: GOOD")
            print("Most critical tests passed. Minor issues may need attention.")
        elif critical_success_rate >= 60:
            print("🟠 MIGRATION STATUS: NEEDS ATTENTION")
            print("Some critical tests failed. Review and fix issues before deployment.")
        else:
            print("🔴 MIGRATION STATUS: CRITICAL ISSUES")
            print("Major critical tests failed. Migration needs significant work.")

        # Recommendations
        recommendations = self.generate_recommendations(results)
        if recommendations:
            print(f"\n💡 RECOMMENDATIONS")
            print("-" * 40)
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")

        # Save detailed report
        report_file = self.reports_dir / 'migration_test_summary.json'
        results['execution_time'] = time.time() - self.start_time
        results['recommendations'] = recommendations

        with open(report_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"\n📄 Detailed report saved to: {report_file}")

    def generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on test results."""
        recommendations = []

        failed_modules = [
            module for module, result in results['test_modules'].items()
            if result.get('status') in ['failed', 'error']
        ]

        # Specific recommendations based on failed modules
        if 'test_flowbite_migration' in failed_modules:
            recommendations.append(
                "Flowbite migration verification failed. Check that Flowbite CSS/JS are properly loaded and configured."
            )

        if 'test_component_functionality' in failed_modules:
            recommendations.append(
                "Component functionality tests failed. Review interactive elements and ensure proper event handling."
            )

        if 'test_migration_accessibility' in failed_modules:
            recommendations.append(
                "Accessibility tests failed. Review ARIA attributes, keyboard navigation, and WCAG compliance."
            )

        if 'test_responsive_design' in failed_modules:
            recommendations.append(
                "Responsive design tests failed. Check breakpoints, mobile navigation, and viewport handling."
            )

        if 'test_theme_switching' in failed_modules:
            recommendations.append(
                "Theme switching tests failed. Verify theme.js is loaded and theme switching functionality works."
            )

        if 'test_component_rendering' in failed_modules:
            recommendations.append(
                "Component rendering tests failed. Check CSS classes, styling, and visual consistency."
            )

        # General recommendations
        if len(failed_modules) > 0:
            recommendations.append(
                "Run individual test modules with -v flag for detailed failure information."
            )

        if results['summary']['failed_modules'] == 0:
            recommendations.extend([
                "All tests passed! Consider running performance tests and cross-browser validation.",
                "Monitor for any visual regressions in production environment.",
                "Document the migration process and update team guidelines."
            ])

        return recommendations

    def run_specific_category(self, category: str) -> Dict[str, Any]:
        """Run tests for a specific category."""
        if category not in TEST_CATEGORIES:
            raise ValueError(f"Unknown category: {category}")

        modules_to_run = TEST_CATEGORIES[category]
        print(f"🎯 Running {category} tests: {', '.join(modules_to_run)}")

        # Temporarily update the modules list
        original_modules = MIGRATION_TEST_MODULES.copy()
        global MIGRATION_TEST_MODULES
        MIGRATION_TEST_MODULES = modules_to_run

        try:
            results = self.run_migration_tests()
        finally:
            MIGRATION_TEST_MODULES = original_modules

        return results


def main():
    """Main entry point for test execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Run DaisyUI to Flowbite migration tests')
    parser.add_argument('--category', choices=['critical', 'important', 'informational', 'all'],
                       default='all', help='Test category to run')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    parser.add_argument('--module', help='Run specific test module only')

    args = parser.parse_args()

    runner = MigrationTestRunner()

    try:
        if args.module:
            # Run specific module
            if args.module in MIGRATION_TEST_MODULES:
                global MIGRATION_TEST_MODULES
                MIGRATION_TEST_MODULES = [args.module]
                results = runner.run_migration_tests(verbose=args.verbose)
            else:
                print(f"❌ Unknown module: {args.module}")
                print(f"Available modules: {', '.join(MIGRATION_TEST_MODULES)}")
                return 1

        elif args.category == 'all':
            # Run all tests
            results = runner.run_migration_tests(verbose=args.verbose)
        else:
            # Run specific category
            results = runner.run_specific_category(args.category)

        # Exit with appropriate code
        if results['summary']['failed_modules'] > 0:
            return 1
        else:
            return 0

    except KeyboardInterrupt:
        print("\n⚠️  Test execution interrupted by user")
        return 130
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        return 1


if __name__ == '__main__':
    exit(main())