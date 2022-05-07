from django.urls import path
from . import views

urlpatterns = [
    path('checkout-details', views.checkout_details, name='checkout_1'),
]