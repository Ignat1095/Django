from datetime import datetime, timedelta
from django.shortcuts import render

from myapp3.models import Order, Product, OrderItem, Client


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Это главная страница сайта',
    }
    return render(request, "myapp3/index.html", context=context)


def view_orders(request, client_id=None):
    if client_id:
        orders = Order.objects.filter(client=client_id)

        context = {
            'title': f'Заказы клиента{client_id}',
            'orders': orders
        }
        return render(request, 'myapp3/get_orders.html', context=context)
    else:
        return render(request, 'myapp3/get_orders.html', {'title': f'Заказы', 'orders': Order.objects.all()})


def view_ordered_goods(request, client_id=None, start_date=None):
    today = datetime.now()
    if start_date == 'week':
        start_date = today - timedelta(weeks=1)
    elif start_date == 'month':
        start_date = today - timedelta(days=31)
    elif start_date == 'year':
        start_date = today - timedelta(days=365)
    else:
        start_date = today - timedelta(days=900)

    products = []
    name_products = []

    if client_id:
        orders = Order.objects.filter(client=client_id, created_timestamp__gte=start_date).order_by(
            '-created_timestamp')
        for order in orders:
            items = OrderItem.objects.filter(order_id=order.id).order_by('-created_timestamp')
            for item in items:
                if item.product.name not in name_products:
                    name_products.append(item.product.name)
                    products.append(item)
                # sorted(products.append(item), key=lambda item: item.created_timestamp)
    else:
        items = OrderItem.objects.all().order_by('-created_timestamp')
        for item in items:
            if item.product.name not in name_products:
                name_products.append(item.product.name)
                products.append(item)

    context = {
        'title': f'Заказанные {Client.objects.filter(id=client_id).first()} товары',
        'products': products
    }
    return render(request, 'myapp3/ordered_goods.html', context=context)


def catalog(request):
    # Показать все имеющиеся товары
    products = Product.objects.all()

    context = {
        'title': 'Товары',
        'products': products,
    }
    return render(request, 'myapp3/catalog.html', context=context)


def product(request, product_slug=False):
    # Страничка товара
    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'myapp3/product.html', context=context)
