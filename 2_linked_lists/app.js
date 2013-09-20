var app = function() {

  var list = DS.linkedList.create(),
      ta_rows = "1",
      ta_cols = "5",
      _app = {};

  function input_val(n) {
    var id = (n === undefined) ? "input1" : "input" + n;
    return document.getElementById(id).value;
  }

  function set_listener() {
    d3.select("#input1").on("keydown", function() {
      if (d3.event.keyCode === 13) {
        app.add(input_val());
        this.value = "";
      }
    });

    d3.select("#link_rdups").on("click", _app.remove_dups);
    d3.select("#input2").on("keydown", function() {
      if (d3.event.keyCode === 13) {
        app.nth(input_val(2));
      }
    });
  }

  function flush_ui_list() {
    d3.select("#main").selectAll("div").remove();
  }

  function update() {
    var a = list.toArray().reverse();

    console.log(a);
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

  _app.nth = function() {
    var n = input_val(2),
        e = list.n_th(list.next(), n);
    console.log(">> " + n + " element to last is: " + e);
    d3.select("#info").text(n + " element to last is: " + e);
    document.getElementById("input2").value = "";
    list.rewind();
  };

  _app.remove_dups = function() {
    var h = {}, curr;
    list.rewind();
    curr = list.next();
    while (curr) {
      if (h[curr.data])
        list.rm();
      else
        h[curr.data] = true;
      curr = list.next();
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

  document.getElementById('input1').focus();
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
