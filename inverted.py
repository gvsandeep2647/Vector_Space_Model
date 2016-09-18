from collections import Counter, defaultdict
import numpy
import math
def create_index (data):
	'''	function to create an index keeping track 
		of each term occuring in document
	'''
	index = defaultdict(list)
	for i, tokens in enumerate(data):
		for token in tokens:
			index[token].append(i)
				
	return index

N = open("abc.txt") #file containing fictitious data
forindex = []

'''
	loop for creating a list of lists for 
	create_index
	and for calculating size of N
'''
size = 0
for line in N:
	inner_list=[elt.strip() for elt in line.split()]
	forindex.append(inner_list)
	size = size + 1
#Printing the list of lists
print forindex
# Function calling for create_index
index = create_index(forindex)
#Printing the obtained index
print index
'''
	attempt at idf scoring
'''
df = []
for token in index:
	df.append(len(index[token]))
print df
idf=[]
for x in xrange(len(df)):
	idf.append(math.log10(size/df[x]))
print idf
N.close()
