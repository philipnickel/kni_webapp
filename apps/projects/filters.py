import django_filters
from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q
from wagtail.models import Collection
from .models import ProjectPage
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ProjectPageFilterSet(django_filters.FilterSet):
    """Advanced filtering for ProjectPage admin list view"""
    
    # Search filter
    search = django_filters.CharFilter(
        method='filter_search',
        widget=forms.TextInput(attrs={
            'placeholder': 'Søg i titel, beskrivelse, kunde...',
            'class': 'form-control'
        }),
        label="Søg"
    )
    
    # Collection filter
    collection = django_filters.ModelChoiceFilter(
        queryset=Collection.objects.all(),
        empty_label="Alle kategorier",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Kategori"
    )
    
    # Status filter
    project_status = django_filters.ChoiceFilter(
        choices=[
            ('', 'Alle statusser'),
            ('planning', 'Planlægning'),
            ('in_progress', 'I gang'),
            ('completed', 'Færdig'),
            ('on_hold', 'På pause'),
            ('cancelled', 'Annulleret')
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Status"
    )
    
    # Priority filter
    priority = django_filters.ChoiceFilter(
        choices=[
            ('', 'Alle prioriteter'),
            ('low', 'Lav'),
            ('medium', 'Medium'),
            ('high', 'Høj'),
            ('urgent', 'Akut')
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Prioritet"
    )
    
    # Featured filter
    featured = django_filters.BooleanFilter(
        widget=forms.Select(
            choices=[
                ('', 'Alle projekter'),
                (True, 'Kun featured'),
                (False, 'Ikke featured')
            ],
            attrs={'class': 'form-control'}
        ),
        label="Featured"
    )
    
    # Owner filter
    owner = django_filters.ModelChoiceFilter(
        queryset=User.objects.filter(is_active=True).order_by('first_name', 'last_name'),
        empty_label="Alle ejere",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Ejer"
    )
    
    # Date range filters
    project_date_from = django_filters.DateFilter(
        field_name='project_date',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="Projekt dato fra"
    )
    
    project_date_to = django_filters.DateFilter(
        field_name='project_date',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="Projekt dato til"
    )
    
    # Budget range filters
    budget_min = django_filters.NumberFilter(
        field_name='estimated_budget',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min budget',
            'step': '1000'
        }),
        label="Min budget (DKK)"
    )
    
    budget_max = django_filters.NumberFilter(
        field_name='estimated_budget',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Max budget',
            'step': '1000'
        }),
        label="Max budget (DKK)"
    )
    
    # Workflow status filter
    has_workflow = django_filters.BooleanFilter(
        method='filter_workflow_status',
        widget=forms.Select(
            choices=[
                ('', 'Alle'),
                (True, 'I workflow'),
                (False, 'Ikke i workflow')
            ],
            attrs={'class': 'form-control'}
        ),
        label="Workflow status"
    )
    
    # Live/Draft status
    live_status = django_filters.ChoiceFilter(
        method='filter_live_status',
        choices=[
            ('', 'Alle'),
            ('live', 'Kun live'),
            ('draft', 'Kun draft'),
            ('both', 'Live + draft ændringer')
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Publikations status"
    )
    
    # Location filter
    location = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Søg lokation...',
            'class': 'form-control'
        }),
        label="Lokation"
    )
    
    # Has images filter
    has_images = django_filters.BooleanFilter(
        method='filter_has_images',
        widget=forms.Select(
            choices=[
                ('', 'Alle'),
                (True, 'Med billeder'),
                (False, 'Uden billeder')
            ],
            attrs={'class': 'form-control'}
        ),
        label="Billeder"
    )
    
    class Meta:
        model = ProjectPage
        fields = []
    
    def filter_search(self, queryset, name, value):
        """Multi-field search"""
        if not value:
            return queryset
            
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(client_name__icontains=value) |
            Q(materials__icontains=value) |
            Q(location__icontains=value) |
            Q(tags__name__icontains=value)
        ).distinct()
    
    def filter_workflow_status(self, queryset, name, value):
        """Filter by workflow status"""
        if value is None:
            return queryset
            
        if value:
            # Projects currently in workflow
            return queryset.filter(workflow_states__status='in_progress').distinct()
        else:
            # Projects not in workflow
            return queryset.exclude(workflow_states__status='in_progress').distinct()
    
    def filter_live_status(self, queryset, name, value):
        """Filter by live/draft status"""
        if not value:
            return queryset
            
        if value == 'live':
            return queryset.filter(live=True)
        elif value == 'draft':
            return queryset.filter(live=False)
        elif value == 'both':
            return queryset.filter(live=True, has_unpublished_changes=True)
            
        return queryset
    
    def filter_has_images(self, queryset, name, value):
        """Filter by whether project has images"""
        if value is None:
            return queryset
            
        if value:
            return queryset.filter(project_images__isnull=False).distinct()
        else:
            return queryset.filter(project_images__isnull=True)


class ProjectPageAdvancedFilter:
    """Advanced filter options for project pages"""
    
    @staticmethod
    def get_filter_choices():
        """Get dynamic filter choices based on current data"""
        
        # Get unique locations
        locations = ProjectPage.objects.live().values_list('location', flat=True).distinct()
        location_choices = [('', 'Alle lokationer')] + [
            (loc, loc) for loc in locations if loc
        ]
        
        # Get unique materials  
        materials = set()
        for material_list in ProjectPage.objects.live().values_list('materials', flat=True):
            if material_list:
                # Split on common separators
                for sep in [',', ';', '\n']:
                    materials.update([m.strip() for m in material_list.split(sep) if m.strip()])
        
        material_choices = [('', 'Alle materialer')] + sorted([
            (mat, mat) for mat in materials
        ])
        
        # Get collections with project counts
        collection_counts = Collection.objects.annotate(
            project_count=models.Count('projectpage')
        ).filter(project_count__gt=0)
        
        return {
            'locations': location_choices,
            'materials': material_choices[:20],  # Limit to top 20
            'collections': collection_counts
        }
    
    @staticmethod
    def get_saved_filters(user):
        """Get user's saved filter presets"""
        # This would be implemented with a SavedFilter model
        return []
    
    @staticmethod
    def get_quick_filters():
        """Get predefined quick filter options"""
        return [
            {
                'name': 'Aktive projekter',
                'filters': {'project_status__in': ['planning', 'in_progress']},
                'icon': 'play',
                'color': 'success'
            },
            {
                'name': 'Featured projekter',
                'filters': {'featured': True},
                'icon': 'pick',
                'color': 'warning'
            },
            {
                'name': 'Høj prioritet',
                'filters': {'priority__in': ['high', 'urgent']},
                'icon': 'warning',
                'color': 'critical'
            },
            {
                'name': 'I workflow',
                'filters': {'workflow_states__status': 'in_progress'},
                'icon': 'list-ul',
                'color': 'info'
            },
            {
                'name': 'Store budgetter',
                'filters': {'estimated_budget__gte': 100000},
                'icon': 'success',
                'color': 'primary'
            }
        ]


# Custom filter form for better UX
class ProjectFilterForm(forms.Form):
    """Custom form for project filtering with enhanced UI"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add CSS classes to all fields
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
    
    def get_filter_groups(self):
        """Group filters for better organization in UI"""
        return {
            'basic': ['search', 'collection', 'project_status', 'priority'],
            'dates': ['project_date_from', 'project_date_to'],
            'budget': ['budget_min', 'budget_max'],
            'advanced': ['owner', 'featured', 'has_workflow', 'live_status'],
            'content': ['location', 'has_images']
        }