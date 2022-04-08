from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from datetime import date


class Booking(models.Model):

    BOOKINGTIMEOPTIONS = [
        ('', 'Choose Time'),('1400', '14:00'), ('1430', '14:30'),
        ('1500', '15:00'), ('1530', '15:30'),('1600', '16:30'), 
        ('1630', '16:30'),('1700', '17:00'), ('1730', '17:30'),
        ('1800', '18:00'), ('1830', '18:30'),('1900', '19:00'), 
        ('1930', '19:30'),('2000', '20:00'), ('2030', '20:30'),
        ('2100', '21:00'), ('2130', '21:30'),('2200', '22:00'), 
        ('2230', '22:30')
    ]

    BOOKINGSIZEOPTIONS = [
        ('', 'Choose Size'),('1', '1'), ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), 
        ('8', '8'), ('9', '9'),('10', '10'),
    ]

    booking_email = models.EmailField(null=False, blank=False, max_length=200)

    booking_name = models.CharField(
        null=False, blank=False, max_length=50, validators=[MinLengthValidator(4)])

    booking_date = models.DateField(null=False, blank=False, max_length=50)

    booking_time = models.CharField(
        null=False, blank=False, choices=BOOKINGTIMEOPTIONS, max_length=10)

    booking_size = models.CharField(
        null=False, blank=False, choices=BOOKINGSIZEOPTIONS, max_length=10)

    def clean(self):
        data = self.booking_date
        if data == None:
            return
        if data < date.today():
            raise ValidationError(
                {'booking_date': "Booking date must be in the future."})
    
    def __str__(self):
        return self.booking_name
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        super().save(*args, **kwargs)
