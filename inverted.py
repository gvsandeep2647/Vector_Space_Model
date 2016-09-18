from collections import Counter, defaultdict
import numpy
import math
def create_index (data):
	index = defaultdict(list)
	for i, tokens in enumerate(data):
		for token in tokens:
			index[token].append(i)
				
	return index

N = [['a','b'],['a','c']] 
index = create_index(N)
size = len(N)
'''print index['a']
print index['b']'''
print size
#tf = numpy.empty(len(index), dtype=object)
df = []
print len(index['a'])
for token in index:
	df.append(len(index[token]))
idf=[]
for x in xrange(len(df)):
	idf.append(math.log10(size/df[x]))
print idf
