from Tkinter import *
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


bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Submit', command=show_entry_fields)
searchButton.pack(side = TOP)
root.mainloop()