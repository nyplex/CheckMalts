from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('cocktails', views.my_cocktails, name='my_cocktails'),
    path('orders', views.my_orders, name='my_orders'),
]