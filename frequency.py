""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pattern.web import *
from pattern.en import tokenize 
from operator import itemgetter, attrgetter, methodcaller

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# Open pre-loaded file
	f = open(file_name,'r')

	# Preparing to remove unwanted txt
	lines = f.readlines() # a single line of txt file
	s_curr_line = 0 # initiate line index for searching from start
	e_curr_line = 0 # initiate line index for searching from end

	# For lines in txt look for string 
	# Returns -1 for failure to find string
	while lines[s_curr_line].find('CHAPTER I') == -1:
		s_curr_line += 1
	while lines[e_curr_line].rfind('THE END') == -1:
		e_curr_line += 1
	# while lines[e_curr_line].rfind('Her sister, Miss Watson, a tolerable slim old maid') == -1:
	# 	e_curr_line += 1

	# Lines now only contains story text 
	lines = str(lines[s_curr_line + 1: e_curr_line -1])

	# Clean lines 
	lines = lines.lower() # convert to lower case
	lines = lines.translate(string.maketrans("",""), string.punctuation) # remove punctuation
	lines = lines.strip() # strip whitespace 
	word_list = lines.split() # split into list of words 

	return word_list
	
	
def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently soccurring
	"""
	dictionary = dict() # initializing empty dictionary 

	# In dictionary words=keys and occurance=value
	for word in word_list: # go through each word in list 
		if word not in dictionary: # if the word is already in the dictionary 
			dictionary[word] = 1 # update dictionary entry
		else: # create a new entry with occurance of one 
			dictionary[word] += 1

	# Orders words based on frequency
	t = dictionary.items() # creates list of tuples of dictionary entires 
	ordered = sorted(t, key=itemgetter(1), reverse=True) # sorts the list of tuples by second entry (value)
	highest_freq = ordered[0:n] # pulls n most freq occuring words 

	return highest_freq

print get_top_n_words(get_word_list('pg32325.txt'),100)

