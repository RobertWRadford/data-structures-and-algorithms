from linked_list import Node, LinkedList

def test_instantiation():
	initialList = LinkedList()
	assert initialList.head == None

def test_insertion():
	initialList = LinkedList()
	initialList.insert(5)
	assert initialList.head.value == 5
def test_insertion_again():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	assert initialList.head.value == 6

def test_multiple_inserts():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	assert initialList.head.value == 6 and initialList.head.next

def test_truthy_includes():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	initialList.insert(7)
	initialList.insert(8)
	assert initialList.includes(6)

def test_falsy_includes():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	initialList.insert(7)
	initialList.insert(8)
	assert initialList.includes(9) == False

def test_return_all_values():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	initialList.insert(7)
	initialList.insert(8)
	assert str(initialList) == '8 ->7 ->6 ->5'