#!/usr/bin/env python
#
import sys

# time complexity: O(n)
# mem  complexity: O(n)
def one(s):
  return ''.join([ s[i] for i in range(len(s)-1, -1, -1) ])

# time complexity: O(n)
# mem  complexity: O(1)
def two(l):
  for i in range(0, len(l)):
    j = len(l) - i - 1
    if i >= len(l)/2:
      break
    l[i], l[j] = l[j], l[i]
  return ''.join(l)

for s in [ "abcd", "abc" ]:
  l = list(s)
  print s, two(l), one(s)
  assert(two(list(s)) ==  one(s))
