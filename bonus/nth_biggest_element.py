# vim: set ts=4 noet:
# Find kth largest number in an array of N numbers

# Time cost: O(nlog(n))
# Space cost: O(n) since I am creating a new list for sorting
def find_kth(l, k):
    if len(l) == 0: return None

    p = 0
    up = 0
    sl = sorted(l)

    while p < len(sl):
        if up == k:
            return sl[p]
        else:
            prev = sl[p]
            p += 1
            while p < len(sl) and prev == sl[p]:
                p += 1
            up += 1

    return None

assert( find_kth([2, 12, 4, 1], 2) == 4 )
assert( find_kth([2, 12, 4, 1], 0) == 1 )
assert( find_kth([], 2) == None )
assert( find_kth([45, 34], 10) == None )
assert( find_kth([45, 34], 10) == None )
assert( find_kth([2, 2, 12, 4, 1], 0) == 1 )
assert( find_kth([2, 2, 12, 4, 1], 1) == 2 )
assert( find_kth([2, 2, 12, 4, 1], 2) == 4 )
assert( find_kth([2, 2, 12, 4, 1], 12) == None )
assert( find_kth([2, 2, 2], 2) == None )
assert( find_kth([2, 2, 2], 0) == 2 )

