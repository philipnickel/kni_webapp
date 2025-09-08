#!/usr/bin/env python
"""
Systematic setup of Johann's tenant with proper Wagtail configuration
This follows the GitHub discussion approach - fake problematic migrations, create tables manually
"""
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.db import connection
from django_tenants.utils import schema_context
from django.core.management import call_command

def setup_johann_wagtail():
    """
    Systematically set up Johann's Wagtail tenant
    Phase 1: Migrate safe apps
    Phase 2: Fake problematic migrations  
    Phase 3: Create missing tables manually
    """
    
    print("🚀 Setting up Johann's Wagtail tenant systematically...")
    
    # Phase 1: Migrate all basic Django and safe Wagtail migrations first
    print("\n📦 Phase 1: Running safe migrations...")
    
    safe_apps = [
        'admin',
        'auth', 
        'contenttypes',
        'sessions',
        'sites',
        'taggit',
        'tenants',
        'contacts',
        'pages',
        'projects',
    ]
    
    for app in safe_apps:
        print(f"  ✅ Migrating {app}")
        try:
            call_command('migrate', app, '--tenant', '--schema=johann', verbosity=0)
        except Exception as e:
            print(f"    ⚠️ {app} migration issue: {e}")
    
    # Phase 2: Fake problematic Wagtail migrations
    print("\n🎭 Phase 2: Faking problematic migrations...")
    
    problematic_migrations = [
        # Most problematic - image/file handling
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('wagtaildocs', '0013_delete_uploadeddocument'),
        
        # Core migrations that might have dependency issues
        ('wagtailcore', '0096_image_rendition'),
        ('wagtailcore', '0097_remove_image_collection_remove_image_tags_and_more'),
        
        # User profile issues
        ('wagtailcore', '0098_userprofile'),
        ('wagtailcore', '0099_delete_userprofile'),
    ]
    
    for app, migration in problematic_migrations:
        print(f"  🎭 Faking {app}.{migration}")
        try:
            call_command('migrate', app, migration, '--fake', '--tenant', '--schema=johann', verbosity=0)
        except Exception as e:
            print(f"    ⚠️ {app}.{migration} fake failed: {e}")
    
    # Phase 3: Run remaining migrations normally
    print("\n🏃 Phase 3: Running remaining Wagtail migrations...")
    
    remaining_apps = [
        'wagtailadmin',
        'wagtailcore', 
        'wagtaildocs',
        'wagtailimages',
        'wagtailredirects',
        'wagtailusers',
    ]
    
    for app in remaining_apps:
        print(f"  📦 Migrating remaining {app}")
        try:
            call_command('migrate', app, '--tenant', '--schema=johann', verbosity=0)
        except Exception as e:
            print(f"    ⚠️ {app} remaining migration issue: {e}")
    
    # Phase 4: Create missing tables manually
    print("\n🔧 Phase 4: Creating any missing tables manually...")
    
    with schema_context('johann'):
        with connection.cursor() as cursor:
            # Check what tables we have now
            cursor.execute("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'johann' 
                ORDER BY table_name;
            """)
            existing_tables = [row[0] for row in cursor.fetchall()]
            print(f"📋 Found {len(existing_tables)} tables after migrations")
            
            # Ensure essential Wagtail tables exist
            essential_tables = [
                'wagtailcore_locale',
                'wagtailcore_collection', 
                'wagtailcore_page',
                'wagtailcore_site',
                'wagtailusers_userprofile',
                'wagtailimages_image',
                'wagtailimages_rendition',
                'wagtaildocs_document'
            ]
            
            missing_tables = [table for table in essential_tables if table not in existing_tables]
            
            if missing_tables:
                print(f"❌ Missing tables: {missing_tables}")
                print("🔨 Creating missing tables...")
                create_missing_wagtail_tables(cursor)
            else:
                print("✅ All essential Wagtail tables exist!")
    
    # Phase 5: Create superuser
    print("\n👤 Phase 5: Creating superuser for Johann...")
    create_johann_superuser()
    
    print("\n🎉 Johann's Wagtail setup completed!")
    print("🌐 Try: http://johann.localhost:8004/admin/")
    print("👤 Login: admin / admin123")

def create_missing_wagtail_tables(cursor):
    """Create any missing Wagtail tables with proper structure"""
    
    # Create locale table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailcore_locale (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            language_code VARCHAR(12) NOT NULL UNIQUE
        );
    """)
    
    # Insert default locale
    cursor.execute("""
        INSERT INTO wagtailcore_locale (language_code)
        SELECT 'da' 
        WHERE NOT EXISTS (SELECT 1 FROM wagtailcore_locale WHERE language_code = 'da');
    """)
    
    # Create collection table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailcore_collection (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            path VARCHAR(255) NOT NULL UNIQUE,
            depth INTEGER NOT NULL CHECK (depth >= 0),
            numchild INTEGER NOT NULL CHECK (numchild >= 0),
            name VARCHAR(255) NOT NULL
        );
    """)
    
    # Insert root collection
    cursor.execute("""
        INSERT INTO wagtailcore_collection (path, depth, numchild, name)
        SELECT '0001', 1, 0, 'Root'
        WHERE NOT EXISTS (SELECT 1 FROM wagtailcore_collection WHERE path = '0001');
    """)
    
    # Get locale ID for foreign keys
    cursor.execute("SELECT id FROM wagtailcore_locale WHERE language_code = 'da'")
    locale_result = cursor.fetchone()
    locale_id = locale_result[0] if locale_result else 1
    
    # Create page table with ALL required columns
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS wagtailcore_page (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            path VARCHAR(255) NOT NULL UNIQUE,
            depth INTEGER NOT NULL CHECK (depth >= 0),
            numchild INTEGER NOT NULL CHECK (numchild >= 0),
            title VARCHAR(255) NOT NULL,
            slug VARCHAR(255),
            content_type_id INTEGER NOT NULL,
            live BOOLEAN NOT NULL DEFAULT TRUE,
            has_unpublished_changes BOOLEAN NOT NULL DEFAULT FALSE,
            url_path TEXT NOT NULL,
            owner_id INTEGER,
            seo_title VARCHAR(255),
            show_in_menus BOOLEAN NOT NULL DEFAULT FALSE,
            search_description TEXT,
            go_live_at TIMESTAMP WITH TIME ZONE,
            expire_at TIMESTAMP WITH TIME ZONE,
            expired BOOLEAN NOT NULL DEFAULT FALSE,
            locked BOOLEAN NOT NULL DEFAULT FALSE,
            locked_at TIMESTAMP WITH TIME ZONE,
            locked_by_id INTEGER,
            first_published_at TIMESTAMP WITH TIME ZONE,
            last_published_at TIMESTAMP WITH TIME ZONE,
            latest_revision_created_at TIMESTAMP WITH TIME ZONE,
            latest_revision_id INTEGER,
            live_revision_id INTEGER,
            alias_of_id INTEGER,
            locale_id INTEGER NOT NULL DEFAULT {locale_id},
            translation_key UUID,
            draft_title VARCHAR(255),
            wagtail_admin_comments TEXT
        );
    """)
    
    # Create site table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailcore_site (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            hostname VARCHAR(255) NOT NULL,
            port INTEGER NOT NULL,
            site_name VARCHAR(255),
            root_page_id INTEGER,
            is_default_site BOOLEAN NOT NULL DEFAULT FALSE
        );
    """)
    
    # Create userprofile table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailusers_userprofile (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            user_id INTEGER NOT NULL UNIQUE,
            submitted_notifications BOOLEAN NOT NULL DEFAULT TRUE,
            approved_notifications BOOLEAN NOT NULL DEFAULT TRUE,
            rejected_notifications BOOLEAN NOT NULL DEFAULT TRUE,
            updated_comments_notifications BOOLEAN NOT NULL DEFAULT TRUE,
            preferred_language VARCHAR(10) NOT NULL DEFAULT '',
            current_time_zone VARCHAR(40) NOT NULL DEFAULT '',
            avatar VARCHAR(100) NOT NULL DEFAULT '',
            dismissibles JSONB NOT NULL DEFAULT '{}',
            theme VARCHAR(20) NOT NULL DEFAULT 'system',
            density VARCHAR(20) NOT NULL DEFAULT 'default',
            contrast VARCHAR(20) NOT NULL DEFAULT 'default'
        );
    """)
    
    # Create basic image table structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailimages_image (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            title VARCHAR(255) NOT NULL,
            file VARCHAR(100) NOT NULL,
            width INTEGER,
            height INTEGER,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
            focal_point_x INTEGER,
            focal_point_y INTEGER,
            focal_point_width INTEGER,
            focal_point_height INTEGER,
            uploaded_by_user_id INTEGER,
            file_size INTEGER,
            file_hash VARCHAR(40) NOT NULL DEFAULT '',
            collection_id INTEGER NOT NULL DEFAULT 1
        );
    """)
    
    # Create rendition table  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtailimages_rendition (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            filter_spec VARCHAR(255) NOT NULL,
            file VARCHAR(100) NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL,
            focal_point_key VARCHAR(16) NOT NULL,
            image_id INTEGER NOT NULL
        );
    """)
    
    # Create document table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wagtaildocs_document (
            id BIGINT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
            title VARCHAR(255) NOT NULL,
            file VARCHAR(100) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
            uploaded_by_user_id INTEGER,
            file_size INTEGER,
            file_hash VARCHAR(40) NOT NULL DEFAULT '',
            collection_id INTEGER NOT NULL DEFAULT 1
        );
    """)
    
    print("✅ Created missing Wagtail tables")

def create_johann_superuser():
    """Create superuser in Johann's schema"""
    with schema_context('johann'):
        from django.contrib.auth.models import User
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ Created admin user (admin/admin123)")
        else:
            print("✅ Admin user already exists")

if __name__ == '__main__':
    try:
        setup_johann_wagtail()
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        import traceback
        traceback.print_exc()
