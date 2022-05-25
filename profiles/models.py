from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
import phonenumbers
import re



class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.email

    
    def clean(self):
        try:
            mobileNumber = self.mobile.replace(' ', '')
            phone_number = phonenumbers.parse(mobileNumber, "GB")
        except:
            raise ValidationError(
                {'mobile': "Invalid Mobile Number"})
    
        if not re.match(r'^\d+$', mobileNumber):
            raise ValidationError(
                {'mobile': "Invalid Mobile Number"})
        if not phonenumbers.is_possible_number(phone_number):
            raise ValidationError(
                {'mobile': "Invalid Mobile Number"})
        if len(self.mobile) < 11:
            raise ValidationError(
                {'mobile': "Invalid Mobile Number"})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()