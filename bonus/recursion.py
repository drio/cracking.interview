# vim: set ts=4 noet:

# <n> is number of disks
# move <p_from> peg, disc <p_to>
# <p_names> is a hash of with the names of the pegs [A,B,C]
def hanoi(pegs, p_from, p_to, n):
	# helper to print the string for an action (move peg)
	def move(disk_num, _from, _to):
		print "move disk %s from peg %s to peg %s" % (disk_num, _from, _to)

	# Given a from and to, tell me the other peg to use
	def find_tmp_peg(_from, _to):
		return [i for i in pegs if i != _from and i != _to][0]

	# Main function, base case, there is only 1 disk to move
	if n == 1:
		move(n, p_from, p_to)
	# recursion case:
	# Move n-1 disk to the temporary peg (tmp_to)
	# now you can move disk n to the p_to peg (the destination peg)
	# And finally move all the disks in the temporary peg to the p_to peg
	else:
		tmp_to = find_tmp_peg(p_from, p_to)
		hanoi(pegs, p_from, tmp_to, n-1)
		move(n, p_from, p_to)
		hanoi(pegs, tmp_to, p_to, n-1)

def factorial(n):
	if n < 2:
		return 1

	return n * factorial(n-1)

def allFactorials(n):
	l = [1] * (n+1)
	doFactorial(n, l)
	return l

def doFactorial(n, l):
	if n < 2:
		l[n] = 1
	else:
		doFactorial(n-1, l)
		l[n] = n * l[n-1]

def itFactorial(n):
	if n == 0:
		return 1

	c = 1
	for i in range(1, n+1):
		c = c * i

	return c

def allFibo(n):
	l = [0] * (n + 1)
	doFibo(l, n)
	return l

def doFibo(l, n):
	for i in range(0, n+1):
		l[i] = fibo(i)

def fibo(n):
	if n == 0:
		return 0
	if n < 2:
		return 1

	return fibo(n-1) + fibo(n-2)

def itFibo(n):
	l = [0] * (n + 1)
	for i in range(0, n+1):
		if i == 0:
			l[i] = 0
		elif i == 1:
			l[i] = 1
		else:
			l[i] = l[i-1] + l[i-2]
	return l



