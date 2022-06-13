from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from match.models import MatchingQuestions


class Cocktail(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, validators=[
                            MinLengthValidator(4)], unique=False)
    friendly_name = models.CharField(
        max_length=50, null=True, blank=True, unique=False, validators=[MinLengthValidator(4)])
    price = models.FloatField(blank=False, null=False, default=0, validators=[
                              MinValueValidator(0), MaxValueValidator(10000)])
    description = models.TextField(blank=True, null=True, max_length=5000)
    out_of_stock = models.BooleanField(null=False, blank=False, default=False)
    prep_time = models.FloatField(null=False, blank=False, validators=[
                                    MinValueValidator(0), MaxValueValidator(1000)])
    image = models.ImageField(
        null=False, blank=True, upload_to='products_images/', default='products_images/default.png')
    ordered = models.IntegerField(null=False, blank=True, default=0)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    has_size = models.BooleanField(null=False, blank=False, default=False)
    sizes = models.ManyToManyField('CocktailsSize', blank=True, null=True)
    allow_match = models.BooleanField(null=False, blank=False, default=False)
    matching_questions = models.ManyToManyField(MatchingQuestions, blank=True, null=True)
    is_mixer = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.friendly_name
    
    def save(self, *args, **kwargs):
        net_price = self.price - (self.price * 0.3)
        self.net_price = net_price
        
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    friendly_name = models.CharField(null=True, blank=True, max_length=50)
    sub_categories = models.ManyToManyField(
        'SubCategory', null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    friendly_name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class CocktailsSize(models.Model):
    SIZESOPTIONS = [('small', '125ml'), ('medium', '175ml'), ('large', '250ml'),
               ('single', 'single'), ('double', 'double'), ('triple', 'triple')]
    
    sizes = models.CharField(choices=SIZESOPTIONS, null=True, blank=True, max_length=10)
    
    def __str__(self):
        return self.sizes