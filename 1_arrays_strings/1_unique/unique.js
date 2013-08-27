var _run = function() {
  var log    = console.log,
      assert = require('assert');

  // Assumes s is ascii encoded and range of values is a..z
  var unique = function(s) {
    var checker = 0, c, char_already_seen;
    for (var i=0; i<s.length; i++) {
      c                 = s.charCodeAt(i) - 'a'.charCodeAt(0),
      char_already_seen = ((1 << c) & checker) > 0;
      if (char_already_seen) return false;
      checker |= (1 << c); // Update the bit vector
    }
    return true;
  };

  if (process.argv.length != 3) {
    assert(unique("abcd"));
    assert(!unique("foo"));
    assert(!unique("david"));
  } else {
    var input_string = process.argv[2];
    unique(input_string);
  }
};

_run();
