# vim: set ts=4 noet:
#
import unittest
import sorting
import coin_change
import recursion

class SortTest(unittest.TestCase):
	def test_isort(self):
		sa = self.assertEqual
		l = [3, 100, 2, 34, 4]
		sorting.isort(l)
		sa(sorted(l), l)

		l = []
		sorting.isort(l)
		sa(sorted(l), l)

		l = [3, 3, 2, 34, 2, 4]
		sorting.isort(l)
		sa(sorted(l), l)

		l = [4545, 454, 4, 3, 34, 2, 234, -23]
		sorting.isort(l)
		sa(sorted(l), l)

	def test_qsort_core(self):
		sa = self.assertEqual
		l = [3, 10, 2, 15, 4]
		sorting.qsort(l, 0, len(l))
		l = [4545, 454, 4, 3, 34, 2, 234, -23]
		sorting.qsort(l, 0, len(l))
		l = []
		sorting.qsort(l, 0, len(l))
		l = [1]
		sorting.qsort(l, 0, len(l))

class ChangeTest(unittest.TestCase):

	def test_change(self):
		sa = self.assertEqual
		sa(1, 1)
		sa(3, coin_change.rec_change(10, [4,5,7], 10))

class BasicTests(unittest.TestCase):
	def test_fibo(self):
		sa = self.assertEqual
		sa(0, recursion.fibo(0))
		sa(1, recursion.fibo(1))
		sa(1, recursion.fibo(2))
		sa(2, recursion.fibo(3))
		sa(3, recursion.fibo(4))
		sa(5, recursion.fibo(5))
		sa(8, recursion.fibo(6))

		l = recursion.allFibo(6)
		sa(0, l[0])
		sa(1, l[1])
		sa(5, l[5])
		sa(8, l[6])

		rl= recursion.itFibo(6)
		sa(0, rl[0])
		sa(1, rl[1])
		sa(5, rl[5])
		sa(8, rl[6])

	def test_factorial(self):
		sa = self.assertEqual
		sa(120, recursion.factorial(5))
		sa(2, recursion.factorial(2))

		l = recursion.allFactorials(5)
		sa(1, l[0])
		sa(1, l[1])
		sa(2, l[2])
		sa(6, l[3])
		sa(24, l[4])
		sa(120, l[5])

		sa(1, recursion.itFactorial(0))
		sa(1, recursion.itFactorial(1))
		sa(120, recursion.itFactorial(5))

if __name__ == '__main__':
  	unittest.main()

