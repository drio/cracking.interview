(function() {

// Detect javascript engine
if (typeof module !== 'undefined' && module.exports)
  exports.create = create;
else {
  DS = window.DS || {};
  DS.linkedList = {create:create};
}

function create(spec) {
  var ll = function() {};

  var first, last, current;

  function init() {
    last    = {data: null, next: null};
    first   = {data: null, next: last};
    current = first;
  }

  init();

  ll.info = function() {
    var log = console.log;
    log(first);
    log(last);
    log(current);
  };

  ll.toArray = function() {
    var p = first, a = [];
    while (p) {
      if (p.data) a.push(p.data);
      p = p.next;
    }
    return a;
  };

  ll.rewind = function() {
    current = first;
    return ll;
  };

  ll.empty = function() {
    return (first.next === last);
  };

  // Move the current pointer to the next element in the list
  ll.next = function() {
    if (ll.empty() || current.next === last)
      return null;
    else
      current = current.next;

    return current ? current.data : null;
  };

  // Add e right after current
  ll.add = function(e) {
    var new_element = { data: e, next: null };

    if (ll.empty()) {
      first.next = new_element;
      new_element.next = last;
    }
    else {
      new_element.next = current.next;
      current.next  = new_element;
    }

    return ll;
  };

  ll.rm = function() {
    var p, e;
    if (ll.empty() || current === first)
      return null;
    else {
      p = first;
      while (p.next !== current)
        p = p.next;
      e = p.next.data;
      p.next = p.next.next;
      // set new current
      if (ll.empty())
        current = first;
      else {
        if (current.next === last) current = p;
        else current = p.next.next;
      }
    }

    return e;
  };

  return ll;
}

})();
