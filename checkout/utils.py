from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from menu.models import Cocktail
from .models import *
import os
from twilio.rest import Client


def send_confirmation_email(order, total_prep_time):
        """Send the user a confirmation email"""
        cust_email = order.user_profile.user.email
        subject = f'CheckMalt Confirmation for Order #{order.id}'
        context = {
            'order': order,
            'prep_time': total_prep_time
        }
        message = get_template(
            'checkout/emails/confirm_order.html').render(context)
        msg = EmailMessage(subject, message, to=[
                           cust_email], from_email=settings.DEFAULT_FROM_EMAIL)
        msg.content_subtype = 'html'
        msg.send()


def send_confirmation_sms(order, total_prep_time):
        """ Send the user a confirmation SMS """
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        user_phone = order.user_profile.mobile
        prep_time = str(total_prep_time)
        message = client.messages \
                        .create(
                            body=f"CheckMalt - Order Confirmation. Your order ID is #{order.id}. Your order should be ready in approx. {prep_time}min. We will send you a message when it's time to get your order.",
                            from_='+447897035269',
                            to=user_phone
                        )

def send_order_ready_sms(order):
        """ Send the user a confirmation SMS """
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        user_phone = order.user_profile.mobile
        first_name = order.user_profile.user.first_name
        message = client.messages \
                        .create(
                            body=f"CheckMalt - Hey {first_name}, your order is ready. If you have a table we will bring your order to you. Otherwise it is time to go and grap your drinks. Cheers!.",
                            from_='+447897035269',
                            to=user_phone
                        )



def send_order_failed_email(order):
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
        

def calculate_prep_time_per_order(order_line):
    
    order_prep_time = 0
    
    for i in order_line:
        item_prep_time = 0
        if i.cocktail.prep_time:
            if i.quantity <= 1:
                item_prep_time += (i.cocktail.prep_time * i.quantity)
            else:
                item_prep_time += (i.cocktail.prep_time * i.quantity) - ((i.cocktail.prep_time * i.quantity) * 0.3)
        order_prep_time += item_prep_time

    return order_prep_time


def calculate_total_prep_time(order, PendingOrders):
    current_pending_order = PendingOrders.objects.filter(order=order).first()
    pending_orders = PendingOrders.objects.filter(pk__lt=current_pending_order.id)
    prep_time = 0
    
    for i in pending_orders:
        prep_time += i.estim_prep_time
    
    return round(prep_time + current_pending_order.estim_prep_time)