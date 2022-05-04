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

    def test_empty_basket_view(self):
        response = self.client.get(reverse('order'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order.html')
        self.assertContains(
            response, 'Browse our menu and start adding items to your order')
        self.assertContains(response, '<p>£0.00</p>')
        self.assertContains(response, '(0 item)')

    def test_non_empty_basket_view(self):
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        response = self.client.get(reverse('order'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order.html')
        self.assertContains(response, '(3 items)')
        self.assertContains(response, '<p>£30.00</p>')
        self.assertContains(
            response, '<p class="text-sm text-gray-400 font-barlow font-normal mb-1 max-w-[70%]">Note: "test note"</p>')

    def test_add_item_noSize_noNote_valid(self):
        response = self.client.post(
            '/basket/add/1/', data={'cocktail_quantity': '3', 'redirect_url': '1'})
        basket = {'1': {'item': {'quantity': {'quantity': 3}}}}
        messages = [msg for msg in get_messages(response.wsgi_request)]
        
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get('basket'), basket)
        self.assertEqual(str(messages[0]), 'Added 3 `TEST1` to your bag')

    def test_add_item_Size_noNote_valid(self):
        response = self.client.post(
            '/basket/add/2/', data={'cocktail_quantity': '2', 'redirect_url': '2', 'cocktail_size': 'small'})
        basket = {'2': {'item': {'size': {'small': 2}}}}
        messages = [msg for msg in get_messages(response.wsgi_request)]
        
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get('basket'), basket)
        self.assertEqual(str(messages[0]), 'Added 2 `TEST2` to your bag')

    def test_add_item_noSize_Note_valid(self):
        response = self.client.post(
            '/basket/add/1/', data={'cocktail_quantity': '2', 'redirect_url': '2', 'cocktail_note': 'test note'})
        basket = {'1': {'items_by_note': [
            {'note': 'test note', 'quantity': 2}]}}
        messages = [msg for msg in get_messages(response.wsgi_request)]
        
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get('basket'), basket)
        self.assertEqual(str(messages[0]), 'Added 2 `TEST1` to your bag')

    def test_add_item_Size_Note_valid(self):
        response = self.client.post(
            '/basket/add/2/', data={'cocktail_quantity': '2', 'redirect_url': '2', 'cocktail_note': 'test note', 'cocktail_size': 'large'})
        basket = {'2': {'items_by_note': [
            {'note': 'test note', 'quantity': 2, 'size': 'large'}]}}
        messages = [msg for msg in get_messages(response.wsgi_request)]
    
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get('basket'), basket)
        self.assertEqual(str(messages[0]), 'Added 2 `TEST2` to your bag')

    def test_add_mulitple_item_valid(self):
        response = self.client.post(
            '/basket/add/2/', data={'cocktail_quantity': '2', 'redirect_url': '2', 'cocktail_note': 'test note', 'cocktail_size': 'large'})
        response = self.client.post(
            '/basket/add/2/', data={'cocktail_quantity': '1', 'redirect_url': '2', 'cocktail_note': 'test note', 'cocktail_size': 'small'})
        response = self.client.post(
            '/basket/add/2/', data={'cocktail_quantity': '3', 'redirect_url': '2', 'cocktail_size': 'small'})
        response = self.client.post(
            '/basket/add/1/', data={'cocktail_quantity': '3', 'redirect_url': '1'})
        response = self.client.post(
            '/basket/add/1/', data={'cocktail_quantity': '2', 'redirect_url': '1', 'cocktail_note': 'test note'})
        
        basket = {'2': {'items_by_note': [{'note': 'test note', 'quantity': 2, 'size': 'large'}, {'note': 'test note', 'quantity': 1, 'size': 'small'}], 'item': {
            'size': {'small': 3}}}, '1': {'item': {'quantity': {'quantity': 3}}, 'items_by_note': [{'note': 'test note', 'quantity': 2}]}}
        messages = [msg for msg in get_messages(response.wsgi_request)]

        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get('basket'), basket)
        self.assertEqual(str(messages[4]), 'Added 2 `TEST1` to your bag')
        self.assertEqual(str(messages[1]), 'Added 1 `TEST2` to your bag')

    
    def test_add_item_without_qty(self):
        response = self.client.post(
            '/basket/add/1/', data={'cocktail_quantity': '0', 'redirect_url': '1'})
        self.assertEquals(response.status_code, 404)
    
    
    def test_add_invalid_item(self):
        response = self.client.post(
            '/basket/add/3/', data={'cocktail_quantity': '2', 'redirect_url': '1'})
        self.assertEquals(response.status_code, 404)