from linked_list import Node, LinkedList

def test_instantiation():
	assert initialList.head == None

initialList.insert(5)

def test_insertion():
	assert initialList.head == Node(5)

initialList.insert(6)
initialList.insert(7)
initialList.insert(8)

test_insertion()

def test_multiple_inserts():
	assert initialList.head == Node(5) && initialList.head.next

def test_truthy_includes():
	assert initialList.includes(6)

def test_falsy_includes():
	assert initialList.includes(9)

def test_return_all_values():
	assert str(initialList) == '5 ->6 ->7 ->8'