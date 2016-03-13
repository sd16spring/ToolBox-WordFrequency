""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

from pattern.web import *
import string
import urllib2
import pickle

def get_text(URL_string, name):
	"""This function grabs the text from a text file on the web and pickles it for future use.
Arguments: URL of text file to be saved as a string, name of the file for use in naming data variables and pickle files (also a string).
 Returns: Pickled data!"""

	text = URL(URL_string).download()
	save_file = open(name + '.pickle', 'w')
	pickle.dump(text, save_file)
	save_file.close()



def open_text(name):
	"""Imports previously-pickled book data (in string format from disk) and returns a list of the strings.
	Arguements: name of the pickle file of previously pickled data (as a string, without the .pickle ending)!
	Returns: a pickle-imported string"""
	# Load data for each from from a file (will be part of your data processing script)
	input_file = open(name+ '.pickle','r')
	text = pickle.load(input_file)
	return text


def is_punct_char(char):
	"""From python.org (link in get_word_listdescription), all this does is check if a character
	is puncutation or not! the ultimate helper funcion!
	Arguments: character
	Returns: True/False if the character it is given is a puncuation mark - 1 is punctuation, 0 is not """
	return char in string.punctuation #1 is punctuation, 0 is not punctuation

def get_word_list(text_string):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case. NOTE: https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal method that I used
"""
	text_no_punc = ''
	text = text_string[600:] #kill the header
	for char in text: #killing punctuation
		if not is_punct_char(char):
			text_no_punc = text_no_punc+char #so extend the string everytime we run into a letter
	text_no_punc_lower = string.lower(text_no_punc)
	list_of_words = []
	list_of_words = text_no_punc_lower.split( ) #splitting the string into the list
	return list_of_words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
	occurring words ordered from most to least frequently occurring.
		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring" """
	freq_dict = make_freq_dict (word_list) # get a dictionary
	ordered_by_frequency = sorted(freq_dict, key=freq_dict.get, reverse=True) # sort
	print ordered_by_frequency[0:n] # print
	return ordered_by_frequency[0:n]



def make_freq_dict(word_list):
	"""This is a helper function for
	get_top_n_words. All this does is make a dictionary; takes a list of words in and makes a frequency dictionary;.
	Arguement: list of words.
	Returns: dictionary with words as keys and frequnecies as values.
		"""

	freq_dict = {}

	for word in word_list: #need to slice each tale into a list of words for this to work
		if word in freq_dict:
			current_val = freq_dict.get(word)
			val = current_val + 1
			freq_dict[word] = val #made a dictionary of the string (word, frequnecy)
		else: #if it isn't in the dictionary
			freq_dict[word] = 1
	return freq_dict





URL_string = 'http://www.gutenberg.org/cache/epub/2591/pg2591.txt'
name = 'grimm'
n = 100 #just doing some definitions to make things run automatically
get_text(URL_string, name) #dump the text into a pickle file
text_string = open_text(name) #open that file and return the string
word_list= get_word_list(text_string) # make a list of words, formatted happily
get_top_n_words(word_list, n) #get a list of the top 100 words!
