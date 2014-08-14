# vim: set ts=4 noet:
#
import unittest
import sorting

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




if __name__ == '__main__':
  	unittest.main()

