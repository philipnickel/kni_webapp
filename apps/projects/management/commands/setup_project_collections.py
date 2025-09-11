from django.core.management.base import BaseCommand
from django.utils.text import slugify
from wagtail.models import Collection


class Command(BaseCommand):
    help = 'Set up project collections (categories) for better organization'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force', 
            action='store_true',
            help='Force recreation of collections even if they already exist'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up project collections...'))
        
        # Get or create root collection
        root_collection = Collection.get_first_root_node()
        
        # Define project categories
        categories = [
            {
                'name': 'Boligprojekter',
                'description': 'Projekter relateret til private boliger og hjem',
                'children': [
                    'Køkkener',
                    'Badeværelser', 
                    'Stuer og opholdszoner',
                    'Soveværelser',
                    'Entréer og gange',
                    'Udendørs terrasser',
                    'Haver og udeområder'
                ]
            },
            {
                'name': 'Erhvervsprojekter',
                'description': 'Kommercielle og erhvervsmæssige projekter',
                'children': [
                    'Kontorer',
                    'Butikker og retail',
                    'Restauranter og caféer',
                    'Hoteller',
                    'Lægegrupper og klinikker',
                    'Uddannelsesinstitutioner'
                ]
            },
            {
                'name': 'Renoveringsprojekter',
                'description': 'Større renoveringer og ombygninger',
                'children': [
                    'Totalrenoveringer',
                    'Tilbygninger',
                    'Loft- og kælderudbyggning',
                    'Facade og ydermure',
                    'Tag og tagkonstruktioner',
                    'Vinduer og døre'
                ]
            },
            {
                'name': 'Specialprojekter',
                'description': 'Særlige og unikke projekter',
                'children': [
                    'Historiske bygninger',
                    'Bæredygtige løsninger',
                    'Smart home integration',
                    'Specialsnedkeri',
                    'Kunstneriske installationer',
                    'Prototype og eksperimentel'
                ]
            },
            {
                'name': 'Maintenance og Service',
                'description': 'Vedligeholdelse og serviceopgaver',
                'children': [
                    'Almindelig vedligeholdelse',
                    'Akut reparationer',
                    'Sæsonopgaver',
                    'Garantiarbejde',
                    'Servicekontrakter'
                ]
            }
        ]
        
        created_count = 0
        updated_count = 0
        
        for category_data in categories:
            category_name = category_data['name']
            
            # Check if main category exists
            existing_category = Collection.objects.filter(
                name=category_name,
                depth=2  # Direct child of root
            ).first()
            
            if existing_category and not options['force']:
                self.stdout.write(f'Category "{category_name}" already exists, skipping...')
                category = existing_category
            else:
                if existing_category:
                    self.stdout.write(f'Updating existing category "{category_name}"...')
                    category = existing_category
                    updated_count += 1
                else:
                    self.stdout.write(f'Creating category "{category_name}"...')
                    category = root_collection.add_child(name=category_name)
                    created_count += 1
            
            # Create subcategories
            subcategory_names = category_data.get('children', [])
            for subcategory_name in subcategory_names:
                existing_subcategory = Collection.objects.filter(
                    name=subcategory_name,
                    depth=3,  # Child of category
                    path__startswith=category.path
                ).first()
                
                if existing_subcategory and not options['force']:
                    continue
                elif existing_subcategory:
                    self.stdout.write(f'  - Updating subcategory "{subcategory_name}"')
                    updated_count += 1
                else:
                    self.stdout.write(f'  - Creating subcategory "{subcategory_name}"')
                    category.add_child(name=subcategory_name)
                    created_count += 1
        
        # Create a special collection for archived/legacy projects
        archived_collection = Collection.objects.filter(
            name='Arkiverede Projekter',
            depth=2
        ).first()
        
        if not archived_collection:
            self.stdout.write('Creating "Arkiverede Projekter" collection...')
            root_collection.add_child(name='Arkiverede Projekter')
            created_count += 1
        
        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\nProject collections setup complete!\n'
                f'Created: {created_count} collections\n'
                f'Updated: {updated_count} collections'
            )
        )
        
        # Display collection hierarchy
        self.display_collection_hierarchy()
        
        # Provide migration guidance
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.WARNING('NEXT STEPS:'))
        self.stdout.write('1. Run migrations to apply model changes')
        self.stdout.write('2. Consider migrating existing projects to appropriate collections')
        self.stdout.write('3. Set up workflows for different collection types')
        self.stdout.write('4. Configure permissions for collection access')
        self.stdout.write('='*50 + '\n')

    def display_collection_hierarchy(self):
        """Display the collection hierarchy"""
        self.stdout.write('\n' + self.style.SUCCESS('Collection Hierarchy:'))
        root = Collection.get_first_root_node()
        
        def print_collection(collection, indent=0):
            prefix = '  ' * indent
            if indent == 0:
                self.stdout.write(f'{prefix}📁 {collection.name} (Root)')
            else:
                icon = '📂' if collection.get_children().exists() else '📄'
                self.stdout.write(f'{prefix}{icon} {collection.name}')
            
            for child in collection.get_children():
                print_collection(child, indent + 1)
        
        print_collection(root)