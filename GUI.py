from Tkinter import *
from main import *
from nltk.tokenize import RegexpTokenizer

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


	

root = Tk()
root.wm_title("Vector Space Model")
topFrame = Frame(root)
topFrame.pack(side=TOP)
intro = Label(topFrame,text="IR ASSIGNMENT # 1\n Vector Space Model",bg="grey",fg="black")
intro.pack(fill=X)
midFrame = Frame(root)
midFrame.pack(side = TOP)

Label(topFrame, text="Query").pack()
e1 = Entry(topFrame)
e1.pack()


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
searchButton = Button(bottomFrame, text='Submit', command=show_entry_fields)
searchButton.pack(side=RIGHT)



root.mainloop()
