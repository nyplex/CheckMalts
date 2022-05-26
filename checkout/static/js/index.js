

//Update serivce charge when user click on tips buttons
$('*[data-standardTips]').on('click', (e) => {
    let value = $(e.currentTarget).attr('data-standardTips')
    $('*[data-standardTips]').removeClass('text-secondaryHoverDarker border-secondaryHoverDarker')
    $(e.currentTarget).addClass('text-secondaryHoverDarker border-secondaryHoverDarker')
    if(value < 0) {
        value = 0
    }
    let total = $('#subtotal').text()
    total = total.substring(1)
    tips = Math.round(((total / 100) * value) * 100) / 100
    grandTotal = parseFloat(tips) + parseFloat(total)
    grandTotal = Math.round(grandTotal * 100) / 100
    $('#id_tips').val(tips)
    $('#tips').text('£' + tips)
    $('#grandTotal').text('£' + parseFloat(grandTotal).toFixed(2))
})

//Update service charge when user enter custom service charge
$('#id_tips').on('input', (e) => {
    $('*[data-standardTips]').removeClass('text-secondaryHoverDarker border-secondaryHoverDarker')
    let value = $(e.currentTarget).val()
    if(value < 0) {
        $('#id_tips').val('0')
        value = 0
    }
    let total = $('#subtotal').text()
    total = total.substring(1)
    tips = Math.round(value * 100) / 100
    grandTotal = parseFloat(tips) + parseFloat(total)
    grandTotal = Math.round(grandTotal * 100) / 100
    $('#tips').text('£' + tips)
    $('#grandTotal').text('£' + parseFloat(grandTotal).toFixed(2))
})



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

function getPrepTime(){
    $.ajax({
     url: '/checkout/preptime',
     type: 'post',
     data: {
         'order': 120
     },
     success: function(response){
      // Perform operation on the return value
      if(response.e) {
          console.log('error!!');
      }else{
        $('#prepTimeTxt').text(response.time + 'min')
        $('#prepTimeLoader').addClass('hidden')
        $('#prepTimeData').removeClass('hidden')
        clearInterval(PrepTimeAjaxInterval)
      }
     }
    });
   }
   
$(document).ready(function(){
    let loader = $('#prepTimeLoader').hasClass('hidden')
    let prepTimeData = $('#prepTimeData').hasClass('hidden')
    if(!loader && prepTimeData){
        PrepTimeAjaxInterval = setInterval(getPrepTime,2000);
    }
});