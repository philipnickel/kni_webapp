#!/usr/bin/env python3
"""
Enhanced Backup and Restore System Test Suite

This test suite verifies the functionality of the new backup and restore system
for the KNI Webapp multi-tenant architecture.
"""

import os
import sys
import json
import tempfile
import shutil
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from django.test import TestCase
from django.core.management import call_command
from django.conf import settings
from django.db import connection
from io import StringIO


class BackupRestoreSystemTest(TestCase):
    """Test suite for backup and restore functionality"""

    def setUp(self):
        """Set up test environment"""
        self.test_backup_dir = Path(tempfile.mkdtemp())
        self.test_baseline_dir = Path(tempfile.mkdtemp())

        # Create test directories
        (self.test_backup_dir / "data").mkdir(parents=True, exist_ok=True)
        (self.test_backup_dir / "media").mkdir(parents=True, exist_ok=True)
        (self.test_backup_dir / "manifests").mkdir(parents=True, exist_ok=True)
        (self.test_backup_dir / "rollback").mkdir(parents=True, exist_ok=True)

        self.test_baseline_dir.mkdir(parents=True, exist_ok=True)

        print(f"Test backup directory: {self.test_backup_dir}")
        print(f"Test baseline directory: {self.test_baseline_dir}")

    def tearDown(self):
        """Clean up test environment"""
        if self.test_backup_dir.exists():
            shutil.rmtree(self.test_backup_dir)
        if self.test_baseline_dir.exists():
            shutil.rmtree(self.test_baseline_dir)

    def test_backup_tenant_command_exists(self):
        """Test that backup_tenant management command exists and is callable"""
        try:
            out = StringIO()
            call_command('backup_tenant', '--help', stdout=out)
            help_text = out.getvalue()
            self.assertIn('schema-aware backups', help_text)
            print("✅ backup_tenant command exists and shows help")
        except Exception as e:
            self.fail(f"backup_tenant command failed: {e}")

    def test_restore_tenant_command_exists(self):
        """Test that restore_tenant management command exists and is callable"""
        try:
            out = StringIO()
            call_command('restore_tenant', '--help', stdout=out)
            help_text = out.getvalue()
            self.assertIn('rollback capabilities', help_text)
            print("✅ restore_tenant command exists and shows help")
        except Exception as e:
            self.fail(f"restore_tenant command failed: {e}")

    def test_list_backups_command_exists(self):
        """Test that list_backups management command exists"""
        try:
            out = StringIO()
            call_command('list_backups', '--help', stdout=out)
            help_text = out.getvalue()
            self.assertIn('available backups', help_text)
            print("✅ list_backups command exists and shows help")
        except Exception as e:
            self.fail(f"list_backups command failed: {e}")

    def test_cleanup_backups_command_exists(self):
        """Test that cleanup_backups management command exists"""
        try:
            out = StringIO()
            call_command('cleanup_backups', '--help', stdout=out)
            help_text = out.getvalue()
            self.assertIn('retention policies', help_text)
            print("✅ cleanup_backups command exists and shows help")
        except Exception as e:
            self.fail(f"cleanup_backups command failed: {e}")

    def test_backup_creation_full(self):
        """Test creating a full backup"""
        try:
            out = StringIO()
            call_command(
                'backup_tenant',
                '--backup-type', 'full',
                '--output-dir', str(self.test_backup_dir),
                '--retention-days', '30',
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('backed up successfully', output)

            # Check that backup files were created
            data_files = list((self.test_backup_dir / "data").glob("*.sql*"))
            manifest_files = list((self.test_backup_dir / "manifests").glob("*.json"))

            self.assertTrue(len(data_files) > 0, "No backup data files created")
            self.assertTrue(len(manifest_files) > 0, "No manifest files created")

            print(f"✅ Full backup created: {len(data_files)} data files, {len(manifest_files)} manifests")

        except Exception as e:
            self.fail(f"Full backup creation failed: {e}")

    def test_backup_creation_incremental(self):
        """Test creating an incremental backup"""
        try:
            out = StringIO()
            call_command(
                'backup_tenant',
                '--backup-type', 'incremental',
                '--output-dir', str(self.test_backup_dir),
                '--retention-days', '7',
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('backed up successfully', output)

            # Check that backup files were created
            data_files = list((self.test_backup_dir / "data").glob("*.sql*"))
            self.assertTrue(len(data_files) > 0, "No incremental backup files created")

            print(f"✅ Incremental backup created: {len(data_files)} files")

        except Exception as e:
            self.fail(f"Incremental backup creation failed: {e}")

    def test_backup_with_compression(self):
        """Test creating compressed backups"""
        try:
            out = StringIO()
            call_command(
                'backup_tenant',
                '--backup-type', 'full',
                '--compress',
                '--output-dir', str(self.test_backup_dir),
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('backed up successfully', output)

            # Check for compressed files
            compressed_files = list((self.test_backup_dir / "data").glob("*.gz"))
            self.assertTrue(len(compressed_files) > 0, "No compressed backup files created")

            print(f"✅ Compressed backup created: {len(compressed_files)} files")

        except Exception as e:
            self.fail(f"Compressed backup creation failed: {e}")

    def test_list_backups_functionality(self):
        """Test listing backups functionality"""
        # First create a backup to list
        call_command(
            'backup_tenant',
            '--backup-type', 'full',
            '--output-dir', str(self.test_backup_dir),
            stdout=StringIO()
        )

        try:
            # Test table format
            out = StringIO()
            call_command(
                'list_backups',
                '--backup-dir', str(self.test_backup_dir),
                '--format', 'table',
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('Available Backups', output)
            self.assertIn('Timestamp', output)
            self.assertIn('Schema', output)

            print("✅ Backup listing (table format) works")

            # Test JSON format
            out = StringIO()
            call_command(
                'list_backups',
                '--backup-dir', str(self.test_backup_dir),
                '--format', 'json',
                stdout=out
            )

            json_output = out.getvalue()
            backup_data = json.loads(json_output)
            self.assertIn('backups', backup_data)
            self.assertIn('total_count', backup_data)

            print("✅ Backup listing (JSON format) works")

        except Exception as e:
            self.fail(f"Backup listing failed: {e}")

    def test_restore_list_available(self):
        """Test restore command's list available functionality"""
        # Create a backup first
        call_command(
            'backup_tenant',
            '--backup-type', 'full',
            '--output-dir', str(self.test_backup_dir),
            stdout=StringIO()
        )

        try:
            out = StringIO()
            call_command(
                'restore_tenant',
                '--list-available',
                '--backup-dir', str(self.test_backup_dir),
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('Available Backups', output)
            self.assertIn('Usage Examples', output)

            print("✅ Restore list available functionality works")

        except Exception as e:
            self.fail(f"Restore list available failed: {e}")

    def test_backup_cleanup_dry_run(self):
        """Test backup cleanup in dry-run mode"""
        # Create some old backup files
        old_backup = self.test_backup_dir / "data" / "old_backup_20230101_000000.sql"
        old_backup.touch()

        # Make it appear old
        old_time = datetime.now() - timedelta(days=35)
        os.utime(old_backup, (old_time.timestamp(), old_time.timestamp()))

        try:
            out = StringIO()
            call_command(
                'cleanup_backups',
                '--backup-dir', str(self.test_backup_dir),
                '--retention-policy', 'default',
                '--dry-run',
                stdout=out
            )

            output = out.getvalue()
            self.assertIn('Dry Run', output)

            # File should still exist after dry run
            self.assertTrue(old_backup.exists(), "File was deleted during dry run")

            print("✅ Backup cleanup dry-run works")

        except Exception as e:
            self.fail(f"Backup cleanup dry-run failed: {e}")

    def test_schema_detection(self):
        """Test that the system can detect database schemas"""
        try:
            # Get list of schemas
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT schema_name
                    FROM information_schema.schemata
                    WHERE schema_name NOT IN ('public', 'information_schema', 'pg_catalog', 'pg_toast')
                    ORDER BY schema_name
                """)
                tenant_schemas = [row[0] for row in cursor.fetchall()]

            # Should always have public schema
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT schema_name
                    FROM information_schema.schemata
                    WHERE schema_name = 'public'
                """)
                public_exists = cursor.fetchone() is not None

            self.assertTrue(public_exists, "Public schema not found")
            print(f"✅ Schema detection works: public + {len(tenant_schemas)} tenant schemas")

        except Exception as e:
            self.fail(f"Schema detection failed: {e}")

    def test_backup_manifest_structure(self):
        """Test that backup manifests have the correct structure"""
        # Create a backup
        call_command(
            'backup_tenant',
            '--backup-type', 'full',
            '--output-dir', str(self.test_backup_dir),
            stdout=StringIO()
        )

        # Find the manifest file
        manifest_files = list((self.test_backup_dir / "manifests").glob("backup_manifest_*.json"))
        self.assertTrue(len(manifest_files) > 0, "No manifest files found")

        manifest_file = manifest_files[0]

        try:
            with manifest_file.open() as f:
                manifest = json.load(f)

            # Check required fields
            required_fields = ['timestamp', 'backup_type', 'schemas', 'retention_days']
            for field in required_fields:
                self.assertIn(field, manifest, f"Missing field: {field}")

            # Check schema structure
            if manifest['schemas']:
                schema_info = manifest['schemas'][0]
                schema_fields = ['schema', 'tenant', 'filename', 'size', 'hash', 'timestamp']
                for field in schema_fields:
                    self.assertIn(field, schema_info, f"Missing schema field: {field}")

            print("✅ Backup manifest structure is correct")

        except Exception as e:
            self.fail(f"Manifest structure test failed: {e}")

    def test_makefile_backup_targets(self):
        """Test that Makefile backup targets exist"""
        makefile_path = PROJECT_ROOT / "Makefile"

        if not makefile_path.exists():
            self.fail("Makefile not found")

        try:
            with makefile_path.open() as f:
                makefile_content = f.read()

            # Check for backup-related targets
            backup_targets = [
                'backup:', 'restore:', 'list-backups:', 'clean-backups:',
                'backup-health:', 'backup-full:', 'backup-incremental:'
            ]

            for target in backup_targets:
                self.assertIn(target, makefile_content, f"Missing Makefile target: {target}")

            print("✅ All Makefile backup targets exist")

        except Exception as e:
            self.fail(f"Makefile backup targets test failed: {e}")

    def test_backup_scheduler_script(self):
        """Test that backup scheduler script exists and is executable"""
        scheduler_path = PROJECT_ROOT / "scripts" / "backup_scheduler.sh"

        self.assertTrue(scheduler_path.exists(), "Backup scheduler script not found")

        # Check if script is executable
        self.assertTrue(os.access(scheduler_path, os.X_OK), "Backup scheduler script is not executable")

        try:
            # Test help command
            result = subprocess.run(
                [str(scheduler_path), 'help'],
                capture_output=True,
                text=True,
                timeout=30
            )

            self.assertEqual(result.returncode, 0, "Backup scheduler help command failed")
            self.assertIn('KNI Webapp Backup Scheduler', result.stdout)

            print("✅ Backup scheduler script exists and is functional")

        except subprocess.TimeoutExpired:
            self.fail("Backup scheduler script timed out")
        except Exception as e:
            self.fail(f"Backup scheduler script test failed: {e}")

    def test_docker_entrypoint_backup_variables(self):
        """Test that Docker entrypoint contains backup-related environment variables"""
        entrypoint_path = PROJECT_ROOT / "docker" / "entrypoint.sh"

        if not entrypoint_path.exists():
            self.fail("Docker entrypoint script not found")

        try:
            with entrypoint_path.open() as f:
                entrypoint_content = f.read()

            # Check for backup environment variables
            backup_vars = [
                'RESTORE_BACKUP_FILE', 'RESTORE_BACKUP_MANIFEST',
                'RESTORE_LATEST_BACKUP', 'LOAD_BASELINE'
            ]

            for var in backup_vars:
                self.assertIn(var, entrypoint_content, f"Missing environment variable: {var}")

            # Check for backup restoration logic
            backup_logic = [
                'SHOULD_RESTORE_BACKUP', 'restore_tenant', 'backup source'
            ]

            for logic in backup_logic:
                self.assertIn(logic, entrypoint_content, f"Missing backup logic: {logic}")

            print("✅ Docker entrypoint contains backup functionality")

        except Exception as e:
            self.fail(f"Docker entrypoint backup test failed: {e}")


def run_tests():
    """Run all backup and restore system tests"""
    print("🧪 Starting Enhanced Backup and Restore System Tests")
    print("=" * 60)

    # Create test suite
    test_suite = [
        'test_backup_tenant_command_exists',
        'test_restore_tenant_command_exists',
        'test_list_backups_command_exists',
        'test_cleanup_backups_command_exists',
        'test_backup_creation_full',
        'test_backup_creation_incremental',
        'test_backup_with_compression',
        'test_list_backups_functionality',
        'test_restore_list_available',
        'test_backup_cleanup_dry_run',
        'test_schema_detection',
        'test_backup_manifest_structure',
        'test_makefile_backup_targets',
        'test_backup_scheduler_script',
        'test_docker_entrypoint_backup_variables',
    ]

    # Run tests
    test_instance = BackupRestoreSystemTest()
    test_instance.setUp()

    passed = 0
    failed = 0

    try:
        for test_name in test_suite:
            try:
                print(f"\n🔬 Running {test_name}...")
                test_method = getattr(test_instance, test_name)
                test_method()
                passed += 1
            except Exception as e:
                print(f"❌ {test_name} failed: {e}")
                failed += 1

    finally:
        test_instance.tearDown()

    # Print summary
    print("\n" + "=" * 60)
    print(f"🎯 Test Summary:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📊 Total:  {passed + failed}")

    if failed == 0:
        print("\n🎉 All tests passed! The enhanced backup and restore system is working correctly.")
        return True
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review the implementation.")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)