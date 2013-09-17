var app = function() {

  var list = DS.linkedList.create(),
      ta_rows = "1",
      ta_cols = "5",
      _app = {},
      input_val = "";

  function set_listener() {
    d3.select("input").on("keydown", function() {
      if (d3.event.keyCode === 13) {
        app.add(this.value);
        this.value = "";
      }
    });
  }

  set_listener();

  update = function() {
    var divs = d3.select("#main")
      .selectAll("div")
      .data(list.toArray().reverse());

    divs.enter()
        .append("div")
        .text(function(d) { return d;});

    divs.exit()
        .transition() // TODO: visual effect
        .duration(1000)
        .remove();
  };

  _app.clean = function() {
    d3.select("#main")
      .selectAll("div")
      .remove();
    list = DS.linkedList.create();
  };

  _app.add = function(element) {
    list.add(element);
    update();
    return _app;
  };

  _app.remove = function(element) {
    list.rewind();
    var c = list.next();
    while (c) {
      if (c === element) list.rm();
      c = list.next();
    }
    update();
    return list;
  };

  return _app;
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
