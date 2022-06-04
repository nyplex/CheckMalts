
from django.shortcuts import get_object_or_404, redirect, render
from checkout.models import Order
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView, LogoutView, LoginView, SignupView, PasswordSetView
from django.contrib import messages
from allauth.account.decorators import login_required
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import User

@login_required()
def account(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile_form = UserProfileForm(instance=profile)
    user_form = UserForm(instance=profile.user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            current_email = EmailAddress.objects.get(user=request.user)
            new_email = user_form.cleaned_data.get('email')
            if current_email.email.strip() != new_email.strip():
                email_in_db = User.objects.filter(email=new_email)
                if len(email_in_db) > 0:
                    user_form.add_error("email", 'This email already exists!')
                    messages.error(request, 'There is an error in the form!', extra_tags='alert')
                else:
                    update = user_form.save(commit=False)
                    update.user = request.user
                    update.save()
                    
                    f = UserProfileForm(request.POST, instance=profile)
                    user_profile_form.save()
                    
                    new_email = EmailAddress(user=request.user, email=request.POST.get('email'), verified=True, primary=True)
                    EmailAddress.objects.get(pk=current_email.id).delete()
                    new_email.save()
                    
                    messages.success(request, 'Your have updated your personnal data.', extra_tags='alert')
            else:
                messages.success(request, 'Your have updated your personnal data.', extra_tags='alert')
        else:
            messages.error(request, 'There is an error in the form!', extra_tags='alert')
    
    context = {
        'user_profile_form': user_profile_form,
        'user_form': user_form
    }
    
    return render(request, 'profiles/account.html', context)


@login_required()
def my_orders(request):
    
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile, is_pending=False).order_by('-date')
    
    context = {
        'orders': orders
    }
    
    return render(request, 'profiles/my_orders.html', context)





@login_required()
def my_favourites(request):
    return render(request, 'profiles/my_favourites.html')





class MyPasswordChangeView(PasswordChangeView):
    """
    Custom class to override the password change view 
    """
    success_url = "/profile/"
    # Override form valid view to keep user logged in
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password has been changed.', extra_tags='alert')
        return super().form_valid(form)
    

class LogoutCustomView(LogoutView):
    """
    Custom class to override the logout view 
    """


class LoginCustomView(LoginView):
    """
    Custom class to override the login view
    """

class SignUpCustomView(SignupView):
    """
    Custom class to override the signup view
    """

class SetPasswordCustomView(PasswordSetView):
    success_url = "/profile/"
    # Override form valid view to keep user logged in
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password has been set.', extra_tags='alert')
        return super().form_valid(form)



def show_message(sender, user, request, **kwargs):
    """ Display success message on logout """
    messages.success(request, 'You have logged out.', extra_tags='alert')
    

user_logged_out.connect(show_message)