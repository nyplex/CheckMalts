
from django.shortcuts import get_object_or_404, render
from checkout.models import Order
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from django.contrib import messages
from allauth.account.decorators import login_required


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
            
            update = user_form.save(commit=False)
            update.user = request.user
            update.save()
            
            f = UserProfileForm(request.POST, instance=profile)
            user_profile_form.save()
            
            new_email = EmailAddress(user=request.user, email=request.POST.get('email'), verified=True, primary=True)
            EmailAddress.objects.get(pk=current_email.id).delete()
            new_email.save()

    
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
def my_cocktails(request):
    return render(request, 'profiles/my_cocktails.html')








class MyPasswordChangeView(PasswordChangeView):
    """
    Custom class to override the password change view 
    """
    success_url = "/profile/"
    # Override form valid view to keep user logged i
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password has been changed.', extra_tags='alert')
        return super().form_valid(form)