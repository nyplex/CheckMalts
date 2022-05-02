from django.shortcuts import redirect, render, get_object_or_404
from menu.models import Cocktail
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.middleware import csrf

from order.views import calculate_price_by_size

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    
    basket = request.session.get('basket')
    if basket == {}:
        return redirect('order')
    
    context = {
        'open': True,
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):

    cocktail = get_object_or_404(Cocktail, pk=item_id)
    quantity = int(request.POST.get('cocktail_quantity'))
    redirect_url = '/order?category=' + request.POST.get('redirect_url')
    size = None
    note = ''

    if 'cocktail_size' in request.POST:
        if cocktail.has_size == False:
            raise Http404()
        size = request.POST['cocktail_size']
    if 'cocktail_note' in request.POST:
        note = request.POST['cocktail_note']
        if len(note) > 80:
            messages.error(request, f'Special note must between 0 and 80 characters', extra_tags='alert')
            return HttpResponseRedirect(redirect_url)
            

    basket = request.session.get('basket', {})
    basket = format_add_basket(item_id, basket, size, note, quantity)
    request.session['basket'] = basket
    
    messages.success(request, f'Added {quantity} `{cocktail.friendly_name.upper()}` to your bag', extra_tags='alert')
    return HttpResponseRedirect(redirect_url)


def format_add_basket(item_id=None, basket=None, size=None, note=None, quantity=None):
    if item_id in list(basket.keys()):
        if note:
            if 'items_by_note' in basket[item_id]:
                if size:
                    basket[item_id]['items_by_note'].append(
                        {'note': note, 'quantity': quantity, 'size': size})
                else:
                    basket[item_id]['items_by_note'].append(
                        {'note': note, 'quantity': quantity})
            else:
                if size:
                    basket[item_id].update(
                        {'items_by_note': [{'note': note, 'quantity': quantity, 'size': size}]})
                else:
                    basket[item_id].update(
                        {'items_by_note': [{'note': note, 'quantity': quantity}]})
        else:
            if 'item' in basket[item_id]:
                if size:
                    if size in basket[item_id]['item']['size'].keys():
                        basket[item_id]['item']['size'][size] += quantity
                    else:
                        basket[item_id]['item']['size'].update(
                            {size: quantity})
                else:
                    basket[item_id]['item']['quantity']['quantity'] += quantity
            else:
                if size:
                    basket[item_id].update(
                        {'item': {'size': {size: quantity}}})
                else:
                    basket[item_id].update(
                        {'item': {'quantity': {'quantity': quantity}}})
    else:
        if not note:
            if size:
                basket[item_id] = {'item': {'size': {size: quantity}}}
            else:
                basket[item_id] = {
                    'item': {'quantity': {'quantity': quantity}}}
        else:
            if size:
                basket[item_id] = {'items_by_note': [
                    {'note': note, 'quantity': quantity, 'size': size}]}
            else:
                basket[item_id] = {'items_by_note': [
                    {'note': note, 'quantity': quantity}]}
    
    return basket


def update_basket(request, item_id):
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    qty = int(request.POST.get('cocktail_quantity'))
    original_qty = int(request.POST.get('original_qty'))
    
    basket = request.session.get('basket', {})
    size = None
    original_size = None
    note = None
    original_note = None
    
    if basket == {} or basket is None:
        return JsonResponse({}, status=500)
    if not qty or not original_qty:
        return JsonResponse({}, status=500)
        
    if 'original_note' in request.POST:
        original_note = request.POST['original_note']
    if 'original_size' in request.POST:
        original_size = request.POST['original_size']
    if 'cocktail_note' in request.POST:
        note = request.POST['cocktail_note']
    if 'cocktail_size' in request.POST:
        size = request.POST['cocktail_size']
    if item_id in list(basket.keys()):           
        basket = format_remove_from_basket(item_id, basket, original_size, original_note, original_qty)
        basket = format_add_basket(item_id, basket, size, note, qty)
    else:
        raise Http404
    
    request.session['basket'] = basket
    messages.success(request, f'Added {qty} `{cocktail.friendly_name.upper()}` to your bag', extra_tags='alert')
    return redirect('basket')

def item_modal(request, item_id):
    cocktail = get_object_or_404(Cocktail, pk=request.POST.get('item_id'))
    qty = request.POST.get('qty')
    size = request.POST.get('size')
    note = request.POST.get('note')
    
    if not qty:
        return JsonResponse({}, status=500)
    
    response = {
        'cocktail': cocktail,
        'qty': int(qty),
    }
    
    if not size:
        response['price'] = round(cocktail.price * int(qty), 2)
    
    if size:
        response['price'] = round(calculate_price_by_size(cocktail.price, cocktail.net_price, size) * int(qty), 2)
        response['size'] = size
    
    if note:
        response['note'] = note
    
    html = render_to_string(
        'order/includes/item_modal.html', {'response': response, 'csrf_token': csrf.get_token(request)})
    
    return HttpResponse(html)


def remove_from_basket(request, item_id):
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    basket = request.session.get('basket')
    size = None
    note = None
    
    if basket == {}:
        raise Http404
    if 'item_size' in request.POST:
        size = request.POST.get('item_size')
    if 'item_note' in request.POST:
        note = request.POST.get('item_note')
    if not 'item_quantity' in request.POST:
        raise Http404
    else:
        quantity = request.POST.get('item_quantity')
    
    if item_id in list(basket.keys()):
        basket = format_remove_from_basket(item_id, basket, size, note, quantity)
    else:
        messages.error(request, f'Error removing item', extra_tags='alert')
    
    
    request.session['basket'] = basket
    
    if request.session['basket'] == {}:
        messages.warning(request, f'Your basket is empty!', extra_tags='alert')
        return redirect('order')
    
    messages.warning(request, f'Removed {quantity}x `{cocktail.friendly_name}`', extra_tags='alert')
    return redirect('basket')


def format_remove_from_basket(item_id=None, basket=None, size=None, note=None, quantity=None):
    if note:
        if size:
            for i in basket[item_id]['items_by_note']:
                if i['note'] == note and int(i['quantity']) == int(quantity) and i['size'] == size:
                    basket[item_id]['items_by_note'].remove(i)
                else:
                    continue
            if basket[item_id]['items_by_note'] == []:
                basket[item_id].pop('items_by_note')
        else:
            for i in basket[item_id]['items_by_note']:
                if i['note'] == note and int(i['quantity']) == int(quantity):
                    basket[item_id]['items_by_note'].remove(i)
                else:
                    continue
            if basket[item_id]['items_by_note'] == []:
                basket[item_id].pop('items_by_note')
    else:
        if size:
            if size in list(basket[item_id]['item']['size']):
                basket[item_id]['item']['size'].pop(size)
            if basket[item_id]['item']['size'] == {}:
                basket[item_id]['item'].pop('size')
        else:
            if int(quantity) == int(basket[item_id]['item']['quantity']['quantity']):
                basket[item_id]['item']['quantity'].pop('quantity')
                if basket[item_id]['item']['quantity'] == {}:
                    basket[item_id]['item'].pop('quantity')

        if basket[item_id]['item'] == {}:
            basket[item_id].pop('item')
    if basket[item_id] == {}:
        basket.pop(item_id)
        
    return basket