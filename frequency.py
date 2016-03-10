""" Analyzes the word frequencies in Great Expectations downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	#opens file and removes Gutenberg header
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	#strips words and appends to a list
	word_list = []
	for line in lines:
		for char in string.punctuation:
			line = line.replace(char,'')
		for word in line.lower().strip().split():
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
	hist = {}
	for word in word_list:
		hist[word] = hist.get(word, 0) + 1

	ordered_by_frequency = sorted(hist, key=hist.get, reverse=True)
	return ordered_by_frequency[:n]

word_list = get_word_list('great_expectations.txt')
print get_top_n_words(word_list,100)