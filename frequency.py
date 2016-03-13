""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from pattern.web import *
from pattern.en import *
"""
f1 = open('AStudyInScarlet', 'w')
url = URL('http://www.gutenberg.org/cache/epub/244/pg244.txt')
study_scarlet = plaintext(URL('http://www.gutenberg.org/cache/epub/244/pg244.txt').download())
f1.write(study_scarlet.encode("UTF-8"))
f1.close()
"""
def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name, 'r')
	lines = f.readlines()
	curr_line = 0
	end_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	while lines[end_line].find('ORIGINAL TRANSCRIBER') == -1:
		end_line +=1
	#for line in lines:
	#	if 'END OF THIS PROJECT GUTENBERG EBOOK' in line:
	#		break
	#	else:
	#		book = ''.join(lines)
	#		new_book = book.split()
	lines = lines[curr_line+1:end_line-1]
	book = ''.join(lines)
	new_book = book.split()
	word_list = []
	for word in new_book:
		new_word = word.strip(string.punctuation)
		newer_word = new_word.strip(string.whitespace)
		newest_word = newer_word.lower()
		word_list.append(newest_word)
	return word_list

file_name = 'AStudyInScarlet'
get_word_list(file_name)

def get_top_n_words(word_list, n):
	"""Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring"""
	
	word_counts = {}
	for word in word_list:
		if word not in word_counts:
			word_counts[word] = 1
		else:
			word_counts[word] += 1
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	return ordered_by_frequency[0:n]


if __name__ == '__main__':
 	file_name = 'AStudyInScarlet'
 	word_list = get_word_list(file_name)
 	n = 100
 	print get_top_n_words(word_list, n)