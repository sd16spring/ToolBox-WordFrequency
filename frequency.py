""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg. I downloaded Moby Dick, because it is maybe the most
	boring book ever. Looks like 'whale' is definitely within the 100 most
	used words."""

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
    word_list = []

    for line in lines:
        line_list = line.split()
        for word in line_list:
            word.strip(string.punctuation)
            word_list.append(word.lower())
    return word_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	hist = dict()
	for word in word_list:
		hist[word] = hist.get(word,0) + 1
	ordered_by_frequency = sorted(hist, key=hist.get, reverse=True)
	return ordered_by_frequency[:n]


if __name__ == "__main__":
	word_list = get_word_list('pg2701.txt')
	print get_top_n_words(word_list, 100)
