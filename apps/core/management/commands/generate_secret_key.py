from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import os


class Command(BaseCommand):
    help = 'Generate a secure Django secret key'

    def add_arguments(self, parser):
        parser.add_argument(
            '--print-only',
            action='store_true',
            help='Only print the key without setting environment variable',
        )
        parser.add_argument(
            '--env-file',
            type=str,
            help='Write the key to a .env file',
        )

    def handle(self, *args, **options):
        secret_key = get_random_secret_key()

        if options['print_only']:
            self.stdout.write(secret_key)
        elif options['env_file']:
            env_file_path = options['env_file']
            try:
                # Read existing content
                content = []
                if os.path.exists(env_file_path):
                    with open(env_file_path, 'r') as f:
                        content = f.readlines()

                # Remove existing DJANGO_SECRET_KEY lines
                content = [line for line in content if not line.startswith('DJANGO_SECRET_KEY=')]

                # Add new secret key
                content.append(f'DJANGO_SECRET_KEY={secret_key}\n')

                # Write back to file
                with open(env_file_path, 'w') as f:
                    f.writelines(content)

                self.stdout.write(
                    self.style.SUCCESS(f'Secret key written to {env_file_path}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to write to {env_file_path}: {e}')
                )
        else:
            # Set environment variable for current process
            os.environ['DJANGO_SECRET_KEY'] = secret_key
            self.stdout.write(
                self.style.SUCCESS(f'Generated and set DJANGO_SECRET_KEY: {secret_key[:10]}...')
            )