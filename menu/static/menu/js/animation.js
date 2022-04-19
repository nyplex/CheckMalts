import {gsap} from '../../../../static/js/gsap/gsap.min.js'
import {ScrollTrigger} from '../../../../static/js/gsap/ScrollTrigger.min.js';
import {TextPlugin} from '../../../../static/js/gsap/TextPlugin.min.js';

gsap.registerPlugin(ScrollTrigger, TextPlugin);



// Main menu title animation moving top to bottom on scroll
gsap.to('#menuTitle', {
	top: '55%',
	scrollTrigger: {
		trigger: '#menuHeaderContainer',
		scrub: 2,
		anticipatePin: true,
		pin: false,
		start: 'top',
		end: 'bottom',
		markers: false
	}
});

//Knight Chess Illustration animation moving from center to ext. on scroll

let scroll_trigger_options = {
	trigger: '#menuHeaderContainer',
	scrub: 2,
	anticipatePin: true,
	pin: true,
	start: 'top',
	end: 'bottom',
	markers: false
}
gsap.to('#chessIllustrationHeader1', {
	x: '-100%',
	scrollTrigger: scroll_trigger_options
});
gsap.to('#chessIllustrationHeader2', {
	x: '100%',
	scrollTrigger: scroll_trigger_options
});


//Menu section's title animation
let section_title = gsap.utils.toArray('*[data-sectiontitle]')
section_title.forEach((section) => {
	let section_title_animation = gsap.timeline({
		scrollTrigger: {
			trigger: section,
			start: "top center+=150",
			markers: false,
			toggleActions: "play none none reverse",
		}
	});
	section_title_animation.from(section, {y: -100,opacity: 0,duration: 1.5})
	section_title_animation.to(section, {y: 0,opacity: 1,duration: 1.5})
})


//Menu secton's content animation
let section_content = gsap.utils.toArray('*[data-sectioncontent]')
section_content.forEach((section) => {
	let section_content_animation = gsap.timeline({
		scrollTrigger: {
			trigger: section,
			start: "top center+=50",
			markers: false,
			toggleActions: "play none none reverse",
		}
	});
	section_content_animation.from(section, {x: -150,opacity: 0,duration: 1.5})
	section_content_animation.to(section, {x: 0,opacity: 1,duration: 0})
})


//Menu section's image animation
let section_image = gsap.utils.toArray('*[data-sectionimage]')
section_image.forEach((section) => {
	let section_image_animation = gsap.timeline({
		scrollTrigger: {
			trigger: section,
			start: "top center+=50",
			markers: false,
			toggleActions: "play none none reverse",
		}
	});
	section_image_animation.from(section, {x: 150,opacity: 0,duration: 1.5})
	section_image_animation.to(section, {x: 0,opacity: 1,duration: 0})
})



