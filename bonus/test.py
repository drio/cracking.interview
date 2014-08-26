# vim: set ts=4 noet:
#
import unittest
import sorting
import coin_change
import recursion
import search
import permutations
import random
import bitman

class PermuTest(unittest.TestCase):

	def test_factoradic(self):
		sa = self.assertEqual
		sa([0], permutations.factRep(0))
		sa([1,0], permutations.factRep(1))
		sa([1,0, 0], permutations.factRep(2))
		sa([1,1, 0], permutations.factRep(3))
		sa([2,0, 0], permutations.factRep(4))

		_ = permutations.factToPerm([0,1,2,3,4,5,6], [4,0,4,1,0,0,0])
		sa([4,0,6,2,1,3,5], _)

		sa(permutations.factRep(463), [3, 4,1, 0, 1, 0])

		l = list("abcd")
		it = permutations.iteratorPerm(l)
		s = set([])
		for i in range(0, permutations.factorial(len(l))):
			s.add(''.join(it()))
		sa(24, len(s))

	def test_Permu(self):
		sa = self.assertEqual
		st = set([])
		permutations.allPermu(list("abcd"), st)
		sa(24, len(st))

		st = set([])
		permutations.allPermu(list("abcde"), st)
		#for p in lp: print p


class SearchTest(unittest.TestCase):
	def test_BS(self):
		sa = self.assertEqual
		l = range(0,100000)
		sa(3, search.binarySearch(l, 3))
		sa(9, search.binarySearch(l, 9))
		sa(0, search.binarySearch(l, 0))
		sa(100, search.binarySearch(l, 100))

		sa(3, search.binarySearch(l, 3, "rec"))
		sa(9, search.binarySearch(l, 9), "rec")
		sa(0, search.binarySearch(l, 0), "rec")
		sa(100, search.binarySearch(l, 100), "rec")

class TestBitMan(unittest.TestCase):
	def test_bucket_sort(self):
		sa = self.assertEqual

		sa(bitman.i_to_bin(2), [1, 0])
		for i in range(0, 1000):
			t = map(lambda e: int(e), list("{0:b}".format(i)))
			sa(bitman.i_to_bin(i), t)

	def test_msb(self):
		sa = self.assertEqual
		sa(bitman.msb(8, 2), [1, 0])
		sa(bitman.msb(123, 3), [1, 1, 1])
		sa(bitman.msb(3423, 4), [1, 1, 0, 1])

	def test_set_bits(self):
		sa = self.assertEqual
		sa(bitman.set_bits(0b1001, 0b11, 1, 2), 0b1111)
		sa(bitman.set_bits(0b100, 0b11, 1, 2), 0b110)
		sa(bitman.set_bits(0b10000000000, 0b10101, 2, 6), 0b10001010100)

class SortTest(unittest.TestCase):
	def random_list(self, n=10, min=-1000, max=1000):
		l = []
		for i in range(0, n):
			l.append(random.randint(min, max))
		return l

	def test_bucket_sort(self):
		sa = self.assertEqual

		l = [23, 12, 12, 12, 1, 5]
		sl = sorted(l)
		sorting.bucket_sort(l, 2)
		sa(sl, l)

		for i in range(1,100):
			sa = self.assertEqual
			ri = random.randint(10,100)
			l = self.random_list(ri, 0, 120)
			sl = sorted(l)
			sorting.bucket_sort(l, 5)
			sa(sl, l)

		for i in range(1,100):
			sa = self.assertEqual
			ri = random.randint(10,100)
			l = self.random_list(ri, 0, 120)
			sl = sorted(l)
			sorting.bucket_sort(l, 6)
			sa(sl, l)

	def test_count_sort(self):
		sa = self.assertEqual

		l = [23, 12, 12, 12, 1, 5]
		sl = sorted(l)
		sorting.count_sort(l)
		sa(sl, l)

		for i in range(1,100):
			sa = self.assertEqual
			l = self.random_list(random.randint(10,100), 0, 120)
			sl = sorted(l)
			sorting.count_sort(l)
			sa(sl, l)

	def test_merge(self):
		sa = self.assertEqual

		l = [2, 7, 3, 4]
		sl = sorted(l)
		sorting.merge(l, 0, 1, 2, 3)
		sa(sl, l)

		l = [7, 2]
		sl = sorted(l)
		sorting.merge(l, 0, 0, 1, 1)
		sa(sl, l)

		l = [-34, 4 ,4, 5, 120, 200, 300, 400]
		sl = sorted(l)
		sorting.merge(l, 0, 4, 5, 7)
		sa(sl, l)

	def test_msort(self):
		for i in range(1,100):
			sa = self.assertEqual
			l = self.random_list(random.randint(10,100))
			sl = sorted(l)
			sorting.msort(l, 0, len(l)-1)
			sa(sl, l)

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

		if True:
			l = [3, 10, 2, 15, 4]
			sorting.qsort(l, 0, len(l))
			sa(l, sorted(l))

			l = [3, 2, -23]
			sorting.qsort(l, 0, len(l))
			sa(l, sorted(l))

		l = [7, 4, 2, -1]
		sorting.qsort(l, 0, len(l))
		sa(l, sorted(l))

		for i in range(1,100):
			sa = self.assertEqual
			l = self.random_list(random.randint(10,100))
			sl = sorted(l)
			sorting.qsort(l, 0, len(l))
			sa(sl, l)

class ChangeTest(unittest.TestCase):
	def test_change(self):
		sa = self.assertEqual
		sa(1, 1)
		sa(3, coin_change.rec_change(10, [4,5,7], 10))

	def test_dp_change(self):
		sa = self.assertEqual
		l = coin_change.dp_change(5, (2,3))
		sa(2, l[5])
		sa(2, l[4])
		sa(1, l[3])
		sa(0, l[0])
		sa(coin_change.inf, l[1])



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

