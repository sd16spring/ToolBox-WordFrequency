""" Anna Buchele

This program takes a .txt document of a book, removes all punctuation, whitespace, and turns uppercase letters to lowercase. 
Then, it analyzes the word frequencies and returns the top n most frequently used words in the book.

"""

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	book = open(file_name, 'r')
	f = ''
	for word in book:
		f = f + word
	a= f.replace(".", "")
	a= a.replace(",", "")
	a=a.replace("'","")
	a=a.replace('"','')
	a=a.replace(':','')
	a=a.replace('?','')
	a=a.replace(';','')
	a=a.replace('!','')
	a=a.replace('-','')
	a=a.replace('*','')
	a=a.replace("/", '')
	a=a.replace('\'','')
	a=a.replace('\xe2\x80\x94','')
	a=a.replace('\xe2\x80\x99','')
	a=a.replace('\xe2\x80\x9c','')
	a=a.replace('\xe2\x80\x9d','')
	a=a.lower()
	l=a.split()
	return l


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	wordscount=dict()
	for word in word_list:
		val= wordscount.get(word,0)
		wordscount[word]=val+1
	wordssort= sorted(wordscount,key=wordscount.__getitem__,reverse=True)
	topn = wordssort[:n]
	return topn

word_list = get_word_list('anne.txt')
print get_top_n_words(word_list,20)