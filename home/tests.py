from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth


class TestHome(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
    
    
    def test_navbar_logged_out(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<a href="#" class="navbar-link">CREATE</a>')
        