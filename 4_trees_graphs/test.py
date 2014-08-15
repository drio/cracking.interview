# vim: set ts=4 noet:
#
import unittest
import trees

class TreeTest(unittest.TestCase):
	def test_insert(self):
		ae = self.assertEqual
		t = trees.BST()
		l = [5, 1, 7, 6, 2]
		t.insert(5)
		ae(t.root.data, 5)

		t.insert(1)
		ae(t.root.left.data, 1)

		t.insert(7)
		ae(t.root.right.data, 7)

		t.insert(6)
		ae(t.root.right.left.data, 6)

		t.insert(2)
		ae(t.root.left.right.data, 2)

	def test_walk(self):
		ae = self.assertEqual
		t = trees.BST()
		l = [5, 1, 7, 6, 2]
		for i in l:
			t.insert(i)

		wl = []
		t.walk(t.root, wl)
		ae(sorted(l), wl)

	def test_search(self):
		ae = self.assertEqual
		t = trees.BST()
		l = [5, 1, 7, 6, 2]
		for i in l:
			t.insert(i)

		ae(7, t.search(t.root, 7).data)
		ae(2, t.search(t.root, 2).data)
		ae(None, t.search(t.root, 12))

	def test_size_per_levels(self):
		ae = self.assertEqual
		t = trees.BST()
		l = [5, 1, 7, 6, 2, 8]
		for i in l:
			t.insert(i)

		d = {}
		t.size_per_levels(t.root, d)
		ae(1, d[0])
		ae(2, d[1])
		ae(3, d[2])

	def test_same_shape(self):
		ae = self.assertEqual
		t1 = trees.BST()
		l = [5, 1, 7, 6, 2]
		for i in l:
			t1.insert(i)

		t2 = trees.BST()
		l = [5, 1, 7, 6, 2]
		for i in l:
			t2.insert(i)
		ae(True, t1.same_shape(t2))

		t2 = trees.BST()
		l = [5, 1, 7, 6, 2, 8]
		for i in l:
			t2.insert(i)
		ae(False, t1.same_shape(t2))

if __name__ == '__main__':
  	unittest.main()

