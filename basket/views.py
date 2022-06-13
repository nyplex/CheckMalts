from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from django.middleware import csrf
from django.conf import settings

from order.views import calculate_price_by_size, format_add_basket
from menu.models import Category, Cocktail

import re


def add_to_basket(request, item_id):
    """ 
    This view is called from the modal
    form to add product to basket 
    """
    
    # Check if store is open
    if settings.OPEN == False:
        return redirect('order')
    
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    quantity = request.POST.get('cocktail_quantity').replace(' ', '')
    mixer_id = None

    if request.POST.get('redirect_url') == 'match_result':
        redirect_url = '/cocktail-match/result'
    else:
        redirect_url = '/order?category=' + request.POST.get('redirect_url')
    
    #Validate quantity 
    if not quantity or quantity == '' or int(quantity) <= 0:
        raise Http404
    if not re.match(r'^([\s\d]+)$', quantity):
        raise Http404
    
    size = None
    note = ''
    quantity = int(quantity)

    #Validate size and note
    if 'cocktail_size' in request.POST:
        if cocktail.has_size == False:
            raise Http404
        size = request.POST['cocktail_size']
    if 'cocktail_note' in request.POST:
        note = request.POST['cocktail_note']
        if len(note) > 80:
            messages.error(
                request, f'Special note must between 0 and 80 characters', extra_tags='alert')
            return HttpResponseRedirect(redirect_url)

    #Add spirit & mixer to bakset
    if request.POST.get('cocktail_mixer'):
        try:
            mixer_id = int(request.POST.get('cocktail_mixer'))
            soft_category = Category.objects.get(name='soft')
            mixer = Cocktail.objects.get(pk=mixer_id, category=soft_category)

            basket = request.session.get('basket', {})
            basket = format_add_basket(mixer.id, basket, None, note, quantity)
            request.session['basket'] = basket

        except:
            messages.error(
                request, f'Oups! Error 505. Try again!', extra_tags='alert')
            return HttpResponseRedirect(redirect_url)

    basket = request.session.get('basket', {})
    basket = format_add_basket(item_id, basket, size, note, quantity)
    request.session['basket'] = basket

    messages.success(
        request, f'Added {quantity} `{cocktail.friendly_name.upper()}` to your bag', extra_tags='alert')
    return HttpResponseRedirect(redirect_url)


def update_basket(request, item_id):
    """ 
    This view is called from the basket modal
    form to update product in basket 
    """
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    qty = request.POST.get('cocktail_quantity').replace(' ', '')
    original_qty = request.POST.get('original_qty').replace(' ', '')

    basket = request.session.get('basket', {})
    size = None
    original_size = None
    note = None
    original_note = None

    if request.POST.get('redirect_url') == 'match_result':
        redirect_url = '/cocktail-match/result'
    else:
        redirect_url = '/order?category=' + request.POST.get('redirect_url')

    if not qty or not original_qty:
        return JsonResponse({}, status=500)
    if qty == '' or original_qty == '':
        return JsonResponse({}, status=500)
    if not re.match(r'^([\s\d]+)$', qty) or not re.match(r'^([\s\d]+)$', original_qty):
        return JsonResponse({}, status=500)
    if int(qty) <= 0 or int(original_qty) <= 0:
        return JsonResponse({}, status=500)
    qty = int(qty)
    original_qty = int(original_qty)

    if basket == {} or basket is None:
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
        basket = format_remove_from_basket(
            item_id, basket, original_size, original_note, original_qty)
        basket = format_add_basket(item_id, basket, size, note, qty)
    else:
        raise Http404

    request.session['basket'] = basket
    messages.success(
        request, f'Added {qty} `{cocktail.friendly_name.upper()}` to your bag', extra_tags='alert')
    return HttpResponseRedirect(redirect_url)


def item_modal(request, item_id):
    """ 
    This view is called from fetch data 
    to the Ajax call for the order item modal 
    """
    
    cocktail = get_object_or_404(Cocktail, pk=request.POST.get('item_id'))
    net_price = cocktail.price - (cocktail.price * 0.3)
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
        response['price'] = round(calculate_price_by_size(
            cocktail.price, net_price, size) * int(qty), 2)
        response['size'] = size
    if note:
        response['note'] = note

    html = render_to_string(
        'order/includes/item_modal.html', {'response': response, 'csrf_token': csrf.get_token(request)})
    return HttpResponse(html)


def remove_from_basket(request, item_id):
    """ 
    This view is called from the basket modal
    form to remove product from basket 
    """
    cocktail = get_object_or_404(Cocktail, pk=item_id)
    basket = request.session.get('basket')
    quantity = request.POST.get('item_quantity').replace(' ', '')
    size = None
    note = None

    if basket == {} or basket == None:
        raise Http404
    if 'item_size' in request.POST:
        size = request.POST.get('item_size')
    if 'item_note' in request.POST:
        note = request.POST.get('item_note')
    if not quantity:
        raise Http404
    if quantity == '':
        raise Http404
    if not re.match(r'^([\s\d]+)$', quantity):
        raise Http404
    if int(quantity) <= 0:
        raise Http404

    quantity = int(quantity)

    if item_id in list(basket.keys()):
        basket = format_remove_from_basket(
            item_id, basket, size, note, quantity)
    else:
        messages.error(request, f'Error removing item', extra_tags='alert')

    request.session['basket'] = basket

    if request.session['basket'] == {}:
        messages.warning(request, f'Your basket is empty!', extra_tags='alert')
        return redirect('order')

    messages.warning(
        request, f'Removed {quantity}x `{cocktail.friendly_name}`', extra_tags='alert')
    return redirect('order')


def format_remove_from_basket(item_id=None, 
                              basket=None, size=None, 
                              note=None, quantity=None):
    """ 
    This method is called to format the items
    into the session's basket 
    """
    
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
