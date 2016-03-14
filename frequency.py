""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string


def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  
		The function returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	
	fin = open(file_name, 'r')

	lines = fin.readlines()

	current_line = 0
	while lines[current_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		current_line += 1
	lines = lines[current_line+1:]


	#improved_lines gives lines without the \n parts
	improved_lines = []
	for line in lines:
		improved_lines.append(line.strip())

	#returns new list without '' inside
	improved_lines_without_spaces = []
	for line in improved_lines:
		if line != '':
			improved_lines_without_spaces.append(line.strip(string.punctuation))
	# print improved_lines_without_spaces

	#Next step: turn all words lowercase

	#Then: Make list that's a histogram

	#Final result: list of words arranged by most used to least used

	fin.close()


print get_word_list('prideandprejudice.txt')






def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	complete_word_list = get_word_list(word_list)
	get_top_n_words = word_list[0:n-1]
	pass