# Imports TkInter.
from tkinter import *

# Creates the screen, configures it and displays it.
root = Tk()
resolution = "500x500"
root.geometry(resolution)
root.title("Buttons - TkInter")

# Creates the button.
def myClick(): # This function will be called when the button is pressed.
    myLabel = Label(root, text="You clicked the button!")
    myLabel.pack()

myButton = Button(root, text="This is a button.", command=myClick, fg="#ffd7ae", bg="#fc0094") # Button properties. Where to be shown, on click function, text color and background color.
myButton.pack() # Makes the button show on screen. Recommended .grid method.

# Program loop.
root.mainloop()