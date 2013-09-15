exports.create = create;

function create(spec) {
  var ll = function() {};

  ll.talk = function() {
    console.log("Yes: " + spec);
  };

  ll.first = null;
  ll.last  = null;

  ll.empty = function() {
    return (ll.first == ll.last && ll.first === null && ll.last === null);
  };

  ll.add = function(e) {
    var new_element = { data: e, next: null };
    if (ll.empty())
      ll.first = new_element;
    else
      ll.last.next = new_element;
    ll.last = new_element;

    return ll;
  };

  // Time Cost O(n)
  // returns the number of elements removed
  ll.rm = function(e_to_rm) {
    var n_del = 0,
        curr,
        prev;

    if (ll.empty())
      return 0;

    if (ll.first === ll.last && ll.first.data === e_to_rm) {
      ll.first = null;
      ll.last = null;
      return 1;
    }

    // common case
    curr = ll.first;
    prev = null;
    while (curr !== null) {
      if (curr.data === e_to_rm) {
        n_del += 1;
        prev.next = curr.next;
        curr = curr.next;
        if (curr === null)
          ll.last = prev;
      }
      else {
        prev = curr;
        curr = curr.next;
      }
    }

    return n_del;
  };

  return ll;
}
