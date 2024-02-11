#!/usr/bin/env python3
#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 9/22/22
#Project #: M08_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports tkinter and stuff needed for GUI
from tkinter import *
 #this starts the tk thing with the root variagle
root = Tk()

#this is where the entry box is made, notice the parameters for it
e = Entry(root, width = 50, bg = "blue", fg = "white", borderwidth = 5)
e.pack()
e.insert (0, "Enter your name") #This puts a default text in the entry box, but it needs to be erased before the user can enter their own data

#Button controls
def myClick():
    hello = "Hello " + e.get() #a variable which adds the word "Hello" to whatever the user has entered, in this case their name
    myLabel = Label(root, text= hello) #this makes the window display the text when the button has been pressed. 'hello' is a variable, which is the variable above in blue.
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick) #button with the command, and it is labeled as "Enter your name"
myButton.pack()

root.mainloop()



