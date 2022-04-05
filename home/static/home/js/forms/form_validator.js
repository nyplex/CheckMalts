const validate = require('validate.js')
import {
    bookingFormValidator
} from './validators.js'


$('#id_booking_email, #id_booking_name').on('input', (e) => {
    let check;
    validate.options = {
        fullMessages: false
    }
    switch (e.target.id) {
        case 'id_booking_email':
            check = validate({
                email: $(e.target).val()
            }, bookingFormValidator, )
            break;
        case 'id_booking_name':
            check = validate({
                name: $(e.target).val()
            }, bookingFormValidator)
            break;
        default:
            break;
    }
    if (check) {
        $(e.target).removeClass('primary-input').addClass('primary-invalid-input')
        let errorsContainer = $(e.target).next()
        $(errorsContainer).empty()
        $(errorsContainer).html(`<p class='input-errors'>${Object.values(check)[0][0]}</p>`)
    } else {
        $(e.target).removeClass('primary-input primary-invalid-input').addClass('primary-input')
        let errorsContainer = $(e.target).next()
        $(errorsContainer).empty()
    }
})

$('#id_booking_time, #id_booking_size').on('change', (e) => {
    let check;
    validate.options = {
        fullMessages: false
    }
    switch (e.target.id) {
        case 'id_booking_time':
            check = validate({
                bookingTime: $(e.target).val()
            }, bookingFormValidator)
            break;
        
        case 'id_booking_size':
            check = validate({
                bookingSize: $(e.target).val()
            }, bookingFormValidator)
            break
        default:
            break;
    }

    if (check) {
        console.log(check);
        $(e.target).removeClass('primary-select-input').addClass('primary-invalid-select-input')
    } else {
        $(e.target).removeClass('primary-select-input primary-invalid-select-input').addClass('primary-select-input')
    }
})