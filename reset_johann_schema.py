#!/usr/bin/env python
"""
Completely reset Johann's tenant schema and recreate it properly
"""
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.db import connection
from django_tenants.utils import schema_context

def reset_johann_schema():
    """Drop and recreate Johann's schema completely"""
    print("🔥 Resetting Johann's tenant schema completely...")
    
    with connection.cursor() as cursor:
        # Drop the entire johann schema
        print("🗑️ Dropping johann schema...")
        cursor.execute("DROP SCHEMA IF EXISTS johann CASCADE;")
        
        # Recreate empty johann schema
        print("🆕 Creating fresh johann schema...")
        cursor.execute("CREATE SCHEMA johann;")
        
        # Set search path to johann
        cursor.execute("SET search_path TO johann;")
        
        print("✅ Johann schema reset successfully!")
        print("📋 Schema is now completely empty and ready for proper setup")

if __name__ == '__main__':
    try:
        reset_johann_schema()
        print("\n🎉 Johann's schema has been reset!")
        print("🔧 Ready for systematic Wagtail setup")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()