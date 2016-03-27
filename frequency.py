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


	#improved_lines gives lines without the \n parts, without the punctuation at the end of each line
	improved_lines = []
	for line in lines:
		improved_lines.append(line.strip().strip(string.punctuation))

	#returns new list without '' inside
	improved_lines_without_spaces = []
	for line in improved_lines:
		if line != '':
			improved_lines_without_spaces.append(line.strip(string.punctuation))
	

	#An attempt to strip punctuation that failed:
	# improved_lines_without_punctuation = []
	# for line in improved_lines_without_spaces:
	# 	improved_lines_without_punctuation.append(line.strip('!@#$%^&*():"<>?;'))
	# print improved_lines_without_punctuation

	#everything_string is a list with all the words (including repeats)
	everything_string = ""
	for a_string in improved_lines_without_spaces:
		everything_string = everything_string + " " + a_string
	everything_list = everything_string.strip().lower().split()

	#Making a histogram, format: list of tuples 
	d = dict() #dictionary of terms:
	for word in everything_list:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	list_of_tuples = d.items()

	#Getting a list of all possible numbers of occurrences given the text
	frequencies = []
	for a_word in list_of_tuples:
		word, occurrence = a_word
		if occurrence not in frequencies:
			frequencies.append(occurrence)
	frequencies.sort(reverse = True)
		
	#finding the words with maximum occurrences:
	sorted_list = []
	for frequency in frequencies:
		for word in d:
			if frequency == d[word]:
				sorted_list.append(word)
	return sorted_list

	#Final result: list of words arranged by most used to least used
	fin.close()


official_word_list = get_word_list('prideandprejudice.txt')
#print official_word_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	get_top_n_words = word_list[0:n-1]
	return get_top_n_words

print get_top_n_words(official_word_list, 20)

