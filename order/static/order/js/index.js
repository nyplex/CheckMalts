import { item_modal } from "./ajax/item_modal";
import "./ajax/basket_item_modal"

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

//Get the item modal
getItemModal()


// Change the max character span on textarea special note input when user type
export let update_span_counter = () => {
	$("#cocktail_note").on("input", (e) => {
		let len = $(e.target).val().length
		let total = 80 - len
		if(total <= 0) {
			$("#noteCharCompter").text(0)
		}else{
			$("#noteCharCompter").text(total)
		}
		
	})
}


//On the order page when page is ready, open the first sub_category if exists.
$(document).ready((e) => {
	$('.subCategoryCollapse').first().addClass('bg-secondaryColor text-primaryColor').removeClass('text-secondaryColor').next().show()
})
//Subcategory collapsible function
$('.subCategoryCollapse').on('click', (e) => {
	let content = $(e.target).next()
	$(e.target).toggleClass('bg-secondaryColor').toggleClass('text-primaryColor').toggleClass('text-secondaryColor')
	$(content).slideToggle('slow')
})


$('*[data-checkoutButton]').on('click', (e) => {
	console.log('hello world');
	let modal = $('#loginModal')
	$(modal).show()
})
