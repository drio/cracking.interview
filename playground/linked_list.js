exports.create = create;

function create(spec) {
  var ll = function() {};

  ll.first   = null;
  ll.current = null;

  ll.empty = function() {
    return (ll.first == ll.last && ll.first === null);
  };

  // Move the current pointer to the next element in the list
  ll.next = function() {
    if (ll.empty())
      return null;
    else
      if (ll.current) ll.current = ll.current.next;

    return ll.current;
  };

  // Add e right after current
  ll.add = function(e) {
    var new_element = { data: e, next: null };

    if (ll.empty()) {
      ll.first = new_element;
      ll.current = { next: ll.first};
    }
    else if (!ll.empty() && ll.current === null) {
      new_element.next = ll.first.next;
      ll.first = new_element;
    }
    else {
      new_element.next = ll.current.next;
      ll.current.next  = new_element;
    }

    return ll;
  };

  return ll;
}
