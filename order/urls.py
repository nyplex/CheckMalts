from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('/item-detail', views.item_detail, name='item-detail'),
    path('/size-price', views.calculate_size_price, name='size-price'),
    path('order-again/<order_id>', views.order_again, name='order_again')
]
