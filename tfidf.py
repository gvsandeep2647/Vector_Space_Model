from new_inverted import dictTitle, dictBlogger, dictCategories, dictPost
from main import megaList
from math import log, pow, sqrt

unique_megaList = []

#dictionaries to hold idf values for tokens in title, blogger and post 
idf_title = {}
idf_blogger = {}
idf_post = {}

#dictionaries to hold tf values for tokens in title, blogger and post for each document
tf_title = {}
tf_blogger = {}
tf_post = {}

def normalize_query(wt):
	l = 0.0
	for word in wt.keys():
		l = l + pow(wt[word],2)
	l = sqrt(l)
	for word in wt.keys():
		if l != 0:
			wt[word] = wt[word]/l
		else:
			wt[word] = 0.0

def calc_tf_idf(tf,idf,org,N): 		#tf-dict to hold tf values, idf-dict to hold idf values, org-positional index dict, N-no of total documents
	for key,val in org.iteritems():
		raw_tf = {}
		idf[key] = (log((float(N)/len(val.keys())),10))		#idf value for token 'key'
		for doc_key,doc_val in val.iteritems():
			if len(doc_val)>0:
				raw_tf[doc_key] = 1 + log(len(doc_val),10)		#tf value for token 'key' and document 'doc_key'
			else:
				raw_tf[doc_key] = 0
		tf[key] = raw_tf

calc_tf_idf(tf_title,idf_title, dictTitle, len(megaList))
calc_tf_idf(tf_blogger,idf_blogger, dictBlogger, len(megaList))
calc_tf_idf(tf_post, idf_post, dictPost, len(megaList))

def normalize_doc(k):
	
	
	for i in xrange(len(megaList)):
		temp = []
		l = 0.0
		print '\n\n\n'
		print i+1
		for word in megaList[i][k]:
			if word not in temp:
				temp.append(word)
		for word in temp:
			if k == 0:
				l = l + pow(tf_title[word][i+1],2)
			elif k == 2:
				l = l + pow(tf_blogger[word][i+1],2)
			elif k == 4:
				print word
				print tf_post[word]
				l = l + pow(tf_post[word][i+1],2)
		l = sqrt(l)
		for word in temp:
			if k == 0:
				tf_title[word][i+1] = tf_title[word][i+1]/l
			elif k == 2:
				tf_blogger[word][i+1] = tf_blogger[word][i+1]/l
			elif k == 4:
				tf_post[word][i+1] = tf_post[word][i+1]/l

normalize_doc(0)
normalize_doc(2)
normalize_doc(4)




		