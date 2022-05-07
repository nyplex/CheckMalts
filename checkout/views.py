from django.shortcuts import render
from allauth.account.decorators import login_required


@login_required()
def checkout_details(request):
    """ A view to render the order page """


    return render(request, 'checkout/place_order.html')