#!/usr/bin/env node

var assert = require('assert');

var DRD = DRD || {};

DRD.is_rotation = function is_rotation(s1, s2) {
    var _cc = s1 + s2;

    if (s1.length < s2.length)
      return false;
    else
      return (s1.indexOf(s2) != -1);
};

assert(!DRD.is_rotation("David", "zzzavi"));
assert(DRD.is_rotation("David", "avi"));
assert(DRD.is_rotation("David", "David"));
assert(!DRD.is_rotation("David", "Av"));
assert(DRD.is_rotation("David", ""));
