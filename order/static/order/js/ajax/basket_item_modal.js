import { item_modal_behaviour } from "./item_modal"

$('*[data-item]').on('click', (e) => {
    let item_id = $(e.target).data('item-id')
    let qty = $(e.target).data('item-quantity')
    let size = $(e.target).data('item-size')
    let note = $(e.target).data('item-note')
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
            item_modal_behaviour()
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status != 200) {
                location.reload()
                return
            }
        }
    })
})