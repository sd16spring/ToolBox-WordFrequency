""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import re
from tabulate import tabulate


def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are NOT converted to lower case, they will be converted in the second function.
	"""
	f = open(file_name, "r")
	lines = f.readlines()

	start_line = 0
	end_line = 0
	while lines[start_line].find("START OF THIS PROJECT GUTENBERG") == -1:
		start_line += 1
	while lines[end_line].find("END OF THIS PROJECT GUTENBERG") == -1:
		end_line += -1
	lines = lines[start_line+1:end_line-1]

	word_list = []
	word_pattern = re.compile('([\w\']+)')
	for line in lines:
		word_list += re.findall(word_pattern, line)

	return word_list


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to have no
					punctuation, but NOT all lowercase)
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_frequencies = {}
	for word in word_list:
		word_frequencies[word.lower()] = word_frequencies.get(word.lower(), 0) + 1

	top_words = sorted(word_frequencies, key=word_frequencies.get, reverse=True)[:n]
	return [(word_frequencies[word], word) for word in top_words]

def print_tabled_words(top_words_data):
	print tabulate(
		[("Frequency", "Word")] + top_words_data, headers="firstrow", tablefmt="rst")

if __name__ == "__main__":
	word_list = get_word_list("46421.txt")
	top_words_data = get_top_n_words(word_list, 100)
	print_tabled_words(top_words_data)
	# unformatted for no tabulate install:
	# print top_words_data
