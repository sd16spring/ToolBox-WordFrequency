"""
Daniel Daugherty 
Word Frequency Analysis

Analyzes the word frequencies in a book downloaded from
Project Gutenberg 

"""

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	
	# Opens the file and strips away the header comment
	f = open(file_name, 'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('Chapter 1') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	# Removes the end comments of the text file 
	curr_line = len(lines) - 1
	while lines[curr_line].find('End of Project Gutenberg') == -1:
		curr_line -= 1
	lines = lines[:curr_line-1]

	# Formats all words into one big list and filters out chapter headers and empty lines
	wordslist = []
	for words in lines:
		if words.split() != [] or words[:7] != "Chapter":
			wordslist += words.lower().split()

	# Removes all punctuation
	final_list = []
	for word in wordslist:
		new_word = ""
		for letter in word:
			if letter in string.punctuation:
				letter = ""
			new_word += letter
		if new_word != "":
			final_list.append(new_word)

	# Returns list of all words in the book
	return final_list


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	# Creates a histogram of how often the same word appears in the book
	word_histogram = dict()
	for word in word_list:
		word_histogram[word] = 1 + word_histogram.get(word, 0)

	# Converts the dictionary into a tuple and sorts the tuple by the frequency of each word
	word_tup = word_histogram.items()
	word_tup = sorted(word_tup, key = lambda x : x[1], reverse = True)

	# Creates a sorted list of the recurring words
	res = []
	for word, frequency in word_tup:
		res.append(word)

	# Returns the n most frequent words within the book
	return res[:n]





if __name__ == '__main__':
	words = get_word_list("Monte_Cristo.txt")
	print get_top_n_words(words, 100)