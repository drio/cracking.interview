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

	qsort(pl, l, m)
	qsort(pl, m+1, u)

def merge(i_list, l1, u1, l2, u2):
	tmp_list = [None] * ((u2 - l1)+1)

	# Generic case
	tmp_i, i, j = 0, l1, l2
	while i <= u1 and j <= u2:
		if i_list[i] < i_list[j]:
			tmp_list[tmp_i] = i_list[i]
			i += 1
		else:
			tmp_list[tmp_i] = i_list[j]
			j += 1
		tmp_i += 1

	# Special case, we have finished one of the lists,
	# copy the rest of the other one to the tmp_list
	if i > u1:
		start, end = j, u2
	else:
		start, end = i, u1

	for i in range(start, end+1):
		tmp_list[tmp_i] = i_list[i]
		tmp_i += 1

	# Copy the temp list in to the input list
	j = l1
	for i in range(0, len(tmp_list)):
		i_list[j] = tmp_list[i]
		j += 1


# input_list, lower index, upper index
def msort(i_list, l, u):
	if l >= u:
		return

	middle = (l + (u-l) / 2)
	msort(i_list, l, middle)
	msort(i_list, middle+1, u)

	# Both "lists" are sorted, I have to merge them
	merge(i_list, l, middle, middle+1, u)
