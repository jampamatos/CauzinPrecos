$(document).ready(function() {
    const productData = JSON.parse(document.getElementById('productData').textContent);
    const additional = JSON.parse(document.getElementById('additionalData').textContent);
    const freight = JSON.parse(document.getElementById('freightData').textContent);
    const includeTax = JSON.parse(document.getElementById('includeTaxData').textContent);

    $('.markup-input').on('input', function() {
        let markup = $(this).val();
        let index = $(this).data('index');
        updatePrices(markup, index);
    });

    function updatePrices(markup, index) {
        $.ajax({
            url: '/update_prices',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                markup: markup,
                index: index,
                product_data: productData,
                additional: additional,
                freight: freight,
                include_tax: includeTax
            }),
            success: function(data) {
                $('table').find('tr').eq(index + 1).find('td').eq(9).text('R$ ' + data.new_selling_price.toFixed(2));
            }
        });
    }
});
