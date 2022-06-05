import {animateCanvas} from './header';
import {} from './carousel'



//render the header scroll animation
animateCanvas('jagerCanvas', 2200, 1238, 150, 'https://checkmalt.s3.amazonaws.com/static/home/images/jagerFrame/', '.headerPin', 'top', 'bottom', true, false);





// Reload the page when user resize the page
if ($(window).width() > 960) {
    window.addEventListener('resize', function () {
        'use strict';
        window.location.reload();
    });
}