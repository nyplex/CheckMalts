import { animateCanvas } from "./header";

//render the header scroll animation
animateCanvas("jagerCanvas", 3840, 2160, 150, "static/home/images/jagerFrame/", ".headerPin", "top", "bottom", true, false);

// prevent user to scroll while the page is loading
$('body').css('overflow-y', 'hidden')

// hide the loader icon and active scrolling when the page is loaded
window.onload = function() {
    $('#loader').hide()
    $('body').css('overflow-y', 'auto')
}

window.addEventListener('resize', function () { 
    "use strict";
    window.location.reload(); 
});