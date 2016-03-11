""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_dict(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a dictonary of the words used in the book mapped to their
		frequencies. All words are converted to lower case.
	"""
	word_freq_dict = {}
	book = open(file_name)
	useless = True
	while useless:
		line = book.readline()
		if 'START OF THIS PROJECT GUTENBERG EBOOK' in line:
			useless = False
	while not useless:
		line = book.readline()
		if 'END OF THIS PROJECT GUTENBERG EBOOK' in line:
			useless = True
			break
		words = line.split()
		for word in words:
			stripped_word = word.strip(string.punctuation).lower()
			word_freq_dict[stripped_word] = word_freq_dict.get(stripped_word, 0) + 1
	return word_freq_dict

def get_top_n_words(file_name, n):
	""" Takes a file as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		returns: a list of n most frequently occurring words and their frequencies ordered from most
				 frequently to least frequently occurring
		It would not be hard to make it fit the original behavior, but I think this is more interesting.
	"""
	words_dict = get_word_dict(file_name)
	words_list = words_dict.items()
	words_list.sort(key=lambda word_frequency_pair: word_frequency_pair[1], reverse=True)
	return words_list[:n]

top_words = get_top_n_words('great_expectations.txt', 100)
for word_pair in top_words:
	print '{} occurs {} times.'.format(word_pair[0], word_pair[1])