'''count the number the of letters in a word'''
def countletters():
	word = input('ENTER YOUR WORD')
	d = dict()
	for c in word:
   		d[c] = d.get(c,0) + 1
	print(d)
