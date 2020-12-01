class Node:
	
	def __init__(self, value=None, children=None):
		self.value = value
		self.children = [] if children is None else children

class karyTree:

	def __init__(self, k, values=[]):
		if not values or not k:
			raise TypeError
		self.head = Node(values[0])
		values.pop(0)
		current_tier = [self.head]
		while values:
			root = current_tier[0]
			current_tier.pop(0)
			for i in range(k):
				next_node = Node(values[0])
				root.children.append(next_node)
				current_tier.append(next_node)
				values.pop(0)

if __name__ == '__main__':
	kTree = karyTree(3, [i for i in range(1, 41)])
	print([kTree.head.children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
	print([kTree.head.children[0].children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
