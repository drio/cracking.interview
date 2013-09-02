#!/usr/bin/env python
#
import sys
from collections import defaultdict

def rotate(m):
  _len = len(m)
  for layer in range(0, _len/2):
    first = layer
    last = _len - 1 - layer
    for i in range(first, last):
      off = i - first
      # save it for later
      top = m[first][i]
      # top <- left
      m[first][i] = m[last - off][first]
      # left <- bottom
      m[last-off][first] = m[last][last - off]
      # bottom <- right
      m[last][last - off] = m[i][last]
      # right <- saved top
      m[i][last] = top

def pp(m):
  print "\n".join(["\t".join(map(str, r)) for r in m])
  print ""

def gen_matrix(_len):
  m = []
  for i in range(0,_len):
    m.append([0] * _len)
    for j in range(0,_len):
      m[i][j] = i*_len + j
  return m

m = gen_matrix(5)
pp(m); rotate(m); pp(m)

