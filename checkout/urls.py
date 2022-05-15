from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('details', views.checkout_details, name='checkout_1'),
    path('payment', views.checkout_payment, name='checkout_2'),
    path('create-payment-intent', views.create_payment, name='create_payment_intent'),
    path('confirmation/<order_id>', views.checkout_confirmation, name='checkout_3'),
    path('wh', webhook, name='webhook'),
]