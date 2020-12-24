def First_Duplicate(string):
	arr = string.split(' ')
	words = {}
	for word in arr:
		counter=0
		for index, char in enumerate(word):
			if not char.isalpha():
				word = word[:index-counter]+word[index+1-counter::]
				counter+=1
		word = word.lower()

		if word in words:
			words[f'{word}'] += 1
		else:
			words[f'{word}'] = 1
		if words[f'{word}'] > 1:
			return word

print(First_Duplicate('wins hands-down, n98ot! just in elegance (and NoT being deprecated;-) but also in performance'))