# vim: set ts=4 noet:

def i_to_bin(n):
    if n == 0:
        return [0]

    bin_l = []
    i = n
    while i:
		bin_l.insert(0, i & 1)
		i = i >> 1

    return bin_l

def msb(n, k):
	return i_to_bin(n)[0:k]
