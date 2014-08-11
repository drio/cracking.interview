# vim: set ts=4 noet:
#
# Linked List
#
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self, d):
		new_node = Node(d)
		_ = self.head
		self.head = new_node
		new_node.next = _
		self.size += 1

	def delete(self, d):
		if self.size == 0: return False

		if self.size == 1:
			if self.head.data == d:
				self.head = None
				self.size = 0
				return d
		else:
			cn = self.head
			while cn.next:
				if cn.next.data == d:
					cn.next = cn.next.next
					self.size -= 1
					return d
				cn = cn.next

		return False

