from django import template
import random
import string


register = template.Library()

@register.filter(name='random_letter')
def random_letter(letter):
    random_letter = random.choice(string.ascii_lowercase).capitalize()
    return f'Does your name contains the letter "{random_letter}" ?'