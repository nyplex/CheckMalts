let loader = $('#prepTimeLoader').hasClass('hidden')
let prepTimeData = $('#prepTimeData').hasClass('hidden')
let orderID

if(!loader && prepTimeData){
    let orderURL = window.location.pathname.split('/')
    orderID = orderURL[3]
}

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
             console.log(response);
             console.log('error!!');
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