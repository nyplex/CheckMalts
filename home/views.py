from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages

# Create your views here.

def home(request):
    """ A view to return the index page """

    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = BookingForm()
            messages.add_message(request, messages.SUCCESS, 'We\'ve got your booking! We sent you a confirmation email.')
        else:
            messages.add_message(request, messages.ERROR, 'We found an error in the form!')

    context = {
        'form': form
    }

    return render(request, 'home/home.html', context)