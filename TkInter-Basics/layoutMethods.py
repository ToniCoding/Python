# Note: In this file, we'll be referring to X as any number.
# Imports.
from tkinter import *

# Creates the screen, configures it and displays it.
root = Tk()
resolution = "1000x500"
root.geometry(resolution)
root.title("Layout Methods - TkInter")

# Label examples that we'll be packing later.
myLabel = Label(root, text="I'm the first label, shown with grid method.")
myLabel2 = Label(root, text="I'm the second label, shown with grid method, plus pady.")
myLabel3 = Label(root, text="I'm the third label, shown with grid method, plus ipady.")
myLabel4 = Label(root, text="I'm the fourth label, shown with place method.")

# The least sofisticated method of all, but sometimes is useful.
# Good thing is that you can use this to pack in a header.
# Bad thing is that it's not compatible with .grid.
# Syntax: (screen, text="")
myLabel.pack()

# One of the best methods to make a organized GUI. Works with a table-like system.
# Good thing is that you can make organized GUIs.
# Bad thing is that you can't jump more than one row and column at the same time.
# Syntax: (row = X, column = X)
# Syntax 2: (ipax = X, ipady = X, pax = X, pady = X, )
# Note: Properties like ipady will be more usefull for entries.
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1, pady=5)
myLabel3.grid(row=5, column= 5, ipady=5)

# In my opinion, the best layout method as you can use it to place widgets anywhere in the screen.
# Good thing is the full placement freedom to show widgets.
# Bad thing is that you need to be very careful about where you put it.
# Syntax: (x= Xaxis, y= Yaxis)
myLabel4.place(x=200, y=200) 

# Program mainloop.
root.mainloop()