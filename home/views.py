from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.

def home(request):
    """ A view to return the index page """
    
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            print("valid!!")
        else:
            print("errrorrororo")
            print(form.errors)
    else:
        form = BookingForm()
    context = {
        "form": form
    }


    return render(request, 'home/home.html', context)


def checkout(request):
    return render(request, 'home/checkout.html')