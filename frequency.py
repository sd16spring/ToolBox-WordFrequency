""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pickle import load, dump

def getWordList(fileName):
	""" 
		Takes raw data from project Gutenberg and cuts out the introduction and bottom part
		It also tranfers the entire text to lowercase and removes punctuation and whitespace

		Returns a list

	>>> s = 'A***H   ***1234@&().ABCab  c***'
	>>> f = open('text.txt', 'w')
	>>> dump(s, f)
	>>> f.close()
	>>> get_word_list('text.txt')
	['abcab', 'c']
	"""
	inputFile = open(fileName, 'r')
	text = load(inputFile)

	l = text.split('***') #marker for stop and end of text in gutenberg
	try: #returns none in case there is something strange with the project gutenberg text
		mainText = l[2] #main text is the third block of text 
	except:
		return None
	mainText = mainText.lower() #changes everything to lowercase
	mainText = mainText.replace("\r\n", "")
	mainText = mainText.translate(string.maketrans("",""), string.punctuation) #removes punctuation
	mainText = mainText.translate(string.maketrans("",""), string.digits) #removes numbers
	mainList = mainText.split()
	return mainList

def getTopNWords(wordList, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	d = {}
	for word in wordList:
		d[word] = d.get(word, 0)
		d[word] += 1

	l = []
	for i in d:
		l.append((d[i], i))
	l.sort(reverse = True)

	mostCommon = l[0:(n-1)]
	words = [x[1] for x in mostCommon]
	return words
if __name__ == "__main__":
	# import doctest
	# doctest.testmod()
	l1 = getWordList('odyssey.txt')
	l2 = getTopNWords(l1, 100)
	print l2