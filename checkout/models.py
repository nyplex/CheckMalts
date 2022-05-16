from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from profiles.models import UserProfile
from menu.models import Cocktail
from datetime import date
import uuid


class Order(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=False, related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False, validators=[
                                      MinValueValidator(0), MaxValueValidator(99999.99)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False, validators=[
                                   MinValueValidator(0), MaxValueValidator(99999.99)])
    serivce_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False, validators=[
                                         MinValueValidator(0), MaxValueValidator(99999.99)])
    table_number = models.IntegerField(null=True, default=0, blank=True, validators=[
                                       MinValueValidator(0), MaxValueValidator(9999)])
    is_done = models.BooleanField(
        'Order done?', blank=False, null=False, default=False)
    is_paid = models.BooleanField(
        'Order paid?', blank=False, null=False, default=False)
    is_cancelled = models.BooleanField(
        'Order cancelled?', blank=False, null=False, default=False)
    is_pending = models.BooleanField(
        'Order pending?', blank=False, null=False, default=True)
    date = models.DateTimeField(auto_now_add=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=True, blank=True, default='')
    
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.id}'


class OrderLine(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    cocktail = models.ForeignKey(
        Cocktail, null=False, blank=False, on_delete=models.CASCADE)
    cocktail_size = models.CharField(max_length=10, null=True, blank=True)
    note = models.TextField(blank=True, null=True, default='', max_length=10000)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

