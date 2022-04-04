from django import forms
from .widgets import SelectCustomWidget
from .models import Booking
from django.core.exceptions import ValidationError
from datetime import date


class BookingForm(forms.ModelForm):

    bookingTimeOptions = (
        ('', 'Choose Time'),
        ('1400', '14:00'), ('1430', '14:30'),
        ('1500', '15:00'), ('1530', '15:30'),
        ('1600', '16:30'), ('1630', '16:30'),
        ('1700', '17:00'), ('1730', '17:30'),
        ('1800', '18:00'), ('1830', '18:30'),
        ('1900', '19:00'), ('1930', '19:30'),
        ('2000', '20:00'), ('2030', '20:30'),
        ('2100', '21:00'), ('2130', '21:30'),
        ('2200', '22:00'), ('2230', '22:30'),
        ('2300', '23:00'),
    )

    bookingSizeOptions = (
        ('', 'Choose Size'),
        ('1', '1'), ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5'), ('6', '6'),
        ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'),
    )

    def clean_booking_date(self):
        data = self.cleaned_data["booking_date"]
        if data < date.today():
            raise ValidationError(
                'Enter a valid date')

        return data

    class Meta:
        model = Booking
        fields = '__all__'

    booking_email = forms.EmailField(label='Your email', max_length=250, widget=forms.TextInput(
        attrs={'class': 'primary-input mb-4', 'placeholder': 'john.doe@gmain.com'}), required=True)

    booking_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'primary-input mb-4', 'placeholder': 'John Doe'}), required=True, max_length=100, min_length=4)

    booking_date = forms.DateField(widget=forms.TextInput(
        {'class': 'primary-date-picker mb-4', 'placeholder': 'Select date', 'datepicker': '', 'datepicker-buttons': ''}), required=True)

    booking_time = forms.ChoiceField(label='Booking Time', widget=SelectCustomWidget(
    ), required=True, choices=bookingTimeOptions)

    booking_size = forms.ChoiceField(label='Booking Size', widget=SelectCustomWidget(
    ), required=True, choices=bookingSizeOptions)

    booking_size.widget.attrs.update({'class': 'primary-select-input mb-4'})

    booking_time.widget.attrs.update({'class': 'primary-select-input mb-4'})
