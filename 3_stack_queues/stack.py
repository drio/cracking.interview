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


class Node(object):
	def __init__(self, d):
		self.data = d
		self.next = None


class Queue(object):
	def __init__(self):
		self.first = None
		self.last = None

	def empty(self):
		return self.first == None and self.last == None

	def queue(self, d):
		n = Node(d)
		if self.empty():
			self.first = n
			self.last = n
		else:
			self.first.next = n
			self.first = n
		return d

	def dequeue(self):
		if self.empty():
			return None
		else:
			e = self.last.data
			if self.first == self.last:
				self.first = None
			self.last = self.last.next
			return e
