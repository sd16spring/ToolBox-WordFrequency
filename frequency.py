""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from string import maketrans

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('TOM!') == -1:
		curr_line += 1
	lines = lines[curr_line:]

	#replace all punctuation and whitespace
	newlines = []
	intab = string.punctuation
	outtab = " " * len(string.punctuation)
	trantab = maketrans(intab, outtab)

	for i in lines[:]:
		i = i.strip() #strip whitespace
		if not(i == ""):
			i = i.translate(trantab) #strip punctuation
			i = i.lower()
			i = i.strip()
			newlines.append(i)

	#split into individual words
	words = []
	for i in newlines[:]:
		i = i.split()
		words.extend(i)

	#take out the words I don't like
	words_i_dont_like = ['the', 'and', 'a', 'to', 'of', 'it', 'he',
						 'was', 'that', 'i', 'in', 'you', 's', 'his',
						 'with', 't', 'they', 'but', 'for', 'had',
						 'him', 'as', 'she', 'on', 'at', 'so', 'said',
						 'all', 'there', 'this', 'be', 'then', 'not', 'up',
						 'by', 'now', 'her', 'out', 'no', 'were', 'if',
						 'what', 'would', 'll', 'don', 'or', 'when', 'me', 'is',
						 'do', 'we', 'their', 'one', 'from', 'time', 'an',
						 'could', 'got', 'well', 'about', 'them', 'have',
						 'down', 'any', 'boys', 'did', 'been', 'upon',
						 'just', 'more', 'see', 'into', 'go', 'd',
						 'over', 'boy', 'away', 'know', 'never', 'again', 'come',
						 'can', 'like', 'other', 'ain', 'back', 'oh', 'came',
						 'some', 'two', 'went', 'get', 'here',
						 'long', 't', 'm', 're', 've', 'too', 'off', 'your']
	final_words=[]
	for word in words:
		if word not in words_i_dont_like:
			final_words.append(word)
	return final_words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_counts = dict()
	for word in word_list:
		#increments word count by 1
		word_counts[word] = word_counts.get(word, 0) + 1
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	return ordered_by_frequency[:n]


word_list = get_word_list("TomSawyer.txt")
print get_top_n_words(word_list,100)