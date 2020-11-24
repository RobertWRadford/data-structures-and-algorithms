class Node():

	def __init__(self, value=None, next_=None):
		self.value = value
		self.next_ = next_

class Stack():

	#Stack, last entered is first seen
	def __init__(self):
		self.top = None

	def push(self, value):
		self.top = Node(value, self.top)

	def pop(self):
		if not self.top:
			raise TypeError
		old_top = self.top
		self.top = old_top.next_
		return old_top.value

	def peek(self):
		if not self.top:
			raise TypeError
		return self.top.value

class PseudoQueue():

	#Queue, first entered is first seen
	def __init__(self, stack_one=Stack(), stack_two=Stack()):
		self.stack_one = stack_one
		self.stack_two = stack_two

	def __str__(self):
		if not self.stack_one.top:
			return None
		ret_string = f'{self.stack_one.top.value}'
		current = self.stack_one.top
		while current.next_:
			current = current.next_
			ret_string += f' ->{current.value}'
		return ret_string

	#stack_one: 5 -> 10 -> 15 -> 20
	#stack_two: ? ->

	def enqueue(self, value):
		if not self.stack_one.top:
			self.stack_one.push(value)
		else:
			while self.stack_one.top:
				self.stack_two.push(self.stack_one.top.value)
				self.stack_one.pop()
			self.stack_two.push(value)
			while self.stack_two.top:
				self.stack_one.push(self.stack_two.top.value)
				self.stack_two.pop()

	def dequeue(self):
		if not self.stack_one.top:
			raise TypeError
		old_back = self.stack_one.top.value
		self.stack_one.top = self.stack_one.top.next_
		return old_back
