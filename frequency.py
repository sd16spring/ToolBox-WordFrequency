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
 
    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].translate(None, string.punctuation)
        lines[i] = lines[i].lower()

    while '' in lines:
        lines.remove('')

    words = []
    for line in lines:
        words_per_line = line.split(' ')
        words += words_per_line

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
    word_counts = {}
    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    return ordered_by_frequency[:n+1]

if __name__ == "__main__":
    print get_top_n_words(get_word_list('pg32325.txt'),100)
