#!/usr/bin/env python
"""
Export Johann's existing content from original database
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
from wagtail.images.models import Image
from wagtail.documents.models import Document
from apps.pages.models import HomePage, GalleryPage, ContactPage, ModularPage, Service, Testimonial, Logo, ThemeSettings
from apps.projects.models import Project, ProjectImage

def export_johann_content():
    """Export all of Johann's content to JSON files"""
    print("🔄 Exporting Johann's existing content...")
    
    # Create export directory
    export_dir = "johann_content_export"
    os.makedirs(export_dir, exist_ok=True)
    
    # Export data
    exports = {
        # Users
        'users': list(User.objects.values(
            'id', 'username', 'email', 'first_name', 'last_name', 
            'is_staff', 'is_superuser', 'date_joined'
        )),
        
        # Pages content
        'homepage': list(HomePage.objects.values()),
        'gallery_pages': list(GalleryPage.objects.values()),
        'contact_pages': list(ContactPage.objects.values()), 
        'modular_pages': list(ModularPage.objects.values()),
        
        # Snippets
        'services': list(Service.objects.values()),
        'testimonials': list(Testimonial.objects.values()),
        'logos': list(Logo.objects.values()),
        'theme_settings': list(ThemeSettings.objects.values()),
        
        # Projects
        'projects': list(Project.objects.values()),
        'project_images': list(ProjectImage.objects.values()),
        
        # Images and Documents
        'images': list(Image.objects.values(
            'id', 'title', 'file', 'width', 'height', 'created_at',
            'focal_point_x', 'focal_point_y', 'file_size', 'file_hash'
        )),
        'documents': list(Document.objects.values(
            'id', 'title', 'file', 'created_at', 'file_size', 'file_hash'
        )),
    }
    
    # Convert complex objects to JSON-serializable format
    def convert_for_json(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__str__') and str(type(obj)).find('UUID') != -1:
            return str(obj)
        elif hasattr(obj, 'stream_data'):  # StreamValue
            return str(obj)  # Convert StreamValue to string representation
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return obj
    
    # Save each export to separate JSON files
    for key, data in exports.items():
        if data:  # Only save non-empty data
            # Convert datetimes in the data
            json_data = []
            for item in data:
                converted_item = {}
                for k, v in item.items():
                    converted_item[k] = convert_for_json(v)
                json_data.append(converted_item)
                
            with open(f"{export_dir}/{key}.json", 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            print(f"  ✅ Exported {len(data)} {key}")
        else:
            print(f"  ⚠️ No {key} found")
    
    # Export page tree structure
    try:
        from wagtail.models import Page
        pages = []
        for page in Page.objects.all():
            pages.append({
                'id': page.id,
                'path': page.path,
                'depth': page.depth,
                'numchild': page.numchild,
                'title': page.title,
                'slug': page.slug,
                'content_type': str(page.content_type),
                'url_path': page.url_path,
                'live': page.live,
            })
        
        with open(f"{export_dir}/page_tree.json", 'w', encoding='utf-8') as f:
            json.dump(pages, f, indent=2, ensure_ascii=False)
        print(f"  ✅ Exported page tree structure ({len(pages)} pages)")
        
    except Exception as e:
        print(f"  ⚠️ Could not export page tree: {e}")
    
    print(f"\n📦 All content exported to {export_dir}/ directory")
    print("🔗 Ready to migrate to new multi-tenant system!")
    
    return export_dir

if __name__ == '__main__':
    try:
        export_johann_content()
    except Exception as e:
        print(f"\n❌ Error during export: {e}")
        import traceback
        traceback.print_exc()