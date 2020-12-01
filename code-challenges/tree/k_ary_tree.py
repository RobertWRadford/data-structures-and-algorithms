class Node:
	
	def __init__(self, value=None, parent=None, children=[]):
		self.value = value
		self.children = children
		self.parent = None

class karyTree:

	def __init__(self, k, values=[]):
		if not values or not k:
			raise TypeError
		current_tier = []
		next_tier = []
		self.head = Node(values[0])
		current_tier.append(self.head)
		values.pop(0)
		while values:
			for node in current_tier:
				root = node
				for i in range(k):
					root.children.append(Node(values[0], root))
					next_tier.append(root.children[i])
					values.pop(0)
			current_tier.clear()
			current_tier.extend(next_tier)
			next_tier.clear()

if __name__ == '__main__':
	kTree = karyTree(3, [i for i in range(1, 41)])
	assert [kTree.head.children[i].value for i in range(3)] == [2,3,4]
	assert [kTree.head.children[0].children[i].value for i in range(3)] == [5,6,7]
	assert [kTree.head.children[0].children[0].children[i].value for i in range(3)] == [14,15,16]