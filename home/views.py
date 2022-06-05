from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException


def home(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def booking(request):
    """ A view to return the index page """

    form = BookingForm()

    if request.method == 'POST':

        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                send_mail('booking confirmation','we receive your booking',settings.DEFAULT_FROM_EMAIL,['nypels.alexandre@outlook.com'])
            except SMTPException as e:
                messages.add_message(request, messages.ERROR, 'We\'ve got an error from our server. Please give us a call to book a table. 0208 444 767', extra_tags='alert')
                return redirect('booking')

            form.save()
            messages.add_message(request, messages.SUCCESS, 'We\'ve got your booking! Check your email for the confirmation.', extra_tags='booking_confirm')
            return redirect('booking')

        else:
            messages.add_message(request, messages.ERROR, 'We found an error in the form!', extra_tags='alert')

    context = {
        'form': form
    }

    return render(request, 'home/booking.html', context)