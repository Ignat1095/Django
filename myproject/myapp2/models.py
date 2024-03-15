from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, ' \
               f'email: {self.email},  ' \
               f'phone: {self.phone}, ' \
               f'address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images')

    # product_image поле не обязательное !

    def __str__(self):
        return f'Product name: {self.name}, ' \
               f'price: {self.price},  ' \
               f'description: {self.description}, ' \
               f'quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Customer: {self.customer.name}, ' \
               f'products: {self.products},  ' \
               f'date_ordered: {self.date_ordered}, ' \
               f'total_price: {self.total_price}'
