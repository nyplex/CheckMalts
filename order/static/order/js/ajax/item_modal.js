import { update_price } from "./update_price"

export let item_modal = (item_id, e) => {
    let token = $('[name=csrfmiddlewaretoken]').val()
    let parent = $(e.target).parent().parent()
    let qty = $('*[data-qty-item]', parent).val()
    let size = $('*[data-size-option]', parent).val()
    let price = $('*[data-price-item]', parent).text()
    $.ajax({
        type: 'POST',
        url: 'order/item-detail',
        data: {
            'item_id': item_id,
            'csrfmiddlewaretoken': token
        },
        success: function (response) {
            let container = $('#itemModalContainer')

            $('#itemModal').replaceWith(response)
            $('#itemModal').show()
            $('#itemModelLoader').hide()
            $('#itemModaBodyContainer').show()
            $('*[data-price-item]', container).text(price)
            $('*[data-size-option]', container).val(size)
            $('*[data-qty-item]', container).val(qty)
            $('#closeItemModal').on('click', (e) => {
                location.reload()
            })
            $('*[data-size-option], *[data-qty-item]').on('change', (e) =>{
                update_price(e)
            })
        }
    })
}





