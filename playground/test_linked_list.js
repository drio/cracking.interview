#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

ml = ll.create();
assert(ml.empty());

ml.add(1);
assert(!ml.empty());

assert(ml.first.data === 1);
assert(ml.last.data === 1);

ml.add(2);
assert(ml.first.data === 1);
assert(ml.last.data === 2);

ml.add(3); // 1,2,3

assert(ml.rm(2) === 1);
assert(ml.first.data === 1);
assert(ml.last.data === 3);

assert(ml.rm(3) === 1);
assert(ml.last.data === 1);
assert(ml.first.data === 1);

assert(ml.rm(12) === 0);

assert(ml.rm(1) === 1);
assert(ml.rm(12) === 0);

ml.add(1).add(2).add(2);
assert(ml.rm(2) === 2);

assert(ml.first.data === 1);
assert(ml.last.data === 1);
ml.rm(1);
assert(ml.empty());

