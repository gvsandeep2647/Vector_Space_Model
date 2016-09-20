from Tkinter import *
query = ""
def show_entry_fields():
   query = (e1.get())
   print query
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
print query
root.mainloop()
