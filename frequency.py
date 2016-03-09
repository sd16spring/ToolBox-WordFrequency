""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg, in this case The Metamorphosis by Franz Kafka"""

import string
from pattern.web import *
import random
import operator

book_txt = URL('http://www.gutenberg.org/cache/epub/5200/pg5200.txt')
Gutenberg = book_txt.download()
downloaded_book = Gutenberg[Gutenberg.index('I'):Gutenberg.index('End of the Project')]
useless_words = ['the', 'to', 'and', 'of', 'it', 'in', 'a', 'as', 'with', 'at', 'but', 'on', 'into', 'his', 'he', 'her', 'she', 'him', 'his', 'for', 'on','by', 'that', 'they', 'from', 'there','this', '', 'them','about', 'then']
fin = open('metamorphosis.txt', 'w')
fin.write(downloaded_book)
fin.close()

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	fin = open(file_name, 'r+')
	strngs = ''
	words = []
	for strng in fin.read().split("\n"):
		strngs += strng.strip(string.whitespace+string.punctuation)+""
		for word in strng.split():
			word = word.strip(string.punctuation+string.whitespace)
			word = word.lower()
	# does not append words in the list useless_words
			if word not in useless_words:
				words.append(word)
			else:
				pass
	return words

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	dictionary = dict()
	for word in word_list:
		dictionary[word] = dictionary.get(word, 0)+1

	most_frequent_words = []
	sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
	for (key,value) in sorted_dictionary:
		most_frequent_words.append(key)
	# print dictionary
	return most_frequent_words

# get_top_n_words(get_word_list('metamorphosis.txt'), 15) 
print get_top_n_words(get_word_list('metamorphosis.txt'), 5) 