# vim: set ts=4 noet:
#
import unittest
import stack

class StackTest(unittest.TestCase):
	def test_basic_push(self):
		ae = self.assertEqual
		s = stack.Stack()
		ae(1, s.push(1))
		ae(2, s.push(2))

	def test_basic_pop(self):
		ae = self.assertEqual
		s = stack.Stack()
		ae(None, s.pop())

	def test_max(self):
		ae = self.assertEqual
		s = stack.Stack()
		for i in range(0,100):
			ae(i, s.push(i))

		ae(None, s.push(100))



if __name__ == '__main__':
  	unittest.main()

