#!/usr/bin/env python
#
import sys
#
# Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?
#
def is_unique(s):
  """
  Using a hash table we get O(n)/O(n) for both Time complexity and Space complexity.
  """
  d = {}
  for c in s:
    if c in d:
      return False
    d[c] = 1
  return True

def is_unique2(s):
  """
  We don't know the internal implementation of the sorting, it may use extra memory.
  Time complexity should be nlog(n) ; merge short
  """
  prev = None
  for c in sorted(s):
    if prev == c:
      return False
    prev = c
  return True

def is_unique3(s):
  """
  Here we take advantage to the fact the characters are ascii. We use a bit vector to
  keep track of what characters we have already seen.
  time comp: O(n)
  mem  comp: O(1)
  NOTE: we force the input charaters to be upper case!
  """
  s = s.lower()
  checker = 0
  for c in (s):
    val = ord(c) - ord('a')
    if checker & (1 << val) > 0:
      return False
    checker |= (1 << val)
  return True

if len(sys.argv) == 2:
  s = sys.argv[1]
  print s, "Unique? ", is_unique3(s)
else:
  for f in is_unique, is_unique2, is_unique3:
    print f
    assert not f("foo")
    assert not f("david")
    assert f("abcde")
