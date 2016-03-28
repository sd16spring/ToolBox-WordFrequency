""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string




def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	#remove header
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('ACT I') == -1:
		curr_line += 1
	lines = lines[curr_line:]
	#remove footer
	while lines[curr_line].find('*** END OF THIS PROJECT GUTENBERG EBOOK PYGMALION ***') == -1:
		curr_line += 1
	lines = lines[:curr_line-1]
	#convert back to string
	book=' '.join(lines)
	for letter in string.punctuation:
		book=book.replace(letter,'')
	#May need to remove character names here
	#convert to lowercase
	book=book.lower()
	#remove whitespace and split into word list
	word_list=book.split()
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
	for word in word_list:
		if not word.isalnum() and word.islower():
			print word
			raise TypeError('This word is either uppercase or non-alphanumeric')
	histogram={}
	for word in word_list:
		curr_amount=histogram.get(word,1)
		histogram[word]=curr_amount+1
	ordered_by_frequency = sorted(histogram, key=histogram.get, reverse=True)
	return ordered_by_frequency[:n]


word_list=get_word_list('pg3825.txt')
print get_top_n_words(word_list, 100)