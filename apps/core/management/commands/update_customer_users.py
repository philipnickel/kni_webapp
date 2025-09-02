from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    help = 'Update customer users to use the new Customer Editors group'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Updating customer users...'))
        
        # Get groups
        try:
            customer_group = Group.objects.get(name='Customer Editors')
            old_editors_group = Group.objects.get(name='Editors')
        except Group.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'Group not found: {e}'))
            return
        
        # Update jcleemann user
        try:
            user = User.objects.get(username='jcleemann')
            
            # Remove from old group
            user.groups.remove(old_editors_group)
            
            # Add to new group
            user.groups.add(customer_group)
            
            # Ensure they have staff access to use admin
            user.is_staff = True
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Updated {user.username}: is_staff={user.is_staff}, '
                    f'groups={list(user.groups.values_list("name", flat=True))}'
                )
            )
            
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING('jcleemann user not found'))
        
        # Show all users status
        self.stdout.write('\n' + '='*60)
        self.stdout.write('ALL USERS STATUS:')
        for user in User.objects.all():
            groups = list(user.groups.values_list('name', flat=True))
            self.stdout.write(
                f'{user.username}: superuser={user.is_superuser}, '
                f'staff={user.is_staff}, groups={groups}'
            )
        self.stdout.write('='*60)