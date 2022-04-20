import './animation.js'

// prevent user to scroll while the page is loading
$('body').css('overflow-y', 'hidden')

// hide the loader icon and active scrolling when the page is loaded
window.onload = function () {
    if(localStorage.getItem('bookingFormSubmited')) {
        //If booking form has been submited, scrolldown to the form
        localStorage.removeItem('bookingFormSubmited');
        document.getElementById('reservationContainer').scrollIntoView({
            behavior: 'auto',
            block: 'center',
            inline: 'center'
        });
    }
}

// Reload the page when user resize the page
window.addEventListener('resize', function () {
    'use strict';
    window.location.reload();
});

//Check if scroll position is in local storage and scroll to saved position when page is loaded
$(document).ready(function() {
    if(localStorage.getItem('scrollPositon')) {
        window.history.pushState('page2', 'Title', '/menu');
        console.log(localStorage.getItem('scrollPositon'));
        $(window).scrollTop(localStorage.getItem('scrollPositon'))
        localStorage.removeItem('scrollPositon');
    }
});

//Save the scroll position when user open cocktail link 
$('*[data-product-link]').on('click', (e) => {
    localStorage.setItem('scrollPositon', $(document).scrollTop());
})


//Product modal
if($('#productModal').length) {
    $('*[data-productModal-toggle]').on('click', (e) => {
      $('#productModal').addClass('hidden')
    })
    $(window).on('click', (e) => {
        if(e.target.id == 'productModal') {
            $('#productModal').addClass('hidden')
        }
    })
}













$('#recipeForm').on('submit', (e) => {
    e.preventDefault()
    let cocktail = $('#cocktail option:selected').val()
    let ingredientsArray = $('*[data-ingredient]')
    let quanityArray = $('*[data-qantity]')
    
    for(let i = 0; i < 15; i++) {
        let ingredient = $(ingredientsArray[i]).val()
        let token = $('[name="csrfmiddlewaretoken"]').val()
        if(ingredient == null) {
            continue
        }
        let quantity = $(quanityArray[i]).val()
        if(quantity == '' || quantity == null) {
            continue
        }

        $.ajax({
            type: 'POST',
            url: '/menu/admin/postRecipe',
            data: {
                'csrfmiddlewaretoken': token,
                'cocktail': cocktail, 
                'ingredient': ingredient,
                'quantity': quantity
            },
            success: function (response) {
                $('#recipeForm').trigger("reset");
            }
        })
    }
})



