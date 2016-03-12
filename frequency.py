""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import re
import string
import operator

def get_word_list(text):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	wordList = re.sub("[^\w]", " ", text).split()
	return wordList



def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	frequencies = dict()
	for word in word_list:
		frequencies[word] = frequencies.get(word, 0) + 1
	sorted_list = sorted(frequencies, key=frequencies.get, reverse=True)
	return sorted_list[0:n]

def strip_text(text):
	stripped_text = text.translate(string.maketrans("",""), string.punctuation)
	return stripped_text.lower()

def open_book(title):
	f = open(title,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('CHAPTER I') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	text = ""
	for line in lines:
		text += line
	return text

text = open_book('pg32325.txt')
stripped_text = strip_text(text)
word_list = get_word_list(stripped_text)
print get_top_n_words(word_list, 100)
