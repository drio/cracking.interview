# -*- coding: utf-8 -*-
#
# 1,$s/'/'/g
# 1,$s/'/'/g

# time cost: O(n)
# space cost: O(n)
def non_rep(input_s):
    d = {}
    for c in input_s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in input_s:
        if d[c] == 1:
            return c

def non_rep_v2(input_s):
    d = [0] * 52000

    for c in input_s:
        d[ord(c)] += 1

    for c in input_s:
        if d[ord(c)] == 1:
            return c

nrep = non_rep_v2

assert(nrep("total") == "o")
assert(nrep("teeter") == "r")
assert(nrep(u"あいヨヨあ") == u"い")
