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
            response, '<div class="h-[100vh] w-full relative overflow-x-hidden" id="menuHeaderContainer">')
        self.assertIn('cocktails', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('subCategories', response.context)
    

    def test_product_modal(self):
        client = Client()

        cocktail = Cocktail.objects.create(
            name='Test cocktail', price=10, prep_time=1, description='Lorem Lispum Test description')
        cocktail.save()
        
        response = client.get('/menu/1')
        messages = list(response.context['messages'])
        
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Cocktail.objects.count(), 1)
        self.assertEqual(str(messages[0].message.price), '10.0')
        self.assertEqual(str(messages[0].message.name), 'Test cocktail')
        self.assertContains(response, '<div id="productModal" tabindex="-1"')


class NavbarView(TestCase):
    def test_navbar_logged_out(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response, '<a href="#" class="navbar-link">CREATE</a>')
