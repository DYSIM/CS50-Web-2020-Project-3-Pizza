
//getCookie function
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

document.addEventListener('DOMContentLoaded', () => {



// remove row and delete from database on clicking trashbin on cart page
  var trash = document.getElementsByClassName("cart-trash")
  for(var i = 0; i < trash.length; i++){
    trash[i].onclick = function() {
      var box = this
      var price = box.parentNode.previousSibling.previousSibling.firstChild.innerHTML;

      var order_id = box.dataset.id
      var trashRequest = new XMLHttpRequest();
      trashRequest.open("POST", '/delete')
      trashRequest.onload = () => {
        this.parentNode.parentNode.style.background = 'yellow';
        setTimeout(function(){
            box.parentNode.parentNode.style.display = 'none';
        },500);

        var totalPriceElement = document.getElementById('priceTotal');
        currTotalPrice = totalPriceElement.innerHTML;
        totalPriceElement.innerHTML = (parseFloat(currTotalPrice) - parseFloat(price)).toFixed(2);


      }
     var csrftoken = getCookie('csrftoken');
     trashRequest.setRequestHeader("X-CSRFToken", csrftoken);
     const data_ = new FormData();
     data_.append('order_id', order_id);
     trashRequest.send(data_);
     return false;


    }
  }
// remove row and delete from database on clicking trashbin on cart page

// submit cart orders
  var submitCartButton = document.getElementById('submitCart');
  submitCartButton.onclick = () => {
    var submitCartRequest = new XMLHttpRequest();
    var csrftoken = getCookie('csrftoken');

    submitCartRequest.open("POST", '/submitcart');
    submitCartRequest.setRequestHeader("X-CSRFToken", csrftoken);
    submitCartRequest.onload = () => {
      var cartEntries = document.getElementsByClassName("cartEntries")
      var cartModalBody = document.getElementById('cartModalBody');
      var cartModalRedirect = document.getElementById('cartModalRedirect');
      var count = 0

      for(var i = 0; i < cartEntries.length; i++){
        if (cartEntries[i].style.display !== 'none'){
          count+=1;
          cartEntries[i].style.display='none';
        }
      }
      if (count=== 0){
        cartModalBody.innerHTML = 'You have no orders!'
        cartModalRedirect.innerHTML = 'Go to menu'
        cartModalRedirect.href = '/';
      }
      else{
        cartModalBody.innerHTML = 'Your orders have been submitted to the kitchen! Thank you for ordering.'
        cartModalRedirect.innerHTML = 'Track your orders'
        cartModalRedirect.href = 'trackorders';
      }
      var totalPriceElement = document.getElementById('priceTotal');
      totalPriceElement.innerHTML = "0.00"
    }
    submitCartRequest.send()
  }
// submit cart orders


})
