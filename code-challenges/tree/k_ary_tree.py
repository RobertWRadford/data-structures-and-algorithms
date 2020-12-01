class Node:
	
	#using a default parameter of [] giving one instance with multiple pointers
	def __init__(self, value=None, children=None):
		self.value = value
		self.children = [] if children is None else children

class KaryTree:

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

	def contains(self, value=None, root=None, matched=False):
		if value is None:
			raise TypeError
		if not root:
			if not self.head:
				return False
			else:
				root = self.head
		if value == root.value:
			matched = True
		# had to use a variable and bounce around here :?
		for child in root.children:
			matched = self.contains(value, child, matched)
		return matched

	def preOrder(self, root=None, contents = []):
		if not root:
			root = self.head
		if root:
			contents.append(root.value)
			for child in root.children:
				self.preOrder(child, contents)
		return contents

	def postOrder(self, root=None, contents = []):
		if not root:
			root = self.head
		if root:
			for child in root.children:
				self.postOrder(child, contents)
			contents.append(root.value)
		return contents

if __name__ == '__main__':
	kTree = KaryTree(3, [i for i in range(1, 41)])
	#																			1
	#					2														3														4
	#	5				6				7						8				9				10						11				12				13
	#14	15	16		17	18	19		20	21	22				23	24	25		26	27	28		29	30	31				32	33	34		35	36	37		38	39	40
	print([kTree.head.children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
	print([kTree.head.children[0].children[0].children[i].value for i, values in enumerate(kTree.head.children[0].children)])
	print('true' if kTree.contains(23) else 'false')
	print('true' if kTree.contains(80) else 'false')
	print(kTree.postOrder())
	print(kTree.preOrder())