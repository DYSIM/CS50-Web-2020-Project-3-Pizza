
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
  var trash = document.getElementsByClassName("trackorder-trash-button")
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

        if (box.parentNode.parentNode.parentNode.id === 'completedOrdersBody'){
          var totalPriceElement = document.getElementById('completedPriceTotal');
        }
        else{
          var totalPriceElement = document.getElementById('pendingPriceTotal');
        }

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


var completed_buttons = document.getElementsByClassName("completed-button");
for (var i = 0; i < completed_buttons.length; i++){
  completed_buttons[i].onclick = function() {
    var box = this;
    var price = box.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.firstChild.innerHTML;
    var completed_button_row = box.parentNode
    var table_row = box.parentNode.parentNode
    var order_id = box.dataset.id
    var request = new XMLHttpRequest();
    request.open("POST", '/completeorder')
    request.onload = () => {
      table_row.style.background= 'yellow'
      setTimeout(function(){
          completed_button_row.remove() //remove the delete button
          document.getElementById('completedOrdersBody').insertBefore(table_row,document.getElementById('completedOrdersBody').lastElementChild) //shift from pending to completed table
          table_row.style.background= 'transparent';
      },500);

      var pendingPriceElement = document.getElementById('pendingPriceTotal');
      pendingTotalPrice = pendingPriceElement.innerHTML;

      pendingPriceElement.innerHTML = (parseFloat(pendingTotalPrice) - parseFloat(price)).toFixed(2);
      var completedPriceElement = document.getElementById('completedPriceTotal');
      completedTotalPrice = completedPriceElement.innerHTML;
      
      if (completedTotalPrice == ''){
        completedTotalPrice = 0.00
      }
      completedPriceElement.innerHTML = (parseFloat(completedTotalPrice) + parseFloat(price)).toFixed(2);
    }
    var csrftoken = getCookie('csrftoken');
    request.setRequestHeader("X-CSRFToken", csrftoken);
    const data_ = new FormData();
    data_.append('order_id', order_id);
    request.send(data_);
    return false;
  }
}
})
