"""
Migration validation script for DaisyUI to Flowbite migration.
Performs static analysis and configuration validation without requiring a running server.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
import time


class MigrationValidator:
    """Validates the DaisyUI to Flowbite migration through static analysis."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.validation_results = {
            'timestamp': time.time(),
            'checks': {},
            'issues': [],
            'recommendations': [],
            'migration_score': 0
        }

    def validate_migration(self) -> Dict[str, Any]:
        """Run all migration validation checks."""
        print("🔍 Starting DaisyUI to Flowbite Migration Validation")
        print("=" * 60)

        # Run validation checks
        checks = [
            self.check_flowbite_installation,
            self.check_tailwind_configuration,
            self.check_template_migration,
            self.check_javascript_migration,
            self.check_css_migration,
            self.check_package_json_migration,
            self.check_accessibility_preservation,
            self.check_theme_system_migration
        ]

        for check_func in checks:
            try:
                check_name = check_func.__name__.replace('check_', '').replace('_', ' ').title()
                print(f"\n🔎 {check_name}...")

                result = check_func()
                self.validation_results['checks'][check_func.__name__] = result

                if result['status'] == 'passed':
                    print(f"✅ {check_name}: PASSED")
                elif result['status'] == 'warning':
                    print(f"⚠️  {check_name}: WARNING - {result.get('message', '')}")
                else:
                    print(f"❌ {check_name}: FAILED - {result.get('message', '')}")

                if result.get('issues'):
                    self.validation_results['issues'].extend(result['issues'])

                if result.get('recommendations'):
                    self.validation_results['recommendations'].extend(result['recommendations'])

            except Exception as e:
                error_result = {
                    'status': 'error',
                    'message': str(e),
                    'issues': [f"Error in {check_func.__name__}: {str(e)}"]
                }
                self.validation_results['checks'][check_func.__name__] = error_result
                print(f"❌ {check_name}: ERROR - {str(e)}")

        # Calculate migration score
        self.calculate_migration_score()

        # Generate final report
        self.generate_final_report()

        return self.validation_results

    def check_flowbite_installation(self) -> Dict[str, Any]:
        """Check if Flowbite is properly installed and configured."""
        issues = []
        recommendations = []

        # Check package.json for Flowbite dependency
        package_json_path = self.project_root / 'package.json'
        if package_json_path.exists():
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)

            # Check for Flowbite in dependencies
            dependencies = package_data.get('dependencies', {})
            dev_dependencies = package_data.get('devDependencies', {})

            if 'flowbite' not in dependencies and 'flowbite' not in dev_dependencies:
                issues.append("Flowbite package not found in package.json dependencies")
            else:
                flowbite_version = dependencies.get('flowbite') or dev_dependencies.get('flowbite')
                print(f"   Found Flowbite version: {flowbite_version}")
        else:
            issues.append("package.json not found")

        # Check for Flowbite CDN in templates
        base_template = self.project_root / 'templates' / 'base.html'
        if base_template.exists():
            with open(base_template, 'r') as f:
                template_content = f.read()

            # Check for Flowbite JavaScript
            if 'flowbite' in template_content.lower():
                print("   Flowbite JavaScript reference found in base template")
            else:
                issues.append("Flowbite JavaScript not found in base template")
        else:
            issues.append("Base template not found")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'Flowbite installation verified'}
        else:
            return {
                'status': 'failed',
                'message': 'Flowbite installation issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_tailwind_configuration(self) -> Dict[str, Any]:
        """Check Tailwind CSS configuration for Flowbite integration."""
        issues = []
        recommendations = []

        tailwind_config = self.project_root / 'tailwind.config.js'
        if tailwind_config.exists():
            with open(tailwind_config, 'r') as f:
                config_content = f.read()

            # Check for Flowbite plugin
            if 'flowbite/plugin' in config_content or 'flowbite' in config_content:
                print("   Flowbite plugin found in Tailwind config")
            else:
                issues.append("Flowbite plugin not found in Tailwind configuration")

            # Check for Flowbite content path
            if 'flowbite/**/*.js' in config_content:
                print("   Flowbite content path configured")
            else:
                recommendations.append("Add 'node_modules/flowbite/**/*.js' to Tailwind content array")

            # Check for DaisyUI remnants
            if 'daisyui' in config_content.lower():
                issues.append("DaisyUI references still found in Tailwind config")

        else:
            issues.append("tailwind.config.js not found")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'Tailwind configuration is properly set up for Flowbite'}
        else:
            return {
                'status': 'failed' if issues else 'warning',
                'message': 'Tailwind configuration issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_template_migration(self) -> Dict[str, Any]:
        """Check template files for DaisyUI to Flowbite migration."""
        issues = []
        recommendations = []
        templates_checked = 0
        daisyui_classes_found = 0

        templates_dir = self.project_root / 'templates'
        if not templates_dir.exists():
            return {'status': 'failed', 'message': 'Templates directory not found'}

        # DaisyUI-specific classes that should be migrated
        daisyui_classes = [
            'btn-ghost', 'btn-outline', 'btn-wide', 'btn-block',
            'card-compact', 'card-side', 'card-normal',
            'hero-content', 'hero-overlay',
            'navbar-start', 'navbar-center', 'navbar-end',
            'dropdown-content', 'dropdown-top', 'dropdown-bottom',
            'menu-horizontal', 'menu-vertical',
            'modal-box', 'modal-backdrop', 'modal-action',
            'alert-info', 'alert-success', 'alert-warning', 'alert-error',
            'badge-primary', 'badge-secondary', 'badge-accent',
            'tabs-bordered', 'tabs-lifted', 'tab-active',
            'collapse-title', 'collapse-content',
            'indicator-item', 'indicator-start', 'indicator-center'
        ]

        # Flowbite equivalent classes or patterns
        flowbite_patterns = [
            'data-modal-toggle', 'data-modal-target', 'data-modal-hide',
            'data-dropdown-toggle', 'data-dropdown-placement',
            'data-tabs-target', 'data-accordion-target',
            'data-tooltip-target', 'data-tooltip-placement'
        ]

        # Scan template files
        for template_file in templates_dir.rglob('*.html'):
            templates_checked += 1

            with open(template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()

            # Check for DaisyUI classes
            for daisyui_class in daisyui_classes:
                if daisyui_class in template_content:
                    daisyui_classes_found += 1
                    issues.append(f"DaisyUI class '{daisyui_class}' found in {template_file.relative_to(self.project_root)}")

            # Check for Flowbite patterns
            flowbite_found = any(pattern in template_content for pattern in flowbite_patterns)

        print(f"   Scanned {templates_checked} template files")
        print(f"   Found {daisyui_classes_found} DaisyUI class references")

        if daisyui_classes_found > 0:
            recommendations.append("Replace remaining DaisyUI classes with Flowbite equivalents")

        if daisyui_classes_found == 0:
            return {'status': 'passed', 'message': 'No DaisyUI classes found in templates'}
        elif daisyui_classes_found < 10:
            return {
                'status': 'warning',
                'message': f'Few DaisyUI classes still found ({daisyui_classes_found})',
                'issues': issues[:5],  # Show first 5 issues
                'recommendations': recommendations
            }
        else:
            return {
                'status': 'failed',
                'message': f'Many DaisyUI classes still found ({daisyui_classes_found})',
                'issues': issues[:10],  # Show first 10 issues
                'recommendations': recommendations
            }

    def check_javascript_migration(self) -> Dict[str, Any]:
        """Check JavaScript files for DaisyUI to Flowbite migration."""
        issues = []
        recommendations = []

        # Check theme.js file
        theme_js = self.project_root / 'static' / 'js' / 'theme.js'
        if theme_js.exists():
            with open(theme_js, 'r') as f:
                theme_content = f.read()

            # Check for theme switching functionality
            if 'switchTheme' in theme_content and 'data-theme' in theme_content:
                print("   Theme switching functionality found")
            else:
                issues.append("Theme switching functionality not found in theme.js")

            # Check for DaisyUI-specific code
            if 'daisyui' in theme_content.lower():
                recommendations.append("Remove DaisyUI-specific references from theme.js")

        else:
            issues.append("theme.js file not found")

        # Check base template for Flowbite JavaScript
        base_template = self.project_root / 'templates' / 'base.html'
        if base_template.exists():
            with open(base_template, 'r') as f:
                template_content = f.read()

            # Check for Flowbite initialization
            if 'flowbite' in template_content.lower() and 'script' in template_content:
                print("   Flowbite JavaScript loading found")
            else:
                issues.append("Flowbite JavaScript loading not found in base template")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'JavaScript migration completed successfully'}
        else:
            return {
                'status': 'failed' if len(issues) > 1 else 'warning',
                'message': 'JavaScript migration issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_css_migration(self) -> Dict[str, Any]:
        """Check CSS files for migration completeness."""
        issues = []
        recommendations = []

        # Check main CSS file
        css_files = [
            self.project_root / 'static' / 'css' / 'site.css',
            self.project_root / 'src' / 'css' / 'input.css',
        ]

        for css_file in css_files:
            if css_file.exists():
                with open(css_file, 'r') as f:
                    css_content = f.read()

                # Check for DaisyUI imports
                if '@import "daisyui"' in css_content or 'daisyui' in css_content:
                    issues.append(f"DaisyUI imports found in {css_file.relative_to(self.project_root)}")

                # Check for Flowbite imports
                if 'flowbite' in css_content.lower():
                    print(f"   Flowbite references found in {css_file.name}")

                # Check for custom component styles
                if '.btn' in css_content or '.card' in css_content:
                    print(f"   Custom component styles found in {css_file.name}")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'CSS migration completed successfully'}
        else:
            return {
                'status': 'warning',
                'message': 'CSS migration issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_package_json_migration(self) -> Dict[str, Any]:
        """Check package.json for migration completeness."""
        issues = []
        recommendations = []

        package_json_path = self.project_root / 'package.json'
        if package_json_path.exists():
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)

            dependencies = {**package_data.get('dependencies', {}), **package_data.get('devDependencies', {})}

            # Check for DaisyUI remnants
            if 'daisyui' in dependencies:
                issues.append("DaisyUI still listed in package.json dependencies")

            # Check for Flowbite
            if 'flowbite' in dependencies:
                print(f"   Flowbite dependency found: {dependencies['flowbite']}")
            else:
                issues.append("Flowbite dependency not found in package.json")

            # Check for Tailwind CSS
            if 'tailwindcss' in dependencies:
                print(f"   Tailwind CSS found: {dependencies['tailwindcss']}")
            else:
                issues.append("Tailwind CSS dependency not found")

        else:
            issues.append("package.json not found")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'Package dependencies properly configured'}
        else:
            return {
                'status': 'failed',
                'message': 'Package configuration issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_accessibility_preservation(self) -> Dict[str, Any]:
        """Check that accessibility features are preserved after migration."""
        issues = []
        recommendations = []

        base_template = self.project_root / 'templates' / 'base.html'
        if base_template.exists():
            with open(base_template, 'r') as f:
                template_content = f.read()

            # Check for skip links
            if 'skip' in template_content.lower() and 'main-content' in template_content:
                print("   Skip links found")
            else:
                issues.append("Skip links not found in base template")

            # Check for ARIA attributes
            aria_attributes = ['aria-label', 'aria-expanded', 'aria-haspopup', 'role']
            aria_found = sum(1 for attr in aria_attributes if attr in template_content)

            if aria_found >= 3:
                print(f"   ARIA attributes found ({aria_found} types)")
            else:
                recommendations.append("Add more ARIA attributes for better accessibility")

            # Check for semantic landmarks
            landmarks = ['<main', '<nav', '<header', '<footer', 'role="banner"', 'role="navigation"']
            landmark_found = sum(1 for landmark in landmarks if landmark in template_content)

            if landmark_found >= 3:
                print(f"   Semantic landmarks found ({landmark_found} types)")
            else:
                recommendations.append("Add semantic landmarks for better accessibility")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'Accessibility features preserved'}
        else:
            return {
                'status': 'warning',
                'message': 'Accessibility issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def check_theme_system_migration(self) -> Dict[str, Any]:
        """Check theme system migration from DaisyUI to Flowbite-compatible."""
        issues = []
        recommendations = []

        theme_js = self.project_root / 'static' / 'js' / 'theme.js'
        if theme_js.exists():
            with open(theme_js, 'r') as f:
                theme_content = f.read()

            # Check for theme functions
            required_functions = ['switchTheme', 'getCurrentTheme', 'getAvailableThemes']
            for func in required_functions:
                if func in theme_content:
                    print(f"   Theme function '{func}' found")
                else:
                    issues.append(f"Theme function '{func}' not found")

            # Check for theme persistence
            if 'localStorage' in theme_content:
                print("   Theme persistence functionality found")
            else:
                recommendations.append("Add theme persistence using localStorage")

            # Check for available themes
            if 'AVAILABLE_THEMES' in theme_content or 'themes' in theme_content:
                print("   Theme configuration found")
            else:
                issues.append("Theme configuration not found")

        else:
            issues.append("Theme system file (theme.js) not found")

        if len(issues) == 0:
            return {'status': 'passed', 'message': 'Theme system successfully migrated'}
        else:
            return {
                'status': 'failed' if len(issues) > 2 else 'warning',
                'message': 'Theme system migration issues found',
                'issues': issues,
                'recommendations': recommendations
            }

    def calculate_migration_score(self) -> None:
        """Calculate overall migration score based on check results."""
        total_checks = len(self.validation_results['checks'])
        if total_checks == 0:
            self.validation_results['migration_score'] = 0
            return

        passed_checks = sum(1 for result in self.validation_results['checks'].values()
                           if result['status'] == 'passed')
        warning_checks = sum(1 for result in self.validation_results['checks'].values()
                            if result['status'] == 'warning')

        # Calculate score: passed = 100%, warning = 70%, failed = 0%
        score = (passed_checks * 100 + warning_checks * 70) / total_checks
        self.validation_results['migration_score'] = round(score, 1)

    def generate_final_report(self) -> None:
        """Generate final migration validation report."""
        print("\n" + "=" * 60)
        print("📊 MIGRATION VALIDATION SUMMARY")
        print("=" * 60)

        score = self.validation_results['migration_score']
        print(f"Migration Score: {score}%")

        # Status assessment
        if score >= 90:
            status = "🟢 EXCELLENT"
            assessment = "Migration is very successful with minimal issues."
        elif score >= 75:
            status = "🟡 GOOD"
            assessment = "Migration is mostly successful with some minor issues."
        elif score >= 60:
            status = "🟠 NEEDS ATTENTION"
            assessment = "Migration has some issues that should be addressed."
        else:
            status = "🔴 CRITICAL"
            assessment = "Migration has significant issues that need immediate attention."

        print(f"Status: {status}")
        print(f"Assessment: {assessment}")

        # Check results summary
        check_results = self.validation_results['checks']
        passed = sum(1 for r in check_results.values() if r['status'] == 'passed')
        warnings = sum(1 for r in check_results.values() if r['status'] == 'warning')
        failed = sum(1 for r in check_results.values() if r['status'] == 'failed')
        errors = sum(1 for r in check_results.values() if r['status'] == 'error')

        print(f"\nCheck Results:")
        print(f"✅ Passed: {passed}")
        print(f"⚠️  Warnings: {warnings}")
        print(f"❌ Failed: {failed}")
        print(f"🚫 Errors: {errors}")

        # Show issues and recommendations
        if self.validation_results['issues']:
            print(f"\n🔍 Issues Found ({len(self.validation_results['issues'])}):")
            for i, issue in enumerate(self.validation_results['issues'][:5], 1):
                print(f"{i}. {issue}")
            if len(self.validation_results['issues']) > 5:
                print(f"   ... and {len(self.validation_results['issues']) - 5} more")

        if self.validation_results['recommendations']:
            print(f"\n💡 Recommendations ({len(self.validation_results['recommendations'])}):")
            for i, rec in enumerate(self.validation_results['recommendations'][:5], 1):
                print(f"{i}. {rec}")
            if len(self.validation_results['recommendations']) > 5:
                print(f"   ... and {len(self.validation_results['recommendations']) - 5} more")

        # Save detailed report
        reports_dir = Path(__file__).parent / 'migration_reports'
        reports_dir.mkdir(exist_ok=True)

        report_file = reports_dir / 'migration_validation_report.json'
        with open(report_file, 'w') as f:
            json.dump(self.validation_results, f, indent=2, default=str)

        print(f"\n📄 Detailed report saved to: {report_file}")


def main():
    """Main entry point for migration validation."""
    project_root = Path(__file__).parent.parent
    validator = MigrationValidator(project_root)

    try:
        results = validator.validate_migration()

        # Exit with appropriate code based on score
        score = results['migration_score']
        if score >= 75:
            return 0  # Success
        elif score >= 50:
            return 1  # Warning
        else:
            return 2  # Critical issues

    except KeyboardInterrupt:
        print("\n⚠️  Validation interrupted by user")
        return 130
    except Exception as e:
        print(f"\n❌ Validation failed: {e}")
        return 1


if __name__ == '__main__':
    exit(main())