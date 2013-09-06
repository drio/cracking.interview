(function() {

  var result = d3.select("#results"),
      log    = function(msg) { result.text(msg); },
      clear  = function()    { result.text(""); },
      s_sub  = "input[name=submit]",
      s_s1   = "#s1",
      s_s2   = "input[name=s2]",
      color_match = 'red',
      color_no_match = 'black',
      width  = 500, height = 100,
      x_g    = 0, y_g = 60,
      svg, text;

function is_rotation(s1, s2) {
  var _cc = s1 + s1;

  if (s1.length < s2.length) return false;
  return (_cc.indexOf(s2) != -1);
}

function find_interval(s1, s2) {
  var _cc = s1 + s1,
      start = _cc.toUpperCase().indexOf(s2.toUpperCase()),
      i, j, data = [];

  for (i = 0; i < _cc.length; ++i) {
    j = (i < s1.length) ? i : i - s1.length;
    if (i < s1.length)
      data.push([ '', '']);
    data[j][0] = s1[j];
    if (data[j][1] != color_match)
      data[j][1] = (i >= start && i < start + s2.length) ? color_match : color_no_match;
  }

  return data;
}

function init_viz(data) {
  svg = d3.select("body")
          .append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
              .attr("transform", "translate(" + x_g + "," + y_g + ")");

  text = svg.append("text");

  text.selectAll("tspan")
    .data(data)
    .enter()
    .append("tspan")
    .text(function(d) { return d[0]; })
    .attr("fill", function(d) { return d[1]; });
}

function clean() {
  d3.select("svg").remove();
}

function update(data) {
  text.selectAll("tspan")
    .data(data)
    .text(function(d) { return d[0]; })
    .attr("fill", function(d) { return d[1]; });
}

function set_key_events() {
  d3.select(s_s2).on("keyup", function() {
    update(find_interval(d3.select(s_s1).text(), this.value));
  });
}

/* main */
set_key_events();
init_viz(find_interval(d3.select(s_s1).text(),
                       d3.select(s_s2).attr("value")));

}());
