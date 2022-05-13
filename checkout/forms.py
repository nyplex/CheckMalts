from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import re


class CheckoutOneForm(forms.Form):
    mobileNumber = forms.CharField(required=True, max_length=25, min_length=7)
    tableNumber = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes & custom widgets
        """
        user = kwargs.pop('user',None)
        checkout_session = kwargs.pop('checkout_session',None) 
        super().__init__(*args, **kwargs)
        
        if user.mobile and user.mobile != '':
            self.fields['mobileNumber'].widget.attrs['value'] = user.mobile
        if checkout_session:
           self.fields['tableNumber'].widget.attrs['value'] = checkout_session['table']
            
        self.fields['mobileNumber'].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
        self.fields['tableNumber'].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
    
    
    def clean_mobileNumber(self):
        mobileNumber = self.cleaned_data['mobileNumber']
        if not re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", mobileNumber):
            raise forms.ValidationError("Invalid phone number")
        return mobileNumber