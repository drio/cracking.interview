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


if __name__ == '__main__':
  	unittest.main()

