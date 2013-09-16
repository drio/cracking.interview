#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

// Basic create/add/next
ml = ll.create();
assert(ml.empty());

assert(!ml.next());
ml.add(1);
assert(!ml.empty());
assert(ml.next() === 1);
ml.add(2);
assert(ml.next() === 2);
assert(!ml.next());
assert(!ml.next());

ml = ll.create();
assert(!ml.rm());
ml.add(1);
assert(!ml.rm());
ml.next();
assert(ml.rm() === 1);
assert(ml.empty());
ml.add(1).add(2).add(3);
assert(ml.next() === 3);
assert(ml.next() === 2);
assert(ml.rm() === 2);
assert(ml.next() === 1);


