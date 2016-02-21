""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

from string import *

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	new_list = []

	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	end_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	while lines[end_line].find('End of the Project Gutenberg EBook of Metamorphosis') == -1:
		end_line -= 1
	lines = lines[curr_line + 1:end_line]

	long_lines = ''.join(str(e) for e in lines)
	long_lines = long_lines.lower()
	long_lines = long_lines.translate(None, punctuation)

	words = long_lines.split()
	for item in words:
		new_list.append(item)

	return new_list


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_counts = dict()
	for word in word_list:
		word_counts[word] = 1 + word_counts.get(word,0)

	words_list = word_counts
	sorted_list = sorted(words_list.items(), key = lambda x: x[1])
	final_list = []

	i = -1
	while i > ((-1 * n) - 1):
		final_list.append(sorted_list[i])
		i -= 1

	list_without_numbers = [x[0] for x in final_list]

	return list_without_numbers

metamorphosis_text = get_word_list('Metamorphosis.txt')
top_100_words = get_top_n_words(metamorphosis_text, 100)

print top_100_words