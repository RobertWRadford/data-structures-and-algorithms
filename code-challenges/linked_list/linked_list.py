class Node:

	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return f'{self.value}'

class LinkedList:

	def __init__(self):
		self.head = None

	def __str__(self):
		if self.head == None: 
			return
		current = self.head
		retStr = str(current)
		while current.next:
			current = current.next
			retStr += ' ->'+str(current)
		return retStr
	
	def insert(self, insertVal):
		newVal = Node(insertVal, self.head)
		self.head = newVal

	def includes(self, checkVal):
		current = self.head
		while current:
			if current.value == checkVal:
				return True
			current = current.next	
		return False