""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import pickle
import collections
from collections import deque
import string
from pattern.web import *

""" Pickling Gutenberg Text"""

# text_FULL = URL('http://www.gutenberg.org/cache/epub/1567/pg1567.txt').download()

# # Save data to a file (will be part of your data fetching script)
# f = open('text_full.pickle','w')
# pickle.dump(text_FULL,f)
# f.close()

# """ Importing Pickled Text"""
input_file = open('text_full.pickle','r')
reloaded_copy_of_text = pickle.load(input_file)

def get_word_list(file_name):

	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	text_nopunct = reloaded_copy_of_text.translate(string.maketrans("",""), string.punctuation) # eliminates all punctuation
	text_lower = text_nopunct.lower()								# converting all words to lowercase
	words_in_text = text_lower.split()
	return words_in_text

text_words_list = get_word_list(reloaded_copy_of_text)

def get_top_n_words(words, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	t = dict()																	# initialize dictionary
	for word in words:															# check for each word in text
		t[word] = 1 + t.get(word, 0)											# count the number of times the word appears in the dic
	ordered_t = collections.OrderedDict(sorted(t.items(), key=lambda t: t[1]))	# creates a list of the frequencies of words in order (greatest --> least)
	l = ordered_t.keys()														# list of frequencies
	return l[-n:-1]

print get_top_n_words(text_words_list, 10)