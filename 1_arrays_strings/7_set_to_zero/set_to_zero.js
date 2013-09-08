(function() {
// Write an algorithm such that if an element in an MxN matrix is 0, its entire
// row and column is set to 0
// Time complexity: O(MN)
// Mem complexity: O(M+N)
function set_to_zero (m) {
  var c,r, // hoisting; JS the good parts, pag 113
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

  return m;
}

var m = [ [ 1,2 ],
          [ 4,5 ],
          [ 7,8 ] ];

console.log(set_to_zero(m));
})();
