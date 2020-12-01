class Node:
	
	def __init__(self, value=None, children=None):
		self.value = value
		self.children = [] if children is None else children

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
				# print(root.value)
				for i in range(k):
					next_node = Node(values[0])
					root.children.append(next_node)
					next_tier.append(next_node)
					values.pop(0)
			# print([root.children[i].value for i, node in enumerate(root.children)])
			current_tier.clear()
			current_tier.extend(next_tier)
			# print([current_tier[i].value for i in range(len(current_tier))])
			next_tier.clear()

if __name__ == '__main__':
	kTree = karyTree(3, [i for i in range(1, 41)])
	print([kTree.head.children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
	print([kTree.head.children[0].children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
