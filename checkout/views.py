import json
from django.shortcuts import render, redirect
from allauth.account.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from profiles.models import UserProfile
from .forms import CheckoutOneForm
from .models import Order, OrderLine
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from basket.contexts import basket_contents
import stripe
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
    #request.session['checkout_session'] = {}
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
            current_user.mobile = request.POST.get('mobileNumber').strip()
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
        
        #Create Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=round(float(current_bag['grandTotal']) * 100),
            currency='gbp',
            payment_method_types=[
                'card'
            ],
            metadata={'order_id':new_order.id}
        )

        return JsonResponse({
            'clientSecret': intent['client_secret'],
            'order_id': new_order.id
        })
    except Exception as e:
        return JsonResponse({'e': 'error'}), 403


@login_required()
def checkout_confirmation(request, order_id):
    """ A view to render the order page """
    
    user_profile = UserProfile.objects.get(user=request.user.id)
    order = Order.objects.get(pk=order_id)
    
    if order.user_profile != user_profile:
        return redirect('order')
    if order.is_pending != True:
        return redirect('order')

    return render(request, 'checkout/checkout_confirmation.html')
