from Tkinter import *
from new_inverted import ultraCategories
from main import *
from nltk.tokenize import RegexpTokenizer
from tfidf import *

from math import log

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')

query = ""


def show_entry_fields():
	global query
	query = (e1.get())
	process_query()


def process_query():
	#tokenize
	_query = re.sub('[^\x00-\x7F]','',decode_unicode_references(query))
	_query = tokenizer.tokenize(str(_query))
	_query = [x.strip('-.?/') for x in _query]  
	_query = filter(None,_query)

	#normalize
	_query = normalizer(_query)

	#calculate tf
	tf_query = {}
	wt_title = {}
	wt_blogger = {}
	wt_post = {}
	for token in _query:
		if token not in tf_query:
			tf_query[token] = 1
		else:
			tf_query[token] = tf_query[token] + 1
	for word in tf_query.keys():
		tf_query[word] = 1 + log(tf_query[word],10)
		if word in idf_title.keys():
			wt_title[word] = tf_query[word]*idf_title[word]
		else:
			wt_title[word] = 0.0
		if word in idf_blogger.keys():
			wt_blogger[word] = tf_query[word]*idf_blogger[word]
		else:
			wt_blogger[word] = 0.0
		if word in idf_post.keys():
			wt_post[word] = tf_query[word]*idf_post[word]
		else:
			wt_post[word] = 0.0
	#print wt_title
	#print wt_blogger
	#print wt_post

	normalize_query(wt_title)
	normalize_query(wt_blogger)
	normalize_query(wt_post)

	title_score = [0]*(len(megaList)+1)
	blogger_score = [0]*(len(megaList)+1)
	post_score = [0]*(len(megaList)+1)
	doc_score = [0]*(len(megaList)+1)

	for word in wt_title:
		if word in tf_title.keys():
			for doc in tf_title[word]:
				title_score[doc] = wt_title[word]*tf_title[word][doc]*TITLE
	for word in wt_blogger:
		if word in tf_blogger.keys():
			for doc in tf_blogger[word]:
				blogger_score[doc] = wt_blogger[word]*tf_blogger[word][doc]*BLOGGER
	for word in wt_post:
		if word in tf_post.keys():
			for doc in tf_post[word]:
				post_score[doc] = wt_post[word]*tf_post[word][doc]*POST

	for i in xrange(len(doc_score)-1):
		doc_score[i+1] = title_score[i+1] + blogger_score[i+1] + post_score[i+1]

	print doc_score





root = Tk()

topFrame = Frame(root)
topFrame.pack(side = TOP)

root.wm_title("Vector Space Model")

intro = Label(topFrame,text="IR ASSIGNMENT # 1\n Vector Space Model",bg="grey",fg="black")
intro.pack(fill=X)

Label(topFrame, text="Query").pack(side = LEFT)
e1 = Entry(topFrame)
e1.pack(side = RIGHT)

midFrame = Frame(root)
midFrame.pack(side=TOP)

def sel():
   selection = ultraCategories[int(str(var.get()))]
   print selection

var = IntVar()
for i in xrange(len(ultraCategories)):
	i = Radiobutton(midFrame,text=ultraCategories[i],variable=var,value=i,command=sel)
	i.pack(side = LEFT)

bottomFrame = Frame(root)

bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Submit', command=show_entry_fields)
searchButton.pack(side = TOP)

root.mainloop()
