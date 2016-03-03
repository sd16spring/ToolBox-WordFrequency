""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from collections import Counter

def get_word_list(filename):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	list_words = []
	fp = processing_file(filename)

	for line in fp.split('\n'):
		process_line(line, list_words)

	return list_words

def process_line(line, list_words):
	'''gets rid of white space and punctuation and puts words into a dictionary'''
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.whitespace + string.punctuation)
		word = word.lower()

		list_words.append(word)

	return list_words

def processing_file(filename):
	"""processing initial file, stripping out guttenberg extra stuff"""
	fp = open(filename)
	all_text = fp.read()
	index_start = all_text.find('CONTENTS')
	index_end = all_text.find('End of Project Gutenberg')
	content =  all_text[index_start: index_end]
	
	new_story = []
	for line in content.split('\n'):
		if any_lowercase(line):
			new_story.append(line)
			
	story = ''.join(new_story)
	return story
	   

def any_lowercase(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag	


def get_top_n_words(filename, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	hist = Counter(get_word_list(filename))
	
	t = []
	for word, count in hist.iteritems():
		t.append((count, word))
		t.sort(reverse = True)
	

	res = []
	for count, word in t[0:n]:
		res.append(word)
	print res
   

get_top_n_words('grimm_fairytales.txt', 100)