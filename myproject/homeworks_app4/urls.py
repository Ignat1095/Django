from django.urls import path

from homeworks_app4 import views
app_name = 'homeworks_app4'

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('change_product/', views.change_product, name='change_product'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
    # path('create_order/<int:id>', views.create_order, name='create_order'),
]
