

//Display the service charge
$('*[data-standardTips]').on('click', (e) => {
    let value = $(e.currentTarget).attr('data-standardTips')
    let total = $('#subtotal').text()
    total = total.substring(1)
    tips = Math.round(((total / 100) * value) * 100) / 100
    grandTotal = parseFloat(tips) + parseFloat(total)
    grandTotal = Math.round(grandTotal * 100) / 100
    $('#id_tips').val(tips)
    $('#tips').text('£' + tips)
    $('#grandTotal').text('£' + parseFloat(grandTotal).toFixed(2))
})


$('#id_tips').on('input', (e) => {
    let value = $(e.currentTarget).val()
    let total = $('#subtotal').text()
    total = total.substring(1)
    tips = Math.round(value * 100) / 100
    grandTotal = parseFloat(tips) + parseFloat(total)
    grandTotal = Math.round(grandTotal * 100) / 100
    $('#tips').text('£' + tips)
    $('#grandTotal').text('£' + parseFloat(grandTotal).toFixed(2))
})