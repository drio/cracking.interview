#!/usr/bin/env python
#
import sys
from collections import defaultdict

# Time complexity: O(n)
# Mem  complexity: O(n)
def is_anagram(l1, l2):
  d = defaultdict(lambda: 0)
  for c in l1:
    d[c] += 1

  d2 = defaultdict(lambda: 0)
  for c in l2:
    d2[c] += 1

  for c, n in d.items():
    if n != d2[c]:
      return False

  return True

def tester(i1, i2, truth):
  l1, l2 = list(i1), list(i2)
  r = is_anagram(l1, l2)
  print i1 + " |", i2, truth, "==", r
  assert(truth == r)

# Main
tester("army", "mary", True)
tester("abcde", "edcba", True)
tester("army", "marym", False)
tester("army", "aaaa", False)
