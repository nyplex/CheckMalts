import './orders.js'

$('#accountForm').on('submit', (e) => {
    e.preventDefault()
    let data = $("input[name='mobile']").val()
    const phoneNumber = phoneInput.getNumber();
    if (phoneInput.isValidNumber()) {
        $('input[name=mobile]').val(phoneNumber)
        $('#accountForm').unbind('submit').submit();
    } else {
        $('#id_mobile').css('border', 'solid 2px red')
    }
})