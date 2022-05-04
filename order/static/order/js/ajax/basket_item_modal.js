import { update_span_counter } from "../"
import { update_price } from "./update_price"



$('*[data-item]').on('click', (e) => {
    let item_id = $(e.target).data('item-id')
    let qty = $(e.target).data('item-quantity')
    let size = $(e.target).data('item-size')
    let note = $(e.target).data('item-note')
    console.log(qty, size, note);
    let token = $('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        type: 'POST',
        url: '/basket/modal/' + item_id,
        data: {
            'item_id': item_id,
            'qty': qty,
            'size': size,
            'note': note,
            'csrfmiddlewaretoken': token
        },
        success: function(response) {
            $('#itemModal').replaceWith(response)
            $('#itemModal').show()
            $('#itemModelLoader').hide()
            $('#itemModaBodyContainer').show()

            $('#closeItemModal').on('click', (e) => {
                $('#itemModal').hide()
            })
            $(window).on('click', (e) => {
                let modal = $('#itemModal')
                if($(modal).attr('id') == $(e.target).attr('id')) {
                    $(modal).hide()
                }
            })
            $('*[data-size-option], *[data-qty-item]').on('change', (e) =>{
                update_price(e)
            })
            update_span_counter()

        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status != 200) {
                location.reload()
                return
            }
        }
    })
})