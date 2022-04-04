import { gsap } from "../../../../static/js/gsap/gsap.min.js"
import { ScrollTrigger } from "../../../../static/js/gsap/ScrollTrigger.min.js";
import { TextPlugin } from "../../../../static/js/gsap/TextPlugin.min.js";

gsap.registerPlugin(ScrollTrigger, TextPlugin);


/**
 *@param {string} canvasId insert the canvas ID
 *@param {number} canvasW insert canvas Width (image width)
 *@param {number} canvasH insert canvas Height (image height)
 *@param {number} frames insert the number of frames
 *@param {string} path insert the path to the frame, do not insert the file name
 *@param {string} triggerEl insert between "" the class or ID of the triggered Element
 *@param {string} triggerStart insert where to start the trigger from the triggered Element
 *@param {string} triggerEnd insert where to end the trigger from the triggered Element
 *@param {boolean} pined insert true or false
 *@param {boolean} marks insert true or false 
 */
 export let animateCanvas = (canvasId, canvasW, canvasH, frames, path, triggerEl, triggerStart, triggerEnd, pined, marks) => {
    const canvas = document.getElementById(canvasId);
    const context = canvas.getContext("2d");

    canvas.width = canvasW;
    canvas.height = canvasH;

    const frameCount = frames;
    const currentFrame = (index) =>
        path + (index + 1).toString().padStart(4, "0") + '.jpg';

    const images = [];
    const animation = {
        frame: 0
    };

    for (let i = 0; i < frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
        images.push(img);
    }


    gsap.to(animation, {
        frame: frameCount - 1,
        snap: "frame",
        scrollTrigger: {
            trigger: triggerEl,
            scrub: 2,
            anticipatePin: true,
            pin: pined,
            start: triggerStart,
            end: triggerEnd,
            markers: marks
        },
        onUpdate: render // use animation onUpdate instead of scrollTrigger's onUpdate
    });

    

    images[0].onload = render;

    function render() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.drawImage(images[animation.frame], 0, 0);
    }

    const headerTitleAnimation = gsap.timeline( { 
        scrollTrigger: {
          trigger: ".headerPin",
          start: "100 top+=150",
          end: "center top+=250",
          scrub: 2,
          markers: false
        }  
    });
       
    headerTitleAnimation
    .to('#header_chess_logo', {width: 5, duration: 8}, 8)
    .to('#header_chess_logo', {width: 100, duration: 8}, 8)
    .to('#jagerCanvas', { opacity: 0, duration: 5 }, 5)
    .to('#jagerCanvas', { opacity: 1, duration: 5 }, 5)

}

