from django.db import models
from django.core.validators import MinLengthValidator, validate_slug, MinValueValidator, MaxValueValidator
from match.models import MatchingQuestions

# Create your models here.


class Ingredient(models.Model):

    UNITCHOICES = [('cl', 'cl'), ('unit', 'unit')]

    CATEGORYCHOICES = [('gin', 'Gin'), ('rum', 'Rum'), ('vodka', 'Vodka'), ('soft', 'Soft drink'), ('garnish', 'Garnish'),
                       ('tequila', 'Tequila'), ('whiskey', 'Whiskey'), ('liqueur',
                                                                        'Liqueur'), ('brandy', 'Brandy'), ('wine', 'Wine'),
                       ('beer', 'Beer')]

    name = models.CharField(null=False, blank=False, unique=True,
                            max_length=100, validators=[MinLengthValidator(3)])

    friendly_name = models.CharField(
        null=True, blank=True, unique=True, max_length=100, validators=[MinLengthValidator(3)])

    out_of_stock = models.BooleanField(null=False, blank=True, default=False)
    unit = models.CharField(null=False, blank=False,
                            default='cl', max_length=10, choices=UNITCHOICES)

    price_per_unit = models.FloatField(null=False, blank=False, validators=[
                                       MinValueValidator(0), MaxValueValidator(10000)])
    allowed_for_creation = models.BooleanField(
        null=False, blank=True, default=False)
    has_alcohol = models.BooleanField(null=False, blank=True, default=False)
    alcohol_volume = models.FloatField(null=True, blank=True, validators=[
                                       MinValueValidator(0), MaxValueValidator(1000)], default=0)
    category = models.CharField(
        null=True, blank=False, choices=CATEGORYCHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, validators=[
                            MinLengthValidator(4)], unique=True)
    friendly_name = models.CharField(
        max_length=50, null=True, blank=True, unique=True, validators=[MinLengthValidator(4)])
    slug = models.SlugField(max_length=100, null=False,
                            unique=True, validators=[validate_slug])
    price = models.FloatField(blank=False, null=False, default=0, validators=[
                              MinValueValidator(0), MaxValueValidator(10000)])
    net_price = models.FloatField(blank=True, null=True, validators=[
                              MinValueValidator(0), MaxValueValidator(10000)])
    description = models.TextField(blank=True, null=True, max_length=5000)
    ingredients = models.ManyToManyField(Ingredient, through='Recipe')
    out_of_stock = models.BooleanField(null=False, blank=False, default=False)
    has_alcohol = models.BooleanField(null=False, blank=False, default=False)
    prep_time = models.FloatField(null=False, blank=False, validators=[
                                    MinValueValidator(0), MaxValueValidator(1000)])
    image = models.ImageField(
        null=False, blank=True, upload_to='products_images/', default='products_images/default.png')
    rating = models.FloatField(null=True, blank=True, validators=[
                               MaxValueValidator(5), MinValueValidator(0)])
    ordered = models.IntegerField(null=False, blank=True, default=0)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    has_size = models.BooleanField(null=False, blank=False, default=False)
    sizes = models.ManyToManyField('CocktailsSize', blank=True, null=True)
    allow_match = models.BooleanField(null=False, blank=False, default=False)
    matching_questions = models.ManyToManyField(MatchingQuestions, blank=True, null=True)

    def __str__(self):
        return self.friendly_name

    def recipe(self):
        return Recipe.objects.filter(cocktail=self)
    
    def save(self, *args, **kwargs):
        recipe = Recipe.objects.filter(cocktail=self.id)
        net_price = 0
        
        for r in recipe:
            net_price += r.ingredient.price_per_unit * r.quantity

        self.net_price = net_price
        
        super().save(*args, **kwargs)


class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False, null=False, validators=[
                                 MinValueValidator(0.1), MaxValueValidator(1000)])

    class Meta:
        unique_together = [['ingredient', 'cocktail']]

    def __str__(self):
        return f'{self.ingredient.name}({self.quantity}{self.ingredient.unit})'


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