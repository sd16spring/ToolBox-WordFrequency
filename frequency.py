""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import urllib

# Creates new file AliceText.txt that contains the contents of Project Gutenbergs html for Alice in Wonderland.
# f = open('AliceText.txt', 'wb')

# url = 'https://www.gutenberg.org/files/11/11-h/11-h.htm'
# s = urllib.urlopen(url).read()

# f = open('AliceText.txt', 'rb')

# Saves to file f
# f.write(s)
# print f.read()
#Ensures that everything you were writing makes it out + Ensures you don't have too many open files.
# f.close()

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	wordlist = []

	f = open(file_name, 'rb')
	file_text = f.read()
	newstring = file_text.lower().translate(None, string.punctuation).replace("\t", "").replace("p", "").replace("mdash", "")

	for word in newstring.split():
		wordlist.append(word)
	f.close()
	return wordlist

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	hist = {}
	sortedlist = []

	for word in word_list:
		if word in hist:
			hist[word] += 1
		else:
			hist[word] = 1
	sorted_filetext = sorted(hist, key = hist.__getitem__, reverse = True)	
	for i in range(1,n):
		sortedlist.append(sorted_filetext[i])
	return sortedlist


wordlist = get_word_list('AliceText.txt')
print get_top_n_words(wordlist, 10)