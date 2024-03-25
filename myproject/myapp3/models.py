from django.db import models


class UpdateQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    username = models.CharField(max_length=100, verbose_name='Пользовательское имя')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    date_reg = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        db_table = 'client'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Client {self.username} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления', blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'



class Order(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Клиент')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус заказа")

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return f'Заказ № {self.pk} | Покупатель {self.client.username}'

    @property
    def order_products(self):
        return OrderItem.objects.filter(order=self)

    def total_price(self):
        return sum(product.products_price() for product in OrderItem.objects.filter(order=self))


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт",
                                default=None)
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    objects = UpdateQueryset.as_manager()

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    def products_price(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self) -> str:
        return f'Заказ № {self.order.pk} | Товар {self.product.name}'
