from django import forms
import phonenumbers
import re


class CheckoutOneForm(forms.Form):
    mobileNumber = forms.CharField(required=True, max_length=25, min_length=7)
    tableNumber = forms.DecimalField(required=False, decimal_places=0, max_digits=3, min_value=0, max_value=100)
    tips = forms.DecimalField(required=False, decimal_places=2, max_digits=7, min_value=0, max_value=99999.99)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes & custom widgets
        """
        user = kwargs.pop('user', None)
        checkout_session = kwargs.pop('checkout_session', None)
        super().__init__(*args, **kwargs)

        if user.mobile and user.mobile != '':
            self.fields['mobileNumber'].widget.attrs['value'] = user.mobile
        if checkout_session:
            self.fields['tableNumber'].widget.attrs['value'] = checkout_session['table']
            self.fields['tips'].widget.attrs['value'] = checkout_session['tips']

        self.fields['mobileNumber'].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
        self.fields['tableNumber'].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
        self.fields['tips'].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'


    def clean_mobileNumber(self):
        mobileNumber = self.cleaned_data['mobileNumber'].replace(' ', '')
        try:
            phone_number = phonenumbers.parse(mobileNumber, None)
        except:
            raise forms.ValidationError("Invalid phone number")
        
        if not re.match(r'(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+', mobileNumber):
            raise forms.ValidationError("Invalid phone number")
        if not phonenumbers.is_possible_number(phone_number):
            raise forms.ValidationError("Invalid phone number")
        
        return mobileNumber
