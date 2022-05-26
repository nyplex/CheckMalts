from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('details', views.checkout_details, name='checkout_1'),
    path('payment', views.checkout_payment, name='checkout_2'),
    path('create-payment-intent', views.create_payment, name='create_payment_intent'),
    path('confirmation/<order_number>', views.checkout_confirmation, name='checkout_3'),
    path('wh', webhook, name='webhook'),
    path('preptime', views.get_prep_time, name='prep_time')
]