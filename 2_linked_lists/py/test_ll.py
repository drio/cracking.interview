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


if __name__ == '__main__':
  unittest.main()
