from Tkinter import *
import ttk
import datetime
import time
from new_inverted import ultraCategories
from main import megaList,normalizer
from stemming import *
from nltk.tokenize import RegexpTokenizer
from new_inverted import dictTitle

query = ""
selection =""

def show_entry_fields():
   global query
   query = (e1.get())

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
for i in xrange(len(ultraCategories)):
	if i :
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

var = StringVar(dateFrame)
var.set(Range[0]) # initial value

w = ttk.Combobox(dateFrame, textvariable=var, values=Range)
w.grid(row = 1 , column = 0)



var1 = StringVar(dateFrame)
var1.set(Range[0]) # initial value

w1 = ttk.Combobox(dateFrame, textvariable=var1, values=Range)
w1.grid(row=1,column = 2)

def ok():
	global startDate
	global endDate
	startDate = var.get()
	endDate = var1.get()

button = Button(dateFrame, text="OK", command=ok)
button.grid(row=2,column=1)


bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Submit', command=show_entry_fields)
searchButton.pack(side = TOP)
root.mainloop()

startDate = time.strptime(startDate,"%B %Y")
startDate = time.mktime(startDate)

endDate = time.strptime(endDate,"%B %Y")
endDate = time.mktime(endDate)

if endDate < startDate :
	endDate = time.strptime("January 2008","%B %Y")
	endDate = time.mktime(endDate)

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
phrase = 0
if query[0]=='"' and query[len(query)-1]=='"':
	phrase = 1
	query = query[1:-1]

PS = PorterStemmer()
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
query = tokenizer.tokenize(query)
query = [x.strip('-.?/') for x in query]
query = filter(None,query)
l = normalizer(query)
if phrase == 1 :
	print positionalintersect(l[0],l[1],1)
