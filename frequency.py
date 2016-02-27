""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	l = []
	fin = open(file_name, 'r')
	header = False
	for line in fin:
		if(not header):
			if 'START OF THIS PROJECT GUTENBERG EBOOK' in line:
				header = True 
		else:
			for punc in string.punctuation:
				line = line.replace(punc, '')
			line = line.replace('\n', '')
			line = line.replace('\t', '')
			line = line.lower()
			words = line.split()
			for word in words:
				l.append(word)
	return l



def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	d = {}
	for word in word_list:
		if word in d.keys():
			d[word] += 1
		else:
			d[word] = 1
	ordered_by_frequency = sorted(d, key=d.get, reverse=True)
	return ordered_by_frequency[:n]

if __name__ == '__main__':
	x = get_word_list('pg84.txt')
	print(get_top_n_words(x, 100))