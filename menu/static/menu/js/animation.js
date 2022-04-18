import { gsap } from '../../../../static/js/gsap/gsap.min.js'
import { ScrollTrigger } from '../../../../static/js/gsap/ScrollTrigger.min.js';
import { TextPlugin } from '../../../../static/js/gsap/TextPlugin.min.js';

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
gsap.to('#chessIllustrationHeader1', {
  x: '-100%',
  scrollTrigger: {
      trigger: '#menuHeaderContainer',
      scrub: 2,
      anticipatePin: true,
      pin: true,
      start: 'top',
      end: 'bottom',
      markers: false
  }
});

gsap.to('#chessIllustrationHeader2', {
  x: '100%',
  scrollTrigger: {
      trigger: '#menuHeaderContainer',
      scrub: 2,
      anticipatePin: true,
      pin: true,
      start: 'top',
      end: 'bottom',
      markers: false
  }
});



// section animation
let cocktail = gsap.timeline({
  scrollTrigger: {
    trigger: "#cocktailsSection",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

let cocktailIll = gsap.timeline({
  scrollTrigger: {
    trigger: "#cocktailsSectionIllustration",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

let cocktailTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#cocktailsSectionTitle",
    start: "top center+=150",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

cocktail.from("#cocktailsSection", {x:-150, opacity:0, duration:1.5})
cocktail.to("#cocktailsSection", {x:0, opacity:1, duration:0})

cocktailTitle.from("#cocktailsSectionTitle", {y:-100, opacity:0, duration:1.5})
cocktailTitle.to("#cocktailsSectionTitle", {y:0, opacity:1, duration:1.5})

cocktailIll.from("#cocktailsSectionIllustration", {x:150, opacity:0, duration:1.5})
cocktailIll.to("#cocktailsSectionIllustration", {x:0, opacity:1, duration:0})



let wine = gsap.timeline({
    scrollTrigger: {
      trigger: "#winesSection",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let wineIll = gsap.timeline({
    scrollTrigger: {
      trigger: "#winesSectionIllustration",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let wineTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#winesSectionTitle",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

wine.from("#winesSection", {x:-150, opacity:0, duration:1.5})
wine.to("#winesSection", {x:0, opacity:1, duration:0})

wineTitle.from("#winesSectionTitle", {y:-100, opacity:0, duration:1.5})
wineTitle.to("#winesSectionTitle", {y:0, opacity:1, duration:1.5})


wineIll.from("#winesSectionIllustration", {x:150, opacity:0, duration:1.5})
wineIll.to("#winesSectionIllustration", {x:0, opacity:1, duration:0})


let beer = gsap.timeline({
    scrollTrigger: {
      trigger: "#beersSection",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let beerIll = gsap.timeline({
    scrollTrigger: {
      trigger: "#beersSectionIllustration",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let beerTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#beersSectionTitle",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

beer.from("#beersSection", {x:-150, opacity:0, duration:1.5})
beer.to("#beersSection", {x:0, opacity:1, duration:0})

beerTitle.from("#beersSectionTitle", {y:-100, opacity:0, duration:1.5})
beerTitle.to("#beersSectionTitle", {y:0, opacity:1, duration:1.5})


beerIll.from("#beersSectionIllustration", {x:150, opacity:0, duration:1.5})
beerIll.to("#beersSectionIllustration", {x:0, opacity:1, duration:0})


let shot = gsap.timeline({
    scrollTrigger: {
      trigger: "#shotsSection",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let shotIll = gsap.timeline({
    scrollTrigger: {
      trigger: "#shotsSectionIllustration",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let shotTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#shotsSectionTitle",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

shot.from("#shotsSection", {x:-150, opacity:0, duration:1.5})
shot.to("#shotsSection", {x:0, opacity:1, duration:0})

shotTitle.from("#shotsSectionTitle", {y:-100, opacity:0, duration:1.5})
shotTitle.to("#shotsSectionTitle", {y:0, opacity:1, duration:1.5})


shotIll.from("#shotsSectionIllustration", {x:150, opacity:0, duration:1.5})
shotIll.to("#shotsSectionIllustration", {x:0, opacity:1, duration:0})



let liqueur = gsap.timeline({
    scrollTrigger: {
      trigger: "#liqueurSection",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let liqueurIll = gsap.timeline({
    scrollTrigger: {
      trigger: "#liqueurSectionIllustration",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let liqueurTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#liqueurSectionTitle",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

liqueur.from("#liqueurSection", {x:-150, opacity:0, duration:1.5})
liqueur.to("#liqueurSection", {x:0, opacity:1, duration:0})

liqueurTitle.from("#liqueurSectionTitle", {y:-100, opacity:0, duration:1.5})
liqueurTitle.to("#liqueurSectionTitle", {y:0, opacity:1, duration:1.5})


liqueurIll.from("#liqueurSectionIllustration", {x:150, opacity:0, duration:1.5})
liqueurIll.to("#liqueurSectionIllustration", {x:0, opacity:1, duration:0})


let soft = gsap.timeline({
    scrollTrigger: {
      trigger: "#softSection",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let softIll = gsap.timeline({
    scrollTrigger: {
      trigger: "#softSectionIllustration",
      start: "top center+=50",  
      markers: false,
      toggleActions: "play none none reverse",
    }
});

let softTitle = gsap.timeline({
  scrollTrigger: {
    trigger: "#softSectionTitle",
    start: "top center+=50",  
    markers: false,
    toggleActions: "play none none reverse",
  }
});

soft.from("#softSection", {x:-150, opacity:0, duration:1.5})
soft.to("#softSection", {x:0, opacity:1, duration:0})

softTitle.from("#softSectionTitle", {y:-100, opacity:0, duration:1.5})
softTitle.to("#softSectionTitle", {y:0, opacity:1, duration:1.5})


softIll.from("#softSectionIllustration", {x:150, opacity:0, duration:1.5})
softIll.to("#softSectionIllustration", {x:0, opacity:1, duration:0})





