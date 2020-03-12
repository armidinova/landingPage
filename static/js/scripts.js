$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(product_id, number, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.number = number;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data['is_delete'] == true;
        }
        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_number);
                if (data.products_total_number) {
                    $('#basket_total_number').text("(" + data.products_total_number + ")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li>' + v.name + ' ' + v.number + ' шт.  по ' + v.price_per_item
                            + ' $ ' + '<a class="delete-item"  href="" data-product_id="'+v.id+'"> X </a>' + '</li>');
                    });
                }
            },
            error: function () {
                console.log("error")
            }
        });
    }

    form.on('submit', function (e) {
        var form = $(this);
        e.preventDefault();
        console.log('123');
        var number = $('#number').val();
        console.log(number);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketUpdating(product_id, number, is_delete = false)


    });

    function showingBasket() {
        $('.basket-items').toggleClass('d-none');
    };

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });
    $('.basket-container').mouseover(function () {
        showingBasket();
    });
    $('.basket-container').mouseout(function () {
        showingBasket();
    });
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id")
        number = 0;
        basketUpdating(product_id, number, is_delete = true)
    });

});