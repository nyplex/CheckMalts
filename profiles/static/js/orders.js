$('*[data-td-order]').on('click', (e) => {
    let target = $(e.target)
    let nextTr;
    let currentTr;
    let currentBtn;
    let currentIcon;
    if(target.is('i')) {
        nextTr = $(e.target).parent().parent().parent().next()
        currentTr = $(e.target).parent().parent().parent()
        currentBtn = $(e.target).parent()
        currentIcon = $(e.target)

    }else if(target.is('button')) {
        nextTr = $(e.target).parent().parent().next()
        currentTr = $(e.target).parent().parent()
        currentBtn = $(e.target)
        currentIcon = $(e.target).children()

    }
    $(nextTr).toggle()
    $(currentTr).toggleClass('bg-secondaryHoverDarker border-b-2')
    $(currentBtn).toggleClass('bg-secondaryHoverDarker bg-secondaryColor hover:bg-secondaryColor hover:bg-secondaryHoverLighter')
    $(currentIcon).toggleClass('fa-angle-down fa-angle-up')

})