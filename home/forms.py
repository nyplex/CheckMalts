from django import forms
from .widgets import SelectCustomWidget
from .models import Booking
from django.core.exceptions import ValidationError
from datetime import date


class BookingForm(forms.ModelForm):

    def clean_booking_date(self):
        data = self.cleaned_data['booking_date']
        today = date.today().strftime('%Y-%d-%m')
        if data < date.today():
            raise ValidationError(
                'Booking date must be in the future')
        return data

    class Meta:
        model = Booking
        fields = '__all__'
        
        error_messages = {
            'booking_name': {
                'max_length': 'This writer\'s name is too long.',
                'min_length': 'This writer\'s name is too long.',
            },
        }

    booking_email = forms.EmailField(label='Your email', max_length=200, widget=forms.TextInput(
        attrs={'class': 'primary-input', 'placeholder': 'john.doe@gmain.com'}), required=True)

    booking_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'primary-input', 'placeholder': 'John Doe'}), required=True, max_length=50, min_length=4, 
                                   error_messages={
                                       'min_length': 'blbablaalb'
                                   })

    booking_date = forms.DateField(widget=forms.TextInput(
        {'class': 'primary-date-picker', 'placeholder': 'Select date', 'datepicker': '', 'datepicker-buttons': '', 'autocomplete': 'off'}), required=True)

    booking_time = forms.ChoiceField(label='Booking Time', widget=SelectCustomWidget(
    ), required=True, choices=Booking.BOOKINGTIMEOPTIONS)

    booking_size = forms.ChoiceField(label='Booking Size', widget=SelectCustomWidget(
    ), required=True, choices=Booking.BOOKINGSIZEOPTIONS)
