import { item_modal } from "./ajax/item_modal";

//Reload the page and pass category value in the URL
$('#category_select_input').on('change', (e) => {
    let value = $('#category_select_input').val()
    window.location = "?category=" + value;
})


//change border color on item when ser hover it
$('.cocktail-name').on('mouseover', (e) => {
    let parent = $(e.target).parent()
    let grand_parent = $(parent).parent()

    $(grand_parent).css({'border-color': '#C27803'})
    $(parent).css('color', '#C27803')
})

//change border color on item when ser hover it
$('.cocktail-name').on('mouseleave', (e) => {
    let parent = $(e.target).parent()
    let grand_parent = $(parent).parent()

    $(grand_parent).css('border-color', 'white')
    $(parent).css('color', 'white')
})


// Get the item modal
var modal = document.getElementById("itemModal");
var btn = $('*[data-order-item-modal]')
var span = document.getElementById("closeItemModal");

//Open modal when user click on item
$(btn).on('click', (e) =>{
    let item_id =  $(e.currentTarget).attr('data-order-item-modal')
    item_modal(item_id)
    modal.style.display = "block";
})
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