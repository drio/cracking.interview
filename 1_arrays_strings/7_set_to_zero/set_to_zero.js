(function() {

var m = [];

m.random = function(n_rows, n_cols) {
  var m = this;

  for (r=0; r<n_rows; r++) {
    m[r] = [];
    for (c=0; c<n_cols; c++)
      m[r][c] = Math.floor((Math.random()*9)+1);
  }
};

// Write an algorithm such that if an element in an MxN matrix is 0, its entire
// row and column is set to 0
// Time complexity: O(MN)
// Mem complexity: O(M+N)
m.set_to_zero = function() {
  var m = this,
      c,r, // hoisting; JS the good parts, pag 113
      n_rows = m.length,
      n_cols,
      zr = {}, zc = {}; // locations of the zeros

  // Check for null matrix
  if (n_rows === 0) return;
  n_cols = m[0].length;

  // Find the zeros
  for (r=0; r<n_rows; r++) {
    for (c=0; c<n_cols; c++) {
      if (m[r][c] === 0) {
        zr[r] = true;
        zc[c] = true;
      }
    }
  }

  // Set the zeros
  for (r=0; r<n_rows; r++)
    for (c=0; c<n_cols; c++)
      if (zr[r] || zc[c])
        m[r][c] = 0;
};

m.flat = function() {
  var m = this, f = [];

  for (var r=0; r<m.length; r++)
    for (var c=0; c<m[0].length; c++)
      f.push([r, c, m[r][c]]);

  return f;
};

var viz = function() {
  var viz = {},
      width = 600, height = 600,
      x_g   = 20, y_g = 20,
      sep = 20,
      svg, text, numbers;

  function update() {
    numbers.data(m.flat())
      .text(function(d) { return d[2]; });
  }

  viz.init = function() {
    svg = d3.select("body")
            .append("svg")
              .attr("width", width)
              .attr("height", height)
              .append("g")
                .attr("transform", "translate(" + x_g + "," + y_g + ")");

    text = svg.append("text");

    numbers = text.selectAll("tspan")
      .data(m.flat())
      .enter()
      .append("tspan")
        .text(function(d) { return d[2]; })
        .attr("x", function(d) { return sep * d[1]; })
        .attr("y", function(d) { return sep * d[0]; })
        .on("click", function(d) {
          m[d[0]][d[1]] = 0;
          m.set_to_zero();
          update();
        });
  };

  return viz;
}();

m.random(20, 20);
viz.init();

})();
