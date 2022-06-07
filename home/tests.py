from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib import auth
from .forms import BookingForm
from .models import Booking
from http import HTTPStatus
from django.contrib.messages import get_messages
from django.core import mail

class HomeView(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertContains(response, '<canvas id="jagerCanvas"></canvas>')
        self.assertContains(
            response, '<div class="w-full home_illustration_1 min-h-[250px]"></div>')
        self.assertContains(
            response, '<div class="carousel__body">')


class MakeReservationTests(TestCase):
    def test_post_success(self):
        data = {
            'booking_email': 'user@test.com',
            'booking_name': 'John Doe',
            'booking_date': '16/04/2030',
            'booking_time': '1600',
            'booking_size': '5'
            }
        response = self.client.post('', data=data)
        
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = [msg for msg in get_messages(response.wsgi_request)]
        self.assertEqual(str(messages[0]), 'We\'ve got your booking! Check your email for the confirmation.')

        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.filter(pk=1).get()
        self.assertEqual(booking.booking_name, 'John Doe')
        self.assertEqual(len(mail.outbox), 1)
    
    def test_post_error(self):
        data = {
            'booking_email': 'user@test.com',
            'booking_name': '',
            'booking_date': '16/04/2020',
            'booking_time': '1600',
            'booking_size': '5'
            }
        response = self.client.post('/booking', data=data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), 'We found an error in the form!')


class ReservationForm(TestCase):
    def test_using_invalid_email(self):
        form = BookingForm(data={
            'booking_email': 'test@test.'
        })
        self.assertEqual(form.errors['booking_email'], ['Enter a valid email address.'])
        
    def test_using_empty_email(self):
        form = BookingForm(data={
            'booking_email': ''
        })
        self.assertEqual(form.errors['booking_email'], ['This field is required.'])
    
    def test_using_short_name(self):
        form = BookingForm(data={
            'booking_name': 't'
        })
        self.assertEqual(form.errors['booking_name'], ['Ensure this value has at least 4 characters (it has 1).'])
    
    def test_using_long_name(self):
        form = BookingForm(data={
            'booking_name': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        })
        self.assertEqual(form.errors['booking_name'], ['Ensure this value has at most 50 characters (it has 51).'])
    
    def test_using_empty_name(self):
        form = BookingForm(data={
            'booking_name': ''
        })
        self.assertEqual(form.errors['booking_name'], ['This field is required.'])
    
    def test_using_past_date(self):
        form = BookingForm(data={
            'booking_date': '05/04/2021'
        })
        self.assertEqual(form.errors['booking_date'], ['Booking date must be in the future.'])
    
    def test_using_invalid_date(self):
        form = BookingForm(data={
            'booking_date': '09/16/2025'
        })
        self.assertEqual(form.errors['booking_date'], ['Enter a valid date.'])
    
    def test_using_empty_date(self):
        form = BookingForm(data={
            'booking_date': ''
        })
        self.assertEqual(form.errors['booking_date'], ['This field is required.'])
    
    def test_using_invalid_time(self):
        form = BookingForm(data={
            'booking_time': '1300'
        })
        self.assertEqual(form.errors['booking_time'], ['Select a valid choice. 1300 is not one of the available choices.'])
    
    def test_using_empty_time(self):
        form = BookingForm(data={
            'booking_time': ''
        })
        self.assertEqual(form.errors['booking_time'], ['This field is required.'])
    
    def test_using_invalid_size(self):
        form = BookingForm(data={
            'booking_size': '55'
        })
        self.assertEqual(form.errors['booking_size'], ['Select a valid choice. 55 is not one of the available choices.'])
    
    def test_using_empty_size(self):
        form = BookingForm(data={
            'booking_size': ''
        })
        self.assertEqual(form.errors['booking_size'], ['This field is required.'])

class NavbarView(TestCase):
    def test_navbar_logged_out(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response, '<a href="/cocktail-match/" class="navbar-link">MATCH</a>')
    


    
    
