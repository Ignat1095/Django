from random import choices, randint

from django.core.management.base import BaseCommand
from homeworks_app3.models import Order, OrderItem, Product


class Command(BaseCommand):
    help = 'Creates new order'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new orders')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for i in Order.objects.all():
            for _ in range(count):
                orderitem = OrderItem(
                    order=i,
                    product=Product.objects.get(id=randint(1,10)),
                    quantity=randint(1, 20)
                )
                orderitem.save()
