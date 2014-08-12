# vim: set ts=4 noet:
#
class Stack(object):
	def __init__(self):
		self.max_size = 100
		self.array = [None] * self.max_size
		self.top = -1

	def push(self, e):
		if self.top == self.max_size - 1:
			return None
		else:
			self.top += 1
			self.array[self.top] = e
			return e

	def pop(self):
		self.top -= 1
		if self.top == -2:
			return None
		else:
			return self.array[self.top + 1]
