from Tkinter import *
import ttk
import datetime
import time
from new_inverted import ultraCategories,dictTitle
from main import *	
from stemming import *
from nltk.tokenize import RegexpTokenizer
from tfidf import *
from math import log

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
query = ""
selection =""
temp = []
def show_entry_fields():
	global query
	global temp
	global flag
	query = (e1.get())
	if len(query)==0:
		print "Query Cannot Be Empty"
	else:
		phrase = 0
		result = []
		if query[0]=='"' and query[len(query)-1]=='"':
			phrase = 1
			query = query[1:-1]

		PS = PorterStemmer()

		print "Your Query : "+query+" Category: "+selection+" Time Range: "+startDate+" to "+endDate
		query = tokenizer.tokenize(query)
		query = [x.strip('-.?/') for x in query]
		query = filter(None,query)
		l = normalizer(query)
		if phrase == 1 :	
			try:
				temp = positionalintersect(l[0],l[1],1)
				if len(temp)==0:
					result = process_query(l)
				else:
					for i in temp:
						print megaList[i][9],megaList[i][8]
			except :
				result = process_query(l)		
		else:
			result = process_query(l)	

		if len(temp)==0	:
			for i in xrange(10):
				print megaList[result[i*2]][9]
				print megaList[result[i*2]][8]
				print result[i*2+1]
				print "~~~~~~~~~~~~~~~~~~~"

		print "=============================="

def process_query(_query):
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

	normalize_query(wt_title)
	normalize_query(wt_blogger)
	normalize_query(wt_post)

	title_score = [0]*(len(megaList))
	blogger_score = [0]*(len(megaList))
	post_score = [0]*(len(megaList))
	doc_score = [0]*(len(megaList))

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

	for i in xrange(len(doc_score)):
		doc_score[i] = title_score[i] + blogger_score[i] + post_score[i]
	result = []
	for i in xrange(10):
		maxi = -1
		maxind = -1
		for j in xrange(len(doc_score)):
			if doc_score[j]>maxi and megaList[j][1] < endDate and megaList[j][1]> startDate and selection in megaList[j][3]:
				maxi = doc_score[j]
				maxind = j	
		doc_score[maxind] = -1
		result.append(maxind)
		result.append(maxi)

	
	return result
	

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
	global selection
   	selection = ultraCategories[int(str(var.get()))]


count = 0
var = IntVar()
var.set(0)
for i in xrange(len(ultraCategories)):
	count = count + 1 
	i = Radiobutton(midFrame,text=ultraCategories[i],variable=var,value=i,command=sel)
	i.grid(row=count/10, column = count%10, sticky = W)


dateFrame = Frame(root)
dateFrame.pack(side=TOP)
Range = []
for i in range(2004,2008):
	for j in range(1,13):
		month = datetime.date(1900, j, 1).strftime('%B')
		month = month + " " +str(i)
		Range.append(month)

Label(dateFrame, text="Select Date Range").grid(row=0,column=1)
startDate = "January 2004"
endDate = "January 2008"

var2 = StringVar(dateFrame)
var2.set(Range[0]) # initial value

w = ttk.Combobox(dateFrame, textvariable=var2, values=Range)
w.grid(row = 1 , column = 0)



var1 = StringVar(dateFrame)
var1.set(Range[len(Range)-1]) # initial value

w1 = ttk.Combobox(dateFrame, textvariable=var1, values=Range)
w1.grid(row=1,column = 2)

def ok():
	global startDate
	global endDate

	startDate = var2.get()
	endDate = var1.get()
	startDate = time.strptime(startDate,"%B %Y")
	startDate = time.mktime(startDate)

	endDate = time.strptime(endDate,"%B %Y")
	endDate = time.mktime(endDate)

	if endDate < startDate :
		endDate = time.strptime("January 2008","%B %Y")
		endDate = time.mktime(endDate)

button = Button(dateFrame, text="OK", command=ok)
button.grid(row=2,column=1)


bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Submit', command=show_entry_fields)
searchButton.pack(side = TOP)


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
	result = []
	for i in answer:
		result.append(i[0])

	return result


root.mainloop()


