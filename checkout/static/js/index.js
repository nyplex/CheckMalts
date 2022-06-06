var PrepTimeAjaxInterval;

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



// Ajax call to get prep time & display it on order confirmation page
function getPrepTime(orderID){
    $.ajax({
     url: '/checkout/preptime',
     type: 'post',
     data: {
         'order': orderID
     },
     success: function(response){
      // Perform operation on the return value
      if(response.e) {
          console.log(response);
          console.log('error!!');
          PrepTimeAjaxInterval = setInterval(getPrepTime(orderID),5000);
      }else{
        $('#prepTimeTxt').text(response.time + 'min')
        $('#prepTimeLoader').addClass('hidden')
        $('#prepTimeData').removeClass('hidden')
        clearInterval(PrepTimeAjaxInterval)
      }
     },
     error: function (xhr, ajaxOptions, thrownError) {
        if(xhr.status == 500) {
            window.location.replace("/order");
        }
    }
    });
}
   

$(document).ready(function(){
    let loader = $('#prepTimeLoader').hasClass('hidden')
    let prepTimeData = $('#prepTimeData').hasClass('hidden')
    if(!loader && prepTimeData){
        let orderURL = window.location.pathname.split('/')
        let orderID = orderURL[3]
        PrepTimeAjaxInterval = setInterval(getPrepTime(orderID),1000);
    }
});