//Reload the page and pass category value in the URL
$('#category_select_input').on('change', (e) => {
    let value = $('#category_select_input').val()
    window.location = "?category=" + value;
})


//change border color on item when ser hover it
$('.cocktail-name').on('mouseover', (e) => {
    let parent = $(e.target).parent()
    let grand_parent = $(parent).parent()

    $(grand_parent).css({'border-color': '#C27803'})
    $(parent).css('color', '#C27803')
})

//change border color on item when ser hover it
$('.cocktail-name').on('mouseleave', (e) => {
    let parent = $(e.target).parent()
    let grand_parent = $(parent).parent()

    $(grand_parent).css('border-color', 'white')
    $(parent).css('color', 'white')
})