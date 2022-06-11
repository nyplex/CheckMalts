from cmath import log
from decimal import Decimal
from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404
from menu.models import Cocktail
from django.forms.models import model_to_dict
from order.views import calculate_price_by_size



def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    
    for item_id, item_data in basket.items():
        cocktail = get_object_or_404(Cocktail, pk=item_id)
        net_price = cocktail.price - (cocktail.price * 0.3)

        if 'item' in item_data:
            if 'quantity' in item_data['item']:
                product_count += item_data['item']['quantity']['quantity']
                total += item_data['item']['quantity']['quantity'] * cocktail.price
                basket_items.append({
                    'item_id': item_id,
                    'quantity': item_data['item']['quantity']['quantity'],
                    'cocktail': model_to_dict(cocktail),
                    'sub_total': item_data['item']['quantity']['quantity'] * cocktail.price
                })
            if 'size' in item_data['item']:
                for size, value in item_data['item']['size'].items():
                    product_count += value
                    price = calculate_price_by_size(cocktail.price, net_price, size)
                    total += price * value
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': value,
                        'size': size,
                        'cocktail': model_to_dict(cocktail),
                        'sub_total': price * value
                    })
                
        if 'items_by_note' in item_data:
            for i in item_data['items_by_note']:
                if 'size' in i:
                    product_count += i['quantity']
                    price = calculate_price_by_size(cocktail.price, net_price, i['size'])
                    total += price * i['quantity']
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': i['quantity'],
                        'size': i['size'],
                        'note': i['note'],
                        'cocktail': model_to_dict(cocktail),
                        'sub_total': price * i['quantity']
                    })
                else:
                    product_count += i['quantity']
                    total += cocktail.price * i['quantity']
                    basket_items.append({
                        'item_id': item_id,
                        'quantity': i['quantity'],
                        'note': i['note'],
                        'cocktail': model_to_dict(cocktail),
                        'sub_total': cocktail.price * i['quantity']
                    })
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'tips': 0,
        'grandTotal': total
    }
    
    if request.session.get('checkout_session'):
        checkout_session = request.session.get('checkout_session')
        if checkout_session['tips'] and checkout_session['tips'] != 0:
            context['tips'] = float(checkout_session['tips'])
            context['grandTotal'] = float(checkout_session['tips']) + total
    
    return context