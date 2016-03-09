""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
		lines = lines[curr_line+1:]

	wordFreq = {}

	for line in lines:
		for word in line.split():
			wordHolder = word
			wordHolder = wordHolder.strip(string.punctuation)
			wordHolder = wordHolder.strip(string.whitespace)
			wordHolder = wordHolder.lower()
			wordFreq[wordHolder] = wordFreq.get(wordHolder, 0) + 1
	f.close()



	wordList = []
	temp = wordFreq.items()

	# reverses the key, value tuple thing
	for j in xrange(len(temp)):
		anotherTemp = temp[j][1], temp[j][0]
		temp[j] = anotherTemp
	# reverse sorts the list and adds it to the sorted list
	temp.sort(reverse=True)
	wordList = temp
	return wordList

def get_top_n_words(wordList, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	return wordList[0:n]

if __name__ == '__main__':
	print get_top_n_words(get_word_list('pg32325.txt'), 100)