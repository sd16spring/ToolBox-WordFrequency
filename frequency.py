from string import punctuation

""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    text = open(file_name)
    lines = text.readlines()
    text.close()
    
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    curr_line = 0
    while lines[curr_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line -= 1
    lines = lines[:curr_line]

    word_list = []
    for i in range(len(lines)):
        lines[i] = lines[i].lower()
        temp = (' '.join(filter(None, (word.strip(punctuation) for word in lines[i].split()))))
        # print lines[i]
        if temp != '':
            for word in temp.split():
                word_list.append(word)
    
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequently occurring
    """
    all_words = dict()

    for word in word_list:
        if word not in all_words:
            all_words[word] = 1
        else:
            all_words[word] += 1

    #create empty tuple
    tupl = []
    #reverses dictionary inside a tuple
    for x,y in all_words.items():
        tupl.append((y,x))
    #sort tuple by frequency of words
    tupl.sort(reverse = True)
    
    lst = []
    #create a list sorted by frequency of words
    counter = 0
    for x,y in tupl:
        if counter <= n:
            lst.append(y)
            counter += 1
    return lst

if __name__ == '__main__':
    print get_top_n_words(get_word_list('pg32325.txt'),100)