#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

// Basic create/add/next
ml = ll.create();
assert(ml.empty());
ml.add(1);
ml.add(2);

assert(ml.next().data === 2);
assert(ml.next().data === 1);
assert(!ml.next());

// More create/add/next but now playing with next to insert in order
ml = ll.create();
assert(ml.empty());
ml.add(1);
ml.next();
ml.add(2);

ml.rewind();
assert(ml.next().data === 1);
assert(ml.next().data === 2);
assert(!ml.next());
