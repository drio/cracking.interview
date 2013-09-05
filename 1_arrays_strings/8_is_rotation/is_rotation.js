var DRD = DRD || {};

DRD.is_rotation = function(s1, s2) {
  var _cc = s1 + s1;

  console.log(_cc);
  if (s1.length < s2.length) return false;
  return (_cc.indexOf(s2) != -1);
};

DRD.init = function() {
  var result = d3.select("#results"),
      log = function(msg) { result.text(msg); },
      clear = function() { result.text(""); };

  log("Introduce strings and click submit.");

  d3.select("input[name=submit]").on('click', function() {
    var get_val = function(sel) { return d3.select(sel).property("value"); };

    clear();
    log(DRD.is_rotation(get_val("input[name=s1]"), get_val("input[name=s2")));
  });
};
