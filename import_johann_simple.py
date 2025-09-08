#!/usr/bin/env python
"""
Simple import of Johann's projects and pages without site references
"""
import os
import sys
import django
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django_tenants.utils import schema_context
from apps.projects.models import Project, ProjectImage
from apps.pages.models import HomePage, GalleryPage, ContactPage, ModularPage

def import_projects_simple():
    """Import projects without site references"""
    print("🔄 Importing Johann's projects and pages (simple)...")
    
    with schema_context('johann'):
        # Import projects manually
        print("\n🏗️ Creating projects...")
        projects_data = [
            {
                "title": "En opgradering af TV alteret hos min kammerat Efter og før",
                "description": "Opgraderingsprojekt af TV-altar med før og efter billeder.",
                "published": True,
                "featured": False
            },
            {
                "title": "Udskiftning af punkteret rude", 
                "description": "Professionel udskiftning af punkteret rude med kvalitetsmaterialer.",
                "published": True,
                "featured": False
            },
            {
                "title": "Bevaringsværdige vinduer",
                "description": "Restaurering og renovering af bevaringsværdige vinduer med respekt for den oprindelige stil.",
                "published": True,
                "featured": True
            },
            {
                "title": "Møbelsnedkeren i mig - simpelt sofabord",
                "description": "Mit første møbel er et simpelt sofabord der viser snedkerteknikker.",
                "published": True,
                "featured": True
            },
            {
                "title": "Fundamentbetonarbejde",
                "description": "Professionelt fundamentbetonarbejde til nye byggerier.",
                "published": True,
                "featured": False
            },
            {
                "title": "Træhuse & nybyggeri",
                "description": "Fulde træbyggeprojekter fra tegning til nøglefærdig bolig med naturlige materialer.",
                "published": True,
                "featured": True
            }
        ]
        
        for project_data in projects_data:
            try:
                project, created = Project.objects.get_or_create(
                    title=project_data["title"],
                    defaults=project_data
                )
                if created:
                    print(f"  ✅ Created project: {project.title}")
                else:
                    print(f"  ✅ Project exists: {project.title}")
            except Exception as e:
                print(f"  ⚠️ Error creating project: {e}")
        
        # Create pages manually
        print("\n📄 Creating pages...")
        
        # Create homepage if it doesn't exist
        try:
            homepage, created = HomePage.objects.get_or_create(
                slug='home',
                defaults={
                    'title': 'Velkommen til JCleemannByg',
                    'intro': '<p>Kvalitets træbyggeri med omtanke. Vi skaber varme træhjem og funktionelle løsninger med over 20 års erfaring i håndværkstradition.</p>',
                    'path': '00010001',
                    'depth': 2,
                    'numchild': 0,
                    'url_path': '/home/',
                    'live': True
                }
            )
            if created:
                print(f"  ✅ Created homepage: {homepage.title}")
            else:
                print(f"  ✅ Homepage exists: {homepage.title}")
        except Exception as e:
            print(f"  ⚠️ Error creating homepage: {e}")
        
        # Create gallery page
        try:
            gallery, created = GalleryPage.objects.get_or_create(
                slug='projekter',
                defaults={
                    'title': 'Vores Projekter',
                    'intro': '<p>Se vores tidligere arbejde og bliv inspireret til dit næste træbyggeri projekt.</p>',
                    'path': '00010002',
                    'depth': 2,
                    'numchild': 0,
                    'url_path': '/projekter/',
                    'live': True
                }
            )
            if created:
                print(f"  ✅ Created gallery page: {gallery.title}")
            else:
                print(f"  ✅ Gallery page exists: {gallery.title}")
        except Exception as e:
            print(f"  ⚠️ Error creating gallery page: {e}")
        
        # Create contact page
        try:
            contact, created = ContactPage.objects.get_or_create(
                slug='kontakt',
                defaults={
                    'title': 'Kontakt Os',
                    'intro': '<p>Kontakt os i dag for et uforpligtende tilbud på dit træbyggeri projekt.</p>',
                    'contact_form_title': 'Få et tilbud',
                    'contact_form_intro': '<p>Beskriv dit projekt og vi vender tilbage hurtigst muligt.</p>',
                    'show_contact_form': True,
                    'path': '00010003',
                    'depth': 2,
                    'numchild': 0,
                    'url_path': '/kontakt/',
                    'live': True
                }
            )
            if created:
                print(f"  ✅ Created contact page: {contact.title}")
            else:
                print(f"  ✅ Contact page exists: {contact.title}")
        except Exception as e:
            print(f"  ⚠️ Error creating contact page: {e}")
        
        print("\n🎉 Simple content migration completed!")
        print("🔗 Johann's Wagtail admin: http://johann.localhost:8004/admin/")
        print("👤 Login: JCleemannByg / admin123")
        
        # Summary
        project_count = Project.objects.count()
        homepage_count = HomePage.objects.count()
        gallery_count = GalleryPage.objects.count()
        contact_count = ContactPage.objects.count()
        
        print(f"\n📊 Content Summary:")
        print(f"  🏗️ Projects: {project_count}")
        print(f"  🏠 Homepage: {homepage_count}")
        print(f"  🖼️ Gallery Pages: {gallery_count}")
        print(f"  📞 Contact Pages: {contact_count}")

if __name__ == '__main__':
    try:
        import_projects_simple()
    except Exception as e:
        print(f"\n❌ Error during import: {e}")
        import traceback
        traceback.print_exc()