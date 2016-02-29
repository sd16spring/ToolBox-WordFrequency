""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	from string import punctuation
	file=open(file_name,'r')
	file_string=file.read()
	file_string=file_string.lower()
	file_string=file_string.partition('contents')[2]# 									only looks at everything past the start of the contents of the book
	file_string=file_string.partition('supplemental material')[0]#						only looks at everything before the end of the book - these probably wouldn't hold for other texts
	file_string = ''.join([char for char in file_string if not char.isdigit()])#		removes all numbers from the text
	file_string = ''.join(char for char in file_string if char not in punctuation)#		removes all punctuation from the text
	words_list=file_string.split()
	return words_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	d = dict()
	for word in word_list:
		d[word]=d.get(word,0)+1#   												This creates a dictionary of all the words in the string and the number of times they appear
	word_list_sorted = []#														empty list to store the output
	for word, frequency in d.iteritems():
		word_list_sorted.append((frequency, word))#      						This creates a list of all the items in the dictionary h
	word_list_sorted=sorted(word_list_sorted,key=lambda x: x[0],reverse=True)#	This sorts the list based on the first element of the tuple (frequency) in order from most frequent to least frequent
	return word_list_sorted[:n]

word_list=get_word_list('douay_rheims.txt')
print get_top_n_words(word_list,100)