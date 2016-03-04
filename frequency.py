""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """


"""
Completed by Kevin Zhang 3/3/2016
Software Design Spring 2016
"""

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""

	#opened file, read lines, and start at the beginning of the book instead of beginning of file
	file = open(file_name,'r')
	content_in_lines = file.readlines()
	curr_line = 0
	while content_in_lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	content_in_lines = content_in_lines[curr_line+1:]


	#put everything into a giant string
	content = ' '.join(content_in_lines)

	punctuation = string.punctuation
	p_list = []


	#appended all punctuations into a list
	for char in punctuation:
		p_list.append(char)

	whitespace = string.whitespace	

	#appended all whitespaces into the list
	for char in whitespace:
		if char != ' ':
			p_list.append(char)

	#got rid of all punctuations and whitespaces		
	for thing in p_list:
		content = content.replace(thing, '')

	#made everything lowercase
	content = content.lower()
	
	#put everything back into array
	temp = content.split(' ')
	list_content = []


	#got rid of weird spaces that were popping up in the list
	for item in temp:
		if item != '':
			list_content.append(item)


	return list_content





def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	
	content_dict = {}


	#getting rid of filler words to make the top 100 look more authentic
	baddictionary = 'me, still, put, want, i\'m, got, stop, don\'t, too, should, the, of, and, a, to, in, is, you, that, it, he, was, for, on, are, as, with, his, they, i, at, be, this, have, from, or, one, had, by, word, but, not, what, all, were, we, when, your, can, said, there, use, an, each, which, she, do, how, their, if, will, up, there, about, out, many, then, them, these, so, some, her, would, make, like, him, into, time, has, look, two, more, write, go, see, number, no, way, could, people, my, than, first, water, been, call, who, oil, its, now, find, long, down, day, did, get, come, made, may, part'
	badwords = baddictionary.split(", ")

	rawlist = [word for word in word_list if word not in badwords]

	#using DSU method to make the histogram
	for word in rawlist:
		content_dict[word] = content_dict.get(word, 0) + 1

	sortedlist = []

	for item, value in content_dict.items():
		sortedlist.append((value, item))

	sortedlist.sort(reverse=True)

	result = []

	for freq, word  in sortedlist:
		result.append(word)
	

	return result[:n]	

def not_in_wordlist(wordslist):


	#reads the giant word file
	file = open('words.txt','r')
	words = file.read()

	not_in_list = []

	#makes and fills a list with words that are not in the wordlist from the book
	for word in wordslist:
		if word not in words:
			not_in_list.append(word)

	return 	not_in_list

if __name__ == '__main__':

	book_words = get_word_list('huckfinn.txt')
	top100 =  get_top_n_words(book_words, 100)
	
	distinct_words = get_top_n_words(book_words, len(book_words))

	print "The number of words in this book is:", len(book_words)
	print "The number of different words used in this book is:", len(distinct_words)
	print "The top 100 most frequently used words in this book are:"

	for i in range(len(top100)):
		print "{}. ".format(i+1) + top100[i]

	print "The words that are not in a common word list are:"
	print ""
	print  not_in_wordlist(distinct_words)	
