"""
  ASSIGNMENT #1
  Project : To build an IR model based on a vector space model 
  
  Instructor : Dr. Aruna Malapati
  
  Contributors : G V Sandeep 2014A7PS106H
                 Kushagra Agrawal 2014AAPS334H
                 Snehal Wadhwani 2014A7PS430H

  Course No : CS F469 Information Retrieval

  Working of GUI.py:
	1. Prints all the unique categories and gives them radio buttons which user can select to narrow down results.
    2. Similarly a drop down menu to select a date range
    3. User can enter queries in two formats:
    	a. In ("") quotes which will trigger a phrase search and return a result a title containing that phase or else will process it is a normal query if no such title exists.
    	b. Normally (without any quotes) in which case it will return top 10 results based on tf-idf score.    	

"""
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
searchResult = []
def show_entry_fields():
	'''
		Global variables are used as the entry widgets in Tkinter Pyhton GUI do not catch the returned values of the function. Hence to preserve the values we store them in globally declared variables.
		This calculates the final output set of documents.
	'''
	global query
	global temp
	global flag
	global searchResult
	temp = []
	searchResult = []
	query = (e1.get())
	if len(query)==0:
		searchResult.append("Query Cannot Be Empty")
	else:
		phrase = 0
		result = []
		#Phrase variable is set to one indicating that the query search is a phrase query. It is set to one if the string's first and last characters are  ' " '
		if query[0]=='"' and query[len(query)-1]=='"':
			phrase = 1
			query = query[1:-1]

		PS = PorterStemmer()

		searchResult.append("Your Query : "+query+" Category: *"+selection+"*")
		if phrase == 1:
			searchResult.append("You Requested A Phrase Query")

		query = tokenizer.tokenize(query)
		query = [x.strip('-.?/') for x in query]
		query = filter(None,query)
		l = normalizer(query)
		if phrase == 1 :	
			# We are checking for exceptions as there might be phrase queries containing words which are not present in the dictionary
			try:
				temp = positionalintersect(l[0],l[1],1)
				answer = finalquery(temp,l)
				if len(l)==2:
					if len(temp)==0:
						result = process_query(l)
					else:
						for i in temp:
							searchResult.append(megaList[i][9])
							searchResult.append(megaList[i][8])
				else:
					if len(answer)==0:
						result = process_query(l)
					else:
						for i in answer:
							searchResult.append(megaList[i][9])
							searchResult.append(megaList[i][8])
			except :
				result = process_query(l)		
		else:
			result = process_query(l)	

		if len(temp)==0	:
			for i in xrange(len(result)):
				if i%2 ==0 :
					searchResult.append(megaList[i][9])
					searchResult.append(megaList[i][8])
				else:
					searchResult.append(result[i])
					searchResult.append("~~~~~~~~~~~~~~~~~~~")

				
				
		searchResult.append("==============================")
		printResult(searchResult)
		
def printResult(searchResult):
	global resultsFrame
	global text
	text.delete("1.0",END)
	for i in searchResult:
		text.insert(END,i+'\n')
	text.pack(side=TOP) 

def process_query(_query):
	'''
		takes in the tokenized, normalized form of the query and calculates the tf-idf score giving the query vector
		after normalizing the query vector to a unit vector, calculates the cosine similarity with all documents based on title, blogger and post 
		return top 10 documents after resolving scoring clashes by taking inlinks, outlinks and comments into consideration
	'''
	tf_query = {}
	wt_title = {}
	wt_blogger = {}
	wt_post = {}

	#calculating raw tf
	for token in _query:
		if token not in tf_query:
			tf_query[token] = 1
		else:
			tf_query[token] = tf_query[token] + 1

	#calculating total weight using the logarithmic formula for tf and multiplying with idf 
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

	#normalizing query vectors to unit vectors for title, blogger, post
	normalize_query(wt_title)
	normalize_query(wt_blogger)
	normalize_query(wt_post)

	title_score = [0]*(len(megaList))
	blogger_score = [0]*(len(megaList))
	post_score = [0]*(len(megaList))
	doc_score = [0]*(len(megaList))

	#cosine similiarity with documents w.r.t. title
	for word in wt_title:
		if word in tf_title.keys():
			for doc in tf_title[word]:
				title_score[doc] = title_score[doc]+ wt_title[word]*tf_title[word][doc]

	#cosine similarity with documents w.r.t blogger
	for word in wt_blogger:
		if word in tf_blogger.keys():
			for doc in tf_blogger[word]:
				blogger_score[doc] = blogger_score[doc] + wt_blogger[word]*tf_blogger[word][doc]
	
	#cosine similarity with documents w.r.t. post
	for word in wt_post:
		if word in tf_post.keys():
			for doc in tf_post[word]:
				post_score[doc] = post_score[doc] + wt_post[word]*tf_post[word][doc]
	
	#total document score 
	for i in xrange(len(doc_score)):
		doc_score[i] = title_score[i] + blogger_score[i] + post_score[i]
	

	#extracting top 10 documents
	result = []
	for i in xrange(10):
		maxi = -1
		maxind = []
		for j in xrange(len(doc_score)):
			if doc_score[j]>maxi: #and megaList[j][1] < endDate and megaList[j][1]> startDate and selection in megaList[j][3]:
				maxi = doc_score[j]
				maxind = []
				maxind.append(j)
			elif doc_score[j]==maxi: #and megaList[j][1] < endDate and megaList[j][1]> startDate and selection in megaList[j][3]:
				maxind.append(j)

		#resolving score conflicts
		if len(maxind)>1:
			doc_score_other = [0]*len(maxind)
			for j in xrange(len(maxind)):
				doc_score_other[j] = OUTLINKS*megaList[maxind[j]][5] + INLINKS*megaList[maxind[j]][6] + COMMENTS*megaList[maxind[j]][7]
			
			if len(maxind) >= 10-len(result):
				for k in xrange(10-len(result)):
					maxj = -1
					maxindj = -1
					for kj in xrange(len(maxind)):
						if doc_score_other[kj]>maxj:
							maxj = doc_score_other[kj]
							maxindj = kj
					
					doc_score_other[maxindj] = -1
					result.append(maxind[maxindj])
					result.append(doc_score[maxind[maxindj]])
			else:
				doc_score_other_temp = []
				for k in xrange(len(doc_score_other)):
					doc_score_other_temp[k] = doc_score_other[k]
				sorted(doc_score_other_temp, reverse=True)
				for k in xrange(len(doc_score_other_temp)):
					ind = doc_score_other.index(doc_score_other_temp[k])
					result.append(doc_score[maxind[ind]])
					doc_score_other[ind] = -1
					result.append(maxind[ind])


		else:
			if maxi != -1:
				doc_score[maxind[0]] = -1
				result.append(maxind[0])
				result.append(maxi)
			else:
				break
	
	return result
	

root = Tk()

topFrame = Frame(root)
topFrame.pack(side = TOP)

root.wm_title("Vector Space Model")
#setting the frame title

intro = Label(topFrame,text="IR ASSIGNMENT # 1\n Vector Space Model",bg="grey",fg="black")
intro.pack(fill=X)

Label(topFrame, text="Query").pack(side = LEFT)
e1 = Entry(topFrame)
e1.pack(side = RIGHT)
#the input bar

midFrame = Frame(root)
midFrame.pack(side=TOP)

def sel():
	'''
		Assigns the global variable the name of the selected category
	'''
	global selection
   	selection = ultraCategories[int(str(var.get()))]


count = 0
var = IntVar()
var.set(-1)
#lists out the unique categories on the screen
for i in range(0,len(ultraCategories)-1):
	if i==0:
		ultraCategories[i]="All"
	i = Radiobutton(midFrame,text=ultraCategories[i],variable=var,value=i,command=sel)
	i.grid(row=count/10, column = count%10, sticky = W)
	count = count + 1 


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
	'''
		Takes the date in the format : Month Year and converts it into an UNIX friendly time stamp which can be used easily for comparing
	'''
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

def finalquery(temp,l):
	answer=[]
	i=1
	for i in xrange(1,len(l)-1):
		temp2 = positionalintersect(l[i],l[i+1],1)
		for j in xrange(len(temp)):
			for k in xrange(len(temp2)):
				if temp2[k][0]==temp[j][0]:
					answer.append(temp2[k][0])
	return answer
resultsFrame = Frame(root)
resultsFrame.pack(side=TOP)
text = Text(resultsFrame)


root.mainloop()


