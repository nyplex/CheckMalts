from django.urls import path
from . import views

urlpatterns = [
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('modal/<item_id>', views.item_modal, name='basket_item_modal'),
    path('update/<item_id>', views.update_basket, name='update_basket'),
    path('remove/<item_id>/', views.remove_from_basket, name='remove_from_basket'),
]