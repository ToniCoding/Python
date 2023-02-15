# Imports TkInter.
from tkinter import *

# Creates the screen, configures it and displays it.
root = Tk()
resolution = "500x500"
root.geometry(resolution)
root.title("Window and text - TkInter")

# TkInter works considering everything as a widget, so now we'll create a label widget with text on it.
myLabel1 = Label(root, text="What time is it? ->") # ~Syntaxis~  Label(nameOfTheScreen, text="<text>")
myLabel2 = Label(root, text="It's 3 P.M.")
myLabel3 = Label(root, text="What's your name? ->")
myLabel4 = Label(root, text="The Real Slim Shady")

# Now the widget is created, we want it to be shown on screen so we'll put it with two different methods: pack and grid.
# With pack we'll put directly on screen and it'll be moved when we manually redimension the screen.
# myLabel1.pack()  --- We can't put both methods at the same time so we'll comment the first label to use grid method.

# With grid we'll put the widget on screen and it won't be mode when we manually redimension the screen.
# myLabel2.grid()

# When we use grid method, we can position the widget with rows and colums as a table. Note that it'll ignore empty rows and columns.
# We're gonna make this look like a little conversation.
myLabel1.grid(row="0", column="0")
myLabel2.grid(row="0", column="1")
myLabel3.grid(row="1", column="0")
myLabel4.grid(row="1", column="1")

# All programs consist of a continuos loop that checks everything. In order to make our program work we need to loop our screen widget.
root.mainloop()