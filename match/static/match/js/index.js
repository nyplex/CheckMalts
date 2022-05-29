$('#matchStartBtn').on('click', (e) => {
    $('#matchIntro').removeClass('flex').addClass('hidden')
    $('#matchFirst').removeClass('hidden').addClass('flex')
})


$('*[data-match-answer-btn]').on('change', (e) => {
    let parent = $(e.target).parent()
    $(parent).toggleClass('match-btn').toggleClass('match-active-btn')
})