import {animateCanvas} from './header';
import {} from './carousel'


if ($(window).width() > 768) {
    //render the header scroll animation
    animateCanvas('jagerCanvas', 2200, 1238, 150, 'https://checkmalt.s3.amazonaws.com/static/home/images/jagerFrame/', '.headerPin', 'top', 'bottom', true, false);
}else{
    const canvas = document.getElementById('jagerCanvas');
    const context = canvas.getContext('2d');

    canvas.width = 2200;
    canvas.height = 1238;

    var img = new Image();
    img.onload = function() {
        context.drawImage(img, 0, 0);
    };
    img.src = 'https://checkmalt.s3.amazonaws.com/static/home/images/jagerFrame/0149.webp';

}


// Reload the page when user resize the page
if ($(window).width() > 960) {
    window.addEventListener('resize', function () {
        'use strict';
        window.location.reload();
    });
}