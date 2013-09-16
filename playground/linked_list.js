exports.create = create;

function create(spec) {
  var ll = function() {};

  var first, last, current, end_reached;

  function init() {
    first       = null;
    last        = null;
    current     = null;
    end_reached = false;
  }

  init();

  ll.rewind = function() {
    current = null;
    end_reached = false;
    return ll;
  };

  ll.empty = function() {
    return (first === null);
  };

  // Move the current pointer to the next element in the list
  ll.next = function() {
    if (ll.empty())
      return null;
    else if (!current && end_reached) // At the end and asking to move
      return null;
    else if (!current && !end_reached)
      current = first;
    else {
      current = current.next;
      if (!current) end_reached = true;
    }

    return current ? current.data : null;
  };

  // Add e right after current
  ll.add = function(e) {
    var new_element = { data: e, next: null };

    if (ll.empty()) {
      first = new_element;
      last  = new_element;
    }
    else {
      if (current) {
        new_element.next = current.next;
        current.next  = new_element;
        if (current === last)
          last = new_element;
      }
      else { // current not set, insert at the beginning
        new_element.next = first;
        first = new_element;
      }
    }

    return ll;
  };

  ll.rm = function() {
    var p, e;
    if (ll.empty()) return null;
    if (!current) return null;
    if (first === current) {
      e = first.data;
      init();
    }
    else {
      p = { next:first };
      while (p.next !== current)
        p = p.next;
      if (p.next === last)
        last = p;
      e = p.next.data;
      p.next = p.next.next;
    }

    return e;
  };

  return ll;
}
