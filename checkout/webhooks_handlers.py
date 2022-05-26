from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Order, OrderLine, PendingOrders
from .utils import *
from menu.models import Cocktail
import json
import os
from twilio.rest import Client


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Update the order to pending=False, send SMS and email to confirm order  + estimation time
        intent = event['data']['object']
        pid = intent['id']
        order_id = intent['metadata']['order_id']

        order = Order.objects.get(pk=order_id)
        bag = order.original_bag
        bag.replace('[', '{')
        bag.replace(']', '}')

        # Update the order in DB
        order.is_paid = True
        order.is_pending = False
        order.stripe_pid = pid
        order.is_cancelled = False
        order.save()

        # Add the orderline
        for i in json.loads(bag):
            try:
                cocktail = Cocktail.objects.get(pk=int(i['item_id']))
                quantity = int(i['quantity'])
                subtotal = float(i['sub_total'])
                size = None
                note = None
                if 'size' in i:
                    size = i['size']
                if 'note' in i:
                    note = i['note']

                orderLine = OrderLine(order=order, cocktail=cocktail, cocktail_size=size,
                                      note=note, lineitem_total=subtotal, quantity=quantity)
                orderLine.save()

            except Cocktail.DoesNotExist:
                print('One of the products in your bag wasn\'t found in our database.')

        # Add the order to the PendingOrders in DB & get prep time
        PendingOrders.objects.create(
            order=order, estim_prep_time=calculate_prep_time_per_order(order))
        total_prep_time = calculate_total_prep_time(order)

        # send_confirmation_email(order, total_prep_time)
        # send_confirmation_sms(order, total_prep_time)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Send an email & SMS of failed payment and cancelled order
        intent = event['data']['object']
        pid = intent['id']
        order_id = intent['metadata']['order_id']
        order = Order.objects.get(pk=order_id)

        # Update the order in DB
        order.is_paid = False
        order.is_pending = True
        order.is_cancelled = False
        order.stripe_pid = pid
        order.save()

        send_order_failed_email(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
