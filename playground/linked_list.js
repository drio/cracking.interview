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

  ll.push = function(e) {
    var new_element = { data: e, next: null };
    if (ll.empty())
      ll.first = new_element;
    else
      ll.last.next = new_element;
    ll.last = new_element;
  };

  return ll;
}
