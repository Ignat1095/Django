from random import uniform, randint

from django.core.management.base import BaseCommand
from homeworks_app3.models import Product


class Command(BaseCommand):
    help = 'Creates new product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of new products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for i in range(1, count):
            product = Product(
                name=f'Товар{i}',
                description=f'Product{i} description.....',
                price=uniform(0.99, 99_999.99),
                quantity=randint(1, 10000)
            )
            self.stdout.write(f'Create {product}')
            product.save()