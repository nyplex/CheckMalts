from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from smtplib import SMTPException
from django.template.loader import get_template


def home(request):
    """ A view to return the index page """
    return render(request, 'home/home.html')


def booking(request):
    """ A view to return the index page """

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            email = request.POST.get('booking_email').strip()
            try:
                cust_email = email
                subject = 'We\'ve got your booking!'
                context = {
                    'booking_time': request.POST.get('booking_time').strip(),
                    'booking_name': request.POST.get('booking_name').strip(),
                    'booking_size': request.POST.get('booking_size'),
                    'booking_date': request.POST.get('booking_date'),
                }
                message = get_template(
                    'home/emails/booking_confirmation.html').render(context)
                msg = EmailMessage(subject, message, to=[
                                cust_email], from_email=settings.DEFAULT_FROM_EMAIL)
                msg.content_subtype = 'html'
                msg.send()
                
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