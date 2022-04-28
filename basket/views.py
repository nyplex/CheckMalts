from django.shortcuts import redirect, render, get_object_or_404
from menu.models import Cocktail
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    quantity = int(request.POST.get('cocktail_quantity'))
    redirect_url = '/order?category=' + request.POST.get('redirect_url')
    size = None
    note = ''
    
    if 'cocktail_size' in request.POST:
        size = request.POST['cocktail_size']
    if 'cocktail_note' in request.POST:
        note = request.POST['cocktail_note']
    
    basket = request.session.get('basket', {})
    # request.session['basket'] = {}         

    if item_id in list(basket.keys()):
        if note:
            if 'items_by_note' in basket[item_id]:
                if size:
                    basket[item_id]['items_by_note'].append({'note': note, 'quantity': quantity, 'size': size})
                    messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
                else:
                    basket[item_id]['items_by_note'].append({'note': note, 'quantity': quantity})
                    messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
            else:
                if size:
                    basket[item_id].update({'items_by_note': [{'note': note, 'quantity': quantity, 'size': size}]})
                    messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
                else:
                    basket[item_id].update({'items_by_note': [{'note': note, 'quantity': quantity}]})
                    messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
        else:
            if 'item' in basket[item_id]:
                if size:
                    if size in basket[item_id]['item']['size'].keys():
                        basket[item_id]['item']['size'][size] += quantity
                    else:
                        basket[item_id]['item']['size'].update({size: quantity})
                else:
                    basket[item_id]['item']['quantity']['quantity'] += quantity
            else:
                if size:
                    basket[item_id].update({'item': {'size': {size: quantity}}})
                else:
                    basket[item_id].update({'item': {'quantity': {'quantity': quantity}}})
    else:
        if not note:
            if size:
                basket[item_id] = {'item': {'size': {size: quantity}}}
                messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
            else:
                basket[item_id] = {'item': {'quantity': {'quantity': quantity}}}
                messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
        else:
            if size:
                basket[item_id] = {'items_by_note': [{'note': note, 'quantity': quantity, 'size': size}]}
                messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')
            else:
                basket[item_id] = {'items_by_note': [{'note': note, 'quantity': quantity}]}
                messages.success(request, f'Added {quantity} `{cocktail.name.upper()}` to your bag', extra_tags='alert')

    request.session['basket'] = basket
    return HttpResponseRedirect(redirect_url)