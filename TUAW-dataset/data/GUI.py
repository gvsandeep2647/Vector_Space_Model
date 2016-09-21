from Tkinter import *
import ttk
import datetime
import time
from new_inverted import ultraCategories

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

var2 = StringVar(dateFrame)
var2.set(Range[0]) # initial value

w = ttk.Combobox(dateFrame, textvariable=var2, values=Range)
w.grid(row = 1 , column = 0)



var1 = StringVar(dateFrame)
var1.set(Range[0]) # initial value

w1 = ttk.Combobox(dateFrame, textvariable=var1, values=Range)
w1.grid(row=1,column = 2)

def ok():
	global startDate
	global endDate
	startDate = var2.get()
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
print query,selection,startDate,endDate