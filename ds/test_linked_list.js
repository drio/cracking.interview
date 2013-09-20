#!/usr/bin/env node

var assert = require('assert'),
    ll = require('./linked_list');

// Basic create/add/next
ml = ll.create();
assert(ml.empty());

assert(!ml.next());
ml.add(1);
assert(!ml.empty());
assert(ml.next().data === 1);
ml.add(2);
assert(ml.next().data === 2);
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
assert(ml.next().data === 3);
assert(ml.next().data === 2);
assert(ml.next().data === 1);
assert(ml.rm() === 1);
assert(ml.next() === null);

ml = ll.create();
ml.add(1).add(2);
ml.next();
assert(ml.rm() === 2);
//console.log(ml.toArray());

ml = ll.create();
ml.add(1).add(2).add(3);
ml.next();
assert(ml.next().data === 2);
assert(ml.rm() === 2);

ml = ll.create();
ml.add(1).add(2).add(23).add(45).add(1).add(2);
ml.rewind();
assert(ml.next().data === 2);
assert(ml.next().data === 1);
assert(ml.next().data === 45);
assert(ml.next().data === 23);
assert(ml.next().data === 2);
assert(ml.rm() === 2);
assert(ml.next().data === 1);
assert(ml.rm() === 1);

function test_nth() {
  var i, ml = ll.create();

  for (i=5; i>=0; i--)
    ml.add(i);
  assert(!ml.empty());

  first = ml.next();
  assert(first.data === 0);

  for (i=0; i>=5; i++)
    assert(ml.n_th(first, i) === i);
}

test_nth();

