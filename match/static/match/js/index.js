let questionNo = 0;

//Display match form when user click on start button
$('#matchStartBtn').on('click', (e) => {
    $('#matchIntro').removeClass('flex').addClass('hidden')
    $('#matchFirst').removeClass('hidden').addClass('flex')
    questionNo += 1
    $('#matchQuestionNo').text(questionNo + '/9')
})

//Change and unique checked when user click on answer
$('*[data-match-answer-btn]').on('change', (e) => {
    let parent = $(e.target).parent()
    let container = $(parent).parent()
    let labels = $(container).find('label')
    let checkboxes = $(container).find('input')

    $(checkboxes).prop('checked', false);
    $(labels).addClass('match-btn').removeClass('match-active-btn')
    $(parent).removeClass('match-btn').addClass('match-active-btn').prop('checked', true)
    $(e.target).prop('checked', true)
    
})

//Go back to prevouis question
$('*[data-match-back]').on('click', (e) => {
    let parent = $(e.target).parent().parent().removeClass('flex').addClass('hidden')
    let previous = $(parent).prev().removeClass('hidden').addClass('flex')
    $('.match-error').addClass('hidden')
    questionNo -= 1
    $('#matchQuestionNo').text(questionNo + '/9')
})

//Go to next question & check one answer has been selected
$('*[data-match-next]').on('click', (e) => {
    let inputs = $(e.target).parent().parent().find('input')
    for(let i = 0; i < inputs.length; i++) {
        if($(inputs[i]).is(':checked')) {
            let parent = $(e.target).parent().parent().removeClass('flex').addClass('hidden')
            $(parent).next().removeClass('hidden').addClass('flex')
            questionNo += 1
            $('#matchQuestionNo').text(questionNo + '/9')
            return
        }else {
            let input = $(e.target).parent().parent()
            let error = input.find('span')
            $(error).removeClass('hidden')
        }
    }
})