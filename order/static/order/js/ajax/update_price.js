
export let update_price = (e) => {
    let item_id =  $(e.currentTarget).attr('data-order-item-modal')
    let parent = $(e.target).parent().parent().parent().parent()
    let token = $('[name=csrfmiddlewaretoken]').val()
    let qty = 1
    let size
    let mixer = 0
    
    if($('*[data-qty-item]', parent).val()) {
        qty = $('*[data-qty-item]', parent).val()
    }
    if($('*[data-size-option]', parent).val()) {
        size = $('*[data-size-option]', parent).val()
    }
    if($('*[data-mixer-option]', parent).val()) {
        mixer = $('*[data-mixer-option]', parent).val()
    }

    $.ajax({
        type: 'POST',
        url: '/order/size-price',
        data: {
            'item_id': item_id,
            'size': size,
            'quantity': qty,
            'mixer': mixer,
            'csrfmiddlewaretoken': token
        },
        success: function (response) {
            $('*[data-price-item]', parent).text('£' + (Math.round(response.response * 100) / 100).toFixed(2))
            
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status != 200) {
                location.reload()
                return
            }
        }
    })
}

