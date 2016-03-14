""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('*** START OF THIS PROJECT GUTENBERG EBOOK BIBLE, KING JAMES VER., COMPLETE ***') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    data = ''.join(lines)
    print type(data)
    data = data.lower
    data = data.translate(None, string.punctuation)
    data = data.split()
    return data 

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
        frequently to least frequently occurring
    """
    word_count = dict()
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    word_count = sorted(word_count, key = word_count.get, reverse = True)
    top_n_words = word_count[0:(n-1)]
    return top_n_words

print get_top_n_words(get_word_list('Bible.txt'), 100)