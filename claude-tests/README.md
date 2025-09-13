# JCleemannByg Test Suite

Comprehensive automated testing framework for the JCleemannByg Django/Wagtail application, designed to ensure production readiness and maintain code quality.

## Overview

This test suite provides comprehensive coverage of:
- **Contact Form Testing**: Form validation, submission, and email processing
- **Page Functionality**: Wagtail pages, navigation, and URL routing
- **Error Handling**: 404/500 errors, form validation, and edge cases
- **Performance Testing**: Load times, database query optimization, and responsiveness
- **Security Testing**: XSS prevention, SQL injection protection, and access control
- **Integration Testing**: Complete user workflows and system integration

## Test Structure

```
claude-tests/
├── __init__.py
├── conftest.py              # Pytest configuration and shared fixtures
├── test_contact_forms.py    # Contact form functionality tests
├── test_pages_navigation.py # Page and navigation tests
├── test_error_handling.py   # Error handling and edge cases
├── test_performance.py      # Performance and load testing
├── test_projects.py         # Project model and admin tests
├── test_utils.py           # Test utilities and helpers
└── README.md               # This documentation
```

## Quick Start

### Using Docker (Recommended)

```bash
# Start the application with test environment
docker-compose -f docker-compose.local.yml up -d

# Install test dependencies in container
docker-compose exec web pip install -r requirements-test.txt

# Run all tests
docker-compose exec web python -m pytest claude-tests/ -v

# Run with coverage
docker-compose exec web python -m pytest claude-tests/ --cov=apps --cov-report=html
```

### Using Local Python

```bash
# Install test dependencies
python test_runner.py --install

# Run all tests
python test_runner.py

# Run specific category
python test_runner.py --category contact

# Run with verbose output
python test_runner.py --verbose
```

## Test Categories

### Contact Form Tests (`test_contact_forms.py`)

Tests the contact form functionality including:
- ✅ Form validation (required fields, email format)
- ✅ Honeypot anti-spam protection
- ✅ Form submission and database storage
- ✅ Success/error page redirects
- ✅ CSRF protection (documented as exempt)
- ✅ Multi-site support

**Key Test Cases:**
```python
# Valid form submission
def test_contact_form_post_valid_data(client, site, valid_contact_form_data)

# Spam detection
def test_contact_form_honeypot_spam_detection(spam_contact_form_data)

# Field validation
def test_contact_form_missing_required_fields()
```

### Page & Navigation Tests (`test_pages_navigation.py`)

Tests Wagtail page functionality and site navigation:
- ✅ Page model creation and configuration
- ✅ URL routing and page accessibility
- ✅ Navigation link functionality
- ✅ Featured projects display
- ✅ Page filtering and search
- ✅ Mobile navigation support

**Key Test Cases:**
```python
# Page creation and routing
def test_homepage_creation(root_page)
def test_gallery_page_routing(client, gallery_page)

# Navigation functionality
def test_main_navigation_links(client, home_page, contact_page)

# Content filtering
def test_gallery_page_filtering(gallery_page)
```

### Error Handling Tests (`test_error_handling.py`)

Comprehensive error handling and security testing:
- ✅ 404 error page handling
- ✅ Form validation error display
- ✅ Database constraint handling
- ✅ XSS protection testing
- ✅ SQL injection prevention
- ✅ Input sanitization

**Key Test Cases:**
```python
# HTTP errors
def test_404_error_page(client)
def test_404_with_special_characters(client)

# Security testing
def test_xss_attempt_handling(client)
def test_sql_injection_attempts(client)

# Input validation
def test_extremely_long_input_fields(client)
```

### Performance Tests (`test_performance.py`)

Performance and optimization testing:
- ✅ Page load time testing (< 2 seconds)
- ✅ Database query optimization (N+1 prevention)
- ✅ Caching effectiveness
- ✅ Mobile responsiveness
- ✅ Concurrent request handling
- ✅ Memory usage monitoring

**Key Test Cases:**
```python
# Load time testing
def test_homepage_load_time(client, home_page)  # < 2 seconds

# Query optimization
def test_gallery_page_query_efficiency(client, gallery_page, django_assert_num_queries)

# Concurrent testing
def test_concurrent_homepage_requests(client, home_page)
```

### Project Tests (`test_projects.py`)

Project model and admin functionality:
- ✅ Project model validation
- ✅ Featured project filtering
- ✅ Admin interface testing
- ✅ Publication status handling
- ✅ Performance with large datasets

## Test Configuration

### Settings (`project/settings_test.py`)

Optimized test settings for fast execution:
```python
# In-memory SQLite for speed
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}

# Disable migrations
MIGRATION_MODULES = DisableMigrations()

# Fast password hashing
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

# Console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Pytest Configuration (`pytest.ini`)

```ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = project.settings_test
testpaths = claude-tests/
addopts =
    --verbose
    --cov=apps
    --cov-report=html:claude-tests/htmlcov
    --cov-fail-under=70

markers =
    unit: Unit tests
    integration: Integration tests
    performance: Performance tests
    slow: Slow running tests
```

## Running Tests

### All Tests
```bash
# Complete test suite with coverage
python test_runner.py

# Without coverage (faster)
python test_runner.py --no-coverage

# Parallel execution
python test_runner.py --parallel
```

### Specific Categories
```bash
# Contact form tests only
python test_runner.py --category contact

# Performance tests only
python test_runner.py --category performance

# Unit tests only
python test_runner.py --category unit
```

### Pattern Matching
```bash
# Tests matching pattern
python test_runner.py --pattern "form"

# Specific test function
python test_runner.py --pattern "test_contact_form_validation"
```

### Test Markers
```bash
# Run only unit tests
python -m pytest -m unit claude-tests/

# Skip slow tests
python -m pytest -m "not slow" claude-tests/

# Integration tests only
python -m pytest -m integration claude-tests/
```

## Coverage Goals

Target coverage metrics:
- **Overall Coverage**: 70%+ (enforced)
- **Critical Paths**: 90%+ (contact forms, page routing)
- **Model Validation**: 85%+
- **View Functions**: 80%+
- **Error Handlers**: 95%+

### Coverage Reports

```bash
# Generate HTML coverage report
python test_runner.py
open claude-tests/htmlcov/index.html

# Terminal coverage report
python test_runner.py --report

# XML report for CI/CD
# Available at: claude-tests/coverage.xml
```

## Fixtures and Test Data

### Key Fixtures (`conftest.py`)

```python
@pytest.fixture
def valid_contact_form_data():
    """Valid contact form data for testing"""

@pytest.fixture
def home_page(site, root_page):
    """Test home page instance"""

@pytest.fixture
def sample_project():
    """Sample project for testing"""
```

### Test Utilities (`test_utils.py`)

```python
# Performance timing
with PerformanceTimer(max_time=2.0) as timer:
    response = client.get('/')

# Custom assertions
TestAssertions.assertResponseTime(response_time, 2.0)

# Security testing
payloads = SecurityTestHelpers.get_xss_payloads()
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_PASSWORD: testpass
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-test.txt

    - name: Run tests
      run: python test_runner.py
      env:
        DATABASE_URL: postgres://postgres:testpass@localhost/testdb

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./claude-tests/coverage.xml
```

## Performance Benchmarks

Expected performance targets:

| Metric | Target | Test |
|--------|--------|------|
| Homepage Load Time | < 2.0s | `test_homepage_load_time` |
| Gallery Load Time | < 3.0s | `test_gallery_page_load_time` |
| Contact Form Submit | < 1.5s | `test_contact_form_post_valid_data` |
| Database Queries | < 10 queries | `test_gallery_page_query_efficiency` |
| Memory Usage | < 100MB increase | `test_memory_usage_under_load` |

## Security Testing

The test suite includes security testing for:

### XSS Prevention
```python
def test_xss_attempt_handling(client):
    xss_data = {
        'name': '<script>alert("XSS")</script>',
        'message': '<img src="x" onerror="alert(1)">'
    }
    # Tests that XSS is properly escaped
```

### SQL Injection Protection
```python
def test_sql_injection_attempts(client):
    malicious_data = {
        'name': "'; DROP TABLE contacts_contactsubmission; --"
    }
    # Tests that SQL injection is prevented
```

### Input Validation
- Unicode character handling
- Extremely long inputs
- Null byte injection
- Path traversal attempts

## Debugging Failed Tests

### Common Issues

1. **Database Migrations**
   ```bash
   # Reset test database
   python manage.py migrate --settings=project.settings_test
   ```

2. **Static Files**
   ```bash
   # Collect static files for admin tests
   python manage.py collectstatic --noinput --settings=project.settings_test
   ```

3. **Permission Errors**
   ```bash
   # Check file permissions
   chmod +x test_runner.py
   ```

### Verbose Output
```bash
# Detailed test output
python test_runner.py --verbose

# Show all print statements
python -m pytest -s claude-tests/

# Stop on first failure
python -m pytest -x claude-tests/
```

## Contributing

### Adding New Tests

1. **Create test file**: Follow naming convention `test_*.py`
2. **Add fixtures**: Use existing fixtures or create new ones in `conftest.py`
3. **Use markers**: Mark tests appropriately (`@pytest.mark.unit`, etc.)
4. **Document tests**: Add docstrings explaining test purpose
5. **Update coverage**: Ensure new code is tested

### Test Guidelines

- **Atomic**: Each test should test one specific behavior
- **Independent**: Tests should not depend on other tests
- **Fast**: Unit tests should complete in milliseconds
- **Descriptive**: Test names should clearly describe what is being tested
- **Maintainable**: Use fixtures and utilities to reduce duplication

## Troubleshooting

### Common Errors

**ImportError: No module named 'pytest'**
```bash
python test_runner.py --install
```

**Database errors**
```bash
# Check database configuration
python manage.py check --settings=project.settings_test
```

**Permission denied**
```bash
# Fix file permissions
chmod +x test_runner.py
```

**Slow tests**
```bash
# Run without slow tests
python -m pytest -m "not slow" claude-tests/
```

## Resources

- [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Wagtail Testing Guide](https://docs.wagtail.org/en/stable/advanced_topics/testing.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)

## Test Results Summary

Current test implementation provides:

✅ **70+ Test Cases** covering critical functionality
✅ **Contact Form Validation** with anti-spam protection
✅ **Page Functionality** and navigation testing
✅ **Error Handling** and security testing
✅ **Performance Benchmarks** and optimization
✅ **CI/CD Ready** configuration
✅ **Comprehensive Documentation** and examples

The test suite is designed to catch regressions early and ensure production readiness of the JCleemannByg application.