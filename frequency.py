""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string


def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	book = open(file_name,'r+')
	lines = book.readlines()
	curr_line = 0
	while lines[curr_line].find('THE PICTURE OF DORIAN GRAY') == -1:
	    curr_line += 1
	nope = lines[:curr_line+1]
	start = len(str(nope))
	dorian = str(lines[start:])
	dorian = dorian[::-1]
	dorian = dorian[30110:]
	dorian = dorian[::-1]

	dorian = dorian.replace("\\r\\n"," ")
	dorian = dorian.translate(None,".,!:;*/_-()\\[]&?1234567890")
	dorian = dorian.replace('"',' ')
	dorian = dorian.replace("'"," ")
	dorian = dorian.replace("rn"," ")
	dorian = dorian.replace("   "," ")
	dorian = dorian.replace("  "," ")
	dorian = dorian.replace("  "," ")
	dorian = dorian.lower()
	dorian = dorian.split()
	return dorian
	book.close()



def histogram(s):
    d = dict()
    for c in s:
        if d.get(c,0)>0:
            d[c] = d[c] + 1
        else:
            d[c] = d.get(c,1) + d.get(c,0)  
    return d

def most_frequent(s):
    hist = histogram(s)
    t = []
    for x, freq in hist.iteritems():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	words = get_word_list(word_list)
	ranking = most_frequent(words)
	return ranking[0:n-1]

print get_word_list('pg32325.txt')
print get_top_n_words('pg32325.txt', 100)
