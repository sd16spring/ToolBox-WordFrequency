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
	lines = f.readlines()
	start_line = 0
	while lines[start_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		start_line += 1
	final_line = 0
	while lines[final_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
		final_line += 1

	lines = lines[start_line+1:final_line]
	words = []

	for line in lines:
		for wordCandidate in line.split():
			refinedWord = wordCandidate.strip(string.whitespace+string.punctuation).lower()
			if len(refinedWord) > 0:
				words.append(refinedWord)

	return words

def get_top_n_words(words, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	dictionary = dict()
	for word in words:
		dictionary[word] = dictionary.get(word,0) + 1
	ordered_list = sorted(dictionary, key=dictionary.get, reverse=True)
	return ordered_list[:n]


if __name__ == "__main__":
	print get_top_n_words(get_word_list("pg2600.txt"), 100)