from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib import auth
from .models import *
from http import HTTPStatus
from django.contrib.messages import get_messages
from django.core import mail
# Create your tests here.


class MenuView(TestCase):
    def test_menu_view(self):
        client = Client()
        response = client.get(reverse('menu'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')
        self.assertContains(
            response, '<div class=class="h-[100vh] w-full relative overflow-x-hidden bg-contrastColor py-4 overflow-hidden" id="menuHeaderContainer">')
        self.assertIn('cocktails', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('subCategories', response.context)
