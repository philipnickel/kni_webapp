from django.db.models import Count, Q, Sum, Avg
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from wagtail.models import Collection
from .models import ProjectPage
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils import timezone

User = get_user_model()


class ProjectAnalyticsDashboard:
    """Analytics class for project dashboard widgets"""
    
    def get_project_status_counts(self):
        """Get count of projects by status"""
        return ProjectPage.objects.live().values('project_status').annotate(
            count=Count('id')
        ).order_by('project_status')
    
    def get_priority_counts(self):
        """Get count of projects by priority"""
        return ProjectPage.objects.live().values('priority').annotate(
            count=Count('id')
        ).order_by('priority')
    
    def get_collection_counts(self):
        """Get count of projects by collection"""
        return ProjectPage.objects.live().select_related('collection').values(
            'collection__name'
        ).annotate(count=Count('id')).order_by('-count')[:10]
    
    def get_budget_analytics(self):
        """Get budget-related analytics"""
        projects = ProjectPage.objects.live().filter(estimated_budget__isnull=False)
        
        return {
            'total_budget': projects.aggregate(total=Sum('estimated_budget'))['total'] or 0,
            'avg_budget': projects.aggregate(avg=Avg('estimated_budget'))['avg'] or 0,
            'budget_by_status': projects.values('project_status').annotate(
                total_budget=Sum('estimated_budget'),
                count=Count('id')
            ).order_by('project_status')
        }
    
    def get_recent_activity(self, days=30):
        """Get recent project activity"""
        cutoff_date = timezone.now() - timedelta(days=days)
        
        return {
            'new_projects': ProjectPage.objects.filter(
                first_published_at__gte=cutoff_date
            ).count(),
            'updated_projects': ProjectPage.objects.filter(
                last_published_at__gte=cutoff_date
            ).exclude(
                first_published_at__gte=cutoff_date
            ).count(),
            'completed_projects': ProjectPage.objects.filter(
                project_status='completed',
                last_published_at__gte=cutoff_date
            ).count()
        }
    
    def get_workflow_stats(self):
        """Get workflow statistics"""
        from wagtail.models import WorkflowState
        
        workflow_stats = WorkflowState.objects.filter(
            base_content_type__model='projectpage'
        ).values('status').annotate(
            count=Count('id')
        )
        
        # Get projects currently in workflow
        in_workflow = ProjectPage.objects.filter(
            workflow_states__status='in_progress'
        ).distinct().count()
        
        return {
            'workflow_breakdown': workflow_stats,
            'projects_in_workflow': in_workflow,
            'pending_approval': WorkflowState.objects.filter(
                base_content_type__model='projectpage',
                status='in_progress'
            ).count()
        }
    
    def get_user_activity(self):
        """Get user activity statistics"""
        return {
            'active_users': User.objects.filter(
                is_active=True,
                last_login__gte=timezone.now() - timedelta(days=30)
            ).count(),
            'total_users': User.objects.filter(is_active=True).count(),
            'projects_by_owner': ProjectPage.objects.live().values(
                'owner__first_name', 'owner__last_name'
            ).annotate(count=Count('id')).order_by('-count')[:5]
        }


# Dashboard widget classes for Wagtail admin
class ProjectStatusWidget:
    """Widget showing project status distribution"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def render(self):
        """Render the widget HTML"""
        status_counts = self.analytics.get_project_status_counts()
        
        status_display = {
            'planning': 'Planlægning',
            'in_progress': 'I gang',
            'completed': 'Færdig',
            'on_hold': 'På pause',
            'cancelled': 'Annulleret'
        }
        
        # Build chart data
        chart_data = []
        colors = {
            'planning': '#3b82f6',
            'in_progress': '#eab308', 
            'completed': '#22c55e',
            'on_hold': '#6b7280',
            'cancelled': '#ef4444'
        }
        
        for item in status_counts:
            status = item['project_status']
            chart_data.append({
                'label': status_display.get(status, status),
                'value': item['count'],
                'color': colors.get(status, '#6b7280')
            })
        
        return {
            'template': 'projects/admin/widgets/project_status_chart.html',
            'context': {
                'title': 'Projekt Status',
                'chart_data': chart_data,
                'total': sum(item['count'] for item in status_counts)
            }
        }


class ProjectBudgetWidget:
    """Widget showing budget analytics"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def render(self):
        """Render budget widget"""
        budget_data = self.analytics.get_budget_analytics()
        
        return {
            'template': 'projects/admin/widgets/budget_analytics.html',
            'context': {
                'title': 'Budget Oversigt',
                'total_budget': budget_data['total_budget'],
                'avg_budget': budget_data['avg_budget'],
                'budget_by_status': budget_data['budget_by_status']
            }
        }


class RecentActivityWidget:
    """Widget showing recent project activity"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def render(self):
        """Render recent activity widget"""
        activity_data = self.analytics.get_recent_activity()
        
        return {
            'template': 'projects/admin/widgets/recent_activity.html',
            'context': {
                'title': 'Aktivitet (30 dage)',
                'new_projects': activity_data['new_projects'],
                'updated_projects': activity_data['updated_projects'],
                'completed_projects': activity_data['completed_projects']
            }
        }


class WorkflowStatusWidget:
    """Widget showing workflow status"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def render(self):
        """Render workflow status widget"""
        workflow_data = self.analytics.get_workflow_stats()
        
        return {
            'template': 'projects/admin/widgets/workflow_status.html',
            'context': {
                'title': 'Workflow Status',
                'projects_in_workflow': workflow_data['projects_in_workflow'],
                'pending_approval': workflow_data['pending_approval'],
                'workflow_breakdown': workflow_data['workflow_breakdown']
            }
        }


class CollectionDistributionWidget:
    """Widget showing project distribution by collection"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def render(self):
        """Render collection distribution widget"""
        collection_data = self.analytics.get_collection_counts()
        
        return {
            'template': 'projects/admin/widgets/collection_distribution.html',
            'context': {
                'title': 'Projekter per Kategori',
                'collection_data': collection_data,
                'total_collections': Collection.objects.count()
            }
        }


# Dashboard summary widget
class ProjectDashboardSummary:
    """Main dashboard summary showing key metrics"""
    
    def __init__(self):
        self.analytics = ProjectAnalyticsDashboard()
    
    def get_summary_data(self):
        """Get summary data for dashboard"""
        total_projects = ProjectPage.objects.live().count()
        active_projects = ProjectPage.objects.live().filter(
            project_status__in=['planning', 'in_progress']
        ).count()
        completed_projects = ProjectPage.objects.live().filter(
            project_status='completed'
        ).count()
        
        budget_data = self.analytics.get_budget_analytics()
        workflow_data = self.analytics.get_workflow_stats()
        
        return {
            'total_projects': total_projects,
            'active_projects': active_projects,
            'completed_projects': completed_projects,
            'total_budget': budget_data['total_budget'],
            'projects_in_workflow': workflow_data['projects_in_workflow'],
            'completion_rate': (completed_projects / total_projects * 100) if total_projects else 0
        }
    
    def render(self):
        """Render summary widget"""
        summary_data = self.get_summary_data()
        
        return {
            'template': 'projects/admin/widgets/dashboard_summary.html',
            'context': {
                'title': 'Projekt Oversigt',
                **summary_data
            }
        }


# Quick actions widget
class QuickActionsWidget:
    """Widget with quick action buttons"""
    
    def render(self):
        """Render quick actions widget"""
        return {
            'template': 'projects/admin/widgets/quick_actions.html',
            'context': {
                'title': 'Hurtige Handlinger',
                'actions': [
                    {
                        'label': 'Nyt Projekt',
                        'url': reverse('wagtailadmin_pages:add', args=['projects', 'projectpage', 2]),  # Assuming gallery page ID 2
                        'icon': 'plus',
                        'class': 'btn-primary'
                    },
                    {
                        'label': 'Workflow Oversigt',
                        'url': reverse('wagtailadmin_workflows:index'),
                        'icon': 'list-ul',
                        'class': 'btn-secondary'
                    },
                    {
                        'label': 'Kollektioner',
                        'url': reverse('wagtailadmin_collections:index'),
                        'icon': 'folder-open-inverse',
                        'class': 'btn-secondary'
                    },
                    {
                        'label': 'Projekt Rapporter',
                        'url': '#',  # Will be implemented later
                        'icon': 'doc-full-inverse',
                        'class': 'btn-secondary'
                    }
                ]
            }
        }