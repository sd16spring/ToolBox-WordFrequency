""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

##I used the given text because project gutenberg kept erroring on the browsers I was using. 
# This is the text file I used shad0kn1ght.tripod.com/basement/PrideandPrejudice.txt

import string
import operator

#The book I'm uploading is PrideandPrejudice

def get_word_list(BookName): #Be sure that this input is a string
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	""" 
	file = open(BookName +'.txt', 'r')
	word_list =[]
	for line in file: 
	#Getting rid of punctuation 
		line = "".join(c for c in line if c not in string.punctuation) + ""
		b = line.split() 
		for word in b: 
			word_list.append(word)

	return word_list

get_word_list("PrideandPrejudice")
	


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_dict2 = {}
	word_list = get_word_list("PrideandPrejudice")
	for word2 in word_list: 
		word_dict2[word2] = word_dict2.get(word2, 0) + 1 
	tuple_list = [(value, key) for key, value in word_dict2.iteritems()]
	tuple_list = sorted(tuple_list, reverse=True)

	final_list = []
	
	for pair in tuple_list[0:n]:
		final_list.append(pair[1]) 

	print(final_list)

word_list = get_word_list("PrideandPrejudice")
get_top_n_words(word_list, 100)