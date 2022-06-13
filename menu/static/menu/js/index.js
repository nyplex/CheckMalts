import './animation.js'

// Reload the page when user resize the page
if ($(window).width() > 960) {
    window.addEventListener('resize', function () {
        'use strict';
        window.location.reload();
    });
}



