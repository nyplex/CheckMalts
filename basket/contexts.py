from decimal import Decimal
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404
from menu.models import Cocktail



def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    print(basket)
    
    for item_id, item_data in basket.items():
        cocktail = get_object_or_404(Cocktail, pk=item_id)
        if 'item' in item_data:
            if 'quantity' in item_data['item']:
                print(cocktail.name + ' ' + str(item_data['item']['quantity']['quantity']) + 'x')
            if 'size' in item_data['item']:
                for size, value in item_data['item']['size'].items():
                    print(cocktail.name + ' ' + str(size) + ', ' + str(value) + 'x')
            if 'items_by_note' in item_data:
                for i in item_data['items_by_note']:
                    if 'size' in i:
                        print(cocktail.name + ' ' + str(i['size']) + ' ' + str(i['quantity']) + 'x => ' + str(i['note']))
                
        elif 'items_by_note' in item_data:
            for i in item_data['items_by_note']:
                if 'size' in i:
                    print(cocktail.name + ' ' + str(i['size']) + ' ' + str(i['quantity']) + 'x => ' + str(i['note']))
                else:
                    print(cocktail.name + ' ' + str(i['quantity']) + 'x => ' + str(i['note']))
        else:
            raise Http404()
    
    context = {
        'basket_items': 'basket_items',
        'total': 1,
        'product_count': 1,
    }

    return context