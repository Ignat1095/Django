from django.core.management.base import BaseCommand
from myapp3.models import Order, Client


class Command(BaseCommand):
    help = 'Creates new order'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new orders')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        clients = Client.objects.all()

        for i in range(1, count):
            client = clients[i]

            order = Order(
                client=client,
            )

            self.stdout.write(f'Create {order}')
            order.save()
