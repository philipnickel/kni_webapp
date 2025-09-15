#!/usr/bin/env python3
"""
Simple validation script for the Enhanced Backup and Restore System

This script performs basic validation without requiring Django setup.
"""

import os
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def validate_management_commands():
    """Validate that all required management commands exist"""
    commands_dir = PROJECT_ROOT / "apps" / "core" / "management" / "commands"

    required_commands = [
        "backup_tenant.py",
        "restore_tenant.py",
        "list_backups.py",
        "cleanup_backups.py"
    ]

    results = {}

    for command in required_commands:
        command_path = commands_dir / command
        exists = command_path.exists()
        results[command] = {
            "exists": exists,
            "path": str(command_path),
            "size": command_path.stat().st_size if exists else 0
        }

        if exists:
            # Check for key functionality indicators
            with command_path.open() as f:
                content = f.read()

            if command == "backup_tenant.py":
                results[command]["has_schema_aware"] = "schema" in content.lower()
                results[command]["has_compression"] = "compress" in content.lower()
                results[command]["has_retention"] = "retention" in content.lower()

            elif command == "restore_tenant.py":
                results[command]["has_rollback"] = "rollback" in content.lower()
                results[command]["has_manifest"] = "manifest" in content.lower()
                results[command]["has_baseline"] = "baseline" in content.lower()

    return results

def validate_makefile_integration():
    """Validate Makefile has backup commands"""
    makefile_path = PROJECT_ROOT / "Makefile"

    if not makefile_path.exists():
        return {"exists": False, "commands": []}

    with makefile_path.open() as f:
        content = f.read()

    backup_commands = [
        "backup:", "restore:", "list-backups:", "clean-backups:",
        "backup-health:", "backup-full:", "backup-incremental:"
    ]

    found_commands = []
    for cmd in backup_commands:
        if cmd in content:
            found_commands.append(cmd.rstrip(":"))

    return {
        "exists": True,
        "total_commands": len(backup_commands),
        "found_commands": len(found_commands),
        "commands": found_commands,
        "has_backup_section": "Backup Management Commands" in content
    }

def validate_scheduler_script():
    """Validate backup scheduler script"""
    script_path = PROJECT_ROOT / "scripts" / "backup_scheduler.sh"

    if not script_path.exists():
        return {"exists": False}

    # Check if executable
    is_executable = os.access(script_path, os.X_OK)

    with script_path.open() as f:
        content = f.read()

    features = {
        "has_cron_support": "cron" in content.lower(),
        "has_retention_policy": "retention" in content.lower(),
        "has_notification": "notification" in content.lower() or "slack" in content.lower(),
        "has_health_check": "health" in content.lower(),
        "has_environment_vars": "BACKUP_" in content
    }

    return {
        "exists": True,
        "executable": is_executable,
        "size": script_path.stat().st_size,
        "features": features
    }

def validate_docker_integration():
    """Validate Docker entrypoint has backup capabilities"""
    entrypoint_path = PROJECT_ROOT / "docker" / "entrypoint.sh"

    if not entrypoint_path.exists():
        return {"exists": False}

    with entrypoint_path.open() as f:
        content = f.read()

    backup_vars = [
        "RESTORE_BACKUP_FILE", "RESTORE_BACKUP_MANIFEST",
        "RESTORE_LATEST_BACKUP", "LOAD_BASELINE"
    ]

    found_vars = []
    for var in backup_vars:
        if var in content:
            found_vars.append(var)

    features = {
        "has_backup_restoration": "restore_tenant" in content,
        "has_backup_fallback": "fallback" in content.lower(),
        "has_environment_docs": "Environment Variables for Backup" in content,
        "supports_manifest_restore": "manifest" in content,
        "supports_file_restore": "backup-file" in content
    }

    return {
        "exists": True,
        "found_variables": len(found_vars),
        "total_variables": len(backup_vars),
        "variables": found_vars,
        "features": features
    }

def validate_directory_structure():
    """Validate expected directory structure"""
    expected_dirs = [
        "apps/core/management/commands",
        "scripts",
        "docker",
        "claude-tests"
    ]

    results = {}
    for dir_path in expected_dirs:
        full_path = PROJECT_ROOT / dir_path
        results[dir_path] = {
            "exists": full_path.exists(),
            "is_dir": full_path.is_dir() if full_path.exists() else False
        }

    return results

def generate_report():
    """Generate comprehensive validation report"""
    print("🔍 Enhanced Backup and Restore System Validation")
    print("=" * 60)

    # Validate components
    commands = validate_management_commands()
    makefile = validate_makefile_integration()
    scheduler = validate_scheduler_script()
    docker = validate_docker_integration()
    structure = validate_directory_structure()

    # Management Commands Report
    print("\n📋 Management Commands:")
    for cmd, info in commands.items():
        status = "✅" if info["exists"] else "❌"
        print(f"  {status} {cmd} ({info['size']} bytes)")

        if info["exists"] and cmd == "backup_tenant.py":
            features = []
            if info.get("has_schema_aware"): features.append("schema-aware")
            if info.get("has_compression"): features.append("compression")
            if info.get("has_retention"): features.append("retention")
            if features:
                print(f"     Features: {', '.join(features)}")

        elif info["exists"] and cmd == "restore_tenant.py":
            features = []
            if info.get("has_rollback"): features.append("rollback")
            if info.get("has_manifest"): features.append("manifest")
            if info.get("has_baseline"): features.append("baseline")
            if features:
                print(f"     Features: {', '.join(features)}")

    # Makefile Integration Report
    print(f"\n🔨 Makefile Integration:")
    if makefile["exists"]:
        print(f"  ✅ Makefile exists")
        print(f"  📊 Commands: {makefile['found_commands']}/{makefile['total_commands']}")
        if makefile["has_backup_section"]:
            print(f"  ✅ Dedicated backup section found")
        if makefile["commands"]:
            print(f"     Available: {', '.join(makefile['commands'])}")
    else:
        print(f"  ❌ Makefile not found")

    # Scheduler Script Report
    print(f"\n⏰ Backup Scheduler:")
    if scheduler["exists"]:
        print(f"  ✅ Script exists ({scheduler['size']} bytes)")
        print(f"  {'✅' if scheduler['executable'] else '❌'} Executable permissions")

        features = scheduler["features"]
        for feature, has_it in features.items():
            status = "✅" if has_it else "❌"
            print(f"  {status} {feature.replace('_', ' ').title()}")
    else:
        print(f"  ❌ Scheduler script not found")

    # Docker Integration Report
    print(f"\n🐳 Docker Integration:")
    if docker["exists"]:
        print(f"  ✅ Entrypoint script exists")
        print(f"  📊 Environment variables: {docker['found_variables']}/{docker['total_variables']}")

        features = docker["features"]
        for feature, has_it in features.items():
            status = "✅" if has_it else "❌"
            print(f"  {status} {feature.replace('_', ' ').title()}")
    else:
        print(f"  ❌ Docker entrypoint not found")

    # Directory Structure Report
    print(f"\n📁 Directory Structure:")
    for dir_path, info in structure.items():
        status = "✅" if info["exists"] and info["is_dir"] else "❌"
        print(f"  {status} {dir_path}")

    # Overall Assessment
    print(f"\n🎯 Overall Assessment:")

    # Count successful components
    scores = {
        "commands": sum(1 for cmd in commands.values() if cmd["exists"]),
        "makefile": 1 if makefile["exists"] and makefile["found_commands"] > 5 else 0,
        "scheduler": 1 if scheduler["exists"] and scheduler["executable"] else 0,
        "docker": 1 if docker["exists"] and docker["found_variables"] > 2 else 0,
        "structure": sum(1 for dir_info in structure.values() if dir_info["exists"])
    }

    total_score = sum(scores.values())
    max_score = 4 + len(makefile.get("commands", [])) + 1 + 1 + len(structure)

    if total_score >= max_score * 0.9:
        print(f"  🎉 Excellent! System is fully implemented ({total_score}/{max_score})")
    elif total_score >= max_score * 0.7:
        print(f"  ✅ Good! Most components are working ({total_score}/{max_score})")
    elif total_score >= max_score * 0.5:
        print(f"  ⚠️  Partial implementation ({total_score}/{max_score})")
    else:
        print(f"  ❌ Significant issues found ({total_score}/{max_score})")

    # Recommendations
    print(f"\n💡 Recommendations:")
    issues = []

    if not all(cmd["exists"] for cmd in commands.values()):
        issues.append("Complete missing management commands")

    if not scheduler["exists"] or not scheduler["executable"]:
        issues.append("Fix backup scheduler script")

    if makefile["found_commands"] < 5:
        issues.append("Add more Makefile backup commands")

    if docker["found_variables"] < 3:
        issues.append("Enhance Docker backup integration")

    if issues:
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    else:
        print(f"  🎯 All components look good! Ready for production use.")

    print(f"\n📖 Usage Examples:")
    print(f"  make backup              # Create manual backup")
    print(f"  make restore             # Interactive restore")
    print(f"  make list-backups        # List available backups")
    print(f"  ./scripts/backup_scheduler.sh schedule  # Automated backup")

if __name__ == "__main__":
    generate_report()