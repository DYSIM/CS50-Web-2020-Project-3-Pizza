
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
      var price = box.parentNode.previousSibling.firstChild.innerHTML;

      var order_id = box.dataset.id
      var xhttp = new XMLHttpRequest();
      xhttp.open("POST", '/delete')
      xhttp.onload = () => {
        this.parentNode.parentNode.style.background = 'yellow';
        setTimeout(function(){
            box.parentNode.parentNode.style.display = 'none';
        },500);

        totalPriceElement = document.getElementById('priceTotal');
        currTotalPrice = totalPriceElement.innerHTML;
        totalPriceElement.innerHTML = (parseFloat(currTotalPrice) - parseFloat(price)).toFixed(2);


      }
     var csrftoken = getCookie('csrftoken');
     xhttp.setRequestHeader("X-CSRFToken", csrftoken);
     const data_ = new FormData();
     data_.append('order_id', order_id);
     xhttp.send(data_);
     return false;


    }
  }
// remove row and delete from database on clicking trashbin on cart page





})
