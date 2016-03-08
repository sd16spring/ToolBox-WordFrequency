"""
@author: Leon Lam (@leonjunwei)
Last updated: 02/22/16
"""


# This is how we rip stuff off the internet.
# def rip_from_internet(webpage, filename): #webpage is the destination URL in string format.
# 	"""filename is just the entire thing: fileTitle.txt"""
# 	import urllib
# 	s = urllib.urlopen(webpage).read()
# 	print len(s)
# 	print type(s) #should be str

# 	f = open(filename,'w')
# 	f.write(s)
# 	f.close()
# 	print 'done'


# rip_from_internet("http://www.kataan.org/public/ebook/countzero.txt",'count-zero.txt')

#*****************************************#

# All hail BeautifulSoup, bringer of plaintext

# from bs4 import BeautifulSoup
# f = open('neuromancer.txt','r')
# raw_html = f.read()
# f.close()

# print raw_html

# soup = BeautifulSoup(raw_html, 'html.parser')
# cleantext = soup.get_text()
# print cleantext
# f = open('neuromancer-clean-trial.txt','w')
# f.write(cleantext)
# f.close()

# f = open('neuromancer-clean-trial.txt','r')
# s = f.read()
# f.close()

# print s

#*****************************************#

# only works for gutenberg - we have to split it along the *** dividers
def generate_wordlist_gutenberg(s):
    import string
    return [f.strip(string.punctuation + string.whitespace) for f in [d.replace("\r\n", " ") for d in s.split('***')][2].split()]


# just taking out \r and \n in case, then spliting along whitespace and
# stripping whitespace + punctuation
def generate_wordlist(s):
    import string
    return [f.strip(string.punctuation + string.whitespace) for f in [d.replace("\r\n", " ") for d in s.split()]]


# this one takes in a list of words and checks to see if the word is already in
def histogram(s, percentile):
    textLength = 1
    d = dict()
    if percentile:
        textLength = len(s)
    for c in s:
        # .lower() because capitalization makes me sad
        d[c.lower()] = (d.get(c.lower(), 0) + 1 / float(textLength))
    return d


# given a dictionary d, returns a list populated with tuples (values,keys)
def reverse_dictionary(d):
    newLst = []
    for i in d:
        newLst.append((d[i], i))
    return newLst


# returns whatever's in a file. I did this because I keep forgetting f.close()
def read_from_file(filename):
    f = open(filename, 'r')
    s = f.read()
    f.close()
    return s


# file should be .txt format, filename is everything before the txt
def generate_histogram(filename, percentile, gutenberg):
    """
    Opens a file filename.txt, generates a histogram from it
    """
    s = read_from_file(filename)
    if gutenberg:
        refined_wordlist = generate_wordlist_gutenberg(s)
    else:
        refined_wordlist = generate_wordlist(s)
    # dictionary with words as keys and occurences as values
    h = histogram(refined_wordlist, percentile)
    return h


#*****************************************#

# sh = pickle.dumps(r) #takes whatever r (e.g. a dictionary, a list) and outputs a string sh that can be stored- use f.write(sh) where f = open('r.pickle','w')
# pickle.loads(r) #takes a string and outputs whatever - use this on
# f.read() where f = open('r.pickle','r')


# filename should end with .txt, picklename should end with .pickle
def histogram_to_pickle(filename, picklename, percentile, gutenberg):
    """
    Function takes in a filename, generates a word histogram from the file, and pickles it as picklename
    """
    import pickle
    sh = pickle.dumps(generate_histogram(filename, percentile, gutenberg))
    f = open(picklename, 'w')
    f.write(sh)
    f.close()


def load_from_pickle(picklename):  # just making these functions so it's easier
    import pickle
    s = read_from_file(picklename)
    return pickle.loads(s)


# histogram_to_pickle('count-zero.txt','count-zero-percentile.pickle', True, False)

#*****************************************#


importance = load_from_pickle('importance-percentile.pickle')

kama_sutra = load_from_pickle('kama-sutra-percentile.pickle')

journey = load_from_pickle('journey-percentile.pickle')

neuromancer = load_from_pickle('neuromancer-percentile.pickle')

dickens = load_from_pickle('dickens-percentile.pickle')

frankenstein = load_from_pickle('frankenstein-percentile.pickle')

count_zero = load_from_pickle('count-zero-percentile.pickle')

textlist = [(importance, 'importance'), (kama_sutra, 'kama_sutra'), (journey, 'journey'), (neuromancer,
           'neuromancer'), (dickens, 'dickens'), (frankenstein, 'frankenstein'), (count_zero, 'count-zero')]

"""Time to generate 100 most common words"""
for item in textlist:
	most_common_100 = sorted(item[0], key = item[0].get, reverse = True)
	print most_common_100[0:100]

#*****************************************#
"""Cosine Similarity calculation here"""

# def dot(d1, d2):
#     count = 0
#     for k in d1:
#         # can actually be d1.get(k) since k is established to be in d1
#         count += d1.get(k, 0) * d2.get(k, 0)
#     return count


# def pairwise_similarity_dot(d1, d2):
#     return dot(d1, d2) / (dot(d1, d1) * dot(d2, d2))**0.5

# from tabulate import tabulate
# result = []
# result.append([i[1] for i in textlist])
# for i in textlist:

#     result.append(["(%.8f)" %((pairwise_similarity_dot(i[0], x[0])))
#                    for x in textlist])
# print tabulate(result)

#*****************************************#
"""Previous text similarity calculation here"""

# def pairwise_similarity(dict1, dict2): #2 percentile histograms
# 	import math
# 	result = []
# 	for c in dict1:
# 		result.append(abs(math.sin((math.pi/2)*dict2.get(c,0) / dict1.get(c,0))))
# 	return sorted(result)[::-1][10:20]
# print pairwise_similarity(r,t)

# def pairwise_similarity_1(dict1, dict2, start = 0, end = 100): #2 percentile histograms
# 	import math
# 	result = []
# 	checkedWords = []
# 	for c in sorted(reverse_dictionary(dict1))[::-1][start:end]:
# 		checkedWords.append(c)
# 		result.append(abs(math.sin((math.pi/2)*dict2.get(c[1],0) / dict1.get(c[1],0))))
# 	for c in sorted(reverse_dictionary(dict2))[::-1][start:end]:
# 		if c not in checkedWords:
# 			result.append(abs(math.sin((math.pi/2)*dict1.get(c[1],0) / dict2.get(c[1],0))))
# 	return result

# def pairwise_similarity_2(dict1, dict2, start = 0, end = 100): #2 percentile histograms
# 	import math
# 	result = []
# 	checkedWords = []
# 	for c in sorted(reverse_dictionary(dict1))[::-1][start:end]:
# 		checkedWords.append(c)
# 		result.append(abs(math.cos(dict2.get(c[1],0) - dict1.get(c[1],0))))
# 	for c in sorted(reverse_dictionary(dict2))[::-1][start:end]:
# 		if c not in checkedWords:
# 			result.append(abs(math.cos(dict1.get(c[1],0) - dict2.get(c[1],0))))
# 	return result
