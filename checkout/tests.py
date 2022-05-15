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


class CheckoutDetailsView(TestCase):


    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='test1', friendly_name='test1')
        Category.objects.create(name='test2', friendly_name='test2')
        size1 = CocktailsSize(sizes='small')
        size2 = CocktailsSize(sizes='medium')
        size3 = CocktailsSize(sizes='large')
        size1.save()
        size2.save()
        size3.save()
        Cocktail.objects.create(name='test1', friendly_name='test1', slug='test-1', price=10, net_price=5,
                                prep_time=1, category=Category.objects.get(pk=1))
        cocktail2 = Cocktail(name='test2', friendly_name='test2', slug='test-2', price=15, net_price=7,
                             prep_time=1, category=Category.objects.get(pk=2), has_size=True)
        cocktail2.save()
        cocktail2.sizes.add(size1)
        cocktail2.sizes.add(size2)
        cocktail2.sizes.add(size3)


    def test_checkout_details_view(self):
        # Test the view 
        # Check the template, the response code 
        # check if the templtate has the correct elements. 
        # check the displayed basket
        # check matching price and qty 
        
        basket = {'1': {'item': {'quantity': {'quantity': 3}}}}
        self.assertEqual(self.client.session.get('basket'), basket)
        
    
    def test_checkout_view_with_empty_basket(self):
        # expected redirect to order page
        print('hello world')