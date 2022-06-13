from .widgets import SelectCustomWidget, DatePickerCustomWidget
from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes & custom widgets
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'booking_email': 'john.doe@gmail.com',
            'booking_name': 'John Doe',
        }

        self.fields['booking_size'].widget = SelectCustomWidget(name='booking_size')
        self.fields['booking_time'].widget = SelectCustomWidget(name='booking_time')
        
        
        for field in self.fields:
            if field == 'booking_email' or field == 'booking_name':
                self.fields[field].widget.attrs['class'] = 'primary-input'
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
                self.fields[field].widget.attrs['minlength'] = 4
                
    booking_date = forms.DateField(input_formats=['%d/%m/%Y'],
                                   widget=DatePickerCustomWidget())