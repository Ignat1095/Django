from django.core.management.base import BaseCommand
# from myapp.models import User
from myapp.models import User


class Command(BaseCommand):
    help = 'Создание фейковых клиентов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Кол-во продуктов для гене/')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = User(name=f'Name_client{i}',
                          email=f'mail{i}@mail.ru',
                          password=f'{555000 + i}',
                          age=f'{i}')
            client.save()
