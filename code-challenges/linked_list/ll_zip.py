from linked_list import Node, LinkedList

def zipLists(list_one, list_two):
	#raise error for bad input
	if type(list_one) != LinkedList or type(list_two) != LinkedList:
		raise TypeError
	#iteration starting points
	current_one, current_two  = list_one.head, list_two.head
	#if either list is empty return the head of the other list
	#could maybe add another condition at the top to check if not current_one and not current_two
	if not current_one:
		return list_two.head
	if not current_two:
		return list_one.head
	#third tracking point to keep track of list_one's next value when current_one becomes a list_two node
	list_one_next = current_one.next_
	#iteration count to keep track of odd even for pathing
	step_count = 0
	#if either value is something other than None it is yet to be added to the zip so it needs to persist
	while current_one or current_two:

		#on off steps where a current_two exists current_one changes next value to current_two
		if step_count % 2 == 0 and current_two:
			current_one.next_ = current_two
			current_two = current_two.next_
			#update the new current_one value in the chain to have the list_one_next as it's next value
			current_one.next_.next_ = list_one_next
		#if step count is odd or current_two reached the end of the list add from list_one_next instead
		elif list_one_next:
			current_one.next_ = list_one_next
			#check to make sure the new value isn't None and then update list_one_next to the next value in the first list
			if current_one.next_:
				list_one_next = current_one.next_.next_
		#if step count is odd, but list_one_next is None add from list_two anyways
		else:
			current_one.next_ = current_two
			#check to make sure current_two isn't None before reassigning to next_
			if current_two:
				current_two = current_two.next_
		
		#increment the stepping values
		step_count+=1
		current_one = current_one.next_
			
	return list_one.head