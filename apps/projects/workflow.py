from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wagtail.models import Task

User = get_user_model()


class ProjectApprovalTask(Task):
    """Custom task for project approval workflow"""
    
    class Meta:
        verbose_name = "Projekt godkendelse"
        verbose_name_plural = "Projekt godkendelser"
    
    def start(self, workflow_state, user=None):
        """Start the task and assign to specific users or groups"""
        task_state = workflow_state.current_task_state
        if task_state.task == self:
            # Send notification to approvers
            self.send_approval_notification(workflow_state, user)
        return super().start(workflow_state, user)
    
    def user_can_access_editor(self, obj, user):
        """Allow specific users to access editor during approval"""
        # Allow superusers and staff to always access
        if user.is_superuser or user.is_staff:
            return True
        
        # Allow the creator to access if they have edit permissions
        if hasattr(obj, 'owner') and obj.owner == user:
            return user.has_perm('wagtailadmin.access_admin')
            
        return False
    
    def user_can_lock(self, obj, user):
        """Control who can lock during approval process"""
        return user.is_staff or user.is_superuser
    
    def user_can_unlock(self, obj, user):
        """Control who can unlock during approval process"""
        return user.is_staff or user.is_superuser
    
    def get_actions(self, obj, user):
        """Define available actions for this task"""
        actions = []
        
        # Only approvers (staff/superuser) can approve or reject
        if user.is_staff or user.is_superuser:
            actions.extend([
                ('approve', 'Godkend projekt', False),
                ('reject', 'Afvis projekt', True),  # True means requires comment
                ('request_changes', 'Anmod om ændringer', True),
            ])
        
        # Anyone with access can cancel their own submission
        if hasattr(obj, 'owner') and obj.owner == user:
            actions.append(('cancel', 'Annuller ansøgning', False))
            
        return actions
    
    def on_action(self, task_state, user, action_name, **kwargs):
        """Handle task actions"""
        workflow_state = task_state.workflow_state
        
        if action_name == 'approve':
            return task_state.approve(user=user)
            
        elif action_name == 'reject':
            comment = kwargs.get('comment', '')
            return task_state.reject(user=user, comment=comment)
            
        elif action_name == 'request_changes':
            comment = kwargs.get('comment', '')
            # Mark as rejected but with a different status message
            task_state.status = 'rejected'
            task_state.finished_at = timezone.now()
            task_state.finished_by = user
            task_state.comment = comment or 'Ændringer anmodet'
            task_state.save()
            
            # Send notification about requested changes
            self.send_changes_requested_notification(workflow_state, user, comment)
            
            return task_state
            
        elif action_name == 'cancel':
            return workflow_state.cancel(user=user)
            
        return super().on_action(task_state, user, action_name, **kwargs)
    
    def send_approval_notification(self, workflow_state, user):
        """Send notification to approvers when project needs approval"""
        from django.core.mail import send_mail
        from django.conf import settings
        
        project = workflow_state.content_object
        
        # Get all staff users for approval notifications
        approvers = User.objects.filter(is_staff=True, is_active=True)
        
        subject = f"Projekt kræver godkendelse: {project.title}"
        message = f"""
        Projekt "{project.title}" er blevet sendt til godkendelse.
        
        Indsendt af: {user.get_full_name() if user else 'Ukendt'}
        
        Log ind på admin panelet for at gennemse og godkende projektet.
        """
        
        recipient_emails = [u.email for u in approvers if u.email]
        
        if recipient_emails:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_emails,
                fail_silently=True,
            )
    
    def send_changes_requested_notification(self, workflow_state, approver, comment):
        """Send notification when changes are requested"""
        from django.core.mail import send_mail
        from django.conf import settings
        
        project = workflow_state.content_object
        
        if hasattr(project, 'owner') and project.owner and project.owner.email:
            subject = f"Ændringer anmodet: {project.title}"
            message = f"""
            Der er anmodet om ændringer til dit projekt "{project.title}".
            
            Kommentar fra {approver.get_full_name()}:
            {comment}
            
            Log ind på admin panelet for at foretage de nødvendige ændringer.
            """
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [project.owner.email],
                fail_silently=True,
            )


class QualityControlTask(Task):
    """Task for quality control review"""
    
    class Meta:
        verbose_name = "Kvalitetskontrol"
        verbose_name_plural = "Kvalitetskontrol"
    
    def user_can_access_editor(self, obj, user):
        """Only QA staff can access during quality control"""
        return user.is_staff and (
            user.groups.filter(name='Quality Control').exists() or 
            user.is_superuser
        )
    
    def get_actions(self, obj, user):
        """Actions available for quality control"""
        if self.user_can_access_editor(obj, user):
            return [
                ('approve', 'Godkend kvalitet', False),
                ('reject', 'Afvis - kvalitetsproblemer', True),
                ('return_for_revision', 'Returner til revision', True),
            ]
        return []
    
    def on_action(self, task_state, user, action_name, **kwargs):
        """Handle QA actions"""
        if action_name == 'approve':
            return task_state.approve(user=user)
            
        elif action_name == 'reject':
            comment = kwargs.get('comment', 'Kvalitetsproblemer identificeret')
            return task_state.reject(user=user, comment=comment)
            
        elif action_name == 'return_for_revision':
            comment = kwargs.get('comment', 'Kræver revision')
            # Mark as rejected for revision
            task_state.status = 'rejected'
            task_state.finished_at = timezone.now()
            task_state.finished_by = user
            task_state.comment = comment
            task_state.save()
            return task_state
            
        return super().on_action(task_state, user, action_name, **kwargs)


class BudgetApprovalTask(Task):
    """Task specifically for budget approval on projects"""
    
    budget_threshold = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=50000,
        verbose_name="Budget grænse",
        help_text="Projekter over denne grænse kræver godkendelse"
    )
    
    class Meta:
        verbose_name = "Budget godkendelse"
        verbose_name_plural = "Budget godkendelser"
    
    def start(self, workflow_state, user=None):
        """Check if budget approval is needed"""
        project = workflow_state.content_object
        
        # Skip if no budget or under threshold
        if (not hasattr(project, 'estimated_budget') or 
            not project.estimated_budget or 
            project.estimated_budget <= self.budget_threshold):
            
            # Auto-approve if under threshold
            task_state = workflow_state.current_task_state
            if task_state.task == self:
                return task_state.approve(user=user, comment="Auto-godkendt (under budget grænse)")
        
        return super().start(workflow_state, user)
    
    def user_can_access_editor(self, obj, user):
        """Only budget managers can approve budgets"""
        return (
            user.groups.filter(name='Budget Managers').exists() or 
            user.is_superuser or
            user.has_perm('projects.can_manage_project_budget')
        )
    
    def get_actions(self, obj, user):
        """Budget approval actions"""
        if self.user_can_access_editor(obj, user):
            return [
                ('approve', 'Godkend budget', False),
                ('reject', 'Afvis budget', True),
                ('request_budget_revision', 'Anmod om budget revision', True),
            ]
        return []
    
    def on_action(self, task_state, user, action_name, **kwargs):
        """Handle budget approval actions"""
        if action_name == 'approve':
            return task_state.approve(
                user=user, 
                comment=f"Budget godkendt af {user.get_full_name()}"
            )
            
        elif action_name == 'reject':
            comment = kwargs.get('comment', 'Budget afvist')
            return task_state.reject(user=user, comment=comment)
            
        elif action_name == 'request_budget_revision':
            comment = kwargs.get('comment', 'Budget revision anmodet')
            task_state.status = 'rejected'
            task_state.finished_at = timezone.now()
            task_state.finished_by = user
            task_state.comment = comment
            task_state.save()
            return task_state
            
        return super().on_action(task_state, user, action_name, **kwargs)


# Custom task forms for better UX
from django import forms


class ProjectApprovalTaskForm(forms.ModelForm):
    """Custom form for project approval task configuration"""
    
    class Meta:
        model = ProjectApprovalTask
        fields = ['name', 'active']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].help_text = "Navn på godkendelsestrinnet"


class QualityControlTaskForm(forms.ModelForm):
    """Custom form for quality control task"""
    
    class Meta:
        model = QualityControlTask
        fields = ['name', 'active']


class BudgetApprovalTaskForm(forms.ModelForm):
    """Custom form for budget approval task"""
    
    class Meta:
        model = BudgetApprovalTask
        fields = ['name', 'active', 'budget_threshold']
        widgets = {
            'budget_threshold': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0',
                'class': 'form-control'
            })
        }