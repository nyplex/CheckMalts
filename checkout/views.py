from django.shortcuts import get_object_or_404, render, redirect
from allauth.account.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib import messages

from basket.contexts import basket_contents

from profiles.models import UserProfile
from .forms import CheckoutOneForm
from .models import *
from .utils import *

import stripe
import json
import os
if os.path.exists("env.py"):
    import env


@login_required()
def checkout_details(request):
    """
    A view to render the first step of the checkout process,
    and create a checkout session to store tips & table Number.
    Finally will store True into session if this first step is completed
    """
        
    current_user = UserProfile.objects.get(user=request.user.id)
    checkout_session = {}
    form = CheckoutOneForm(
        user=current_user, checkout_session=request.session.get('checkout_session'))
    
    if not request.session.get('basket'):
        return redirect('order')
    if request.session.get('basket') == {}:
        return redirect('order')

    if request.method == 'POST':
        form = CheckoutOneForm(request.POST, user=current_user,
                               checkout_session=request.session.get('checkout_session'))
        if form.is_valid():
            tableNumber = request.POST.get('tableNumber').strip()
            tips = request.POST.get('tips').strip()
            current_user.mobile = request.POST.get('mobileNumber').replace(' ', '')
            current_user.save()

            if request.POST.get('tableNumber').strip() == '':
                tableNumber = 0
            if request.POST.get('tips').strip() == '':
                tips = 0

            checkout_session['table'] = int(tableNumber)
            checkout_session['tips'] = float(tips)
            checkout_session['step1'] = True
            request.session['checkout_session'] = checkout_session
            return redirect('checkout_2')

        else:
            checkout_session['table'] = 0
            checkout_session['tips'] = 0
            checkout_session['step1'] = False
            request.session['checkout_session'] = checkout_session
            messages.add_message(
                request, messages.ERROR, 'We found an error in the form!', extra_tags='alert')

    context = {
        'userProfile': current_user,
        'checkout_session': request.session.get('checkout_session'),
        'form': form
    }

    return render(request, 'checkout/checkout_details.html', context)


@login_required()
def checkout_payment(request):
    """ A view to render the second second step of the checkout process """

    if not request.session.get('checkout_session'):
        return redirect('checkout_1')
    checkout_session = request.session.get('checkout_session')
    if checkout_session['step1'] != True:
        return redirect('checkout_1')
    if not request.session.get('basket'):
        return redirect('order')
    if request.session.get('basket') == {}:
        return redirect('order')

    return render(request, 'checkout/checkout_payment.html')


@login_required
@method_decorator(csrf_exempt)
def create_payment(request):
    """ A view to create the stripe payment """

    current_bag = basket_contents(request)
    bag = current_bag['basket_items']
    for i in bag:
        del i['cocktail']
    bag = json.dumps(bag)

    checkout_session = request.session.get('checkout_session')
    user_profile = UserProfile.objects.get(user=request.user.id)
    stripe.api_key = os.environ.get('STRIPE_SECRET_CLIENT')

    try:
        # Delete previous pending orders
        Order.objects.filter(user_profile=user_profile,
                             is_pending=True).delete()
        # Create new pending order
        new_order = Order.objects.create(
            user_profile=user_profile,
            grand_total=current_bag['grandTotal'],
            subtotal=current_bag['total'],
            serivce_amount=current_bag['tips'],
            table_number=checkout_session['table'],
            original_bag=bag
        )
        new_order.save()

        # Create Payment Intent
        customer = stripe.Customer.create()
        intent = stripe.PaymentIntent.create(
            customer=customer['id'],
            amount=round(float(current_bag['grandTotal']) * 100),
            currency='gbp',
            payment_method_types=[
                'card'
            ],
            metadata={'order_id': new_order.id}
        )

        return JsonResponse({
            'clientSecret': intent['client_secret'],
            'order_id': new_order.id,
            'order_number': new_order.order_number
        })
    except Exception as e:
        return JsonResponse({'e': 'error'}), 403


@login_required()
def checkout_confirmation(request, order_number):
    """ A view to render the order page """

    user_profile = UserProfile.objects.get(user=request.user.id)
    order = get_object_or_404(Order, order_number=order_number)

    if order.user_profile != user_profile:
        return redirect('order')
    if order.is_cancelled == True:
        return redirect('order')
    if not request.session.get('checkout_session'):
        return redirect('order')
    if not request.session.get('basket'):
        return redirect('order')

    del request.session['basket']
    del request.session['checkout_session']

    context = {
        'order': order
    }

    messages.add_message(
        request, messages.SUCCESS, 'Order confirmed!', extra_tags='alert')

    return render(request, 'checkout/checkout_confirmation.html', context)


@login_required
@method_decorator(csrf_exempt)
def get_prep_time(request):
    """ A view to send the prep time to the Ajax call """

    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        order_id = request.POST.get('order')
        order = Order.objects.get(order_number=order_id)
        try:
            pending_order = PendingOrders.objects.get(order=order)
        except Exception as e:
            return JsonResponse({'e': 'error1'})
            
        if pending_order == None:
            return JsonResponse({'e': 'error2'})
        else:
            if order.user_profile != user_profile:
                return JsonResponse({'e': 'error3'})
            else:
                prep_time = calculate_total_prep_time(order, PendingOrders)
                return JsonResponse({'time': prep_time})
    else:
        return JsonResponse({'e': 'error4'})
