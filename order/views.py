from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def order(request):
        
    return render(request, 'order/order.html')
