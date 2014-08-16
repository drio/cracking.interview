# vim: set ts=4 noet:

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



