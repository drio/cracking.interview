# vim: set ts=4 noet:
#
import sorting
from recursion import itFactorial as factorial

swap = sorting.swap

def allPermu(l, lp=set([]), p=0):
	if p >= len(l):
		lp.add(''.join(l))
		return

	for i in range(p, len(l)):
		swap(l, p, i)
		allPermu(l, lp, p+1)
		swap(l, p, i)

def iterAllPermu(l):
	n = len(l)
	r = len(l)

	for i in range(n):
		for j in range(n):
			print l[i] + " " + l[j]

def factRep(n):
	i = 12
	while factorial(i) > n and i > 0:
		i-=1

	result = []
	for j in range(i, -1, -1):
		fact = factorial(j)
		coef = n / fact
		result.append(coef)
		n = n % fact

	return result

def factToPerm(l, f):
	copy_l = list(l)
	result = []
	f_padded = [0] * (len(l)-len(f)) + f
	for i in f_padded:
		result.append(copy_l[i])
		del copy_l[i]
	return result

def iteratorPerm(input_list):
	max_num_perm = factorial(len(input_list))
	i = [-1]
	def closure():
		i[0] += 1
		if i[0] >= max_num_perm:
			return None
		else:
			fr = factRep(i[0])
			return factToPerm(input_list, fr)
	return closure
