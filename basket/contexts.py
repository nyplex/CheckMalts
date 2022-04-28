from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Cocktail



def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    print(basket)
    
    context = {
        'basket_items': 'basket_items',
        'total': 1,
        'product_count': 1,
    }

    return context