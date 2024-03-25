from django.core.management.base import BaseCommand
from homeworks_app3.models import Client


class Command(BaseCommand):
    help = 'Creates new client'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new clients')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for i in range(1, count):
            client = Client(
                name=f'Name{i}',
                username =f'Username{i}',
                email=f'email{i}@mail.ru',
                phone_number=f'{i:08}',
                address=f'Address... Home{i}'
            )
            self.stdout.write(f'Create {client}')
            client.save()
