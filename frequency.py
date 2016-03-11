""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg 

	AUTHOR: GABY CLARKE"""

import string

def cleanUpLine(s):
	""" takes an unformatted string and returns a list of lowercase words without
		punctuation

		s: a string
		returns: a formatted list of words in the string
	"""

	s = s.lower()

	for char in string.punctuation:
		s = s.replace(char, '')

	wordList = s.split()
	return wordList

def getWordList(file_name):
	""" Reads the specified Project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""

	f = open(file_name,'r')
	content = f.read()
	start = content.find('START OF THIS PROJECT GUTENBERG EBOOK')
	end = content.find('END OF THIS PROJECT GUTENBERG EBOOK')
	content = content[start:end]
	content = content.splitlines()
	content = [i for i in content if i != '']

	wordList = []

	for line in content:
		words = cleanUpLine(line)
		if 'gutenberg' not in words:
			for word in words:
				wordList.append(word)

	f.close()
	return wordList


def histogram(wordList):
	""" Takes a list of words and returns a histogram of how many times each
		word appears in the list.

		wordList: a list of words
		returns: dictionary with items 'word':freq
	"""
	
	hist = dict()
	
	for word in wordList:
		hist[word] = hist.get(word, 0) + 1

	return hist


def getTopWords(wordList, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		wordList: a list of words (assumed to all be in lower case with no
					punctuation)
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""

	hist = histogram(wordList)
	
	ordered = sorted(hist, key=hist.get, reverse=True)
	return ordered[:n]


def getWordsOfMinFreq(wordList, n):
	""" Takes a list of words and returns a list of words that appear at least n 
		times in the list.

		wordList: a list of words (assumed to all be in lower case with no
					punctuation)
		n: the minimum frequency
		returns: a list of words that appear more than n times in wordList ordered
					from most frequently to least frequently occurring
	"""

	hist = histogram(wordList)
	histOfMinFreq = dict()

	for key, value in hist.items():
		if value >= n:
			histOfMinFreq[key] = value

	ordered = sorted(histOfMinFreq, key=hist.get, reverse=True)
	return ordered


def printTop100Words(filename):
	""" Takes a file and prints the 100 most frequently occurring words in the
		file.

		filename: name of the file
		generates: a list of the 100 most frequently occurring words in the file
	"""
	wordList = getWordList(filename)
	print getTopWords(wordList, 100)


def printWordsOfMinFreq20(filename):
	""" Takes a file and prints all words occurring more than 20 times in the file.

		filename: name of the file
		generates: a list of all words occurring more than 20 times in the file
	"""
	wordList = getWordList(filename)
	print getWordsOfMinFreq(wordList, 20)



if __name__ == "__main__":
	printTop100Words('Conrad.txt')
	# printWordsOfMinFreq20('Conrad.txt')
