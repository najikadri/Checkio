def letter_queue (commands):
	word = []
	for x in commands:
		if len(x) > 3:
			y = x.split()
			word.append(y[1])
		elif len(word) > 0:
			word[0:1] = []
	return ''.join(word)
