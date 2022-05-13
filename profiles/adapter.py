from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import SignupForm
from django import forms


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        print(request)
        path = "/order"
        return path
