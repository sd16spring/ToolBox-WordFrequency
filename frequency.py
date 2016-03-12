""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import csv
import string
import pickle
import operator

def get_word_list(file_name):
        """ Reads the specified project Gutenberg book.  Header comments,
            punctuation, and whitespace are stripped away.  The function
            returns a list of the words used in the book as a list.
            All words are converted to lower case.
        """
        text = open(file_name,'r').read()
        text = string.lower(text)
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = string.replace(text, ch, ' ')
        words = string.split(text)

        counts = {}
        for w in words:
            counts[w] = counts.get(w,0) + 1

        f = open('./wordcount', 'w')
        pickle.dump(counts,f)
        f.close()
        return counts

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                        punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                    frequently to least frequentlyoccurring
	"""
    inf = open('./wordcount', 'r')
    data = pickle.load(inf)
    sorted_data = sorted(word_list.items(), key=operator.itemgetter(1), reverse = True)
    #orted_data =sorted(word_list)
    outf = open('./sortedwordcounts' , 'w')
    pickle.dump(sorted_data,outf)
    return sorted_data[:n]

print(get_top_n_words(get_word_list('merchantofvenice'), 100))