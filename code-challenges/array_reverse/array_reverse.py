def reverseArray(arr):
	return arr[::-1]

def otherReversal(arr):
	newArr = []
	for n in arr:
		newArr.insert(0, n)
	return newArr

def anotherReversal(arr):
	newArr = []
	for i in range (1, len(arr)+1):
		newArr.insert(0, i)
	return newArr

print(reverseArray([1, 2, 3]), otherReversal([1, 2, 3]), anotherReversal([1, 2, 3]))