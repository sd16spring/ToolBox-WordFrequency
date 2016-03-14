""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg 

	Python 2"""

import string, re

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	infile = open(file_name, 'r')
	text = infile.readlines()
	infile.close()
	for line in range(len(text)):
		if text[line].find('START OF THIS PROJECT GUTENBERG EBOOK') != -1:
			header = line + 1
		if text[line].find('END OF THIS PROJECT GUTENBERG EBOOK') != -1:
			footer = line
	text = text[header:footer]
	s = ''
	for line in text:
		if line != '\n':
			s += line
	s = s.translate(None, string.punctuation)
	text = re.split(' |\n', s)
	filtered_list = []
	for word in text:
		if word != '':
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
	word_counts = dict()
	for word in word_list:
		word_counts[word] = word_counts.get(word, 0) + 1
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	return ordered_by_frequency [:100]

if __name__ == '__main__':
	words = get_word_list('pg5200.txt')
	top_words = get_top_n_words(words, 100)
	print(top_words)