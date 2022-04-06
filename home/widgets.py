from .models import Booking
from django.forms.widgets import Select, TextInput
from django.utils.translation import gettext_lazy as _


class SelectCustomWidget(Select):

    def __init__(self, attrs=None, name=None):
        super(Select, self).__init__(attrs)
        if name == 'booking_size':
            self.choices = Booking.BOOKINGSIZEOPTIONS
        if name == 'booking_time':
            self.choices = Booking.BOOKINGTIMEOPTIONS
        self.attrs = {'class': 'primary-select-input'}

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = 'disabled'
        return option


class DatePickerCustomWidget(TextInput):
    def __init__(self, attrs=None):
        super(TextInput, self).__init__(attrs)
        self.attrs = {
            'class': 'primary-date-picker',
            'datepicker': '',
            'datepicker-buttons': '',
            'placeholder': 'Select date',
            'autocomplete': 'off'}

