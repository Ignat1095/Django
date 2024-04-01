from django.urls import path

from myapp5 import views
app_name = 'myapp5'

urlpatterns = [
    path('', views.index, name='index'),
    # path('get_orders/', views.get_orders, name='get_orders'),
    # path('orders_view/', orders_view, name='orders_view'),
]
