from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from profiles.models import UserProfile
from datetime import date


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=False, related_name='orders')
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False)
    vat_amount = models.FloatField(null=False, default=0, blank=False)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False)
    service_percantage = models.IntegerField(null=False, default=0, blank=False)
    serivce_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0, blank=False)
    table_number = models.IntegerField(null=True, default=0, blank=True)
    is_done = models.BooleanField('Order done?', blank=False, null=False, default=False)
    is_paid = models.BooleanField('Order paid?', blank=False, null=False, default=False)
    is_cancelled = models.BooleanField('Order cancelled?', blank=False, null=False, default=False)
    date = models.DateTimeField(auto_now_add=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')