""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(filename):
	"""
	Reads the specified project Gutenberg book.  Header comments,
	punctuation, and whitespace are stripped away.  The function
	returns a list of the words used in the book as a list.
	All words are converted to lower case. 
	"""
	bookraw = open(filename, 'r')
	bookstring = ''
	for line in bookraw:
		bookstring = bookstring + line
	bookstring = bookstring.replace("\n", " ")
	bookstring = bookstring.replace(string.punctuation, "")
	bookstring = bookstring.lower()
	booklist = bookstring.split()

	counter = 0
	while counter < 2:
		if booklist[0] == '***':
			counter += 1
			print counter
			del booklist[0]
		else:
			del booklist[0]
	return booklist



def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	histogram = {}
	for word in word_list:
		histogram[word] = histogram.get(word, 0) + 1
	hist_list = []
	ordered_by_frequency = sorted(histogram, key=histogram.get, reverse=True)
	return ordered_by_frequency[0:n]

def word_frequency_stuff(filename, n)
	word_list = get_word_list(filename)
	print get_top_n_words(word_list, n)

