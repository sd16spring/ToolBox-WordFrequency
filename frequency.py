""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

from pattern.web import *
import string
import random
import operator


# url = URL('http://www.gutenberg.org/cache/epub/1342/pg1342.txt')
# all_gutenberg = url.download()

# start_index = all_gutenberg.index('Chapter 1')
# end_index = all_gutenberg.index('End of the Project Gutenberg EBook of Pride and Prejudice, by Jane Austen')

# just_book = all_gutenberg[start_index:end_index]


# f = open('pride_prejudice.txt', 'w')
# f.write(just_book)
# f.close()

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name, 'r+')
	
	lines = ""
	words = []

	for line in f.read().split("\n"):
		lines += line.strip(string.punctuation + string.whitespace) + " "
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()
			words.append(word)

			


	return words

# print get_word_list('pride_prejudice.txt')


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	hist = dict()
	for word in word_list:
		hist[word] = hist.get(word, 0) + 1

	res = []
	sorted_hist = sorted(hist.items(), key=operator.itemgetter(1), reverse = True)
	for (key,value) in sorted_hist:
		res.append(key)
	return res


print get_top_n_words(get_word_list('pride_prejudice.txt'), 10)