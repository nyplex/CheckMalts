from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib import auth
from .models import *
from menu.models import *
from http import HTTPStatus
from django.contrib.messages import get_messages
from django.core import mail
# Create your tests here.


class BasketView(TestCase):

    def test_empty_basket_view(self):
        response = self.client.get(reverse('basket'))
        self.assertRedirects(response, reverse("order"))
    
    
