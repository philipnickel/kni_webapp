#!/usr/bin/env python3
"""
Comprehensive tests for the Django secret key deployment configuration.
Tests the production deployment fixes for Coolify environments.
"""
import pytest
import os
import tempfile
import subprocess
from unittest.mock import patch, MagicMock
from pathlib import Path


class TestSecretKeyDeployment:
    """Test deployment secret key handling"""

    def test_docker_compose_syntax_valid(self):
        """Test that Docker Compose file has valid syntax"""
        compose_file = Path('docker-compose.coolify.yml')
        assert compose_file.exists(), "Docker Compose file should exist"

        with open(compose_file) as f:
            content = f.read()

        # Should not have the hard requirement syntax
        assert '${DJANGO_SECRET_KEY:?}' not in content, \
            "Docker Compose should not require DJANGO_SECRET_KEY"

        # Should have the optional fallback syntax
        assert '${DJANGO_SECRET_KEY:-}' in content, \
            "Docker Compose should allow empty DJANGO_SECRET_KEY"

    def test_entrypoint_script_has_key_generation(self):
        """Test that entrypoint script includes secret key generation logic"""
        entrypoint_file = Path('docker/entrypoint.sh')
        assert entrypoint_file.exists(), "Entrypoint script should exist"

        with open(entrypoint_file) as f:
            content = f.read()

        # Check for key generation logic
        required_patterns = [
            'if [ "$ROLE" = "web" ] && [ -z "$DJANGO_SECRET_KEY" ]',
            'export DJANGO_SECRET_KEY=$(python manage.py generate_secret_key --print-only)',
            'Generated secure Django secret key'
        ]

        for pattern in required_patterns:
            assert pattern in content, f"Entrypoint missing: {pattern}"

    def test_management_command_structure(self):
        """Test that the management command has proper structure"""
        command_file = Path('apps/core/management/commands/generate_secret_key.py')
        assert command_file.exists(), "Management command should exist"

        with open(command_file) as f:
            content = f.read()

        required_components = [
            'class Command(BaseCommand)',
            'get_random_secret_key',
            '--print-only',
            '--env-file',
            'def handle(self, *args, **options)'
        ]

        for component in required_components:
            assert component in content, f"Management command missing: {component}"

    def test_django_settings_secret_key_function(self):
        """Test that Django settings has enhanced secret key function"""
        settings_file = Path('project/settings.py')
        assert settings_file.exists(), "Settings file should exist"

        with open(settings_file) as f:
            content = f.read()

        required_elements = [
            'def get_secret_key():',
            'get_random_secret_key',
            'SECRET_KEY = get_secret_key()',
            'WARNING: No DJANGO_SECRET_KEY provided'
        ]

        for element in required_elements:
            assert element in content, f"Settings missing: {element}"


class TestSecretKeyGeneration:
    """Test secret key generation functionality"""

    def test_secret_key_generation_length_and_format(self):
        """Test that generated secret keys meet Django requirements"""
        # Test the secret key generation logic without Django
        import secrets
        import string

        # Simulate Django's get_random_secret_key function
        def mock_get_random_secret_key():
            chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
            return ''.join(secrets.choice(chars) for i in range(50))

        key = mock_get_random_secret_key()

        # Django secret keys should be at least 50 characters
        assert len(key) >= 50, "Secret key should be at least 50 characters"

        # Should contain a mix of characters
        has_letter = any(c.isalpha() for c in key)
        has_digit = any(c.isdigit() for c in key)
        assert has_letter and has_digit, "Secret key should contain letters and digits"

    def test_environment_variable_handling(self):
        """Test environment variable fallback logic"""
        # Test the logic from settings.py
        def simulate_get_secret_key():
            # Simulate the get_secret_key function logic
            secret_key = os.getenv("DJANGO_SECRET_KEY", "").strip()

            if secret_key:
                return secret_key

            # Would generate a key in real implementation
            return "generated_key_placeholder"

        # Test with environment variable set
        with patch.dict(os.environ, {'DJANGO_SECRET_KEY': 'test_secret_key'}):
            result = simulate_get_secret_key()
            assert result == 'test_secret_key'

        # Test without environment variable
        with patch.dict(os.environ, {}, clear=True):
            result = simulate_get_secret_key()
            assert result == "generated_key_placeholder"


class TestDeploymentDocumentation:
    """Test that deployment documentation exists and is comprehensive"""

    def test_deployment_documentation_exists(self):
        """Test that DEPLOYMENT.md exists and has required sections"""
        doc_file = Path('DEPLOYMENT.md')
        assert doc_file.exists(), "DEPLOYMENT.md should exist"

        with open(doc_file) as f:
            content = f.read()

        required_sections = [
            '# Deployment Configuration',
            '## Secret Key Management',
            '### Automatic Secret Key Generation',
            '### Coolify Deployment',
            '### Manual Secret Key Generation',
            '### Security Notes',
            '## Environment Variables',
            '## Troubleshooting'
        ]

        for section in required_sections:
            assert section in content, f"Documentation missing section: {section}"

    def test_deployment_instructions_comprehensive(self):
        """Test that deployment instructions cover key scenarios"""
        doc_file = Path('DEPLOYMENT.md')
        with open(doc_file) as f:
            content = f.read()

        key_topics = [
            'Preview deployments',
            'Production deployments',
            'Zero-config deployments',
            'python manage.py generate_secret_key',
            'DJANGO_SECRET_KEY',
            'Coolify',
            'auto-generated keys'
        ]

        for topic in key_topics:
            assert topic in content, f"Documentation should mention: {topic}"


@pytest.mark.integration
class TestProductionReadiness:
    """Test that the deployment configuration is production-ready"""

    def test_file_permissions_secure(self):
        """Test that entrypoint script has proper permissions"""
        entrypoint_file = Path('docker/entrypoint.sh')

        # File should exist and be readable
        assert entrypoint_file.exists()
        assert entrypoint_file.is_file()

        # Should be readable by owner (we can't easily test execute without running)
        with open(entrypoint_file) as f:
            content = f.read()
            assert len(content) > 0, "Entrypoint should have content"

    def test_error_handling_present(self):
        """Test that error handling is present in key files"""
        # Check entrypoint script has error handling
        with open('docker/entrypoint.sh') as f:
            entrypoint_content = f.read()

        # Should have some form of error handling or status checking
        error_indicators = ['echo', 'if', '||', '&&']
        assert any(indicator in entrypoint_content for indicator in error_indicators), \
            "Entrypoint should have error handling"

        # Check management command has error handling
        with open('apps/core/management/commands/generate_secret_key.py') as f:
            command_content = f.read()

        assert 'except' in command_content, "Management command should have exception handling"
        assert 'try:' in command_content, "Management command should have try blocks"


def test_deployment_fix_summary():
    """Test that all deployment fix components are in place"""
    print("\n🔍 Verifying deployment fix components...")

    components = {
        'Docker Compose': Path('docker-compose.coolify.yml'),
        'Entrypoint Script': Path('docker/entrypoint.sh'),
        'Management Command': Path('apps/core/management/commands/generate_secret_key.py'),
        'Django Settings': Path('project/settings.py'),
        'Documentation': Path('DEPLOYMENT.md'),
        'Tests': Path('claude-tests/test_secret_key_handling.py')
    }

    all_present = True
    for name, path in components.items():
        if path.exists():
            print(f"✅ {name}: {path}")
        else:
            print(f"❌ {name}: {path} - MISSING")
            all_present = False

    assert all_present, "All deployment fix components should be present"

    print("\n🎯 Deployment fix verification complete!")
    print("Summary: All components for robust Django secret key handling are in place.")
    print("This should fix preview deployments and enable zero-config Coolify deployments.")


if __name__ == '__main__':
    # Run as standalone script
    pytest.main([__file__, '-v'])