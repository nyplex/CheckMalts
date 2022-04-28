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


class OrderView(TestCase):
    
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
    
        
    def test_order_view(self):
        client = Client()
        response = client.get(reverse('order'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order.html')
        self.assertContains(
            response, '<div class="max-w-screen-md mx-auto w-full mt-12 px-2" id="orderHeader">')
        self.assertEqual(
            1, response.context['selected'])
        self.assertIn('cocktails', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('selected', response.context)
        self.assertIn('open', response.context)
        self.assertIn('sub_categories', response.context)
    
    
    def test_valid_category_change(self):
        client = Client()
        response = client.get('/order?category=2')
        self.assertEqual(2, response.context['selected'])
    
    
    def test_invalid_category_change(self):
        client = Client()
        response = client.get('/order?category=4535435435735')
        self.assertEquals(response.status_code, 404)
        
    
    def test_open_valid_modal(self):
        client = Client()
        response = client.post('/order/item-detail', data={'item_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response, '<div id="itemModal" class="hidden fixed z-[1000] left-0 top-0 w-full h-full overflow-auto item-modal">')
        self.assertContains(
            response, '<select data-qty-item data-order-item-modal="1"')
        self.assertIn('cocktail', response.context)
        cocktail = Cocktail.objects.get(pk=1)
        self.assertEqual(response.context['cocktail'], cocktail)
    
    
    def test_open_invalid_modal(self):
        client = Client()
        response = client.post('/order/item-detail', data={'item_id': 5})
        self.assertEquals(response.status_code, 404)
    
    
    def test_update_price_on_invalid_item(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': 3, 'item_id': 543})
        self.assertEquals(response.status_code, 404)
    
        
    def test_update_price_on_quantity(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': 3, 'item_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': 30})
    
    def test_update_price_on_negative_quantity(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': -3, 'item_id': 1})
        self.assertEquals(response.status_code, 404)
    
    
    def test_update_price_on_over_quantity(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': 11, 'item_id': 1})
        self.assertEquals(response.status_code, 404)
    
    
    def test_update_price_on_size(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': 1, 'size': 'small', 'item_id': 2})
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': 15})
    
    
    def test_update_price_on_invalid_size(self):
        client = Client()
        response = client.post('/order/size-price', data={'quantity': 1, 'size': 'error', 'item_id': 2})
        self.assertEquals(response.status_code, 404)