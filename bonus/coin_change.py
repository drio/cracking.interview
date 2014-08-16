# vim: set ts=4 noet:
# Find kth largest number in an array of N numbers

inf = 10000000

def rec_change(m, c, d):
    if d < 0:
        return inf

    if d == 0:
        return 1

    best = inf
    for cc in c:
		if d-cc >= 0:
			_ = rec_change(m, c, d-cc)
			if _ < best:
				best = _
    return 1 + best
