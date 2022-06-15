import { update_span_counter } from ".."
import { update_price } from "./update_price"

//Open item modal to add item to basket
export let item_modal = (item_id, e) => {
    let parent = $(e.target).parent().parent()
    let qty = $('*[data-qty-item]', parent).val()
    let size = $('*[data-size-option]', parent).val()
    let price = $('*[data-price-item]', parent).text()
    let token = $('[name=csrfmiddlewaretoken]').val()

    $.ajax({
        type: 'POST',
        url: '/order/item-detail',
        data: {
            'item_id': item_id,
            'csrfmiddlewaretoken': token,
            'match_modal': matchModal
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
            item_modal_behaviour()

        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status != 200) {
                location.reload()
                return
            }
        }
    })
}

//Define modal's behavior
export let item_modal_behaviour = () => {
    //Listen to close the modal
    $('#closeItemModal').on('click', (e) => {
        $('#itemModal').hide()
    })
    $(window).on('click', (e) => {
        let modal = $('#itemModal')
        if($(modal).attr('id') == $(e.target).attr('id')) {
            $(modal).hide()
        }
    })

    //Listen add + item
    $('#plusQty').on('click', (e) => {
        let currentQty = parseInt($('#modalQty').text())
        let newQty = currentQty + 1
        if (newQty >= 10) {
            newQty = 10
        }else if (newQty <= 0) {
            newQty = 1
        }
        $('#modalQty').text(newQty)
        $('#formItemQty').val(newQty)
        $('#formItemQty').change();
        
    })

    //Listen minus - item
    $('#minusQty').on('click', (e) => {
        let currentQty = parseInt($('#modalQty').text())
        let newQty = currentQty - 1
        if (newQty >= 10) {
            newQty = 10
        }else if (newQty <= 0) {
            newQty = 1
        }
        $('#modalQty').text(newQty)
        $('#formItemQty').val(newQty)
        $('#formItemQty').change();
        
    })

    //Listen size, qty & mixer change to update price
    $('*[data-size-option], *[data-qty-item], *[data-mixer-option]').on('change', (e) =>{
        update_price(e)
    })

    //Listen for special request and handle animation
    $('#requestBtn').on('click', (e) => {
		$('#requestBtn').slideToggle('slow')
		$('#requestTextAreaContainer').slideToggle('slow')
	})

    //Listen for input on request 
    update_span_counter()
}