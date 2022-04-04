from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def checkout(request):
    return render(request, 'home/checkout.html')