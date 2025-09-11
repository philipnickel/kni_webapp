from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from wagtail.models import Task, Workflow

User = get_user_model()


class Command(BaseCommand):
    help = 'Set up project workflows for content approval'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force', 
            action='store_true',
            help='Force recreation of workflows even if they already exist'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up project workflows...'))
        
        # Import our custom tasks
        from apps.projects.workflow import ProjectApprovalTask, QualityControlTask, BudgetApprovalTask
        
        # Create workflows
        workflows_created = 0
        
        # 1. Basic Project Approval Workflow
        basic_workflow, created = Workflow.objects.get_or_create(
            name='Basic Project Approval',
            defaults={
                'active': True,
            }
        )
        
        if created or options['force']:
            self.stdout.write('Creating Basic Project Approval workflow...')
            
            # Clear existing tasks if forcing
            if options['force']:
                basic_workflow.workflow_tasks.all().delete()
            
            # Create approval task
            approval_task, task_created = ProjectApprovalTask.objects.get_or_create(
                name='Project Review and Approval',
                defaults={'active': True}
            )
            
            # Add task to workflow
            basic_workflow.workflow_tasks.create(
                task=approval_task,
                sort_order=0
            )
            
            workflows_created += 1
        
        # 2. Complete Project Workflow (with QC and Budget approval)
        complete_workflow, created = Workflow.objects.get_or_create(
            name='Complete Project Workflow',
            defaults={
                'active': True,
            }
        )
        
        if created or options['force']:
            self.stdout.write('Creating Complete Project Workflow...')
            
            if options['force']:
                complete_workflow.workflow_tasks.all().delete()
            
            # Create tasks
            approval_task, _ = ProjectApprovalTask.objects.get_or_create(
                name='Initial Project Review',
                defaults={'active': True}
            )
            
            budget_task, _ = BudgetApprovalTask.objects.get_or_create(
                name='Budget Approval',
                defaults={
                    'active': True,
                    'budget_threshold': 50000  # Projects over 50k DKK need budget approval
                }
            )
            
            qa_task, _ = QualityControlTask.objects.get_or_create(
                name='Quality Control Review',
                defaults={'active': True}
            )
            
            final_approval_task, _ = ProjectApprovalTask.objects.get_or_create(
                name='Final Project Approval',
                defaults={'active': True}
            )
            
            # Add tasks to workflow in order
            workflow_tasks = [
                (approval_task, 0),
                (budget_task, 1),
                (qa_task, 2),
                (final_approval_task, 3)
            ]
            
            for task, order in workflow_tasks:
                complete_workflow.workflow_tasks.create(
                    task=task,
                    sort_order=order
                )
            
            workflows_created += 1
        
        # 3. Quick Approval Workflow (for small projects)
        quick_workflow, created = Workflow.objects.get_or_create(
            name='Quick Approval Workflow',
            defaults={
                'active': True,
            }
        )
        
        if created or options['force']:
            self.stdout.write('Creating Quick Approval Workflow...')
            
            if options['force']:
                quick_workflow.workflow_tasks.all().delete()
            
            # Single approval task
            quick_approval_task, _ = ProjectApprovalTask.objects.get_or_create(
                name='Quick Project Approval',
                defaults={'active': True}
            )
            
            quick_workflow.workflow_tasks.create(
                task=quick_approval_task,
                sort_order=0
            )
            
            workflows_created += 1
        
        # 4. Budget-Only Workflow (for budget changes)
        budget_workflow, created = Workflow.objects.get_or_create(
            name='Budget Approval Only',
            defaults={
                'active': True,
            }
        )
        
        if created or options['force']:
            self.stdout.write('Creating Budget Approval Only workflow...')
            
            if options['force']:
                budget_workflow.workflow_tasks.all().delete()
            
            budget_only_task, _ = BudgetApprovalTask.objects.get_or_create(
                name='Budget Change Approval',
                defaults={
                    'active': True,
                    'budget_threshold': 10000  # Lower threshold for budget-only changes
                }
            )
            
            budget_workflow.workflow_tasks.create(
                task=budget_only_task,
                sort_order=0
            )
            
            workflows_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Workflows setup complete! Created/updated {workflows_created} workflows.'
            )
        )
        
        # Display workflow summary
        self.display_workflow_summary()
        
        # Setup user groups and permissions
        self.setup_user_groups()
        
        # Provide guidance
        self.provide_setup_guidance()

    def display_workflow_summary(self):
        """Display summary of all workflows"""
        self.stdout.write('\n' + self.style.SUCCESS('Workflow Summary:'))
        
        workflows = Workflow.objects.all().order_by('name')
        for workflow in workflows:
            self.stdout.write(f'\n📋 {workflow.name}')
            self.stdout.write(f'   Status: {"Active" if workflow.active else "Inactive"}')
            
            workflow_tasks = workflow.workflow_tasks.all().order_by('sort_order')
            if workflow_tasks:
                self.stdout.write('   Tasks:')
                for wt in workflow_tasks:
                    task_type = wt.task.__class__.__name__
                    self.stdout.write(f'     {wt.sort_order + 1}. {wt.task.name} ({task_type})')
            else:
                self.stdout.write('   No tasks configured')

    def setup_user_groups(self):
        """Set up user groups for workflow permissions"""
        self.stdout.write('\n' + self.style.SUCCESS('Setting up user groups...'))
        
        groups_data = [
            {
                'name': 'Project Managers',
                'permissions': [
                    'projects.can_approve_projects',
                    'projects.change_projectpage',
                    'projects.can_bulk_edit_projects'
                ]
            },
            {
                'name': 'Quality Control',
                'permissions': [
                    'projects.change_projectpage',
                    'projects.can_set_project_priority'
                ]
            },
            {
                'name': 'Budget Managers',
                'permissions': [
                    'projects.can_manage_project_budget',
                    'projects.change_projectpage'
                ]
            },
            {
                'name': 'Project Contributors',
                'permissions': [
                    'projects.add_projectpage',
                    'projects.change_projectpage'
                ]
            }
        ]
        
        for group_data in groups_data:
            group, created = Group.objects.get_or_create(
                name=group_data['name']
            )
            
            if created:
                self.stdout.write(f'  ✓ Created group: {group.name}')
            else:
                self.stdout.write(f'  - Group already exists: {group.name}')

    def provide_setup_guidance(self):
        """Provide next steps guidance"""
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.WARNING('WORKFLOW SETUP COMPLETE'))
        self.stdout.write('='*60)
        
        self.stdout.write('\n📋 Available Workflows:')
        self.stdout.write('   • Basic Project Approval - For standard projects')
        self.stdout.write('   • Complete Project Workflow - For complex projects with full review')
        self.stdout.write('   • Quick Approval Workflow - For small, simple projects')
        self.stdout.write('   • Budget Approval Only - For budget change approvals')
        
        self.stdout.write('\n👥 User Groups Created:')
        self.stdout.write('   • Project Managers - Can approve projects and manage workflows')
        self.stdout.write('   • Quality Control - Can review project quality and set priorities')
        self.stdout.write('   • Budget Managers - Can approve budgets and financial changes')
        self.stdout.write('   • Project Contributors - Can create and edit their own projects')
        
        self.stdout.write('\n⚡ Next Steps:')
        self.stdout.write('   1. Assign users to appropriate groups in Django Admin')
        self.stdout.write('   2. Configure workflow assignments to specific collections/page types')
        self.stdout.write('   3. Test workflows with sample projects')
        self.stdout.write('   4. Configure email notifications for workflow events')
        self.stdout.write('   5. Set up scheduled content publishing if needed')
        
        self.stdout.write('\n🔧 Admin URLs:')
        self.stdout.write('   • Workflows: /admin/workflows/')
        self.stdout.write('   • User Groups: /admin/auth/group/')
        self.stdout.write('   • Collections: /admin/collections/')
        
        self.stdout.write('\n' + '='*60 + '\n')