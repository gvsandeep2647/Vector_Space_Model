from new_inverted import dictTitle, dictBlogger, dictCategories, dictPost
from main import megaList
from math import log

#dictionaries to hold idf values for tokens in title, blogger, categories and post 
idf_title = {}
idf_blogger = {}
idf_categories = {}
idf_post = {}

#dictionaries to hold tf values for tokens in title, blogger, categories and post for each document
tf_title = {}
tf_blogger = {}
tf_categories = {}
tf_post = {}
N = len(megaList)


def calc_tf_idf(tf,idf,org):
	for key,val in org.iteritems():
		raw_tf = {}
		idf[key] = (log((float(N)/len(val.keys())),10))		#idf value for token 'key'
		for doc_key,doc_val in val.iteritems():
			if len(doc_val)>0:
				raw_tf[doc_key] = 1 + log(len(doc_val),10)		#tf value for token 'key' and document 'doc_key'
			else:
				raw_tf[doc_key] = 0
		tf[key] = raw_tf

#test = {}
#test['hello'] = {'1':[2,5,6,8],'2':[3,7,9,10],'4':[1]}
#test['world'] = {'2':[1],'4':[3,6]}
#calc_tf_idf(tf_title,idf_title, test)
calc_tf_idf(tf_title,idf_title, dictTitle)
calc_tf_idf(tf_blogger,idf_blogger, dictBlogger)
calc_tf_idf(tf_categories,idf_categories,dictCategories)
calc_tf_idf(tf_post, idf_post, dictPost)

