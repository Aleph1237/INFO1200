#!/usr/bin/env python3
#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/3/22
#Project #: M08_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports tkinter and stuff needed for GUI
from tkinter import *
#imports the math library
import math
 #this starts tk as a variable named root
root = Tk()
root.title("Right Triangle Calculator") #displays program title

nameLabel = Label(root, text="Corbin's Right Triangle Calculator!") #welcome message
nameLabel.pack()

instructions = Label(root, text = "Enter the side lengths below, then hit Run Calculation!") #instructions on how to use the program
instructions.pack()


#text entry box for the A side
numA = Entry(root, width = 30, bg = "blue", fg = "white", borderwidth = 5) # A side entry box
numA.pack()
numA.insert (0, "Enter Side A") #This puts a default text in the entry box, but it needs to be erased before the user can enter their own data


#text entry box for the B side
numB = Entry(root, width = 30, bg = "black", fg = "white", borderwidth = 5) # B side entry box
numB.pack()
numB.insert (0, "Enter Side B") #This puts a default text in the entry box, but it needs to be erased before the user can enter their own data

#Button controls
def calculate():
    A=int(numA.get()) #converts numA into an int  from string
    B=int(numB.get()) #converts numB into an int from string
    SideC = math.sqrt(A**2 + B**2)   #A variable which does the pythagorean theoreom using A and B variables
    LabelC = Label(root, text= round(SideC,3)) #shows the answer rounded to 3 decimal places.
    LabelC.pack()

myButton = Button(root, text="Run Calculation!", command=calculate) #button that runs calculations, the command above, when clicked.
myButton.pack()

root.mainloop()