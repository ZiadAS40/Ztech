
$('button.add-btn').on('click', function() {
    let $lt = $(this).closest('div.lt');
    let dataId = $lt.data("id");
    let dataType = $lt.data("type");
    let result;
    let basketNum;

    $.get(`http://127.0.0.1:5000/api/v1/products/${dataType}/${dataId}`)
    .done((response) => {
        result = response;

        $.ajax({
            url: `http://127.0.0.1:5000/api/v1/shopping_cart`,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(result),
            success: (response) => {
                console.log("submitted successfully:", response);
                $.get(`http://127.0.0.1:5000/api/v1/shopping_cart`)
                .done((response) => {
                    basketNum = Object.keys(response).length;
                    $('.basket-circul p').text(basketNum);
                });
            },
            error: (xhr, status, error) => {
                console.error("Form submission failed:", error);
            }
        });
    })
    .fail((xhr, status, error) => {
        console.error("Error:", error);
    });
});
$.get(`http://127.0.0.1:5000/api/v1/shopping_cart`)
                .done((response) => {
                    basketNum = Object.keys(response).length;
                    $('.basket-circul p').text(basketNum);
                });