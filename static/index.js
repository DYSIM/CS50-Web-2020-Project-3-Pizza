
document.addEventListener('DOMContentLoaded', () => {

  var picture = document.getElementsByClassName('pizzaEntry')

  for (var i=0; i<picture.length; i++){
    var x = picture[i]
    x.onclick = function(click) {
      if (document.contains(document.getElementById("orderPlaceHolder"))) {
        document.getElementById("orderPlaceHolder").remove()
      }
      var orders = document.getElementById('userOrders')
      var dataset = x.dataset;
      var pElement = document.createElement('p');
      for (d in dataset) {
        let content =
          `${d}: ${dataset[d]}\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0`;
        pElement.innerHTML += content;

        
      }

      orders.appendChild(pElement)
      click.preventDefault();
    }
  }



})
