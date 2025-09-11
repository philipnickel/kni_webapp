from django.utils.translation import gettext as _
from django.contrib import messages
from django.db import transaction
from wagtail.admin.views.pages.bulk_actions.page_bulk_action import PageBulkAction
from wagtail.admin.forms.collections import CollectionChoiceField
from wagtail import hooks
from wagtail.models import Collection
from django import forms


class ProjectBulkStatusChangeForm(forms.Form):
    """Form for bulk status changes"""
    status = forms.ChoiceField(
        choices=[
            ('planning', 'Planlægning'),
            ('in_progress', 'I gang'),
            ('completed', 'Færdig'),
            ('on_hold', 'På pause'),
            ('cancelled', 'Annulleret')
        ],
        label="Ny status",
        help_text="Vælg den nye status for alle valgte projekter"
    )


class ProjectBulkPriorityChangeForm(forms.Form):
    """Form for bulk priority changes"""
    priority = forms.ChoiceField(
        choices=[
            ('low', 'Lav'),
            ('medium', 'Medium'),
            ('high', 'Høj'),
            ('urgent', 'Akut')
        ],
        label="Ny prioritet",
        help_text="Vælg den nye prioritet for alle valgte projekter"
    )


class ProjectBulkCollectionChangeForm(forms.Form):
    """Form for bulk collection changes"""
    collection = CollectionChoiceField(
        label="Ny kategori",
        help_text="Vælg den nye kategori for alle valgte projekter"
    )


@hooks.register('register_bulk_action')
class ProjectBulkStatusChangeAction(PageBulkAction):
    display_name = _("Ændre status")
    aria_label = _("Ændre status for valgte projekter")
    action_type = "change_status"
    template_name = "projects/bulk_actions/confirm_bulk_status_change.html"
    models = ['projects.ProjectPage']
    
    def get_form_class(self):
        return ProjectBulkStatusChangeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_display'] = dict([
            ('planning', 'Planlægning'),
            ('in_progress', 'I gang'),
            ('completed', 'Færdig'),
            ('on_hold', 'På pause'),
            ('cancelled', 'Annulleret')
        ])
        return context
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        new_status = kwargs.get('status')
        if not new_status:
            return 0, 0
            
        num_updated = 0
        
        with transaction.atomic():
            for project in objects:
                if hasattr(project, 'project_status'):
                    project.project_status = new_status
                    project.save(update_fields=['project_status'])
                    num_updated += 1
        
        return num_updated, 0
    
    def get_success_message(self, num_parent_objects, num_child_objects):
        status_display = {
            'planning': 'Planlægning',
            'in_progress': 'I gang',
            'completed': 'Færdig',
            'on_hold': 'På pause',
            'cancelled': 'Annulleret'
        }
        new_status = self.cleaned_form.cleaned_data.get('status')
        status_name = status_display.get(new_status, new_status)
        return _(f"{num_parent_objects} projekter blev ændret til status: {status_name}")


@hooks.register('register_bulk_action')
class ProjectBulkPriorityChangeAction(PageBulkAction):
    display_name = _("Ændre prioritet")
    aria_label = _("Ændre prioritet for valgte projekter")
    action_type = "change_priority"
    template_name = "projects/bulk_actions/confirm_bulk_priority_change.html"
    models = ['projects.ProjectPage']
    
    def get_form_class(self):
        return ProjectBulkPriorityChangeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['priority_display'] = dict([
            ('low', 'Lav'),
            ('medium', 'Medium'),
            ('high', 'Høj'),
            ('urgent', 'Akut')
        ])
        return context
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        new_priority = kwargs.get('priority')
        if not new_priority:
            return 0, 0
            
        num_updated = 0
        
        with transaction.atomic():
            for project in objects:
                if hasattr(project, 'priority'):
                    project.priority = new_priority
                    project.save(update_fields=['priority'])
                    num_updated += 1
        
        return num_updated, 0
    
    def get_success_message(self, num_parent_objects, num_child_objects):
        priority_display = {
            'low': 'Lav',
            'medium': 'Medium',
            'high': 'Høj',
            'urgent': 'Akut'
        }
        new_priority = self.cleaned_form.cleaned_data.get('priority')
        priority_name = priority_display.get(new_priority, new_priority)
        return _(f"{num_parent_objects} projekter fik ændret prioritet til: {priority_name}")


@hooks.register('register_bulk_action')
class ProjectBulkCollectionChangeAction(PageBulkAction):
    display_name = _("Ændre kategori")
    aria_label = _("Ændre kategori for valgte projekter")
    action_type = "change_collection"
    template_name = "projects/bulk_actions/confirm_bulk_collection_change.html"
    models = ['projects.ProjectPage']
    
    def get_form_class(self):
        return ProjectBulkCollectionChangeForm
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        new_collection_id = kwargs.get('collection')
        if not new_collection_id:
            return 0, 0
            
        try:
            new_collection = Collection.objects.get(id=new_collection_id)
        except Collection.DoesNotExist:
            return 0, 0
            
        num_updated = 0
        
        with transaction.atomic():
            for project in objects:
                if hasattr(project, 'collection'):
                    project.collection = new_collection
                    project.save(update_fields=['collection'])
                    num_updated += 1
        
        return num_updated, 0
    
    def get_success_message(self, num_parent_objects, num_child_objects):
        collection_id = self.cleaned_form.cleaned_data.get('collection')
        try:
            collection = Collection.objects.get(id=collection_id)
            collection_name = collection.name
        except Collection.DoesNotExist:
            collection_name = "ny kategori"
        return _(f"{num_parent_objects} projekter blev flyttet til kategori: {collection_name}")


@hooks.register('register_bulk_action')
class ProjectBulkFeaturedToggleAction(PageBulkAction):
    display_name = _("Toggle featured status")
    aria_label = _("Toggle featured status for selected projects")
    action_type = "toggle_featured"
    template_name = "projects/bulk_actions/confirm_bulk_featured_toggle.html"
    models = ['projects.ProjectPage']
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        num_updated = 0
        
        with transaction.atomic():
            for project in objects:
                if hasattr(project, 'featured'):
                    project.featured = not project.featured
                    project.save(update_fields=['featured'])
                    num_updated += 1
        
        return num_updated, 0
    
    def get_success_message(self, num_parent_objects, num_child_objects):
        return _(f"Featured status blev ændret for {num_parent_objects} projekter")