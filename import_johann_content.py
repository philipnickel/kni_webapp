#!/usr/bin/env python
"""
Import Johann's original content into his multi-tenant schema
"""
import os
import sys
import django
import json
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core import serializers
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from wagtail.images.models import Image
from wagtail.documents.models import Document
from apps.pages.models import HomePage, GalleryPage, ContactPage, ModularPage, Service, Testimonial, Logo, ThemeSettings
from apps.projects.models import Project, ProjectImage

def import_johann_content():
    """Import Johann's content into his tenant schema"""
    print("🔄 Importing Johann's content into tenant schema...")
    
    export_dir = "johann_content_export"
    if not os.path.exists(export_dir):
        print(f"❌ Export directory {export_dir} not found!")
        return False
    
    # Import everything in Johann's tenant schema
    with schema_context('johann'):
        try:
            # 1. Update admin username to 'JCleemannByg'
            print("\n👤 Updating admin user...")
            try:
                admin_user = User.objects.get(username='admin')
                admin_user.username = 'JCleemannByg'
                admin_user.email = 'johann@jcleemannbyg.dk'
                admin_user.first_name = 'Johann'
                admin_user.last_name = 'Cleemann'
                admin_user.save()
                print(f"  ✅ Updated admin user to: JCleemannByg")
            except User.DoesNotExist:
                # User already exists as JCleemannByg, just update details
                try:
                    admin_user = User.objects.get(username='JCleemannByg')
                    admin_user.email = 'johann@jcleemannbyg.dk'
                    admin_user.first_name = 'Johann'
                    admin_user.last_name = 'Cleemann'
                    admin_user.save()
                    print(f"  ✅ Updated existing JCleemannByg user details")
                except User.DoesNotExist:
                    print("  ⚠️ No admin user found")
            
            # 2. Import images
            print("\n🖼️ Importing images...")
            images_file = f"{export_dir}/images.json"
            if os.path.exists(images_file):
                with open(images_file, 'r', encoding='utf-8') as f:
                    images_data = json.load(f)
                
                for image_obj in serializers.deserialize('json', json.dumps(images_data)):
                    try:
                        image = image_obj.object
                        image.save()
                        print(f"  ✅ Imported image: {image.title}")
                    except Exception as e:
                        print(f"  ⚠️ Error importing image: {e}")
            
            # 3. Import snippets (Services, Testimonials, Logos) - skip ThemeSettings for now
            snippets_to_import = [
                ('services', Service, 'Services'),
                ('testimonials', Testimonial, 'Testimonials'), 
                ('logos', Logo, 'Logos'),
            ]
            
            for filename, model_class, display_name in snippets_to_import:
                print(f"\n📋 Importing {display_name}...")
                file_path = f"{export_dir}/{filename}.json"
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    for obj in serializers.deserialize('json', json.dumps(data)):
                        try:
                            obj.save()
                            print(f"  ✅ Imported {display_name}: {getattr(obj.object, 'title', obj.object)}")
                        except Exception as e:
                            print(f"  ⚠️ Error importing {display_name}: {e}")
            
            # 3b. Import Theme Settings manually due to site references
            print(f"\n📋 Importing Theme Settings...")
            theme_file = f"{export_dir}/theme_settings.json"
            if os.path.exists(theme_file):
                try:
                    # Create theme settings without site reference dependency
                    theme_settings = ThemeSettings.objects.create(default_theme='forest')
                    print(f"  ✅ Created default theme settings")
                except Exception as e:
                    print(f"  ⚠️ Error creating theme settings: {e}")
            
            # 4. Import projects and project images
            print("\n🏗️ Importing projects...")
            projects_file = f"{export_dir}/projects.json"
            if os.path.exists(projects_file):
                with open(projects_file, 'r', encoding='utf-8') as f:
                    projects_data = json.load(f)
                
                for project_obj in serializers.deserialize('json', json.dumps(projects_data)):
                    try:
                        project = project_obj.object
                        project.save()
                        print(f"  ✅ Imported project: {project.title}")
                    except Exception as e:
                        print(f"  ⚠️ Error importing project: {e}")
            
            # Import project images
            print("\n📸 Importing project images...")
            project_images_file = f"{export_dir}/project_images.json"
            if os.path.exists(project_images_file):
                with open(project_images_file, 'r', encoding='utf-8') as f:
                    project_images_data = json.load(f)
                
                for proj_img_obj in serializers.deserialize('json', json.dumps(project_images_data)):
                    try:
                        proj_img_obj.save()
                        print(f"  ✅ Imported project image")
                    except Exception as e:
                        print(f"  ⚠️ Error importing project image: {e}")
            
            # 5. Import pages
            page_types = [
                ('homepage', HomePage, 'Homepage'),
                ('gallery_pages', GalleryPage, 'Gallery Pages'),
                ('contact_pages', ContactPage, 'Contact Pages'),
                ('modular_pages', ModularPage, 'Modular Pages'),
            ]
            
            for filename, model_class, display_name in page_types:
                print(f"\n📄 Importing {display_name}...")
                file_path = f"{export_dir}/{filename}.json"
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    for page_obj in serializers.deserialize('json', json.dumps(data)):
                        try:
                            page = page_obj.object
                            # Ensure page has proper parent and path
                            if hasattr(page, 'get_parent') and not page.get_parent():
                                # This is a root-level page, set it as child of root
                                from wagtail.models import Page
                                root = Page.get_first_root_node()
                                root.add_child(instance=page)
                            else:
                                page.save()
                            print(f"  ✅ Imported {display_name}: {page.title}")
                        except Exception as e:
                            print(f"  ⚠️ Error importing {display_name}: {e}")
            
            # 6. Create site mapping for Johann's pages
            print("\n🌐 Setting up site configuration...")
            try:
                from wagtail.models import Site, Page
                
                # Get or create a site for Johann's tenant
                homepage = HomePage.objects.first()
                if homepage:
                    site, created = Site.objects.get_or_create(
                        hostname='johann.localhost',
                        defaults={
                            'port': 8004,
                            'site_name': 'JCleemannByg',
                            'root_page': homepage,
                            'is_default_site': True
                        }
                    )
                    if created:
                        print("  ✅ Created site configuration for Johann")
                    else:
                        print("  ✅ Site configuration already exists")
            except Exception as e:
                print(f"  ⚠️ Error setting up site: {e}")
            
            print("\n🎉 Johann's content migration completed!")
            print("🔗 Johann's Wagtail admin: http://johann.localhost:8004/admin/")
            print("👤 Login: JCleemannByg / admin123")
            return True
            
        except Exception as e:
            print(f"\n❌ Error during import: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == '__main__':
    import_johann_content()