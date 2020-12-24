class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Binary_Tree:

	def __init__(self, values=None):
		self.head = None
		if isinstance(values, object):
			for item in values:
				self.insert(item)

	def insert(self, node):
		if not isinstance(node, Node):
			node = Node(node)
		if self.head is None:
			self.head = node
			return
		current = self.head
		while current:
			if node.value <= current.value:
				if current.left is None:
					current.left = node
					return
				else:
					current = current.left
			else:
				if current.right is None:
					current.right = node
					return
				else:
					current = current.right

def tree_intersection(tree_one, tree_two):
	if not tree_one.head or not tree_two.head:
		raise Exception('One or both trees is empty')
	first = set()
	second = set()

	def walk(tree, set_):
		branches = [tree.head]

		while len(branches):
			root = branches[0]
			branches.pop(0)

			set_.add(root.value)
			if root.left:
				branches.append(root.left)
			if root.right:
				branches.append(root.right)
			
	walk(tree_one, first)
	walk(tree_two, second)
	return first&second

print(tree_intersection(Binary_Tree([1,2,3,4,5,6]), Binary_Tree([4,5,6,7,8,9])))