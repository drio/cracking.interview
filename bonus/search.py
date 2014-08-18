# vim: set ts=4 noet:
#
def binarySearch(l, n, engine="iter"):
	if engine == "iter":
   		return doBinarySearch(l, n, 0, len(l)-1)
	else:
		return doRecBinarySearch(l, n, 0, len(l)-1)

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

def doRecBinarySearch(sl, t, l, u):
	if l > u:
		return -1

	m = (l + u)/2

	if sl[m] == t:
		return m
	if sl[m] < t:
		return doRecBinarySearch(sl, t, m+1, u)
	else:
		return doRecBinarySearch(sl, t, l, m-1)

