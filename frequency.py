""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """
import pickle
import string
import BeautifulSoup as bs
from pattern.web import *
# pnp_full_text = URL('http://www.gutenberg.org/files/1342/1342.txt').download()
# # Save data to a file
# f = open('pride_and_prejudice_and_.pickle','w')
# pickle.dump(pnp_full_text,f)
# f.close()
#
# input_file = open('pride_and_prejudice_and_.pickle','r')
# pnp = pickle.load(input_file)
# input_file = (pnp,open('pride_and_prejudice.txt','w'))
# input_file.close()

# input_file = open('kpop.pickle','r')
# bad_taste = pickle.load(input_file)
# input_file.close()
# print bad_taste

# f = open('dickens.txt', 'w')
# print f
# f.write(s)
# f.close()
# print 'done'
def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	all_words = []
	#f = pickle.load(open(file_name,'r'))
	f = open(file_name,'r')
	# f = pickle.load()
	lines = f.readlines()
	# print lines
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	# end_line = 0
	# while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
	# 	end_line += 1
	# lines = lines[curr_line+1:end_line-2]
	for line in range(len(lines)):
		# lines[line] = lines[line].translate(' ','whitespace')
		# lines[line] = lines[line].strip()
		# lines[line] = lines[line].unicode()
		lines[line] = lines[line].lower()
			# if char == 'rn':
			# 	line = line.replace(char,' ')
		words = lines[line].split(' ')
		for word in range(len(words)):
			words[word] = words[word].strip()
			# words.append(words[word].split('/'))
			for char in words[word]:
				if char in string.punctuation:
					words[word] = words[word].replace(char,'')
		all_words += words
		return all_words
	# for i in range(len(all_words)):
	# 	try:
	# 		all_words[i] = all_words[i].strip()
	# 	except UnicodeEncodeError:
	# 		all_words[i] = ''

the_words = get_word_list('pride_and_prejudice_and_.pickle')

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_counts = {}
	for word in word_list:
		word_counts[word] = word_counts.get(word,0)+1
	# print sorted(all_english.items(),lambda x,y:x[1]-y[1],reverse = True)

	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	print ordered_by_frequency[:n-1]

get_top_n_words(the_words,100)
