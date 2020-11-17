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
	assert initialList.head.value == 6 and initialList.head.next_

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

def test_append():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.append(8)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_before():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(8)
	initialList.insertBefore(7, 8)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_after():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(8)
	initialList.insertAfter(7, 6)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_before():
	initialList = LinkedList()
	initialList.append(6)
	initialList.append(7)
	initialList.append(8)
	initialList.insertBefore(5, 6)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_after():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.insertAfter(8, 7)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_delete_middle():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.insertAfter(8, 7)
	initialList.delete(6)
	assert str(initialList) == '5 ->7 ->8'

def test_insert_delete_first():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.insertAfter(8, 7)
	initialList.delete(5)
	assert str(initialList) == '6 ->7 ->8'

def test_insert_delete_last():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.insertAfter(8, 7)
	initialList.delete(8)
	assert str(initialList) == '5 ->6 ->7'

def test_initialize_with_list():
	initialList = LinkedList([5,6,7,8])
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_nth_greater_than():
	initialList = LinkedList([5,6,7,8])
	assert initialList.nthFromEnd(8) == 'Exception'

def test_nth_last():
	initialList = LinkedList([5,6,7,8])
	assert initialList.nthFromEnd(4) == 5

def test_nth_negative():
	initialList = LinkedList([5,6,7,8])
	assert initialList.nthFromEnd(-2) == 'Exception'

def test_nth_list_of_one():
	initialList = LinkedList([5])
	assert initialList.nthFromEnd(0) == 5

def test_nth_average_use():
	initialList = LinkedList([5,6,7,8,9,10,11])
	assert initialList.nthFromEnd(3) == 8