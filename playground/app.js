var app = function() {

  var app = function() {};

  app.init = function() {
    app.add([ "foo","bar"]);
  };

  app.clean = function() {
    d3.select("#main")
      .selectAll("div")
      .remove();
  };

  app.add = function(data) {
    d3.select("#main")
      .selectAll("div")
      .data(data, String)
      .enter()
        .append("div")
        .attr("class", "element")

        .selectAll("textarea")
        .data(function(d) { return [d];})
        .enter()
          .append("textarea")
          .text(function(d) { return d; })
          .attr("rows", "1")
          .attr("cols", "5");
  };

  return app;
}();


/*
function drag_start(event) {
  var style = window.getComputedStyle(event.target, null);
  event.dataTransfer.setData("text/plain",
    (parseInt(style.getPropertyValue("left"), 10) - event.clientX) + ',' +
    (parseInt(style.getPropertyValue("top"), 10) - event.clientY));
}

function drag_over(event) {
  event.preventDefault();
  return false;
}

function drop(event) {
  var offset = event.dataTransfer.getData("text/plain").split(',');
  var dm = document.getElementById('dragme');

  dm.style.left = (event.clientX + parseInt(offset[0],10)) + 'px';
  dm.style.top = (event.clientY + parseInt(offset[1],10)) + 'px';
  event.preventDefault();
  return false;
}

var dm = document.getElementById('dragme');
dm.addEventListener('dragstart',drag_start,false);
document.body.addEventListener('dragover',drag_over,false);
document.body.addEventListener('drop',drop,false);
*/
