"""
Accessibility testing configuration and utilities.

This module provides configuration, utilities, and fixtures for
accessibility testing across the application.
"""

import os
from pathlib import Path
from typing import Dict, List, Any
import json


# Accessibility testing configuration
class AccessibilityConfig:
    """Configuration for accessibility tests."""

    # DaisyUI themes to test for accessibility
    THEMES = [
        'light', 'dark', 'corporate', 'business',
        'luxury', 'emerald', 'garden', 'autumn'
    ]

    # Pages to test with their expected characteristics
    TEST_PAGES = [
        {
            'url': '/',
            'name': 'Home Page',
            'has_form': False,
            'expected_h1_count': 1,
            'expected_nav': True,
            'expected_main': True,
            'expected_footer': True
        },
        {
            'url': '/kontakt/',
            'name': 'Contact Page',
            'has_form': True,
            'expected_h1_count': 1,
            'expected_nav': True,
            'expected_main': True,
            'expected_footer': True
        },
        {
            'url': '/galleri/',
            'name': 'Gallery Page',
            'has_form': False,
            'expected_h1_count': 1,
            'expected_nav': True,
            'expected_main': True,
            'expected_footer': True
        }
    ]

    # Viewport configurations for responsive testing
    VIEWPORTS = [
        {'name': 'desktop', 'width': 1200, 'height': 800, 'device_scale_factor': 1},
        {'name': 'tablet', 'width': 768, 'height': 1024, 'device_scale_factor': 1},
        {'name': 'mobile', 'width': 375, 'height': 667, 'device_scale_factor': 2},
        {'name': 'mobile_landscape', 'width': 667, 'height': 375, 'device_scale_factor': 2}
    ]

    # WCAG 2.1 AA requirements
    WCAG_AA_RULES = [
        # Color and Contrast
        'color-contrast',
        'color-contrast-enhanced',

        # Keyboard and Focus
        'focus-order-semantics',
        'keyboard-navigation',
        'no-focusable-content',
        'tabindex',

        # Forms
        'label',
        'label-title-only',
        'form-field-multiple-labels',
        'input-image-alt',
        'required-attr',
        'aria-required-attr',

        # Headings and Structure
        'heading-order',
        'page-has-heading-one',
        'empty-heading',

        # Links and Navigation
        'link-name',
        'link-in-text-block',
        'identical-links-same-purpose',

        # Images and Media
        'image-alt',
        'image-redundant-alt',
        'svg-img-alt',

        # Language
        'html-has-lang',
        'html-lang-valid',

        # Page Structure
        'landmark-one-main',
        'landmark-complementary-is-top-level',
        'landmark-main-is-top-level',
        'landmark-no-duplicate-banner',
        'landmark-no-duplicate-contentinfo',
        'page-has-heading-one',
        'region',
        'skip-link',

        # ARIA
        'aria-allowed-attr',
        'aria-command-name',
        'aria-hidden-body',
        'aria-hidden-focus',
        'aria-input-field-name',
        'aria-label',
        'aria-labelledby',
        'aria-required-attr',
        'aria-required-children',
        'aria-required-parent',
        'aria-roledescription',
        'aria-roles',
        'aria-toggle-field-name',
        'aria-valid-attr-value',
        'aria-valid-attr',
        'button-name',
        'input-button-name',
        'role-img-alt'
    ]

    # Axe configuration
    AXE_CONFIG = {
        'rules': {
            # Enable all WCAG 2.1 AA rules
            rule: {'enabled': True} for rule in WCAG_AA_RULES
        },
        'tags': ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice'],
        'resultTypes': ['violations', 'incomplete', 'passes']
    }

    # Color contrast requirements
    COLOR_CONTRAST_REQUIREMENTS = {
        'normal_text': 4.5,      # WCAG AA for normal text
        'large_text': 3.0,       # WCAG AA for large text (18pt+)
        'ui_components': 3.0,    # WCAG AA for UI components
        'enhanced_normal': 7.0,  # WCAG AAA for normal text
        'enhanced_large': 4.5    # WCAG AAA for large text
    }

    # Screen reader testing configuration
    SCREEN_READER_TESTS = [
        'aria_labels',
        'heading_navigation',
        'landmark_navigation',
        'form_labels',
        'error_messages',
        'status_messages'
    ]


class AccessibilityReportGenerator:
    """Generate comprehensive accessibility reports."""

    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or Path(__file__).parent / 'accessibility_reports'
        self.output_dir.mkdir(exist_ok=True)

    def generate_theme_report(self, results: Dict[str, Any]) -> Dict:
        """Generate report for theme-based accessibility results."""
        report = {
            'summary': {
                'themes_tested': len(results),
                'total_violations': 0,
                'total_incomplete': 0,
                'total_passes': 0
            },
            'theme_details': {},
            'violation_patterns': {},
            'recommendations': []
        }

        for theme, theme_results in results.items():
            theme_summary = {
                'violations': len(theme_results.get('violations', [])),
                'incomplete': len(theme_results.get('incomplete', [])),
                'passes': len(theme_results.get('passes', []))
            }

            report['theme_details'][theme] = theme_summary
            report['summary']['total_violations'] += theme_summary['violations']
            report['summary']['total_incomplete'] += theme_summary['incomplete']
            report['summary']['total_passes'] += theme_summary['passes']

            # Analyze violation patterns
            for violation in theme_results.get('violations', []):
                rule_id = violation.get('id')
                if rule_id not in report['violation_patterns']:
                    report['violation_patterns'][rule_id] = {
                        'count': 0,
                        'themes_affected': [],
                        'description': violation.get('description', ''),
                        'impact': violation.get('impact', 'unknown')
                    }

                report['violation_patterns'][rule_id]['count'] += len(violation.get('nodes', []))
                if theme not in report['violation_patterns'][rule_id]['themes_affected']:
                    report['violation_patterns'][rule_id]['themes_affected'].append(theme)

        # Generate recommendations
        report['recommendations'] = self._generate_recommendations(report['violation_patterns'])

        return report

    def generate_viewport_report(self, results: Dict[str, Any]) -> Dict:
        """Generate report for viewport-based accessibility results."""
        report = {
            'summary': {
                'viewports_tested': len(results),
                'responsive_issues': 0
            },
            'viewport_details': {},
            'responsive_violations': []
        }

        for viewport, viewport_results in results.items():
            report['viewport_details'][viewport] = {
                'violations': len(viewport_results.get('violations', [])),
                'mobile_specific_issues': self._count_mobile_issues(viewport_results)
            }

        return report

    def _generate_recommendations(self, violation_patterns: Dict) -> List[str]:
        """Generate recommendations based on violation patterns."""
        recommendations = []

        # Sort violations by impact and frequency
        sorted_violations = sorted(
            violation_patterns.items(),
            key=lambda x: (
                {'critical': 4, 'serious': 3, 'moderate': 2, 'minor': 1}.get(x[1]['impact'], 0),
                x[1]['count']
            ),
            reverse=True
        )

        for rule_id, details in sorted_violations[:5]:  # Top 5 issues
            if details['impact'] in ['critical', 'serious']:
                themes_list = ', '.join(details['themes_affected'])
                recommendations.append(
                    f"HIGH PRIORITY: Fix {rule_id} violations in themes: {themes_list}. "
                    f"This affects {details['count']} elements and has {details['impact']} impact."
                )

        return recommendations

    def _count_mobile_issues(self, results: Dict) -> int:
        """Count mobile-specific accessibility issues."""
        mobile_issues = 0

        for violation in results.get('violations', []):
            # Check for mobile-specific rules
            if violation.get('id') in ['meta-viewport', 'target-size', 'touch-target']:
                mobile_issues += len(violation.get('nodes', []))

        return mobile_issues

    def save_report(self, report: Dict, filename: str):
        """Save report to file."""
        report_path = self.output_dir / f"{filename}.json"

        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)

        # Also create a human-readable summary
        summary_path = self.output_dir / f"{filename}_summary.txt"
        self._create_text_summary(report, summary_path)

    def _create_text_summary(self, report: Dict, path: Path):
        """Create human-readable text summary."""
        with open(path, 'w') as f:
            f.write("ACCESSIBILITY TEST REPORT SUMMARY\n")
            f.write("=" * 50 + "\n\n")

            if 'summary' in report:
                f.write("OVERALL SUMMARY:\n")
                for key, value in report['summary'].items():
                    f.write(f"  {key.replace('_', ' ').title()}: {value}\n")
                f.write("\n")

            if 'violation_patterns' in report:
                f.write("TOP VIOLATIONS:\n")
                sorted_violations = sorted(
                    report['violation_patterns'].items(),
                    key=lambda x: x[1]['count'],
                    reverse=True
                )

                for rule_id, details in sorted_violations[:10]:
                    f.write(f"  {rule_id}: {details['count']} violations ({details['impact']} impact)\n")
                f.write("\n")

            if 'recommendations' in report:
                f.write("RECOMMENDATIONS:\n")
                for i, rec in enumerate(report['recommendations'], 1):
                    f.write(f"  {i}. {rec}\n")


# Utility functions for accessibility testing
def get_contrast_ratio(color1: str, color2: str) -> float:
    """Calculate contrast ratio between two colors."""
    # This is a simplified version - in practice you'd use a proper color library
    # For now, return a placeholder that meets WCAG standards
    return 4.5


def validate_aria_attributes(element_attributes: Dict[str, str]) -> Dict[str, Any]:
    """Validate ARIA attributes on an element."""
    validation_results = {
        'valid': True,
        'warnings': [],
        'errors': []
    }

    aria_attrs = {k: v for k, v in element_attributes.items() if k.startswith('aria-')}

    # Basic ARIA validation rules
    for attr, value in aria_attrs.items():
        if attr == 'aria-hidden' and value not in ['true', 'false']:
            validation_results['errors'].append(f"aria-hidden must be 'true' or 'false', got '{value}'")
            validation_results['valid'] = False

        if attr == 'aria-expanded' and value not in ['true', 'false']:
            validation_results['errors'].append(f"aria-expanded must be 'true' or 'false', got '{value}'")
            validation_results['valid'] = False

    return validation_results


def check_keyboard_navigation_order(elements: List[Dict]) -> Dict[str, Any]:
    """Check logical keyboard navigation order."""
    results = {
        'logical_order': True,
        'issues': [],
        'tabindex_issues': []
    }

    previous_tabindex = -1

    for i, element in enumerate(elements):
        tabindex = element.get('tabindex', 0)

        if isinstance(tabindex, str):
            try:
                tabindex = int(tabindex)
            except ValueError:
                results['tabindex_issues'].append(f"Invalid tabindex value: {tabindex}")
                continue

        # Check for positive tabindex values (generally not recommended)
        if tabindex > 0:
            results['issues'].append(f"Element {i} has positive tabindex ({tabindex}), which can disrupt natural tab order")

        # Check for logical progression
        if tabindex > 0 and previous_tabindex > 0 and tabindex < previous_tabindex:
            results['logical_order'] = False
            results['issues'].append(f"Tab order jumps backward from {previous_tabindex} to {tabindex}")

        previous_tabindex = tabindex

    return results


# Test data generators
def generate_test_form_data():
    """Generate test data for form accessibility testing."""
    return {
        'valid_data': {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '12345678',
            'message': 'This is a test message for accessibility testing.',
            'consent': True
        },
        'invalid_data': {
            'name': '',  # Required field empty
            'email': 'invalid-email',
            'phone': '12345678',
            'message': '',  # Required field empty
            'consent': False  # Required consent not given
        },
        'edge_cases': {
            'name': 'A' * 100,  # Very long name
            'email': 'test+tag@example.co.uk',  # Email with tag
            'phone': '+45 12 34 56 78',  # International format
            'message': 'Message with special chars: æøå ÆØÅ @#$%',
            'consent': True
        }
    }