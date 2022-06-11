from django import template
from menu.models import Cocktail, Category


register = template.Library()

@register.filter(name='soft_drinks')
def soft_drinks(cocktails):
    category = Category.objects.filter(name='soft').first()
    softs = Cocktail.objects.filter(category=category)
    return softs