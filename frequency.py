""" Analyzes the word frequencies in a book downloaded from
        Project Gutenberg. """

import string


def get_word_list(file_name):
    """Reads the specified Project Gutenberg book. Header comments, punctuation,
    and whitespace are stripped away. The function returns a list of the words
    used in the book as a list. All words are converted to lower case.
    """
    # this opens the file and removes the header comments
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    # this splits the text into a list
    list_of_lines = []
    for i in range(len(lines)):
        list_of_lines.append(lines[i].split())
    list_of_words = []
    for line in list_of_lines:
        list_of_words.extend(line)
    # this strips the punctuation and makes the words lowercase
    punc = string.punctuation
    new_list = []
    for word in list_of_words:
        lowerword = word.lower()
        new_list.append(lowerword.strip(punc))
    return new_list


def get_top_n_words(word_list, n):
    """Takes a list of words as input and returns a list of the n most
    frequently occuring words ordered from most to least frequently occuring.

        word_list: a list of words (assumed to all be in lower case with no
            punctuation)
        n: the number of words to return
        returns: a list of n most frequently occuring words ordered from most
            frequently to least frequently occuring
    """
    histogram = {}
    for word in word_list:
        histogram[word] = histogram.get(word, 0) + 1
    most_frequent = []
    for key, value in histogram.items():
        most_frequent.append((value, key))
    most_frequent.sort(reverse=True)
    list_frequent = []
    for item in most_frequent[:n]:
        list_frequent.append(item[1])
    return list_frequent[:n]

if __name__ == '__main__':
    word_list =  get_word_list('135-0.txt')
    print get_top_n_words(word_list, 100)
