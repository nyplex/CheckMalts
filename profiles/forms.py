from allauth.account.forms import SignupForm, LoginForm, ChangePasswordForm, SetPasswordForm
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
            })


class CustomPasswordChangeForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg',
                'placeholder': ''
            })


class CustomSetPasswordForm(SetPasswordForm):
     def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
            })
            
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile',)
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
            self.fields[field].required = True
            

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'login-form-input rounded-sm w-full focus:border-secondaryHoverDarker focus:ring-0 text-primaryColor text-lg'
            self.fields[field].required = True
            self.fields[field].minlength = 4
    
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 3 or len(first_name) > 150:
            raise forms.ValidationError("Must have between 2 and 150 characters")
        return self.cleaned_data['first_name']
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 3 or len(last_name) > 150:
            raise forms.ValidationError("Must have between 2 and 150 characters")
        return self.cleaned_data['last_name']
    