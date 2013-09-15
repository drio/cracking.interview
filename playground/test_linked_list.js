#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

ml = ll.create();
assert(ml.empty());
ml.add(1);
ml.add(2);

assert(ml.next().data === 2);
assert(ml.next().data === 1);
assert(ml.next() === null);
assert(ml.next() === null);
