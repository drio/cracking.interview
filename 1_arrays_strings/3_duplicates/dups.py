#!/usr/bin/env python
#
import sys
from collections import defaultdict

def fi(s):
  """
  Find the locations of the characters we have to remove
  Time complexity: O(n)
  Mem  complexity: O(n/2+n/2) = O(n)
  """
  found_before, i_to_remove = defaultdict(lambda: False), []
  for i,c in enumerate(s):
    if found_before[c]:
      i_to_remove.append(i)
    else:
      found_before[c] = True
  return i_to_remove

def remove(ls, indices):
  """
  Remove duplicates from ls (list version of the string). indices has of the locations of
  the characters to remove in ls
  Time complexity: O(n/2 * n)  = O(n^2)
  Mem  complexity: O(1)
  """
  for i in sorted(indices, reverse=True):
    for j in range(i, len(ls)-1):
      ls[j] = ls[j+1]
    del ls[-1]

  return ''.join(ls)

def tester(s, truth_i, truth_s):
  _fi = fi(s)
  assert(_fi == truth_i)

  l = list(s)
  cleaned = remove(l,_fi)
  print "OK" if cleaned == truth_s else "WRONG!", s, cleaned
  assert(cleaned == truth_s)

# Main
tester("AbcAde", [3], "Abcde")
tester("david", [4], "davi")
tester("FFo", [1], "Fo")
tester("davdd", [3,4], "dav")
