const { getPrepTime } = require(".");

$(document).ready(function(){
    let loader = $('#prepTimeLoader').hasClass('hidden')
    let prepTimeData = $('#prepTimeData').hasClass('hidden')
    if(!loader && prepTimeData){
        let orderURL = window.location.pathname.split('/')
        let orderID = orderURL[3]
        setTimeout(function(){ getPrepTime(orderID); }, 5000);
    }
});