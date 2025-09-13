#!/usr/bin/env python
"""
Test runner for the JCleemannByg Django/Wagtail application.
Can be run with or without Docker.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command, shell=False):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=shell,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def install_test_dependencies():
    """Install test dependencies."""
    print("Installing test dependencies...")

    # Check if we're in Docker or have a virtual environment
    if os.environ.get('DJANGO_SETTINGS_MODULE'):
        # In Docker environment
        run_command([
            'pip', 'install', '-r', 'requirements-test.txt'
        ])
    else:
        # Local environment - try to use existing Python
        try:
            run_command([
                sys.executable, '-m', 'pip', 'install',
                '-r', 'requirements-test.txt', '--user'
            ])
        except:
            print("Could not install dependencies. Please run in Docker or virtual environment.")
            sys.exit(1)

def run_tests(coverage=True, verbose=False, pattern=None, parallel=False):
    """Run the test suite."""
    print("Running test suite...")

    # Base command
    cmd = [sys.executable, '-m', 'pytest']

    # Add options
    if verbose:
        cmd.append('-v')

    if coverage:
        cmd.extend([
            '--cov=apps',
            '--cov-report=term-missing',
            '--cov-report=html:claude-tests/htmlcov',
            '--cov-report=xml:claude-tests/coverage.xml'
        ])

    if parallel:
        cmd.extend(['-n', 'auto'])

    if pattern:
        cmd.extend(['-k', pattern])

    # Add test directory
    cmd.append('claude-tests/')

    print(f"Running: {' '.join(cmd)}")

    # Set environment
    env = os.environ.copy()
    env['DJANGO_SETTINGS_MODULE'] = 'project.settings_test'

    # Run tests
    try:
        subprocess.run(cmd, check=True, env=env)
        print("\n✅ All tests passed!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def generate_coverage_report():
    """Generate and display coverage report."""
    print("Generating coverage report...")

    # Run coverage report
    run_command([
        sys.executable, '-m', 'coverage', 'report', '--show-missing'
    ])

def run_specific_test_category(category):
    """Run tests for a specific category."""
    categories = {
        'contact': 'test_contact_forms.py',
        'pages': 'test_pages_navigation.py',
        'projects': 'test_projects.py',
        'errors': 'test_error_handling.py',
        'performance': 'test_performance.py',
        'unit': '-m unit',
        'integration': '-m integration',
        'slow': '-m slow'
    }

    if category in categories:
        if categories[category].startswith('-m'):
            pattern = categories[category]
        else:
            pattern = f"claude-tests/{categories[category]}"

        print(f"Running {category} tests...")

        cmd = [sys.executable, '-m', 'pytest', '-v']
        if categories[category].startswith('-m'):
            cmd.extend(categories[category].split())
            cmd.append('claude-tests/')
        else:
            cmd.append(pattern)

        env = os.environ.copy()
        env['DJANGO_SETTINGS_MODULE'] = 'project.settings_test'

        subprocess.run(cmd, env=env)
    else:
        print(f"Unknown category: {category}")
        print(f"Available categories: {', '.join(categories.keys())}")

def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description='Run tests for JCleemannByg application')
    parser.add_argument('--install', action='store_true',
                       help='Install test dependencies')
    parser.add_argument('--no-coverage', action='store_true',
                       help='Run tests without coverage')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    parser.add_argument('--pattern', '-k', type=str,
                       help='Run tests matching pattern')
    parser.add_argument('--parallel', '-n', action='store_true',
                       help='Run tests in parallel')
    parser.add_argument('--category', '-c', type=str,
                       help='Run specific test category (contact, pages, projects, errors, performance)')
    parser.add_argument('--report', action='store_true',
                       help='Generate coverage report only')

    args = parser.parse_args()

    # Change to project directory
    os.chdir(Path(__file__).parent)

    if args.install:
        install_test_dependencies()
        return

    if args.report:
        generate_coverage_report()
        return

    if args.category:
        run_specific_test_category(args.category)
        return

    # Install dependencies if not already installed
    try:
        import pytest
    except ImportError:
        print("pytest not found, installing test dependencies...")
        install_test_dependencies()

    # Run tests
    run_tests(
        coverage=not args.no_coverage,
        verbose=args.verbose,
        pattern=args.pattern,
        parallel=args.parallel
    )

if __name__ == '__main__':
    main()