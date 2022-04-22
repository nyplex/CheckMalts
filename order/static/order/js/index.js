//Reload the page and pass category value in the URL
$('#category_select_input').on('change', (e) => {
    let value = $('#category_select_input').val()
    window.location = "?category=" + value;
})