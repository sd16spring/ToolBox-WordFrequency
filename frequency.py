""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import re


def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('CHAPTER I') == -1:
	    curr_line += 1

	lines = lines[curr_line+1:]

	word = ""
	for line in lines:
		word += line

	#strip punctuation
	word = word.translate(string.maketrans("",""), string.punctuation)

	#strip whitespace and convert to list
	word_list = re.sub("[^\w]", " ",  word).split()

	#convert each word to lowercase
	new_word_list = []
	for word in word_list:
		new_word_list.append(word.lower())

	return new_word_list

	


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_counter = {}
	for word in word_list:
		if word in word_counter:
			word_counter[word] += 1
		else:
			word_counter[word] = 1

	ordered_by_frequency = sorted(word_counter, key=word_counter.get, reverse=True)

	return ordered_by_frequency[:100]


get_word_list('pg32325.txt')
print get_top_n_words(get_word_list('pg32325.txt'), 10)