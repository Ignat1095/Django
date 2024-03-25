from django.urls import path

from myapp3 import views
app_name = 'myapp3'

urlpatterns = [
    path('', views.index, name='index'),
    # path('get_orders/', views.view_orders, name='get_orders'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('view_orders/<int:client_id>/', views.view_orders, name='view_orders'),
    path('ordered_goods/', views.view_ordered_goods, name='ordered_goods'),
    path('ordered_goods/<int:client_id>/', views.view_ordered_goods, name='ordered_goods_id'),
    path('ordered_goods/<int:client_id>/<str:start_date>/', views.view_ordered_goods, name='ordered_goods_id_date'),
]
