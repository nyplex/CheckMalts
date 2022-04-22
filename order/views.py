from django.shortcuts import render
from django.contrib import messages
from menu.models import *

# Create your views here.


def order(request):
    
    categories = Category.objects.all()
    
    if not Category.objects.filter(pk=request.GET.get('category')).exists() or request.GET.get('category') is None :
        category = 1
    else:
        category = int(request.GET.get('category'))

    cocktails = Cocktail.objects.filter(category=category)
    sub_categories = SubCategory.objects.filter(category__id=category)

    context = {
        'open': True,
        'categories': categories,
        'sub_categories': sub_categories,
        'cocktails': cocktails,
        'selected': category
    }
        
    return render(request, 'order/order.html', context)
