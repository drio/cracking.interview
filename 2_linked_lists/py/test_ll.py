# vim: set ts=4 noet:
#
import unittest
import linked_list

class LinkedListTest(unittest.TestCase):
	def basic_list(self):
		return None

	def test_insert(self):
		ae = self.assertEqual
		ll = linked_list.LinkedList()
		ae(0, ll.size)
		ll.insert("A")
		ae(1, ll.size)
		ll.insert("B")
		ae(2, ll.size)

	def test_delete(self):
		ae = self.assertEqual
		ll = linked_list.LinkedList()
		ll.insert("A")
		ll.insert("B")
		ll.insert("C")

		ae(False, ll.delete("D"))

		ae(3, ll.size)
		ae("A", ll.delete("A"))
		ae(2, ll.size)

		ae("B", ll.delete("B"))
		ae(1, ll.size)

		ae("C", ll.delete("C"))
		ae(0, ll.size)

		ae(False, ll.delete("X"))
		ae(0, ll.size)

	def test_n_to_last(self):
		ae = self.assertEqual
		ll = linked_list.LinkedList()
		l = [ "A", "B", "C", "D" ]
		for e in l:
			ll.insert(e)
		ae("A", ll.n_to_last(0).data)
		ae("B", ll.n_to_last(1).data)
		ae("C", ll.n_to_last(2).data)
		ae("D", ll.n_to_last(3).data)
		ae(None, ll.n_to_last(4))

		ll = linked_list.LinkedList()
		ae(None, ll.n_to_last(4))
		ae(None, ll.n_to_last(0))


	def test_remove_dups(self):
		ae = self.assertEqual
		ll = linked_list.LinkedList()
		ll.insert("A")
		ll.insert("B")
		ll.insert("A")
		ll.insert("B")
		ll.insert("C")
		ll.remove_dups()
		ae(["C", "B", "A"], ll.plist())

		ll = linked_list.LinkedList()
		ll.insert("A")
		ll.insert("A")
		ll.insert("A")
		ll.remove_dups()
		ae(["A"], ll.plist())

		ll = linked_list.LinkedList()
		ll.insert("A")
		ll.insert("C")
		ll.insert("A")
		ll.remove_dups()
		ae(["A", "C"], ll.plist())


if __name__ == '__main__':
  unittest.main()
