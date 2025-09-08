#!/usr/bin/env python
"""
Simple export of Johann's content using Django's built-in serialization
"""
import os
import sys
import django

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
    """Export all of Johann's content using Django serialization"""
    print("🔄 Exporting Johann's existing content...")
    
    # Create export directory
    export_dir = "johann_content_export"
    os.makedirs(export_dir, exist_ok=True)
    
    # Export using Django's serialization
    models_to_export = [
        ('users', User.objects.all()),
        ('homepage', HomePage.objects.all()),
        ('gallery_pages', GalleryPage.objects.all()),
        ('contact_pages', ContactPage.objects.all()),
        ('modular_pages', ModularPage.objects.all()),
        ('services', Service.objects.all()),
        ('testimonials', Testimonial.objects.all()),
        ('logos', Logo.objects.all()),
        ('theme_settings', ThemeSettings.objects.all()),
        ('projects', Project.objects.all()),
        ('project_images', ProjectImage.objects.all()),
        ('images', Image.objects.all()),
        ('documents', Document.objects.all()),
    ]
    
    for name, queryset in models_to_export:
        if queryset.exists():
            with open(f"{export_dir}/{name}.json", 'w', encoding='utf-8') as f:
                serializers.serialize('json', queryset, stream=f, indent=2, use_natural_foreign_keys=True)
            print(f"  ✅ Exported {queryset.count()} {name}")
        else:
            print(f"  ⚠️ No {name} found")
    
    # Also export specific content we care about
    print("\n📋 Content Summary:")
    if HomePage.objects.exists():
        home = HomePage.objects.first()
        print(f"  🏠 Homepage: '{home.title}'")
        if hasattr(home, 'body') and home.body:
            print(f"     Body content: {len(str(home.body))} characters")
    
    if Project.objects.exists():
        projects = Project.objects.all()
        print(f"  🏗️ Projects: {projects.count()}")
        for project in projects:
            images_count = project.project_images.count() if hasattr(project, 'project_images') else 0
            print(f"     - {project.title} ({images_count} images)")
    
    if Service.objects.exists():
        services = Service.objects.all()
        print(f"  🔧 Services: {services.count()}")
        for service in services:
            print(f"     - {service.title}")
    
    if Testimonial.objects.exists():
        testimonials = Testimonial.objects.all()
        print(f"  💬 Testimonials: {testimonials.count()}")
        for testimonial in testimonials:
            print(f"     - {testimonial.name}")
    
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