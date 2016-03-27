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
	book = open(file_name, 'r')
	text = book.readlines()
	book.close()

	for line in range(len(text)):
		if text[line].find('START OF THIS PROJECT GUTENBERG EBOOK') != -1:
			header = line + 1
		if text[line].find('END OF THIS PROJECT GUTENBERG EBOOK') != -1:
			footer = line

	text = text[header:footer]
	mystring = ''

	for line in text:
		if line != '\n':
			mystring += line

	mystring = mystring.translate(None, string.punctuation)
	mystring = mystring.lower()
	text = re.split(' |\n', mystring)
	filtered_list = []

	for word in text:
		#word = word.lower()
		if word != '' :
			filtered_list.append(word)
	return filtered_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.
		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""

	mydict = dict()

	for word in word_list:
		mydict[word] = mydict.get(word, 0) + 1

	ordered = sorted(mydict, key=mydict.get, reverse=True) 
	most_frequent = ordered[0:n] 
	return most_frequent

if __name__ == '__main__':

	print get_top_n_words(get_word_list('pg8800.txt'),100)
	