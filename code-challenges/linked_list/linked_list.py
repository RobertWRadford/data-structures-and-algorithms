class Node:

	def __init__(self, value=None, next_=None):
		self.value = value
		self.next_ = next_

	def __str__(self):
		return f'{self.value}'

class LinkedList:

	def __init__(self, arr=[]):
		self.head = None
		for value in arr[::-1]:
			self.insert(value)

	def __str__(self):
		if self.head == None: 
			return
		current = self.head
		retStr = str(current)
		while current.next_:
			current = current.next_
			retStr += ' ->'+str(current)
		return retStr

	def length(self):
		length = 0
		current = self.head
		while current:
			length+=1
			current = current.next_
		return length
	
	def nthFromEnd(self, n=0):
		if type(n) != int:
			return 'Exception'
		if n > self.length() or n < 0:
			return 'Exception'
		current = staggered = self.head
		counter = 0
		while current.next_:
			current = current.next_
			counter+=1
			if counter > n:
				staggered = staggered.next_
		return staggered.value

	def insert(self, insertVal):
		self.head = Node(insertVal, self.head)

	def append(self, appVal):
		newVal = Node(appVal)
		if not self.head:
			self.head = newVal
			return
		current = self.head
		while current.next_:
			current = current.next_
		current.next_ = newVal

	def insertBefore(self, insertVal, checkVal):
		current = self.head
		if not current: return
		if current.value == checkVal:
			newVal = Node(insertVal, current)
			self.head = newVal
		else:
			while current.next_:
				if current.next_.value == checkVal:
					break
				current = current.next_
			if current.next_.value == checkVal:
				newVal = Node(insertVal, current.next_)
				current.next_ = newVal

	def insertAfter(self, insertVal, checkVal):
		current = self.head
		if not current: return
		while current.next_:
			if current.value == checkVal:
				break
			current = current.next_
		if current.value == checkVal:
			newVal = Node(insertVal, current.next_)
			current.next_ = newVal

	def delete(self, delVal):
		current = self.head
		if not current: 
			return
		if current.value == delVal:
			self.head = current.next_
		else:
			while current.next_:
				if current.next_.value == delVal:
					current.next_ = current.next_.next_
					break
				current = current.next_

	def includes(self, checkVal):
		current = self.head
		while current:
			if current.value == checkVal:
				return True
			current = current.next_	
		return False