""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg 

    @AUTHOR REBECCA PATTERSON 03-10-16"""
#import packages that are used
import pickle
import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    #first load the data file with the text
    input_file= open(file_name, 'r')
    #strips away the header comment
    lines= input_file.readlines()
    current_line=0
    while lines[current_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        current_line+=1
    lines= lines[current_line+1:]
    #converts all letters in text to lower case
    lower_text=str()
    for line in lines:
        lower_text+= " " +line.lower()
    #create list of words in string (to eliminate white space) with puncuation stripped away
    clean_text= [x.strip(string.punctuation) for x in lower_text.split()]
    return clean_text


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequently occurring
    """
    #make empty dictionary, fill with key=word, value=word count from input word list
    d= dict()
    for word in word_list:
        d[word]= d.get(word, 0)+1
    #creates list of tuples with count before the word for elements in dictionary
    word_count= []
    for word in d:
            word_count.append((d[word], word))
    #sort list in order of decreasing word count value
    word_count.sort(reverse=True)
    #rewrite with just the word
    words= []
    for count, word in word_count:
        words.append(word)
    #create list of top n occuring words
    top= words[0:n-1]   
    return top

if __name__=='__main__':
    """when the code is ran, the chosen book pickle file is converted into a list
    that is then analyezed for word count"""
    n=100
    word_list= get_word_list('Dracula_full_text.txt')
    top_words= get_top_n_words(word_list, n)
    print top_words