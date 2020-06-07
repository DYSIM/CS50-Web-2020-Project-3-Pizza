
document.addEventListener('DOMContentLoaded', () => {

  var picture = document.getElementsByClassName('pizzaEntry')

  for (var i=0; i<picture.length; i++){
    var x = picture[i]
    x.onclick = function(click) {
      var body = document.getElementsByTagName("body")[0]
      var foodMenu = document.getElementById('Menu')
      var dataset = x.dataset;
      var divElement = document.createElement('div');
      divElement.setAttribute('class','jumbotron jumbotron-fluid')
      for (d in dataset) {
        divElement.innerHTML += dataset[d];
      }
      // divElement.innerHTML = 'hello'

      body.insertBefore(divElement,foodMenu)
      click.preventDefault();
    }
  }



})
