import {gsap} from '../../../../static/js/gsap/gsap.min.js'
import {ScrollTrigger} from '../../../../static/js/gsap/ScrollTrigger.min.js';
import {TextPlugin} from '../../../../static/js/gsap/TextPlugin.min.js';

gsap.registerPlugin(ScrollTrigger, TextPlugin);


// Menu header animation
let scroll_trigger_options = {
	trigger: '#menuHeaderContainer',
	scrub: 2,
	anticipatePin: true,
	pin: true,
	start: 'top',
	end: 'bottom',
	markers: false
}
gsap.to('#chessIllustrationHeader1', {x: '-100%',scrollTrigger: scroll_trigger_options});
gsap.to('#chessIllustrationHeader2', {x: '100%',scrollTrigger: scroll_trigger_options});
gsap.to('#menuTitle', {top: '55%',scrollTrigger: scroll_trigger_options});



//Menu sections animation
let scroll_menu_options = {markers: false,toggleActions: "play none none reverse", start: 'top center+=50'}

let section_title = gsap.utils.toArray('*[data-sectiontitle]')
section_title.forEach((section) => {
	scroll_menu_options['trigger'] = section
	let section_title_animation = gsap.timeline({
		scrollTrigger: scroll_menu_options
	});
	section_title_animation.from(section, {y: -100,opacity: 0,duration: 1.5})
	section_title_animation.to(section, {y: 0,opacity: 1,duration: 1.5})
})


let section_content = gsap.utils.toArray('*[data-sectioncontent]')
section_content.forEach((section) => {
	scroll_menu_options['trigger'] = section
	let section_content_animation = gsap.timeline({
		scrollTrigger: scroll_menu_options
	});
	section_content_animation.from(section, {x: -150,opacity: 0,duration: 1.5})
	section_content_animation.to(section, {x: 0,opacity: 1,duration: 0})
})


let section_image = gsap.utils.toArray('*[data-sectionimage]')
section_image.forEach((section) => {
	scroll_menu_options['trigger'] = section
	let section_image_animation = gsap.timeline({
		scrollTrigger: scroll_menu_options
	});
	section_image_animation.from(section, {x: 150,opacity: 0,duration: 1.5})
	section_image_animation.to(section, {x: 0,opacity: 1,duration: 0})
})



