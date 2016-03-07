""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name,'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    words = []
    for line in lines:
        linelist = line.split()
        for word in linelist:
            words.append(word.strip(string.punctuation))
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
    word_hist = {}
    for word in word_list:
        word_hist[word] = word_hist.get(word, 0) + 1

    lst = [(word_hist[key], key) for key in word_hist]
    lst.sort(reverse=True)
    return lst[:n]


if __name__ == '__main__':

    print(get_top_n_words(get_word_list('ulysses.txt'), 100))
