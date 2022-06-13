let loader = $('#prepTimeLoader').hasClass('hidden')
let prepTimeData = $('#prepTimeData').hasClass('hidden')
let orderID

//Get the product ID from the url
if(!loader && prepTimeData){
    let orderURL = window.location.pathname.split('/')
    orderID = orderURL[3]
}

// Ajax call to get the prep_time on the confirmation page
var myInterval = setInterval(function(){
    $.ajax({
        url: '/checkout/preptime',
        type: 'post',
        data: {
            'order': orderID
        },
        success: function(response){
         // Perform operation on the return value
         if(response.e) {
            console.log('waiting for server to respond...');
         }else{
           $('#prepTimeTxt').text(response.time + 'min')
           $('#prepTimeLoader').addClass('hidden')
           $('#prepTimeData').removeClass('hidden')
           clearInterval(myInterval)
         }
        },
        error: function (xhr, ajaxOptions, thrownError) {
           if(xhr.status == 500) {
               window.location.replace("/order");
           }
       }
    });
}, 2000);