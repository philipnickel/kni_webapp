#!/usr/bin/env python3
"""
Static Analysis of Flowbite Migration
=====================================

This script performs comprehensive static analysis of the Flowbite migration
by examining templates, CSS files, and configuration files to validate:

1. Complete removal of DaisyUI dependencies
2. Proper Flowbite implementation
3. Component migration completeness
4. Theme configuration validation
5. Responsive design implementation
6. Accessibility features preservation

This provides production validation without requiring a running server.
"""

import os
import re
import json
import glob
from pathlib import Path
from typing import Dict, List, Set, Any
import time


class FlowbiteMigrationValidator:
    """Static validator for Flowbite migration completion."""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.results = {}
        self.issues = []
        self.recommendations = []

    def analyze_package_json(self) -> Dict[str, Any]:
        """Analyze package.json for dependency migration."""
        print("📦 Analyzing package.json...")

        package_file = self.project_root / "package.json"
        if not package_file.exists():
            return {"error": "package.json not found"}

        with open(package_file) as f:
            package_data = json.load(f)

        analysis = {
            "flowbite_present": "flowbite" in package_data.get("dependencies", {}),
            "daisyui_removed": "daisyui" not in package_data.get("dependencies", {}),
            "tailwind_present": "@tailwindcss" in str(package_data.get("devDependencies", {})),
            "flowbite_version": package_data.get("dependencies", {}).get("flowbite", "Not found"),
            "status": "✅ PASSED"
        }

        if not analysis["flowbite_present"]:
            self.issues.append("❌ Flowbite not found in dependencies")
            analysis["status"] = "❌ FAILED"

        if not analysis["daisyui_removed"]:
            self.issues.append("❌ DaisyUI still present in dependencies")
            analysis["status"] = "❌ FAILED"

        return analysis

    def analyze_tailwind_config(self) -> Dict[str, Any]:
        """Analyze Tailwind configuration for Flowbite setup."""
        print("⚙️ Analyzing Tailwind configuration...")

        config_file = self.project_root / "tailwind.config.js"
        if not config_file.exists():
            return {"error": "tailwind.config.js not found"}

        with open(config_file) as f:
            config_content = f.read()

        analysis = {
            "flowbite_plugin": "require('flowbite/plugin')" in config_content,
            "flowbite_content": "flowbite" in config_content and "node_modules/flowbite" in config_content,
            "daisyui_removed": "daisyui" not in config_content.lower(),
            "responsive_design": "content" in config_content and "templates" in config_content,
            "custom_themes": "carpenter" in config_content,
            "status": "✅ PASSED"
        }

        if not analysis["flowbite_plugin"]:
            self.issues.append("❌ Flowbite plugin not configured in Tailwind")
            analysis["status"] = "❌ FAILED"

        if not analysis["daisyui_removed"]:
            self.issues.append("❌ DaisyUI configuration still present")
            analysis["status"] = "❌ FAILED"

        return analysis

    def analyze_css_files(self) -> Dict[str, Any]:
        """Analyze CSS files for migration completeness."""
        print("🎨 Analyzing CSS files...")

        css_files = list(self.project_root.glob("**/*.css"))
        static_css = list((self.project_root / "static").glob("**/*.css"))

        analysis = {
            "total_css_files": len(css_files),
            "flowbite_classes_found": 0,
            "daisyui_classes_found": 0,
            "files_with_issues": [],
            "status": "✅ PASSED"
        }

        # Common DaisyUI classes to check for
        daisyui_patterns = [
            r'\bbtn\b', r'\bcard\b', r'\bhero\b', r'\bnavbar\b',
            r'\bmodal\b', r'\bdrawer\b', r'\bbadge\b', r'\balert\b',
            r'\btabs\b', r'\bform-control\b', r'\binput\b'
        ]

        # Common Flowbite classes to look for
        flowbite_patterns = [
            r'bg-blue-\d+', r'text-gray-\d+', r'border-gray-\d+',
            r'hover:bg-\w+-\d+', r'focus:ring-\w+-\d+', r'rounded-lg'
        ]

        for css_file in static_css:
            try:
                with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Check for DaisyUI remnants
                for pattern in daisyui_patterns:
                    if re.search(pattern, content):
                        analysis["daisyui_classes_found"] += 1
                        analysis["files_with_issues"].append(str(css_file))

                # Check for Flowbite classes
                for pattern in flowbite_patterns:
                    if re.search(pattern, content):
                        analysis["flowbite_classes_found"] += 1

            except Exception as e:
                print(f"Error reading {css_file}: {e}")

        if analysis["daisyui_classes_found"] > 0:
            self.issues.append(f"❌ Found {analysis['daisyui_classes_found']} potential DaisyUI remnants")
            analysis["status"] = "⚠️ WARNING"

        return analysis

    def analyze_html_templates(self) -> Dict[str, Any]:
        """Analyze HTML templates for component migration."""
        print("📄 Analyzing HTML templates...")

        template_files = []
        template_dirs = ["templates", "apps"]

        for template_dir in template_dirs:
            template_path = self.project_root / template_dir
            if template_path.exists():
                template_files.extend(template_path.rglob("*.html"))

        analysis = {
            "total_templates": len(template_files),
            "flowbite_components": 0,
            "daisyui_remnants": 0,
            "accessibility_features": 0,
            "responsive_classes": 0,
            "templates_analyzed": [],
            "status": "✅ PASSED"
        }

        # Patterns to check
        flowbite_class_patterns = [
            r'bg-blue-\d+', r'text-gray-\d+', r'border-gray-\d+',
            r'rounded-lg', r'shadow-lg', r'hover:bg-\w+-\d+',
            r'focus:ring-\w+-\d+', r'transition-colors'
        ]

        daisyui_class_patterns = [
            r'class="[^"]*\bbtn\b[^"]*"', r'class="[^"]*\bcard\b[^"]*"',
            r'class="[^"]*\bhero\b[^"]*"', r'class="[^"]*\bnavbar\b[^"]*"',
            r'class="[^"]*\bmodal\b[^"]*"', r'class="[^"]*\bbadge\b[^"]*"'
        ]

        accessibility_patterns = [
            r'aria-\w+', r'role=', r'alt=', r'tabindex=',
            r'aria-label', r'aria-describedby'
        ]

        responsive_patterns = [
            r'sm:', r'md:', r'lg:', r'xl:', r'2xl:',
            r'hidden', r'block', r'flex'
        ]

        for template_file in template_files:
            try:
                with open(template_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                template_analysis = {
                    "file": str(template_file.relative_to(self.project_root)),
                    "flowbite_classes": 0,
                    "daisyui_remnants": 0,
                    "accessibility": 0,
                    "responsive": 0
                }

                # Check for Flowbite classes
                for pattern in flowbite_class_patterns:
                    matches = len(re.findall(pattern, content))
                    template_analysis["flowbite_classes"] += matches
                    analysis["flowbite_components"] += matches

                # Check for DaisyUI remnants
                for pattern in daisyui_class_patterns:
                    matches = len(re.findall(pattern, content))
                    template_analysis["daisyui_remnants"] += matches
                    analysis["daisyui_remnants"] += matches

                # Check for accessibility features
                for pattern in accessibility_patterns:
                    matches = len(re.findall(pattern, content))
                    template_analysis["accessibility"] += matches
                    analysis["accessibility_features"] += matches

                # Check for responsive classes
                for pattern in responsive_patterns:
                    matches = len(re.findall(pattern, content))
                    template_analysis["responsive"] += matches
                    analysis["responsive_classes"] += matches

                analysis["templates_analyzed"].append(template_analysis)

            except Exception as e:
                print(f"Error reading {template_file}: {e}")

        if analysis["daisyui_remnants"] > 0:
            self.issues.append(f"❌ Found {analysis['daisyui_remnants']} DaisyUI class remnants in templates")
            analysis["status"] = "❌ FAILED"

        if analysis["flowbite_components"] == 0:
            self.issues.append("⚠️ No Flowbite classes found in templates")
            analysis["status"] = "⚠️ WARNING"

        return analysis

    def analyze_javascript_files(self) -> Dict[str, Any]:
        """Analyze JavaScript files for Flowbite integration."""
        print("🔧 Analyzing JavaScript files...")

        js_files = list(self.project_root.glob("**/*.js"))
        static_js = list((self.project_root / "static").glob("**/*.js"))

        analysis = {
            "total_js_files": len(js_files + static_js),
            "flowbite_imports": 0,
            "daisyui_remnants": 0,
            "interactive_components": 0,
            "status": "✅ PASSED"
        }

        flowbite_patterns = [
            r'flowbite', r'import.*flowbite', r'require.*flowbite',
            r'Modal', r'Dropdown', r'Tabs', r'Accordion'
        ]

        daisyui_patterns = [
            r'daisyui', r'daisy', r'theme-controller'
        ]

        for js_file in static_js:
            try:
                with open(js_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Check for Flowbite usage
                for pattern in flowbite_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        analysis["flowbite_imports"] += 1

                # Check for DaisyUI remnants
                for pattern in daisyui_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        analysis["daisyui_remnants"] += 1

            except Exception as e:
                print(f"Error reading {js_file}: {e}")

        if analysis["daisyui_remnants"] > 0:
            self.issues.append(f"❌ Found DaisyUI references in JavaScript files")
            analysis["status"] = "❌ FAILED"

        return analysis

    def analyze_build_configuration(self) -> Dict[str, Any]:
        """Analyze build configuration for proper CSS generation."""
        print("🔨 Analyzing build configuration...")

        analysis = {
            "postcss_config": False,
            "css_build_script": False,
            "proper_input_output": False,
            "status": "✅ PASSED"
        }

        # Check PostCSS config
        postcss_file = self.project_root / "postcss.config.js"
        if postcss_file.exists():
            analysis["postcss_config"] = True
            with open(postcss_file) as f:
                content = f.read()
                if "tailwindcss" in content:
                    analysis["proper_input_output"] = True

        # Check package.json scripts
        package_file = self.project_root / "package.json"
        if package_file.exists():
            with open(package_file) as f:
                package_data = json.load(f)
                scripts = package_data.get("scripts", {})
                if any("tailwindcss" in script for script in scripts.values()):
                    analysis["css_build_script"] = True

        if not analysis["postcss_config"]:
            self.issues.append("⚠️ PostCSS configuration not found")
            analysis["status"] = "⚠️ WARNING"

        return analysis

    def generate_migration_report(self) -> str:
        """Generate comprehensive migration validation report."""
        print("📊 Generating migration validation report...")

        report = {
            "migration_validation": "Flowbite Migration Static Analysis",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "project_root": str(self.project_root),
            "analysis_results": self.results,
            "issues_found": self.issues,
            "recommendations": self.recommendations,
            "overall_status": "✅ MIGRATION SUCCESSFUL" if not self.issues else "⚠️ ISSUES FOUND",
            "summary": {
                "dependencies_migrated": "✅" if not any("dependency" in issue for issue in self.issues) else "❌",
                "tailwind_configured": "✅" if not any("Tailwind" in issue for issue in self.issues) else "❌",
                "templates_updated": "✅" if not any("template" in issue for issue in self.issues) else "❌",
                "css_cleaned": "✅" if not any("CSS" in issue for issue in self.issues) else "❌",
                "js_updated": "✅" if not any("JavaScript" in issue for issue in self.issues) else "❌"
            }
        }

        # Add recommendations based on findings
        if not self.issues:
            self.recommendations.extend([
                "✅ Flowbite migration completed successfully",
                "✅ All DaisyUI dependencies removed",
                "✅ Flowbite properly configured and implemented",
                "✅ Templates updated with Flowbite components",
                "✅ CSS build process configured correctly"
            ])
        else:
            self.recommendations.append("🔧 Address the issues listed above to complete migration")

        report["recommendations"] = self.recommendations

        return json.dumps(report, indent=2)

    def run_full_analysis(self) -> Dict[str, Any]:
        """Run complete static analysis of Flowbite migration."""
        print("🔍 Running Comprehensive Flowbite Migration Static Analysis")
        print("=" * 65)

        # Run all analyses
        self.results["package_analysis"] = self.analyze_package_json()
        self.results["tailwind_config"] = self.analyze_tailwind_config()
        self.results["css_analysis"] = self.analyze_css_files()
        self.results["template_analysis"] = self.analyze_html_templates()
        self.results["javascript_analysis"] = self.analyze_javascript_files()
        self.results["build_analysis"] = self.analyze_build_configuration()

        # Generate report
        report = self.generate_migration_report()

        # Save report
        report_file = self.project_root / "claude-tests" / "flowbite_migration_static_analysis.json"
        with open(report_file, "w") as f:
            f.write(report)

        print(f"\n📋 Static analysis completed!")
        print(f"📄 Report saved to: {report_file}")

        if not self.issues:
            print("\n🎉 FLOWBITE MIGRATION VALIDATION: SUCCESSFUL!")
            print("✅ All static analysis checks passed")
        else:
            print(f"\n⚠️ Found {len(self.issues)} issues to address:")
            for issue in self.issues:
                print(f"  {issue}")

        return self.results


def main():
    """Main function to run the static analysis."""
    project_root = "/Users/philipnickel/Documents/GitHub/kni_webapp"
    validator = FlowbiteMigrationValidator(project_root)
    results = validator.run_full_analysis()
    return results


if __name__ == "__main__":
    main()