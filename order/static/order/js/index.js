import { item_modal } from "./ajax/item_modal";
import { update_price } from "./ajax/update_price";

//Reload the page and pass category value in the URL
$('#category_select_input').on('change', (e) => {
    let value = $('#category_select_input').val()
    window.location = "?category=" + value;
})


//Show and hide the item modal
export let getItemModal = () => {
	let modal = $('#itemModal')
	let btn = $('*[data-toggle-modal]')
	let span = $('#closeItemModal')

	$(btn).on('click', (e) =>{
		let item_id =  $(e.currentTarget).attr('data-order-item-modal')
		item_modal(item_id, e)
		$(modal).show()
	})
	$(window, span).on('click', (e) => {
		if (e.target == modal) {
			$(modal).hide()
		}
	})
}

getItemModal()

$('*[data-size-option], *[data-qty-item]').on('change', (e) =>{
  update_price(e)
})
