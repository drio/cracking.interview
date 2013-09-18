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

    d3.select("#link_rdups").on("click", function() {
      var foo = _app.remove_dups();
    });
  }

  function flush_ui_list() {
    d3.select("#main").selectAll("div").remove();
  }

  function update() {
    var a = list.toArray().reverse();

    var divs = d3.select("#main")
      .selectAll("div")
      .data(a);

    divs.enter()
        .append("div")
        .text(function(d) { return d;});

    divs.exit()
        .transition() // TODO: visual effect
        .duration(1000)
        .remove();
  }

  _app.remove_dups = function() {
    var h = {}, e;
    list.rewind();
    e = list.next();
    while (e) {
      if (h[e])
        list.rm();
      else
        h[e] = true;
      e = list.next();
    }
    flush_ui_list();
    list.rewind();
    update();
    return list;
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

  document.getElementById('input').focus();
  set_listener();
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
