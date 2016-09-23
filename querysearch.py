from main import megaList,normalizer
from collections import defaultdict
from stemming import *
from nltk.tokenize import RegexpTokenizer
from new_inverted import dictTitle

def positionalintersect(q1,q2,k):
	answer = []
	key = dictTitle[q1].keys()
	key2 = dictTitle[q2].keys()
	c = 0
	a = 0
	while c<len(key) and a<len(key2):
		if key[c]==key2[a]:
			l = []
			pp1 = dictTitle[q1][key[c]]
			pp2 = dictTitle[q2][key2[a]]
			for i in pp1:
				for j in pp2:
					if abs(i-j)<=k:
						l.append(j)
					elif j>i:
						break
				while l and abs(l[0] - i)>k:
					l.remove(l[0])
				for ps in l:
					answer.append([key[c],i,ps])
			c = c+1
			a = a+1
		elif key[c]<key[a]:
			c = c+1
		else:
			a = a+1
	return answer

def finalquery(temp,l):
	answer=[]
	for i in xrange(1,len(l)-1):
		temp2 = positionalintersect(l[i],l[i+1],100)
		for j in xrange(len(temp)):
			for k in xrange(len(temp2)):
				if temp2[j][0]==temp[k][0]:
					answer.append(temp[k][0])
	return answer
		
'''		
	changes made- returns document where it occurs
	 
				
				
		



'''



#Input from GUI.py

PS = PorterStemmer()
# let the query be Q
Q = raw_input()
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
Q = tokenizer.tokenize(Q)
l = normalizer(Q)

i = 0
temp=(positionalintersect(l[0],l[1],100))
'''while i<len(l)-1:
	temp.append(positionalintersect(l[i],l[i+1],100))
	i = i +1'''
print finalquery(temp,l)
print temp



