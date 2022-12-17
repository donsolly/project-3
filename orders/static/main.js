 document.addEventListener('DOMContentLoaded', () => {
    

         document.querySelector('.checkout').onclick = () => {

              


                var total_order = document.querySelector('.totals-value').innerHTML;
                document.querySelector('#total_order').value = total_order ;
                var all_product = document.querySelectorAll('.product-title');
                products = [];
                for (var i = 0; i < all_product.length; i++) {
                  products.push(all_product[i].innerHTML);
                    }
                document.querySelector('#products').value= products;
                var all_description = document.querySelectorAll('.product-description');
                description = [];
                for (var i = 0; i < all_product.length; i++) {
                  description.push(all_description[i].innerHTML);
                    }
                document.querySelector('#description').value= description;
                var all_price = document.querySelectorAll('.price');
                price = [];
                for (var i = 0; i < all_price.length; i++) {
                  price.push(all_price[i].innerHTML);
                    }
                document.querySelector('#price').value= price;
                var all_quantity = document.querySelectorAll('.quantity');
                quantity = [];
                for (var i = 0; i < all_quantity.length; i++) {
                  quantity.push(all_quantity[i].value);
                    }
                document.querySelector('#quantity').value= quantity;
                var all_subtotal = document.querySelectorAll('.subtotal');
                subtotal = [];
                for (var i = 0; i < all_product.length; i++) {
                  subtotal.push(all_subtotal[i].innerHTML);
                    }
                document.querySelector('#subtotal').value= subtotal;
                console.log(total_order,products,description,price,quantity,subtotal);
                

            
          };
        




          /* Set rates + misc */
var taxRate = 0.00;
var shippingRate = 0.00; 
var fadeTime = 300;


/* Assign actions */
$('.product-quantity input').change( function() {
  updateQuantity(this);
});

$('.product-removal button').click( function() {
  removeItem(this);
});


/* Recalculate cart */
function recalculateCart()
{
  var subtotal = 0;
  
  /* Sum up row totals */
  $('.product').each(function () {
    subtotal += parseFloat($(this).children('.product-line-price').text());
  });
  
  /* Calculate totals */
  var tax = subtotal - subtotal;
  var shipping = (subtotal > 0 ? shippingRate : 0);
  var total = subtotal + tax + shipping;
  
  /* Update totals display */
  $('.totals-value').fadeOut(fadeTime, function() {
    $('#cart-subtotal').html(subtotal.toFixed(2));
    $('#cart-tax').html(tax.toFixed(2));
    $('#cart-shipping').html(shipping.toFixed(2));
    $('#cart-total').html(total.toFixed(2));
    if(total == 0){
      $('.checkout').fadeOut(fadeTime);
    }else{
      $('.checkout').fadeIn(fadeTime);
    }
    $('.totals-value').fadeIn(fadeTime);
  });
}

recalculateCart(window.onload);

/* Update quantity */
function updateQuantity(quantityInput)
{
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.product-price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;
  
  /* Update line price display and recalc cart totals */
  productRow.children('.product-line-price').each(function () {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });  
}


/* Remove item from cart */
function removeItem(removeButton)
{
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).parent().parent();
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
  });
}



    });