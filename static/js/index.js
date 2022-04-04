import "../css/style.css"
import "flowbite"
import Datepicker from '@themesberg/tailwind-datepicker/Datepicker';



var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = mm + '/' + dd + '/' + yyyy;

const datepickerEl = document.getElementById('id_booking_date');
new Datepicker(datepickerEl, {
    autohide: true,
    format: 'dd/mm/yyyy',
    minDate: today.toString(),
}); 