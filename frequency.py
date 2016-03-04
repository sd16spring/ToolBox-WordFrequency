""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string
from pattern.web import *

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """

    f = open(file_name,'r')
    text = f.read()
    f.close()

    #"Chapter" only occurs at the beginning of chapters, so this is fine
    chapter_list = text.split('Chapter')
    #Removes everything before the first real chapter
    chapter_list.pop(0)

    #Remove the ending Project Gutenberg text
    ending_index = chapter_list[-1].index('End of the Project')
    chapter_list[-1] = chapter_list[-1][:ending_index]

    #Replace all punctuation with spaces
    #Case correct
    #Split chapter into list of words
    #Remove first "word" (it's the chapter number)
    clean_chapters = []
    #removes apostrophes from string.punctuation
    translation_table = string.maketrans(string.punctuation[:6]+string.punctuation[7:],' '*(len(string.punctuation)-1))
    for chapter in chapter_list:
        new_chapter = chapter.translate(translation_table)
        new_chapter = new_chapter.lower()
        new_chapter = new_chapter.split()
        new_chapter = new_chapter[1:]
        clean_chapters.append(new_chapter)

    #Return only the list of words
    return [word for chapter in clean_chapters for word in chapter]

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    d = {}
    for word in word_list:
        d[word] = d.get(word,0) + 1

    tuple_list = d.items()
    #Sort by the number of occurences
    tuple_list.sort(key=lambda tup: tup[1],reverse=True)

    #Return a list of only the top n words
    return [tuple_list[i][0] for i in range(n)]


top_100_words = get_top_n_words(get_word_list('pride_and_prejudice_full_text.txt'),100)
print top_100_words