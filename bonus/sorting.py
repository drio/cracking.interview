# vim: set ts=4 noet:
#
def swap(pl, i, j):
	pl[i], pl[j] = pl[j], pl[i]

# Insert sort: O(n^2)
def isort(l):
    for i, e in enumerate(l):
        s = i+1
        for j in range(s, len(l)):
            if l[j] < l[i]:
              	swap(l,i,j)


def qsort(pl, l, u): # python list, lower, uper
	if l >= u:
		return

	m = l
	for i in range(l+1, u):
		if pl[i] < pl[l]:
			m += 1
			swap(pl, i, m)
	swap(pl, l, m)

	print ">> ", pl

	qsort(pl, l, m)
	qsort(pl, m+1, u)
