import '../css/main.css'
import '../css/messages.css'
import '../css/home_carousel.css'
import '../css/home.css'
import 'flowbite'


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