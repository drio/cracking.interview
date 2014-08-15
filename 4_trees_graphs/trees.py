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

	# time: O(log(n))
	# space: O(log(n))
	def size_per_levels(self, cn, nl, l=0):
		if not cn:
			return nl

		if l not in nl:
			nl[l] = 0
		nl[l] += 1

		self.size_per_levels(cn.left, nl, l+1)
		self.size_per_levels(cn.right, nl, l+1)

	# Check if two trees have the same shape
	# time: O(log(n))
	# space: O(log(n))
	def same_shape(self, t2):
		d1, d2 = {}, {}
		self.size_per_levels(self.root, d1)
		self.size_per_levels(t2.root, d2)

		if len(d1.keys()) != len(d2.keys()):
			return False

		for k,v in d1.items():
			if v != d2[k]:
				return False

		return True
