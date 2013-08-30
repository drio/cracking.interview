#!/usr/bin/env python
#
import sys
from collections import defaultdict

# Time complexity: O(n)
# mem  complexity: O(n)
def replace(l, rs="%20"):
  new = []
  for c in l:
    if c == ' ':
      new.append(rs)
    else:
      new.append(c)
  return ''.join(new)

def tester(s, truth):
  l = list(s)
  new = replace(l)
  print "OK" if new == truth else "WRONG!", s, new
  assert(new == truth)

# Main
tester("david", "david")
tester("fo o", "fo%20o")
tester("foo ", "foo%20")
tester(" foo ", "%20foo%20")
tester(" foo", "%20foo")
