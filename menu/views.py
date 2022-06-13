from django.shortcuts import render
from .models import *




def menu(request, product_id=None):
    """ A view to return the menu page & product details modal """

    cocktails = Cocktail.objects.all().order_by('category')
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()

    context = {
        'cocktails': cocktails,
        'categories': categories,
        'subCategories': subCategories
    }
    
    return render(request, 'menu/menu.html', context)