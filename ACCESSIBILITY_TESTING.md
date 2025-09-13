# Accessibility Testing Framework

This document describes the comprehensive accessibility testing framework implemented for the JCleemannByg Django/Wagtail application. The framework ensures WCAG 2.1 AA compliance across all 8 DaisyUI themes and provides visual regression testing capabilities.

## Overview

The accessibility testing framework includes:

1. **WCAG 2.1 AA Compliance Testing** - Automated tests using axe-core
2. **Visual Regression Testing** - Screenshot comparison across themes and viewports
3. **Keyboard Navigation Testing** - Comprehensive keyboard accessibility validation
4. **Form Accessibility Testing** - Contact form accessibility compliance
5. **Theme-specific Testing** - Testing all 8 DaisyUI themes for accessibility
6. **Responsive Design Testing** - Accessibility across different viewports

## Framework Components

### Core Test Files

- `claude-tests/test_accessibility.py` - Main WCAG compliance tests
- `claude-tests/test_accessibility_features.py` - Feature-specific accessibility tests
- `claude-tests/test_visual_regression.py` - Visual regression testing
- `claude-tests/test_accessibility_basic.py` - Basic setup verification tests
- `claude-tests/accessibility_config.py` - Configuration and utilities
- `run_accessibility_tests.py` - Test runner script

### Configuration Files

- `pytest.ini` - Updated with accessibility test markers
- `playwright.config.py` - Playwright configuration for accessibility testing
- `requirements-test.txt` - Updated with accessibility testing dependencies

## Installation and Setup

### 1. Install Dependencies

```bash
# Activate your virtual environment
source venv/bin/activate

# Install test dependencies
pip install -r requirements-test.txt

# Install Playwright browsers
playwright install chromium
```

### 2. Verify Setup

Run the basic accessibility tests to verify the framework is properly configured:

```bash
python -m pytest claude-tests/test_accessibility_basic.py -v
```

## Running Accessibility Tests

### Using the Test Runner

The easiest way to run accessibility tests is using the provided test runner:

```bash
# Run all accessibility tests
python run_accessibility_tests.py run

# Run WCAG compliance tests only
python run_accessibility_tests.py wcag

# Run visual regression tests only
python run_accessibility_tests.py visual

# Run keyboard navigation tests only
python run_accessibility_tests.py keyboard

# Run theme-specific tests
python run_accessibility_tests.py themes

# Generate baseline screenshots for visual regression
python run_accessibility_tests.py baselines
```

### Using Pytest Directly

You can also run tests directly with pytest:

```bash
# Run all accessibility tests
pytest claude-tests/ -m accessibility -v

# Run specific test categories
pytest claude-tests/ -m wcag -v
pytest claude-tests/ -m visual_regression -v
pytest claude-tests/ -m keyboard_navigation -v

# Run tests for specific themes
pytest claude-tests/test_accessibility.py -k "light" -v

# Generate HTML report
pytest claude-tests/ -m accessibility --html=accessibility_report.html
```

## Test Categories and Markers

The framework uses pytest markers to categorize tests:

- `@pytest.mark.accessibility` - All accessibility tests
- `@pytest.mark.wcag` - WCAG 2.1 AA compliance tests
- `@pytest.mark.visual_regression` - Visual regression tests
- `@pytest.mark.keyboard_navigation` - Keyboard navigation tests
- `@pytest.mark.screen_reader` - Screen reader compatibility tests
- `@pytest.mark.contact_form` - Contact form accessibility tests

## DaisyUI Theme Testing

The framework tests accessibility across all 8 DaisyUI themes:

1. `light` - Light theme (default)
2. `dark` - Dark theme
3. `corporate` - Corporate theme
4. `business` - Business theme
5. `luxury` - Luxury theme
6. `emerald` - Emerald theme
7. `garden` - Garden theme
8. `autumn` - Autumn theme

Each theme is tested for:
- Color contrast ratios (WCAG AA: 4.5:1 for normal text, 3:1 for large text)
- Focus indicator visibility
- Interactive element accessibility
- Visual consistency

## Key Test Features

### WCAG 2.1 AA Compliance

Tests include comprehensive coverage of:

- **Color and Contrast**: Automated contrast ratio validation
- **Keyboard Navigation**: Tab order, focus management, keyboard traps
- **Form Accessibility**: Labels, validation messages, error handling
- **Semantic Markup**: Proper heading hierarchy, landmarks, ARIA usage
- **Images and Media**: Alt text validation, decorative image handling
- **Language Attributes**: Proper language declaration

### Visual Regression Testing

- **Baseline Management**: Automated baseline screenshot generation
- **Multi-Viewport Testing**: Desktop, tablet, mobile, mobile landscape
- **Theme Comparison**: Visual consistency across all themes
- **Interaction States**: Hover, focus, active states testing
- **Responsive Design**: Layout validation across screen sizes

### Form Accessibility Testing

Specialized tests for the contact form:

- **Label Association**: Proper label-field relationships
- **Validation Messages**: Accessible error messaging with ARIA
- **Keyboard Navigation**: Full form completion using only keyboard
- **Screen Reader Support**: ARIA live regions for dynamic content
- **Honeypot Field**: Anti-spam field doesn't interfere with accessibility

## Accessibility Standards

The framework enforces these WCAG 2.1 AA requirements:

### Level A Requirements
- Images have alt text
- Form controls have labels
- Page has proper heading structure
- Content has proper language declaration

### Level AA Requirements
- Color contrast ratio ≥ 4.5:1 for normal text
- Color contrast ratio ≥ 3.0:1 for large text
- Focus indicators are visible
- No keyboard traps
- Skip links are provided where needed

### Additional Best Practices
- Semantic HTML usage
- ARIA attributes used correctly
- Responsive design considerations
- Performance impact of accessibility features

## Configuration

### Accessibility Configuration (`accessibility_config.py`)

```python
# Themes to test
THEMES = ['light', 'dark', 'corporate', 'business', 'luxury', 'emerald', 'garden', 'autumn']

# Pages to test
TEST_PAGES = [
    {'url': '/', 'name': 'Home Page'},
    {'url': '/kontakt/', 'name': 'Contact Page', 'has_form': True},
    {'url': '/galleri/', 'name': 'Gallery Page'}
]

# WCAG 2.1 AA color contrast requirements
COLOR_CONTRAST_REQUIREMENTS = {
    'normal_text': 4.5,
    'large_text': 3.0,
    'ui_components': 3.0
}
```

### Playwright Configuration

The framework uses Playwright for browser automation:

- **Browser**: Chromium (for consistent results)
- **Viewport**: Responsive testing across multiple sizes
- **Locale**: Danish (da-DK) to match the website
- **Color Scheme**: Both light and dark mode testing
- **Reduced Motion**: Respects user preferences

## Reporting

### Test Reports

Tests generate multiple types of reports:

1. **HTML Report**: Visual test results with screenshots
2. **Coverage Report**: Code coverage for accessibility features
3. **JSON Report**: Machine-readable test results
4. **Visual Baseline Index**: Catalog of baseline screenshots

### Report Locations

- `claude-tests/accessibility_report.html` - Main HTML report
- `claude-tests/accessibility_reports/` - Detailed JSON reports
- `claude-tests/visual_baselines/` - Screenshot baselines
- `claude-tests/screenshots/` - Test screenshots

## Integration with CI/CD

The framework is designed to integrate with CI/CD pipelines:

### GitHub Actions Example

```yaml
- name: Run Accessibility Tests
  run: |
    source venv/bin/activate
    playwright install chromium
    python run_accessibility_tests.py run --coverage

- name: Upload Reports
  uses: actions/upload-artifact@v3
  with:
    name: accessibility-reports
    path: claude-tests/accessibility_report.html
```

### Coverage Requirements

The framework maintains accessibility test coverage requirements:

- Minimum 80% coverage of interactive elements
- All themes must pass WCAG AA tests
- Visual regression tolerance < 1% pixel difference
- Zero critical accessibility violations

## Troubleshooting

### Common Issues

1. **Playwright Installation**
   ```bash
   playwright install chromium
   ```

2. **Django Settings**
   ```bash
   export DJANGO_SETTINGS_MODULE=project.settings_test
   ```

3. **Missing Dependencies**
   ```bash
   pip install -r requirements-test.txt
   ```

### Debug Mode

Run tests with debug information:

```bash
pytest claude-tests/ -m accessibility -v --tb=long --capture=no
```

### Visual Regression Issues

If visual regression tests fail:

1. Review the diff images in `claude-tests/visual_baselines/`
2. Update baselines if changes are intentional:
   ```bash
   python run_accessibility_tests.py baselines
   ```

## Best Practices

### Writing Accessibility Tests

1. **Test Real User Scenarios**: Focus on how users actually interact with the site
2. **Use Semantic Selectors**: Prefer ARIA roles and semantic HTML over CSS selectors
3. **Test Across Themes**: Ensure accessibility doesn't regress in different themes
4. **Validate Error States**: Test form validation and error messaging
5. **Check Focus Management**: Ensure logical tab order and visible focus indicators

### Maintaining Tests

1. **Regular Updates**: Run tests with each deployment
2. **Baseline Management**: Update visual baselines when design changes
3. **Performance Monitoring**: Monitor test execution time and optimize as needed
4. **Documentation**: Keep accessibility documentation updated

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe-core Rules](https://dequeuniversity.com/rules/axe/)
- [DaisyUI Documentation](https://daisyui.com/)
- [Playwright Documentation](https://playwright.dev/)

## Support

For questions about the accessibility testing framework:

1. Review the test documentation in `claude-tests/`
2. Check the configuration in `accessibility_config.py`
3. Run the basic tests to verify setup: `pytest claude-tests/test_accessibility_basic.py`
4. Generate reports to see detailed results: `python run_accessibility_tests.py run`