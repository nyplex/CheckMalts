from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib import auth
from checkout.models import *
from menu.models import *
from http import HTTPStatus
from django.contrib.messages import get_messages
from django.core import mail
from django.contrib.auth.models import User
from profiles.models import UserProfile
from datetime import datetime
from allauth.account.models import EmailAddress
from .forms import UserProfileForm, UserForm
# Create your tests here.


class AccountView(TestCase):

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
        Cocktail.objects.create(name='test1', friendly_name='test1', slug='test-1',
                                price=10, net_price=5, prep_time=1, 
                                category=Category.objects.get(pk=1))
        cocktail2 = Cocktail(name='test2', friendly_name='test2', slug='test-2', 
                             price=15, net_price=7, prep_time=1, category=Category.objects.get(pk=2), 
                             has_size=True)
        cocktail2.save()
        cocktail2.sizes.add(size1)
        cocktail2.sizes.add(size2)
        cocktail2.sizes.add(size3)

        user = User.objects.create(username='testuser', first_name='Jon', last_name='Doe', email='jon.doe@gmail.com')
        user.set_password('12345')
        user.save()
        
        user2 = User.objects.create(username='testuser2', first_name='Jon2', last_name='Doe2', email='jon2.doe@gmail.com')
        user2.set_password('12345')
        user2.save()

        user_profile = UserProfile.objects.get(user=user)
        user_profile.mobile = '07808808808'
        user_profile.save()
        
        user_profile2 = UserProfile.objects.get(user=user2)
        user_profile2.mobile = '07808606606'
        user_profile2.save()
        
        EmailAddress.objects.create(user=user, email='jon.doe@gmail.com', verified=True, primary=True)
        EmailAddress.objects.create(user=user2, email='jon2.doe@gmail.com', verified=True, primary=True)
        
        
        Order.objects.create(user_profile=user_profile, order_number='13456789', 
                             grand_total=15, subtotal=10, serivce_amount=5, 
                             table_number=0, is_done=False, is_paid=True, is_cancelled=False,
                             is_pending=False, date=datetime.now(),
                             original_bag='[{"item_id": "1", "quantity": 1, "sub_total": 10.0}]',
                             stripe_pid='pi_3L2yioEUSVW7Sz1s0xfCjLAD')
    
    
    
    def test_orders_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('my_orders'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_orders.html')
        self.assertContains(
            response, '<td class="px-6 py-4">#1</td>')
        self.assertContains(
            response, '<td class="px-6 py-4">£15.00</td>')
        self.assertContains(
            response, '<h1 class="text-primaryColor font-barlow font-semibold text-3xl mb-4">My Orders</h1>')
    
    
    def test_orders_view_no_login(self):
        response = self.client.get(reverse('my_orders'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/profile/login?next=/profile/orders', 
                             status_code=302, target_status_code=200, 
                             msg_prefix='', fetch_redirect_response=True)
        

    def test_account_view(self):

        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('account'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/account.html')
        self.assertContains(
            response, '<h2 class="font-barlow text-white font-semibold text-2xl ml-4 pb-4">Jon Doe</h2>')
        self.assertContains(
            response, '<input type="text" name="first_name" value="Jon" maxlength="150"')
        
        
    def test_account_view_no_login(self):
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/profile/login?next=/profile/', 
                             status_code=302, target_status_code=200, 
                             msg_prefix='', fetch_redirect_response=True)
    
    
    def test_account_valid_post(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'email': 'newemail@gmail.com',
            'mobile': '07802354504'
        }
        response = self.client.post(reverse('account'), data=data)

        self.assertEquals(response.status_code, 200)
        messages = [msg for msg in get_messages(response.wsgi_request)]
        self.assertEqual(str(messages[0]), 'Your have updated your personnal data.')
        
        userprofile = UserProfile.objects.get(pk=1)
        self.assertEqual(userprofile.user.first_name, 'NewFirstName')
        self.assertEqual(userprofile.user.last_name, 'NewLastName')
        self.assertEqual(userprofile.user.email, 'newemail@gmail.com')
        self.assertEqual(userprofile.mobile, '07802354504')
    
    
    def test_account_invalid_post(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'email': 'jon2.doe@gmail.com',
            'mobile': '07802354504'
        }
        response = self.client.post(reverse('account'), data=data)

        self.assertEquals(response.status_code, 200)
        messages = [msg for msg in get_messages(response.wsgi_request)]
        self.assertEqual(str(messages[0]), 'There is an error in the form!')
        self.assertContains(
            response, '<p class="input-errors">This email already exists!</p>')

    
    
class AccountUserForm(TestCase):
    
    def test_using_short_first_name(self):
        form = UserForm(data={
            'first_name': 'a'
        })
        self.assertEqual(form.errors['first_name'], ['Must have between 2 and 150 characters'])
    
    def test_using_long_first_name(self):
        first_name = 'x' * 151
        form = UserForm(data={
            'first_name': first_name
        })
        self.assertEqual(form.errors['first_name'], ['Ensure this value has at most 150 characters (it has 151).'])
    
    def test_using_empty_first_name(self):
        form = UserForm(data={
            'first_name': ''
        })
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        
    def test_using_short_last_name(self):
        form = UserForm(data={
            'last_name': 'a'
        })
        self.assertEqual(form.errors['last_name'], ['Must have between 2 and 150 characters'])
    
    def test_using_long_last_name(self):
        last_name = 'x' * 151
        form = UserForm(data={
            'last_name': last_name
        })
        self.assertEqual(form.errors['last_name'], ['Ensure this value has at most 150 characters (it has 151).'])
    
    def test_using_empty_last_name(self):
        form = UserForm(data={
            'last_name': ''
        })
        self.assertEqual(form.errors['last_name'], ['This field is required.'])
    
    def test_using_short_mobile(self):
        form = UserProfileForm(data={
            'mobile': '07802805805805'
        })
        self.assertEqual(form.errors['mobile'], ['Invalid Mobile Number'])
    
    def test_using_long_mobile(self):
        form = UserProfileForm(data={
            'mobile': '078023540'
        })
        self.assertEqual(form.errors['mobile'], ['Invalid Mobile Number'])
    
    def test_using_invalid_mobile(self):
        form = UserProfileForm(data={
            'mobile': '11111111111'
        })
        self.assertEqual(form.errors['mobile'], ['Invalid Mobile Number'])
    
    def test_using_empty_mobile(self):
        form = UserProfileForm(data={
            'mobile': ''
        })
        self.assertEqual(form.errors['mobile'], ['This field is required.', 'Invalid Mobile Number'])
    
    def test_using_long_email(self):
        xtra_char = 'x' * 250
        email = 'test@gmail.' + xtra_char
        form = UserForm(data={
            'email': email
        })
        self.assertEqual(form.errors['email'], ['Enter a valid email address.', 'Ensure this value has at most 254 characters (it has 261).'])
    
    def test_using_empty_email(self):
        form = UserForm(data={
            'email': ''
        })
        self.assertEqual(form.errors['email'], ['This field is required.'])
        


        



