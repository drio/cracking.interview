var list = function() {

  var list = function() {},
      ta_rows = "1",
      ta_cols = "5";

  list.data = [];

  update = function() {
    var divs = d3.select("#main")
      .selectAll("div")
      .data(list.data, String);

    divs.enter()
      .append("div")
      .attr("class", "element")
      .selectAll("textarea")
        .data(function(d) { return [d];})
        .enter()
          .append("textarea")
          .text(function(d) { return d; })
          .attr("rows", ta_rows)
          .attr("cols", ta_cols);

    divs.exit()
        .transition() // TODO: visual effect
        .duration(1000)
        .remove();
  };

  list.clean = function() {
    d3.select("#main")
      .selectAll("div")
      .remove();
    list.data = [];
  };


  list.add = function(element) {
    list.data.push(element);
    update();
    return list;
  };

  list.remove = function(element) {
    for (var i=0; i<list.data.length; ++i)
      if (list.data[i] === element)
        list.data.splice(i, 1);
    update();
    return list;
  };

  return list;
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
