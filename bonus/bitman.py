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

def set_bits(i_input, i_copy, c_start, c_end):
	clean_input = 0
	for i in range(0, (c_end - c_start)+1):
		clean_input = (clean_input << 1) | (i_copy & 1)
		i_copy >>= 1

	return i_input | (clean_input << c_start)
