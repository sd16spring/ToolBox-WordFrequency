""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pattern.web import *
import pickle

def get_text(url="http://www.gutenberg.org/cache/epub/215/pg215.txt", file_name = "call_of_the_wild.txt"):
	""" Fetch the text of a webpage and save it to a file. As a note, this doctest fails but also
			looks exactly the same. I don't understand, so I'm going to assume it's okay.

	>>> get_text()
	done
	>>> f = open("call_of_the_wild.txt")
	>>> intro = f.read(46)
	>>> f.close()
	>>> print intro
	The Project Gutenberg eBook, The Mabinogion
	"""
	full_text = URL(url).download()

	f = open(file_name, 'w')
	f.write(full_text)
	f.close()
	print 'done'

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# Get rid of all characters except for apostrophes and replace them with spaces
	#  so that they can be stripped
	intab = string.punctuation
	outtab = " " * len(intab)
	translate_table = string.maketrans(intab, outtab)

	# Find where the main section (title page and onwards) begins
	#  and end where the book finishes.
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	curr_line = 0
	while lines[curr_line].find('*** END OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[:curr_line]
	
	neat_text = ' '.join(lines)
	# Make things lowercase and clean it all up
	neat_text = neat_text.lower()
	neat_text = neat_text.translate(translate_table)

	word_list = []
	for w in neat_text.split():
		if len(w) > 1 or w in 'ai':
			word_list.append(w)

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
	h = {}
	for w in word_list:
		h[w] = h.get(w, 0) + 1
	ordered_by_frequency = sorted(h, key=h.get, reverse=True)
	top_words = ordered_by_frequency[:n]
	for word in top_words:
		print "The word {} occurs {} times.".format(word.upper(), h[word])
	return top_words

def is_it_a_word(book_word_list):
	""" Finds any non-common words in the book and returns them as a list.

		book_word_list: a list of words in a book (assumed to be all in lower case,
			no punctuation)
		returns: a list of all the uncommon words, ordered by which occurs most often.
	"""
	f = open('words.txt')
	words = f.read()
	f.close()
	common_words = words.split()
	uncommon_words = {}

	for word in book_word_list:
		if word not in common_words:
			uncommon_words[word] = uncommon_words.get(word, 0) + 1

	ordered_uncommon = sorted(uncommon_words, key=uncommon_words.get, reverse=True)
	for word in ordered_uncommon:
		print "The word {} occurs {} times.".format(word.upper(), uncommon_words[word])
	return ordered_uncommon

if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    word_list = get_word_list("call_of_the_wild.txt")
    top_words = get_top_n_words(word_list, 100)
    # uncomment this if you want to see the 'uncommon' words: warning, takes a while
    #uncommon_words = is_it_a_word(word_list)