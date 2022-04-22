import '../css/main.css'
import '../css/messages.css'
import '../css/home_carousel.css'
import '../css/home.css'
import '../css/menu.css'
import '../css/order.css'
import 'flowbite'

// prevent user to scroll while the page is loading
$('body').css('overflow-y', 'hidden')

// target element that will be dismissed
const targetEl = document.getElementById('alert-1');

// options object
const options = {
  triggerEl: document.getElementById('triggerEl'),
  transition: 'transition-opacity',
  duration: 1000,
  timing: 'ease-out',

  // callback functions
  onHide: (targetEl) => {
    console.log('element has been dismissed')
    console.log(targetEl)
  }
};

const dismiss = new Dismiss(targetEl, options);


//hide alert box after 10sec
if($('*[data-alertbox]').length) {
  setTimeout(() => {
      $('*[data-alertbox]').animate({opacity: 0}, 1000)
      setTimeout(() => {
        $('*[data-alertbox]').addClass('hide')
    }, 2000)
  }, 9000)
  
}

// Reload the page when user resize the page
window.addEventListener('resize', function () {
  'use strict';
  window.location.reload();
});


// hide the loader icon and active scrolling when the page is loaded
window.onload = function () {
  $('#loader').hide()
  $('body').css('overflow-y', 'auto')
}
