
function addToLocalStorage(key, obj) {
    localStorage.setItem(key, JSON.stringify(obj));
    console.log('added to the local storage');
    $('.basket-circul p').text();
}



$('button.logout').on('click', function () {
    $.ajax({
        url: '/logout',
        type: 'POST',
        success: function (response) {
            localStorage.removeItem('access_token');
            location.reload();
        },
        error: function(error) {
            alert('Error logging out');
        }
    })
})






$('button.add-btn').on('click', function() {
    let $lt = $(this).closest('div.lt');
    let dataId = $lt.data("id");
    let dataType = $lt.data("type");
    let result;
    let basketNum;

    $.get(`http://127.0.0.1:5000/api/v1/products/${dataType}/${dataId}`)
    .done((response) => {
        result = response;
        const access_token = localStorage.getItem('access_token')
        if (access_token) {
            $.ajax({
                url: `http://127.0.0.1:5000/api/v1/shopping_cart`,
                type: "POST",
                headers: {
                    'Authorization': `Bearer ${access_token}`,
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(result),
                success: (response) => {
                    $.get(`http://127.0.0.1:5000/api/v1/shopping_cart`)
                    .done((response) => {
                        console.log(response);
                        let counter = 0;
                        for (let key in response) {
                            if (response.hasOwnProperty(key)) {
                                counter  += response[key].length;  // Add the length of each array to the total count
                            }
                          }
                          console.log(counter)
                        basketNum = Object.keys(response).length;
                        $('.basket-circul p').text(counter);
                    });
                },
                error: (xhr, status, error) => {
                    console.error("Form submission failed:", error);
                }
            });
        } else {
            $.ajax({
                url: `http://127.0.0.1:5000/api/v1/loggout_shopping_cart`,
                type: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(result),
                success: (response) => {
                    $.get(`http://127.0.0.1:5000/api/v1/loggout_shopping_cart`)
                    .done((response) => {
                        let counter = 0;
                            for (let key in response) {
                                if (response.hasOwnProperty(key)) {
                                    counter  += response[key].length;
                                }
                              }
                        basketNum = Object.keys(response).length;
                        $('.basket-circul p').text(counter);
                });
                },
                error: (xhr, status, error) => {
                    console.error("Form submission failed:", error);
                }
            });
        }

    })
    .fail((xhr, status, error) => {
        console.error("Error:", error);
    });
});
access_token = localStorage.getItem('access_token');
if (access_token){
$.get(`http://127.0.0.1:5000/api/v1/shopping_cart`)
                .done((response) => {
                    let counter = 0;
                        for (let key in response) {
                            if (response.hasOwnProperty(key)) {
                                counter  += response[key].length;
                            }
                          }
                    basketNum = Object.keys(response).length;
                    $('.basket-circul p').text(counter);
});
} else {
    $.get(`http://127.0.0.1:5000/api/v1/loggout_shopping_cart`)
    .done((response) => {
        let counter = 0;
            for (let key in response) {
                if (response.hasOwnProperty(key)) {
                    counter  += response[key].length;
                }
              }
        basketNum = Object.keys(response).length;
        $('.basket-circul p').text(counter);
});
}
