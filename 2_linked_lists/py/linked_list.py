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

	def n_to_last(self, n):
		stop = self.size - n - 1
		p = self.head

		if stop < 0:
			return None

		if stop == 0:
			return p

		for i in range(0, stop):
			p = p.next

		return p

	def plist(self):
		p = self.head
		l = []
		while p.next:
			l.append(p.data)
			p = p.next
		l.append(p.data)
		return l

	def remove_dups(self):
		if self.size == 0: return 0

		p = self.head
		d = p.data
		while d:
			first = p
			while p.next:
				if p.next.data == d:
					p.next = p.next.next
					self.size -= 1
				if p.next:
					p = p.next

			if p.data == d:
				first.next = p.next

			if first.next:
				p = first.next
				d = first.next.data
			else:
				d = None

