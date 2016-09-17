from Tkinter import *

root = Tk()
root.wm_title("Vector Space Model")
topFrame = Frame(root)
topFrame.pack(side=TOP)
intro = Label(topFrame,text="IR ASSIGNMENT # 1\n Vector Space Model",bg="grey",fg="black")
intro.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
searchButton = Button(bottomFrame,text="Search")
searchButton.pack(side=LEFT)

root.mainloop()