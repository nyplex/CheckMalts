
from django.shortcuts import get_object_or_404, render

from .models import UserProfile
from .forms import UserForm, UserProfileForm


def account(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    user_profile_form = UserProfileForm(instance=profile)
    user_form = UserForm(instance=profile.user)
    
    context = {
        'user_profile_form': user_profile_form,
        'user_form': user_form
    }
    
    return render(request, 'profiles/account.html', context)



def my_cocktails(request):
    return render(request, 'profiles/my_cocktails.html')



def my_orders(request):
    
    return render(request, 'profiles/my_orders.html')

