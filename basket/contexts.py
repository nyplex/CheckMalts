



def basket_contents(request):
    context = {
        'basket_item': ['bag_items'],
        'basket_product_count': 5,
    }

    return context