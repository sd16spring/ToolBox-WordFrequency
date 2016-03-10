""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg

    @author: March Saper

    Written for Software Design 2016 - Olin College"""

import string
from pattern.web import*


def get_word_list(name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    bookURL = URL(name).download()
    text = plaintext(bookURL)
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    text = text.lower()
    text = text.split()
    return text


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
        >>> get_top_n_words(['one', 'short', 'day', 'in', 'the', 'one', 'one', 'short'], 2)
        ['one', 'short']

    """
    freq = {}
    for w in word_list:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    word_freq = freq.items()
    freq_word = []
    for word, freq in word_freq:
        freq_word.append((freq, word))
    freq_word.sort(reverse = True)
    most_pop = []
    for i in range(n):
        most_pop.append(freq_word[i][1])
        
    return most_pop


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    book = get_word_list('http://gutenberg.readingroo.ms/5/1/514/514.txt')
    top_words = get_top_n_words(book, 20)
    print top_words