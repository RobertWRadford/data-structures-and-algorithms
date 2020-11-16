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

	def append(self, appVal):
		newVal = Node(appVal)
		if not self.head:
			self.head = newVal
			return
		current = self.head
		while current.next:
			current = current.next
		current.next = newVal

	def insertBefore(self, insertVal, checkVal):
		current = self.head
		if not current: return
		if current.value == checkVal:
			newVal = Node(insertVal, current)
			self.head = newVal
		else:
			while current.next:
				if current.next.value == checkVal:
					break
				current = current.next
			if current.next.value == checkVal:
				newVal = Node(insertVal, current.next)
				current.next = newVal


	def insertAfter(self, insertVal, checkVal):
		current = self.head
		if not current: return
		while current.next:
			if current.value == checkVal:
				break
			current = current.next
		if current.value == checkVal:
			newVal = Node(insertVal, current.next)
			current.next = newVal

	def delete(self, delVal):
		current = self.head
		if not current: 
			return
		if current.value == delVal:
			self.head = current.next
		else:
			while current.next:
				if current.next.value == delVal:
					current.next = current.next.next
					break
				current = current.next

	def includes(self, checkVal):
		current = self.head
		while current:
			if current.value == checkVal:
				return True
			current = current.next	
		return False