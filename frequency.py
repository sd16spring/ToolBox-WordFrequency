""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    chars = string.punctuation + string.whitespace #characters to strip out

    f = open(file_name,'r')
    lines = f.readlines()

    # Strip away header
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    # Strip away footer
    curr_line = 0
    while lines[curr_line].find('THE END') == -1:
        curr_line += 1
    lines = lines[:curr_line]

    list_of_lists = [line.split(' ') for line in lines]
    joined_list = [word for sublist in list_of_lists for word in sublist]
    words = [word.strip(chars) for word in joined_list if word.strip(chars) != '']

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
    def histogram(seq):
        d = dict()
        for c in seq:
            d[c] = 1 + d.get(c, 0)
        return d

    word_counts = histogram(word_list)

    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)

    return ordered_by_frequency[:n]

print get_top_n_words(get_word_list('pg32325.txt'), 100)
