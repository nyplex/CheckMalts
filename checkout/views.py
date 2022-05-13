from django.shortcuts import render, redirect
from allauth.account.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from profiles.models import UserProfile
from .forms import CheckoutOneForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import stripe



@login_required()
def checkout_details(request):
    """ A view to render the first step of the checkout process """
    #request.session['checkout_session'] = {}
    current_user = UserProfile.objects.get(user=request.user.id)
    checkout_session = {}
    form = CheckoutOneForm(user=current_user, checkout_session=request.session.get('checkout_session'))
    
    if not request.session.get('basket'):
        return redirect('order')
    if request.session.get('basket') == {}:
        return redirect('order')
    
    if request.method == 'POST':
        form = CheckoutOneForm(request.POST, user=current_user, checkout_session=request.session.get('checkout_session'))
        if form.is_valid():
            tableNumber = request.POST.get('tableNumber').strip()
            current_user.mobile = request.POST.get('mobileNumber').strip()
            current_user.save()
            
            if request.POST.get('tableNumber').strip() == '':
                tableNumber = 0
            checkout_session['table'] = int(tableNumber)
            checkout_session['step1'] = True
            request.session['checkout_session'] = checkout_session
            return redirect('checkout_2')
        
        else:
            checkout_session['table'] = 0
            checkout_session['step1'] = False
            request.session['checkout_session'] = checkout_session
            messages.add_message(request, messages.ERROR, 'We found an error in the form!', extra_tags='alert')

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

    
    context = {
        'stripe_public_key': 'pk_test_51KyyMtEUSVW7Sz1sy5Jl5Lu3V8WargxHJh4yfUGKupPIRwZ7oxurpMWedQ9z1SXipvxMTdKk5U2CxnXVVQ2cV05S00WBkcxrrj',
        'client_secret': 'test secret client'
    }

    
    return render(request, 'checkout/checkout_payment.html', context)


@method_decorator(csrf_exempt)
def create_payment(request):
    stripe.api_key = 'sk_test_51KyyMtEUSVW7Sz1sSFyAssUs1mdh7w1WtM5V3fAdX6BMSxUPraeEnyh2zk4DoX0biZezk52mxMXc6Cicx2lhhWJf00n7x0acLi'
    try:
        # data = json.loads(request.POST)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=10000,
            currency='gbp',
            payment_method_types=[
                'card'
            ],
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        print(e)
        return JsonResponse({'e': 'error'}), 403    



@login_required()
def checkout_confirmation(request):
    """ A view to render the order page """
    
    return render(request, 'checkout/checkout_confirmation.html')