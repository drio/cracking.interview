# vim: set ts=4 noet:
#

# Binary Tree Node
class Node(object):
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None


class BST(object):
	def __init__(self):
		self.root = None

	# O(log(n))
	def insert(self, d):
		p = None
		cn = self.root

		while cn:
			p = cn
			if d < cn.data:
				cn = cn.left
			else:
				cn = cn.right

		nn = Node(d)
		if not p: # Empty tree
			self.root = nn
		else:
			if p.data > d:
				p.left = nn
			else:
				p.right = nn

	# O(log(n))
	def walk(self, cn, l):
		if cn:
			self.walk(cn.left, l)
			l.append(cn.data)
			self.walk(cn.right, l)

	# O(log(n))
	def search(self, cn, k):
		if not cn:
			return None

		if cn.data == k:
			return cn

		if cn.data <= k:
			return self.search(cn.right, k)
		else:
			return self.search(cn.left, k)

