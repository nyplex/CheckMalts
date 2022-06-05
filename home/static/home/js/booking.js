import './forms/form_validator'
import Datepicker from '@themesberg/tailwind-datepicker/Datepicker';


// Setup and Init the Input Date Picker
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = dd + '/' + mm + '/' + yyyy;

const datepickerEl = document.getElementById('id_booking_date');
new Datepicker(datepickerEl, {
    autohide: true,
    format: 'dd/mm/yyyy',
    minDate: today.toString(),
}); 

$('#reservationForm').on('submit', (e) => {
    $('#loader').show()
    $('#bookingSubmit').attr('disabled', 'disabled')
})


//Booking modal
if($('#bookingModal').length) {
    $('*[data-bookingModal-toggle]').on('click', (e) => {
      $('#bookingModal').addClass('hidden')
    })
}
