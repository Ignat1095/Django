from django.contrib import admin

from myapp3.models import Client, Product, OrderItem, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    search_fields = ['username', 'email', ]


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'image']
    list_editable = ['price']
    search_fields = ['name', 'description']
    list_filter = ['quantity', 'price']
    fields = [
        "name",
        "slug",
        "description",
        "image",
        "price",
        "quantity",
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "quantity"
    search_fields = (
        "order",
        "product",
    )
    readonly_fields = ('created_timestamp',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
    search_fields = (
        "id", "client"
    )
    readonly_fields = ("created_timestamp",)

    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
