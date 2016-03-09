""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from nltk.corpus import stopwords


def get_word_list(file_name):

	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# open book for reading/parsing
	ft = open(file_name, 'r')
	
	# create empty list to append words from book into
	Grimms_edit = []

	# list of stopwords to filter out boring words
	stop = set(stopwords.words('english'))


	for line in ft:
		""" for each line in the book, remove punctuation and hyphens """
		line = line.translate(None, string.punctuation)
		line = line.replace('-', ' ')

		""" for each word in each line, remove extra whitespace and lowercase all letters """
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()

			# filter out boring words
			if word not in stop:
				Grimms_edit.append(word)		# append to empty list
			else:
				pass
	get_top_n_words(Grimms_edit, 100)			# top 100 words of filtered words from book


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	# initialize dictionary called histogram
	hist = dict()

	# for each word in the list, find frequency
	for word in word_list:
		hist[word] = hist.get(word, 0) + 1

	# create new list of words sorted by frequency
	t = []
	for key,value in hist.items():
		t.append((value, key))

	t.sort(reverse = True)

	# print most common words based on n
	print 'The most common words are: '
	for freq,word in t[:n]:
		print word, '\t', freq


get_word_list('GrimmsFairyTales.txt')