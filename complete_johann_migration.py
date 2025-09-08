#!/usr/bin/env python
"""
Complete Johann's content migration with proper site references
"""
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django_tenants.utils import schema_context
from wagtail.models import Site
from apps.projects.models import Project

def complete_johann_migration():
    """Complete Johann's content migration"""
    print("🔄 Completing Johann's content migration...")
    
    with schema_context('johann'):
        # Get the site
        site = Site.objects.first()
        if not site:
            print("❌ No site found in Johann's schema")
            return False
        
        print(f"🌐 Using site: {site.hostname}:{site.port}")
        
        # Create projects with site reference
        print("\n🏗️ Creating projects with site reference...")
        projects_data = [
            {
                "title": "En opgradering af TV alteret hos min kammerat",
                "description": "Opgraderingsprojekt af TV-altar med før og efter billeder. Moderne løsning med kvalitetsmaterialer.",
                "published": True,
                "featured": False,
                "site": site
            },
            {
                "title": "Udskiftning af punkteret rude", 
                "description": "Professionel udskiftning af punkteret rude med kvalitetsmaterialer og omhyggelig finish.",
                "published": True,
                "featured": False,
                "site": site
            },
            {
                "title": "Bevaringsværdige vinduer",
                "description": "Restaurering og renovering af bevaringsværdige vinduer med respekt for den oprindelige stil og håndværkstradition.",
                "published": True,
                "featured": True,
                "site": site
            },
            {
                "title": "Møbelsnedkeren i mig - simpelt sofabord",
                "description": "Mit første møbel er et simpelt sofabord der viser klassiske snedkerteknikker og kærlighed til træ.",
                "published": True,
                "featured": True,
                "site": site
            },
            {
                "title": "Fundamentbetonarbejde og skjulere",
                "description": "Professionelt fundamentbetonarbejde til nye byggerier med fokus på holdbarhed og præcision.",
                "published": True,
                "featured": False,
                "site": site
            },
            {
                "title": "Træhuse & nybyggeri",
                "description": "Fulde træbyggeprojekter fra tegning til nøglefærdig bolig med naturlige materialer og bæredygtige løsninger.",
                "published": True,
                "featured": True,
                "site": site
            },
            {
                "title": "Lærepladsen - undertag konstruktion",
                "description": "Underviser og guider lærlinge i korrekt undertag konstruktion trods vejrforholdene.",
                "published": True,
                "featured": False,
                "site": site
            },
            {
                "title": "Dørfuger og vedligeholdelse",
                "description": "Udskiftning af slidte fuger på døre for bedre isolering og længere holdbarhed.",
                "published": True,
                "featured": False,
                "site": site
            },
            {
                "title": "Lille trin i Jatoba træ",
                "description": "Elegant lille trin udført i eksotisk Jatoba træ med præcis finish og slidstærke egenskaber.",
                "published": True,
                "featured": True,
                "site": site
            }
        ]
        
        created_count = 0
        for project_data in projects_data:
            try:
                project, created = Project.objects.get_or_create(
                    title=project_data["title"],
                    defaults=project_data
                )
                if created:
                    print(f"  ✅ Created project: {project.title}")
                    created_count += 1
                else:
                    # Update existing project
                    for key, value in project_data.items():
                        if key != 'title':
                            setattr(project, key, value)
                    project.save()
                    print(f"  ✅ Updated project: {project.title}")
            except Exception as e:
                print(f"  ⚠️ Error with project '{project_data['title']}': {e}")
        
        print(f"\n🎉 Johann's content migration completed!")
        print(f"📊 Projects: {Project.objects.count()} total")
        print(f"🔗 Johann's Wagtail admin: http://johann.localhost:8004/admin/")
        print(f"👤 Login: JCleemannByg / admin123")
        print(f"\n✨ Johann can now manage his construction business website!")
        
        return True

if __name__ == '__main__':
    try:
        complete_johann_migration()
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        import traceback
        traceback.print_exc()