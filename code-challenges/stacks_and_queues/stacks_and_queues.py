class Node:

	def __init__(self, value=None, next_=None):
		self.value = value
		self.next_ = next_

class Stack:

	def __init__(self, top=None):
		self.top = top

	def push(self, value):
		new_node = Node(value, self.top)
		self.top = new_node

	def pop(self):
		
		if not self.top:
			raise TypeError
		remove_node = self.top
		self.top = remove_node.next_
		return remove_node

	def peek(self):
		if not self.top:
			raise TypeError
		return self.top

	def isEmpty(self):
		if not self.top:
			return True
		else:
			return False

class Queue:

	def __init__(self, front=None, back=None):
		self.front = front
		self.back = back

	def enqueue(self, value):
		current_last = self.back
		current_last.next_ = Node(value)
		self.back = current_last.next_

	def dequeue(self):
		if not self.front:
			raise TypeError
		remove_node = self.front
		self.front = remove_node.next_
		return remove_node

	def peek(self):
		if not self.front:
			raise TypeError
		return self.front

	def isEmpty(self):
		if not self.front:
			return True
		else:
			return False