import './animation.js'




$(document).ready((e) => {
    if(localStorage.getItem('scrollPositon')) {
        window.history.pushState('page2', 'Title', '/menu');
        $(window).scrollTop(localStorage.getItem('scrollPositon'))
        localStorage.removeItem('scrollPositon');
    }
})


// Reload the page when user resize the page
window.addEventListener('resize', function () {
    'use strict';
    window.location.reload();
});


//Save the scroll position when user open cocktail link 
$('*[data-product-link]').on('click', (e) => {
    localStorage.setItem('scrollPositon', $(document).scrollTop());
})


//Product modal
if($('#productModal').length) {
    $('*[data-productModal-toggle]').on('click', (e) => {
        localStorage.setItem('scrollPositon', $(document).scrollTop());
        window.location.reload();
    })
    $(window).on('click', (e) => {
        if(e.target.id == 'productModal') {
            localStorage.setItem('scrollPositon', $(document).scrollTop());
            window.location.reload();
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



