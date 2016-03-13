""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from string import maketrans

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('TOM!') == -1:
		curr_line += 1
	lines = lines[curr_line:]

	#replace all punctuation and whitespace
	newlines = []
	intab = string.punctuation
	outtab = " " * len(string.punctuation)
	trantab = maketrans(intab, outtab)

	for i in lines[:]:
		i = i.strip() #strip whitespace
		if not(i == ""):
			i = i.translate(trantab) #strip punctuation
			i = i.lower()
			i = i.strip()
			newlines.append(i)

	#split into individual words
	words = []
	for i in newlines[:]:
		i = i.split()
		words.extend(i)
	return words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_counts = dict()

get_word_list("TomSawyer.txt")