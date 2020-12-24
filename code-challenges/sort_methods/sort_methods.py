import random

def InsertionSort(arr):
	#as asked for from pseudo code
	for index, item in enumerate(arr):
		temp = item
		counter = index-1
		while counter >= 0 and temp < arr[counter]:
			arr[counter+1] = arr[counter]
			arr[counter] = temp
			counter -= 1

def ReverseSort(arr):
	for index, item in enumerate(arr):
		temp = item
		counter = index-1
		while counter >= 0 and temp > arr[counter]:
			arr[counter+1] = arr[counter]
			arr[counter] = temp
			counter -= 1

def SortedUniques(arr):
	temp = []
	pop_points = []
	InsertionSort(arr)
	for index, item in enumerate(arr):
		if not item in temp:
			temp.append(item)
			pop_points.append(index)
	for index in pop_points[::-1]:
		arr.pop(index)
	InsertionSort(temp)
	for i in range(1, len(temp)+1):
		arr.insert(0, temp[-i])

def MergeSort(arr):

	def Merge(left, right, arr):
		left_counter = 0
		right_counter = 0
		arr_counter = 0

		while left_counter < len(left) and right_counter < len(right):
			if left[left_counter] <= right[right_counter]:
				arr[arr_counter] = left[left_counter]
				left_counter+=1
			else:
				arr[arr_counter] = right[right_counter]
				right_counter+=1
			arr_counter+=1

		while left_counter < len(left):
			arr[arr_counter] = left[left_counter]
			left_counter+=1
			arr_counter+=1
		while right_counter < len(right):
			arr[arr_counter] = right[right_counter]
			right_counter+=1
			arr_counter+=1

	if len(arr) > 1:
		mid_index = len(arr)//2
		left_half = arr[:mid_index]
		right_half = arr[mid_index:]
		MergeSort(left_half)
		MergeSort(right_half)
		Merge(left_half, right_half, arr)

def QuickSort(arr, left, right):

	def Partition(arr, left, right):

		pivot = arr[right]
		low = left-1
		for i in range(left, right):
			if arr[i] <= pivot:
				low+=1
				arr[i], arr[low] = arr[low], arr[i]
				# Swap(arr, i, low)
		arr[right], arr[low+1] = arr[low+1], arr[right]
		# Swap(arr, right, low+1)
		return low+1

	if left < right:
		pos = Partition(arr, left, right)
		QuickSort(arr, left, pos-1)
		QuickSort(arr,pos+1,right)


int_arr = [random.randint(0,26) for i in range(31)]

print(int_arr)

#simple sort reverse for testing
ReverseSort(int_arr)

#simple sort uniques for testing
SortedUniques(int_arr)

#simple sort method, very slow at high scale
InsertionSort(int_arr)

#best scaling sort option of these choices
MergeSort(int_arr)

#Fast but crashes at approximately size 25k due to recursion depth
QuickSort(int_arr, 0, len(int_arr)-1)

print(int_arr)