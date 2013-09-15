#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

ml = ll.create();
assert(ml.empty());

ml.push(1);
assert(!ml.empty());

assert(ml.first.data === 1);
assert(ml.last.data === 1);

ml.push(2);
assert(ml.first.data === 1);
assert(ml.last.data === 2);

