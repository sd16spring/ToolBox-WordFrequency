""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# obtain the text
	f = open(dorian_gray.txt, 'r')
	lines = f.readlines()
	current_line = 0

	# finds the start of the text
	while lines[current_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		current_line += 1
	lines = lines[current_line+1:]

	# creates a new string of text with punctuation removed
	words_alone = ''
	punctuation = string.punctuation
	for character in lines:
		if character not in punctuation:
			words_alone += character

	# splits string into list of words in all lower case
	word_list = []
	for word in words_alone.split():
		word = str.lower(word)
		word_list.append(word)

	return word_list
	

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	# creates dictionary of all words in book
	d = dict()
	for word in word_list:
		d[word] = 1 + d.get(word, 0)
	
	# orders words in list of most frequent to least frequent
	frequent_words = sorted(d, key = d.get, reverse = True)

	# list of the n most frequent words
	most_frequent = frequent_words[:n]
	return most_frequent

