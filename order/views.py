from tabnanny import check
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from requests import Response
from menu.models import *
from checkout.models import Order, OrderLine
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.middleware import csrf
from django.conf import settings



def order(request):
    """ A view to render the order page """
    
    if request.session.get('checkout_session'):
        del request.session['checkout_session']

    categories = Category.objects.all()
    
    if request.GET.get('category') is None:
        category = 1
    elif not Category.objects.filter(pk=request.GET.get('category')).exists():
        raise Http404
    else:
        category = int(request.GET.get('category'))

    cocktails = Cocktail.objects.filter(category=category, out_of_stock=False)
    sub_categories = SubCategory.objects.filter(category__id=category)

    context = {
        'open': settings.OPEN,
        'categories': categories,
        'sub_categories': sub_categories,
        'cocktails': cocktails,
        'selected': category
    }
    return render(request, 'order/order.html', context)


def item_detail(request):
    """ A view to return the item modal from the Ajax call """

    if request.method == "POST":
        try:
            cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
        except Cocktail.DoesNotExist:
            return JsonResponse({}, status=404)
    
    if request.POST['match_modal'] == 'true':
        match = True
    else:
        match = False
        
    html = render_to_string(
        'order/includes/item_modal.html', {'cocktail': cocktail, 'csrf_token': csrf.get_token(request), 'match': match})
    return HttpResponse(html)


def calculate_size_price(request):
    """ A view that return the updated price of a item 
        to the ajax call depending of its size & qty """

    if request.method == "POST":
        try:
            cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
        except Cocktail.DoesNotExist:
            return JsonResponse({}, status=404)
        
        net_price = cocktail.price - (cocktail.price * 0.3) 
        price = cocktail.price

        if cocktail.has_size == True:
            if(request.POST['size']
               and request.POST['size']
               in ['small', 'medium', 'large', 'single', 'double', 'triple']):

                size = request.POST['size']
                price = calculate_price_by_size(price, net_price, size)
                
            else:
                return JsonResponse({}, status=404)

        if request.POST['quantity']:
            if int(request.POST['quantity']) <= 0 or int(request.POST['quantity']) > 10:
                return JsonResponse({}, status=404)
            qty = int(request.POST['quantity'])
        else:
            qty = 1

        price = round(price * qty, 1)

        if request.POST['mixer']:
            if (int(request.POST['mixer'])) != 0:
                try:
                    mixer = Cocktail.objects.get(pk=request.POST['mixer'])
                except Cocktail.DoesNotExist:
                    return JsonResponse({}, status=404)
                if mixer.category.name != 'soft':
                    return JsonResponse({}, status=404)
                price += mixer.price
        
        return JsonResponse({"response": price}, status=200)
    


def calculate_price_by_size(price, net_price, size):
    diff = price - net_price
    match size:
        case 'small' | 'single':
            price = price
        case 'medium':
            price = price = round(
                (((net_price * 2) / 3) * 2) + diff, 1)
        case 'large':
            price = round((net_price * 2) + diff, 1)
        case 'double':
            price = round(price * 2, 1)
        case 'triple':
            price = round(price * 3, 1)
        case _:
            raise Http404
    
    return price


def order_again(request, order_id):
    try:
        order = Order.objects.get(pk=int(order_id))
        line_order = order.lineitems.all()
        for i in line_order:
            if i.note == None or i.note == '':
                note = None
            else:
                note = i.note
            
            if i.cocktail_size == None or i.cocktail_size == '':
                cocktail_size = None
            else:
                cocktail_size = i.size

            quantity = int(i.quantity)
            if request.session['basket']:
                del request.session['basket']
            basket = request.session.get('basket', {})
            basket = format_add_basket(i.cocktail.id, basket, cocktail_size, note, quantity)
            request.session['basket'] = basket
        return redirect('checkout_1')
    except:
        return redirect('my_orders')
    


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