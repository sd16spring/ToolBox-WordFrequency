""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pattern.web import *
import operator
url = URL('http://www.gutenberg.org/ebooks/161.txt.utf-8')
all_gutenberg = url.download()
start_location = all_gutenberg.index('Chapter 1')
end_location = all_gutenberg.index('End of the Project Gutenberg EBook of Sense and Sensibility, by Jane Austen')
just_book = all_gutenberg[start_location:end_location]


f = open('sense_and_sensibility.txt', 'w')
f.write(just_book)
f.close()



def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name, 'r+')
	lines = ""
	words = []
	for line in f.read().split("\n"):
		lines += line.strip(string.punctuation + string.whitespace) + " "
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()
			words.append(word)
	return words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

    wordcount={} # new dictionary
    for word in word_list:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse = True)
    res = [] #list of words in order of most to lesat frequent
    for (key,value) in sorted_wordcount:
 		res.append(key)
    return res[:n]

print get_top_n_words(get_word_list('sense_and_sensibility.txt'), 100)
