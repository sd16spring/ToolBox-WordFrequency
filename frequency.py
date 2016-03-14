""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """
import pickle
import string

#pulls from previously downloaded file of The Wizard of Oz without changing the original file
wiz_downloaded = open('wiz_downloaded.txt', 'r')
wizard_full_text = wiz_downloaded.read()
wiz_downloaded.close()

#write a modified Wizard of Oz to a file
f = open('wizard_of_oz.txt','w')
#removes headers from before start of book and footers from end of book
wizard_no_headers = wizard_full_text[wizard_full_text.find('START OF THIS PROJECT GUTENBERG EBOOK'):] 
wizard_no_headers_or_footers = wizard_no_headers[:wizard_no_headers.find('End of Project Gutenberg')]
pickle.dump(wizard_no_headers_or_footers, f)
f.close()

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	g = open(file_name,'r')
	g_read = g.read()
	#load string, make lowercase, remove punctuation
	s = (pickle.loads(g_read)).lower()
	s = s.translate(string.maketrans('',''),string.punctuation)
	#split string into list at any whitespace
	wordList = s.split()
	return wordList

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	#create a dictionary of words and their corresponding tallied frequencies
	d = {}
	for word in word_list:
		d[word] = d.get(word, 0)+1
	wordList = []
	#create a list of tuples of (frequency, word) that are then sorted by frequency
	for word in d:
		wordList.append((d[word], word))
	wordList.sort(reverse=True)

	#create list of only top n words
	i = 0
	top_n_list = []
	for frequency, word in wordList:
		if i < n:
			i += 1
			top_n_list.append(word)
		else:
			break
	return top_n_list #can also return 'wordList' if want list of all words in order by frequency

#test with wizard of oz
s = get_word_list('wizard_of_oz.pickle')
t = get_top_n_words(s, 30)
