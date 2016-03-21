""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	book = open(file_name, 'r') #open the file
	lines = book.readlines() #creates a list of strings. Each string is one line of the book
	begin_line = lines.index('*** START OF THIS PROJECT GUTENBERG EBOOK FRANKENSTEIN ***\r\n') #finds the index value for the header
	end_line = lines.index('End of the Project Gutenberg EBook of Frankenstein, by\r\n') #finds the index value for the footer
	lines = lines[begin_line+1:end_line] #modifies list lines to start after the header and end before the footer
	book = ''.join(lines) #rejoins the lines into one string
	punc = string.punctuation + '\r\n' #creates a list of all possible punctuations, as well as the newline command
	spaces = ''
	for char in punc:
		spaces += ' ' #creates a list of spaces that's just as long as punc
	translator = string.maketrans(punc, spaces) #key for translation
	bookNoPunc = book.translate(translator) #finds all items in punc that are present in the book and converts them to spaces
	bookNoSpaces = bookNoPunc.split() #separates the book out into a list in which each word is separate and spaces are gone
	wordsList = []
	for word in range(len(bookNoSpaces)):
		wordsList.append(bookNoSpaces[word].lower()) #makes sure that every word in the final list is entirely lowercase
	return wordsList

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	#creating a dictionary in which each unique word is a key and its value is the number of times it appears
	word_dict = {}
	for word in word_list:
		if word not in word_dict:
			word_dict[word] = 1
		elif word in word_dict:
			word_dict[word] += 1
	ordered_by_frequency = sorted(word_dict, key=word_dict.get, reverse = True) #sorts by value, as given in the hints for this toolbox
	return ordered_by_frequency[:n]

bookToSearch = get_word_list('Frankenstein.txt')
print get_top_n_words(bookToSearch, 100)