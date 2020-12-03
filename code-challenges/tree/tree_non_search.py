class Node:

	def __init__(self, value=None, next_=None, left=None, right=None):
		self.value = value
		self.next_ = next_
		self.right = right
		self.left = left

class Stack:

	def __init__(self):
		self.top = None

	def push(self, node=None):
		if node is None:
			raise Exception('No value given')
		if self.top:
			node.next_ = self.top
		else:
			node.next_ = None
		self.top = node
		

	def pop(self):
		if self.top is None:
			raise Exception('The stack is already empty')
		old_top = self.top
		self.top = old_top.next_
		return old_top

	def peek(self):
		if self.top is None:
			raise Exception('The stack is empty')
		return self.top

class Queue:

	def __init__(self, front_stack=None, dump_stack=None):
		self.front_stack = front_stack if not front_stack is None else Stack()
		self.dump_stack = dump_stack if not dump_stack is None else Stack()

	def enqueue(self, node=None):
		if node is None:
			raise Exception('No value was given')
		if not isinstance(node, object):
			node = Node(node)
		if not self.front_stack.top:
			self.front_stack.push(node)
		else:
			while self.front_stack.top:
				self.dump_stack.push(self.front_stack.pop())
			self.dump_stack.push(node)
			while self.dump_stack.top:
				self.front_stack.push(self.dump_stack.pop())

	def dequeue(self):
		if not self.front_stack.top:
			raise Exception('Queue is empty')
		old_back = self.front_stack.top
		self.front_stack.top = self.front_stack.top.next_
		return old_back

	def contents(self):
		if not self.front_stack.top:
			raise Exception('Queue is empty')
		contents = []

		while self.front_stack.top:

			contents.append(self.dequeue().value)

		return contents


class BinaryTree:

	def __init__(self, head=None):
		self.head = head

	def add(self, value=None, root=None):
		# catch errors
		if value is None:
			raise TypeError
		# check if a head exists
		if not root:
			if not self.head:
				self.head = Node(value)
				return
			else:
				root = self.head
		# Create a container for the row
		current_row = Queue()
		current_row.enqueue(root)
		#traverse to next opening
		while current_row.front_stack.top:

			root = current_row.dequeue()

			if not root.left:
				root.left = Node(value)
				break
			else:
				current_row.enqueue(root.left)

			if not root.right:
				root.right = Node(value)
				break
			else:
				current_row.enqueue(root.right)

	def find_max(self):
		if not self.head:
			return None
		current_row = Queue()
		current_row.enqueue(self.head)

		max_val = self.head.value

		while current_row.front_stack.top:

			root = current_row.dequeue()

			if root.value > max_val:
				max_val = root.value

			if root.left:
				current_row.enqueue(root.left)
			if root.right:
				current_row.enqueue(root.right)

		return max_val

	def traverse_tree(self):
		if not self.head:
			return None

		all_values = Queue()
		current_row = Queue()
		current_row.enqueue(self.head)

		while current_row.front_stack.top:

			root = current_row.dequeue()
			all_values.enqueue(root)

			if root.left:
				current_row.enqueue(root.left)
			if root.right:
				current_row.enqueue(root.right)

		return all_values.contents()



if __name__ == '__main__':
	xmas = BinaryTree()
	for i in range(300):
		xmas.add(i)
	# xmas.add(5)
	# xmas.add(3)
	# xmas.add(6)
	# xmas.add(8)
	# xmas.add(10)
	# xmas.add(17)
	# xmas.add(19)
	# xmas.add(1)
	# xmas.add(3)
	#            5
	#      3            6
	#   8     10    17     19
	# 1   3
	print(xmas.find_max())
	print(xmas.traverse_tree())