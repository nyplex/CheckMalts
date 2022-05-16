from email import message
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLine
from menu.models import Cocktail
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
    
    def _send_confirmation_sms(self, order):
        """ Send the user a confirmation SMS """
        print("SMS sent!")        

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
        
        order.is_paid = True
        order.is_pending = False
        order.stripe_pid = pid
        order.save()
        
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
                
                orderLine = OrderLine(order=order, cocktail=cocktail, cocktail_size=size, note=note, lineitem_total=subtotal)
                orderLine.save()
            
            except Cocktail.DoesNotExist:
                print('One of the products in your bag wasn\'t found in our database.')
                
                
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Send an email & SMS of failed payment and cancelled order
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)