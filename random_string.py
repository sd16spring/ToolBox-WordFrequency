""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from string import punctuation,whitespace
from pattern.web import *
import pickle

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	#load book, create list of lines
	text = open(file_name,'r+')
	# text_lines = text.readlines()
	# curr_line = 0
	# while text_lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
	# 	curr_line += 1
	# text_lines = text_lines[curr_line+1:]
	#separate words in each line, put them in a list
	word_list = []
	# for line in text_lines:
	for word in text.read().split():
		word_now = ""
		for char in word:
			if char not in punctuation:
				if char not in whitespace:
					char = char.lower()
					word_now += char
		word_list.append(word_now)
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
	hist = dict()
	for word in word_list:
		hist[word] = hist.get(word,0) + 1
	in_order = []
	for word,number in hist.items():
		in_order.append((number,word))
	in_order.sort(reverse = True)
	top_n = in_order[0:n]
	return top_n

PP = 'Add, some code, some that, that calls that the two functions you just wrote so that you get the words'
#PP = URL('http://www.gutenberg.org/cache/epub/1342/pg1342.txt').download()
f = open('Pride_and_Prejudice','w')
f.write(PP)
f.close()
print get_top_n_words(get_word_list('Pride_and_Prejudice'),4)