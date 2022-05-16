from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib import auth
from .models import *
from menu.models import *
from http import HTTPStatus
from django.contrib.messages import get_messages
from django.core import mail
from django.contrib.auth.models import User
from profiles.models import UserProfile
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

        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        user_profile = UserProfile.objects.get(user=user)
        user_profile.mobile = '07808808808'
        user_profile.save()

    def test_checkout_details_view(self):

        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        response = self.client.get(reverse('checkout_1'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        self.assertContains(
            response, '<span class="mr-2 max-w-[70%]">2x <span class="font-normal">TEST1 </span></span>')
        self.assertContains(
            response, '<span class="mr-2 max-w-[70%]">1x <span class="font-normal">TEST1 </span></span>')
        self.assertContains(response, '<p id="subtotal">£30.00</p>')

    def test_checkout_details_with_empty_basket(self):

        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {}
        basket.save()

        response = self.client.get(reverse('checkout_1'))
        self.assertEquals(response.status_code, 302)

    def test_checkout_view_without_logged_in(self):

        response = self.client.get(reverse('checkout_1'))
        self.assertEquals(response.status_code, 302)

    def test_checkout_view_with_mobile_saved(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        response = self.client.get(reverse('checkout_1'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        self.assertContains(
            response, '<input type="text" name="mobileNumber" maxlength="25" minlength="7" value="07808808808"')

    def test_checkout_valid_post(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': '07808808808',
            'tableNumber': '2',
            'tips': '10'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 2
        checkout_session['tips'] = 10
        checkout_session['step1'] = True

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
    
    
    def test_checkout_invalid_table(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': '07808808808',
            'tableNumber': 'a',
            'tips': '10'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 0
        checkout_session['tips'] = 0
        checkout_session['step1'] = False

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'We found an error in the form!')
        self.assertContains(response, '<p class="input-errors">Enter a number.</p>') 
        

    def test_checkout_invalid_tips(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': '07808808808',
            'tableNumber': '11',
            'tips': 'a'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 0
        checkout_session['tips'] = 0
        checkout_session['step1'] = False

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'We found an error in the form!')
        self.assertContains(response, '<p class="input-errors">Enter a number.</p>') 
    

    def test_checkout_invalid_phone(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': 'invalid',
            'tableNumber': '11',
            'tips': '10'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 0
        checkout_session['tips'] = 0
        checkout_session['step1'] = False

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'We found an error in the form!')
        self.assertContains(response, '<p class="input-errors">Invalid phone number</p>')  
    
    
    def test_checkout_without_phone(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': '',
            'tableNumber': '11',
            'tips': '10'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 0
        checkout_session['tips'] = 0
        checkout_session['step1'] = False

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
        self.assertTemplateUsed(response, 'checkout/checkout_details.html')
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'We found an error in the form!')
        self.assertContains(response, '<p class="input-errors">This field is required.</p>')  
    
    
    # test with new phone number and check it has been updated 
    def test_checkout_with_new_phone(self):
        self.client.login(username='testuser', password='12345')
        basket = self.client.session
        basket['basket'] = {'1': {'item': {'quantity': {
            'quantity': 2}}, 'items_by_note': [{'note': 'test note', 'quantity': 1}]}}
        basket.save()

        data = {
            'mobileNumber': '07666666541',
            'tableNumber': '11',
            'tips': '10'
        }
        response = self.client.post('/checkout/details', data=data)
        checkout_session = {}
        checkout_session['table'] = 11
        checkout_session['tips'] = 10
        checkout_session['step1'] = True
        
        user = UserProfile.objects.get(pk=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get(
            'checkout_session'), checkout_session)
        self.assertEqual(user.mobile, '07666666541') 
    
    
class CheckoutPaymentView(TestCase):
    
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

        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        user_profile = UserProfile.objects.get(user=user)
        user_profile.mobile = '07808808808'
        user_profile.save()
    
