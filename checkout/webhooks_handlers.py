from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Order, OrderLine
from menu.models import Cocktail
import json
import os
from twilio.rest import Client


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.user_profile.user.email
        subject = f'CheckMalt Confirmation for Order #{order.id}'
        context = {
            'order': order
        }
        message = get_template(
            'checkout/emails/confirm_order.html').render(context)
        msg = EmailMessage(subject, message, to=[
                           cust_email], from_email=settings.DEFAULT_FROM_EMAIL)
        msg.content_subtype = 'html'
        msg.send()

    def _send_confirmation_sms(self, order):
        """ Send the user a confirmation SMS """
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        user_phone = order.user_profile.mobile

        message = client.messages \
                        .create(
                            body=f"CheckMalt - Order Confirmation. Your order ID is #{order.id}. \
                            Your order should be ready in approx. 15min. We will send you \
                            a message when it's time to get your order.",
                            from_='+17752563749',
                            to=f'+44{user_phone}'
                        )

    def _send_order_failed_email(self, order):
        cust_email = order.user_profile.user.email
        subject = f'CheckMalt Order Cancelled!'
        context = {
            'order': order
        }
        message = get_template(
            'checkout/emails/failed_order.html').render(context)
        msg = EmailMessage(subject, message, to=[
                           cust_email], from_email=settings.DEFAULT_FROM_EMAIL)
        msg.content_subtype = 'html'
        msg.send()

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

        #self._send_confirmation_email(order)
        #self._send_confirmation_sms(order)

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

        self._send_order_failed_email(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
