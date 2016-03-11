""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg."""

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
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    wordlist = []
    for line in lines:
        line = line.lower()
        for char in line:
            line = line.replace('\r\n', '')
            if char in string.punctuation:
                line = line.replace(char, '')
        wordlist += line.split(' ')
    return wordlist

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequently occurring
    """
    #create dictionary
    wordcounts = {}
    #add 1 for every occurence of the word
    for word in wordlist:
        wordcounts[word] = wordcounts.get(word, 0) + 1
    #remove empty string from dictionary
    if '' in wordcounts: del wordcounts['']
    #sorts the dictionary elements by frequency
    ordered_by_frequency = sorted(wordcounts, key=wordcounts.get, reverse=True)
    #get the first n items and return them
    return ordered_by_frequency[0:n]

    
wordlist = get_word_list('pg32325.txt')
print get_top_n_words(wordlist, 100)