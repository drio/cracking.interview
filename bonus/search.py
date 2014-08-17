# vim: set ts=4 noet:
#
def binarySearch(l, n):
    return doBinarySearch(l, n, 0, len(l)-1)

def doBinarySearch(sl, t, l, u):

    while True:
        if l > u:
            return -1

    	m = (l + u) / 2

        # t mustbe between x(l,u)
        if sl[m] == t:
            break

        # must recompute the range interval
        if sl[m] < t:
            l = m + 1
        else:
            u = m - 1
    return m
