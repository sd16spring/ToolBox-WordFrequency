""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	"""	
	Reads the specified project Gutenberg book.  Header comments,
	punctuation, and whitespace are stripped away.  The function
	returns a list of the words used in the book as a list.
	All words are converted to lower case.
	"""
	file1 = open(file_name) #opens text file
	lines = file1.readlines()
	curr_line = 0
	end_line = 0
	# finds the start of the book
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
			curr_line += 1
	# finds the end of the book
	while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
			end_line += 1
	lines = lines[curr_line+1:end_line]

	# creates a new string wihtout punctuation 
	no_punctuation = ''	
	punctuation = string.punctuation
	for character in lines:
		if character not in punctuation:
			no_punctuation = no_punctuation + character

	# makes a new list with all lower case words
	final_word_list = []
	for word1 in no_punctuation.split():
		word2 = str.lower(word1)
		final_word_list.append(word2)

	return final_word_list


# print(get_word_list('alice1.txt'))


def get_top_n_words(word_list, n):
	""" 
	Takes a list of words as input and returns a list of the n most frequently
	occurring words ordered from most to least frequently occurring.

	word_list: a list of words (assumed to all be in lower case with no
			punctuation
	n: the number of words to return
	returns: a list of n most frequently occurring words ordered from most
			frequently to least frequentlyoccurring
	"""
	word_dictionary = {} #creates an empty dictionary to hold words
	# adds words and the number of times they exist to the empty dictionary
	for words in word_list:
		word_dictionary[words] = word_dictionary.get(words, 0) + 1

	# sorts words by the number of times they appear
	ordered_by_frequency = sorted(word_dictionary, key=word_dictionary.get, reverse=True)

	# creates a list of the n most common words
	n_most_common = ordered_by_frequency[:n]
	print n_most_common


# word_list1 = get_word_list('alice1.txt')
# print get_top_n_words(word_list1, 100)