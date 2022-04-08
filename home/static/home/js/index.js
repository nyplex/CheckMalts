import {animateCanvas} from './header';
import {} from './carousel'
import './forms/form_validator'
import Datepicker from '@themesberg/tailwind-datepicker/Datepicker';


//render the header scroll animation
animateCanvas('jagerCanvas', 2200, 1238, 150, 'static/home/images/jagerFrame/', '.headerPin', 'top', 'bottom', true, false);

// prevent user to scroll while the page is loading
$('body').css('overflow-y', 'hidden')

// hide the loader icon and active scrolling when the page is loaded
window.onload = function () {
    if(localStorage.getItem('bookingFormSubmited')) {
        //If booking form has been submited, scrolldown to the form
        localStorage.removeItem('bookingFormSubmited');
        document.getElementById('reservationContainer').scrollIntoView({
            behavior: 'auto',
            block: 'center',
            inline: 'center'
        });
    }
    $('#loader').hide()
    $('body').css('overflow-y', 'auto')
}

// Reload the page when user resize the page
window.addEventListener('resize', function () {
    'use strict';
    window.location.reload();
});


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
    localStorage.setItem('bookingFormSubmited', true);
})


//Booking modal
if($('#bookingModal').length) {
    $('*[data-bookingModal-toggle]').on('click', (e) => {
      $('#bookingModal').addClass('hidden')
    })
}

//Show loader when booking form submited and disable submit btn to prevent multiple form submission
$('#reservationForm').on('submit', (e) => {
    $('#loader').show()
    $('#bookingSubmit').attr('disabled', 'disabled')
})
