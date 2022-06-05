import './animation.js'






// Reload the page when user resize the page
if ($(window).width() > 960) {
    window.addEventListener('resize', function () {
        'use strict';
        window.location.reload();
    });
}




// $('#recipeForm').on('submit', (e) => {
//     e.preventDefault()
//     let cocktail = $('#cocktail option:selected').val()
//     let ingredientsArray = $('*[data-ingredient]')
//     let quanityArray = $('*[data-qantity]')
    
//     for(let i = 0; i < 15; i++) {
//         let ingredient = $(ingredientsArray[i]).val()
//         let token = $('[name="csrfmiddlewaretoken"]').val()
//         if(ingredient == null) {
//             continue
//         }
//         let quantity = $(quanityArray[i]).val()
//         if(quantity == '' || quantity == null) {
//             continue
//         }

//         $.ajax({
//             type: 'POST',
//             url: '/menu/admin/postRecipe',
//             data: {
//                 'csrfmiddlewaretoken': token,
//                 'cocktail': cocktail, 
//                 'ingredient': ingredient,
//                 'quantity': quantity
//             },
//             success: function (response) {
//                 $('#recipeForm').trigger("reset");
//             }
//         })
//     }
// })



