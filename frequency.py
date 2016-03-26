""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
	punctuation, and whitespace are stripped away.  The function
	returns a list of the words used in the book as a list.
	All words are converted to lower case.
    """
    #open and read file
    f = open(file_name, 'r')
    text = f.read()

    #create word list which we will return
    word_list = []

    #make lowercase
    text = string.lower(text)

    #replace punctuation with spaces
    for char in string.punctuation:
        text = string.replace(text, char, ' ')

    for line in text.split('\n'):
        for word in line.split(' '):
            word_list.append(word)

    #don't include lines with only empty or \r
    word_list = [x for x in word_list if x != '']
    word_list = [x for x in word_list if x != '\n']
    word_list = [x for x in word_list if x != '\r']

    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
	occurring words ordered from most to least frequently occurring.

	word_list: a list of words (assumed to all be in lower case with no punctuation
	n: the number of words to return
	returns: a list of n most frequently occurring words ordered from most
	frequently to least frequentlyoccurring
    """
    histogram = []

    for uniq in set(word_list):
        counter = 0
        for word in word_list:
            if uniq == word:
                counter += 1
        histogram.append((uniq, counter))
    histogram.sort(key=lambda tup: tup[1], reverse=True)
    return histogram[0:n]



file = 'pg4908.txt'

word_list =  get_word_list(file)
top_words = get_top_n_words(word_list, 20)

for item in top_words:
    print 'word = {}, number of times = {}'.format(item[0], item[1])
#it appears that something is going wrong with the text parsing.  I get some sort of space
#or new line in the histogram.
