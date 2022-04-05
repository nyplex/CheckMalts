from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth


class TestHome(TestCase):
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
        self.assertContains(
            response, '<input type="text" name="booking_email" class="primary-input mb-4" placeholder="john.doe@gmain.com" maxlength="250" required id="id_booking_email">')


class TestNavbar(TestCase):
    def test_navbar_logged_out(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response, '<a href="#" class="navbar-link">CREATE</a>')
