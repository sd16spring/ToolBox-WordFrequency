""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	with open(file_name,'r') as f:
		text = f.read()
		text = text.translate(None, string.punctuation).lower() #Formatting
	return string.split(text)

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_dict = {}
	for word in word_list:
		word_dict[word] = word_dict.get(word, 0) + 1
	ordered_list = sorted(word_dict, key=word_dict.get, reverse=True)
	return ordered_list[:n]

if __name__ == '__main__':
	lisht = get_word_list('pg32325.txt')
	print get_top_n_words(lisht, 100)
