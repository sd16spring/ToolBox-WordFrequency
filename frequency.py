""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg 
    
    For the Olin College Software Design class. 
    Script skeleton provided.

    @Author Elizabeth Sundsmo 3/10/2016
    """
import string
from operator import itemgetter

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    #Opens book file. Should be in same folder as this script. (plaintext)
    chosen_book = open(file_name,'r')

    #strip out header comment
    lines = chosen_book.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:] #list of lines

    #convert list of lines into list of lowercase words
    book_contents = str()
    for line in lines:
        book_contents +=" "+ line.lower()

    #cuts the text string wherever there is a space, 
    #then removes all punctuation from the cut string and places in a list
    clean_text = [s.strip(string.punctuation) for s in book_contents.split()]
    
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
    #create a dictionary of words present in text. 
    d = dict()
    for word in word_list:
        #If word exists increment counter from current value, or create key with value 1
        d[word] = d.get(word, 0) +1
    
    #sorts the dictionary based on the values from high to low 
    frequency_all_words = sorted(d.items(), key=itemgetter(1), reverse=True)
    # print frequency_all_words
    #puts the first n keys from the ordered dictionary into a list
    top_n_words = []
    for word, count in frequency_all_words:
        top_n_words.append(word)

    return top_n_words[0:n-1]



if __name__ == '__main__':

    book_word_list = get_word_list('alice_in_wonderland_texts.txt')
    top_100_words = get_top_n_words(book_word_list, 100)
    print top_100_words