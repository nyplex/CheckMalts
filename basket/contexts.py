from cmath import log
from decimal import Decimal
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404
from menu.models import Cocktail
from order.views import calculate_price_by_size



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
                product_count += item_data['item']['quantity']['quantity']
                total += item_data['item']['quantity']['quantity'] * cocktail.price
                basket_items.append({
                    'item_id': item_id,
                    'quantity': item_data['item']['quantity']['quantity'],
                    'cocktail': cocktail,
                    'sub_total': item_data['item']['quantity']['quantity'] * cocktail.price
                })
            if 'size' in item_data['item']:
                for size, value in item_data['item']['size'].items():
                    product_count += value
                    price = calculate_price_by_size(cocktail.price, cocktail.net_price, size)
                    total += price * value
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': value,
                        'size': size,
                        'cocktail': cocktail,
                        'sub_total': price * value
                    })

                
        if 'items_by_note' in item_data:
            for i in item_data['items_by_note']:
                if 'size' in i:
                    product_count += i['quantity']
                    price = calculate_price_by_size(cocktail.price, cocktail.net_price, i['size'])
                    total += price * i['quantity']
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': i['quantity'],
                        'size': i['size'],
                        'note': i['note'],
                        'cocktail': cocktail,
                        'sub_total': price * i['quantity']
                    })
                else:
                    product_count += i['quantity']
                    total += cocktail.price * i['quantity']
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': i['quantity'],
                        'note': i['note'],
                        'cocktail': cocktail,
                        'sub_total': cocktail.price * i['quantity']
                    })
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }
    return context