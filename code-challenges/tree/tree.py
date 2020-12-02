class Node:

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.right = right
		self.left = left

class BinaryTree:

	def __init__(self, head=None):
		self.head = head

	def add(self, value=None, root=None):
		if value is None:
			raise TypeError
		if not root:
			if not self.head:
				self.head = Node(value)
			else:
				root = self.head
		if value < root.value:
			if not root.left:
				root.left = Node(value)
			else:
				self.add(value, root.left)
		else:
			if not root.right:
				root.right = Node(value)
			else:
				self.add(value, root.right)


	def contains(self, value=None, root=None, matched=False):
		
		if value is None:
			raise TypeError

		if not root:
			if not self.head:
				return False
			else:
				root = self.head

		if value == root.value:
			return True

		if value < root.value:
			if root.left:
				matched = self.contains(value, root.left, matched)
			else:
				return False
		else:
			if root.right:
				matched = self.contains(value, root.right, matched)
			else:
				return False

		return matched

	def preOrder(self, root=None, contents = []):
		if not root:
			root = self.head
		if root:
			contents.append(root.value)
			if root.left:
				self.preOrder(root.left, contents)
			if root.right:
				self.preOrder(root.right, contents)
		return contents


	def inOrder(self, root=None, contents = []):
		if not root:
			root = self.head
		if root:
			if root.left:
				self.inOrder(root.left, contents)
			contents.append(root.value)
			if root.right:
				self.inOrder(root.right, contents)
		return contents

	def postOrder(self, root=None, contents = []):
		if not root:
			root = self.head
		if root:
			if root.left:
				self.postOrder(root.left, contents)
			if root.right:
				self.postOrder(root.right, contents)
			contents.append(root.value)
		return contents