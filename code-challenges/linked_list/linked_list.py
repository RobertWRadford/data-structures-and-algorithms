class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None

	def __str__(self):
		return f'{value}'

class LinkedList:

	def __init__(self):
		self.head = None

	def __str__(self):
		if self.head == None: 
			return
		current = self.head
		retStr = current.value
		while current.next:
			current = current.next
			retStr += ' ->'+str(current)
		return retStr
	
	def insert(self, insertVal):
		newVal = Node(insertVal)
		if self.head == None: 
			self.head = newVal
			return
		current = self.head
		while current.next:
			current = current.next
		current.next = newVal

	def includes(self, checkVal):
		if self.head == None:
			return
		current = self.head
		if current == checkVal:
			return True
		while current.next:
			current = current.next
			if current == checkVal:
				return True
		return False