# Imports TkInter.
from tkinter import *

# Creates the screen, configures it and displays it.
root = Tk()
resolution = "500x500"
root.geometry(resolution)
root.title("Input fields - TkInter")

# Creation of the entry box.
name = Entry(root, width=50, )
name.pack(ipady=3)
name.insert(0, "Enter your right here") # This will make a text appear inside the entry by default.

# Function that will reveal the name, once the button is clicked. This function will be called by the button widget.
def clickOn():
    greeting = "Your name is:  " + name.get() # Variable made in order to make the label widget properties smaller.
    revealName = Label(root, text=greeting)
    revealName.place(x=90, y=30)

# Creation, display and placemente of the button submit that will call the ClickOn function.
submitButton = Button(root, text="Submit", command=clickOn)
submitButton.place(x=400, y=0)

# Program mainloop.
root.mainloop()
