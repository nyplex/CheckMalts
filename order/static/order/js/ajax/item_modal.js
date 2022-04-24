export let item_modal = (item_id) => {
    let token = $('[name=csrfmiddlewaretoken]').val()
    $.ajax({
        type: 'POST',
        url: 'order/item-detail',
        data: {
            'item_id': item_id,
            'csrfmiddlewaretoken': token
        },
        success: function (response) {
            $('#itemModal').replaceWith(response)
            $('#itemModal').show()
            $('#itemModelLoader').hide()
            $('#itemModaBodyContainer').show()
            // Get the item modal
            var modal = document.getElementById("itemModal");
            var btn = $('*[data-order-item-modal]')
            var span = document.getElementById("closeItemModal");
            // When the user clicks on <span> (x), close the modal
            span.onclick = function() {
            modal.style.display = "none";
            }
            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
            }
        }
    })
}





