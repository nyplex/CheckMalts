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