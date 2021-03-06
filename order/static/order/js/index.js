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
	let textContainer = $('#cocktail_note').val()
	if (textContainer.length > 0 || textContainer.length < 80) {
		let total = 80 - textContainer.length
		$("#noteCharCompter").text(total)
	}else{
		$("#noteCharCompter").text(0)
	}
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


//Subcategory collapsible function
$('.subCategoryCollapse').on('click', (e) => {
	let target = $(e.target)
	let content;
	if (target.is('h3')) {
		content = $(e.target).next()
		$(e.target).children().first().toggleClass('fa-angle-down fa-angle-up')
	}else if (target.is('i')) {
		content = $(e.target).parent().next()
		$(e.target).toggleClass('fa-angle-down fa-angle-up')
	}
	$(content).slideToggle(500)
	
})



//Edit remove btns animation
if ($(window).width() > 768) {
	$('.basketItemContainer').on('mouseover', (e) => {
		$(e.currentTarget).next().animate({'marginRight':'0'},300);
	})
	$('.basketMainItemContainer').on('mouseleave', (e) => {
		$(e.currentTarget).children().next().animate({'marginRight':'-35'},200);
	})
}