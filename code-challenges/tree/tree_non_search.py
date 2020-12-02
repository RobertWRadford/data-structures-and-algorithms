class Node:

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.right = right
		self.left = left

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
		current_row = [root]
		#traverse to next opening
		while len(current_row):

			root = current_row[0]
			current_row.pop(0)

			if not root.left:
				root.left = Node(value)
				break
			else:
				current_row.append(root.left)

			if not root.right:
				root.right = Node(value)
				break
			else:
				current_row.append(root.right)

	def find_max(self):
		if not self.head:
			return None
		max_val = 0
		current_row = [self.head]
		while len(current_row):

			root = current_row[0]
			current_row.pop(0)
			
			if root.value > max_val:
				max_val = root.value

			if root.left:
				current_row.append(root.left)
			if root.right:
				current_row.append(root.right)

		return max_val


if __name__ == '__main__':
	xmas = BinaryTree()
	xmas.add(5)
	xmas.add(3)
	xmas.add(6)
	xmas.add(8)
	xmas.add(10)
	xmas.add(17)
	xmas.add(19)
	xmas.add(1)
	xmas.add(3)
	#            5
	#      3            6
	#   8     10    17     19
	# 1   3
	print(xmas.find_max())