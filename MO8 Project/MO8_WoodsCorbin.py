#!/usr/bin/env python3
#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/3/22
#Project #: M08_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports tkinter and stuff needed for GUI
from msilib.schema import ListBox
from tkinter import *
#imports the math library
import math
from tkinter import messagebox
 #this starts tk as a variable named root
root = Tk()
root.title("Dog Simulator") #title name


def woof():
    woofLabel = Label(root, text = "Woof!")# makes woof appear on the screen
    woofLabel.pack()

woofButton = Button(root, text="Press for Woof", command=woof) #button that makes the program go woof.
woofButton.pack()

def boneGive():
   messagebox.showinfo("A bone!", "8---8") #displays a bone message

boneButton = Button(root, text="Get a bone!", command = boneGive) #button that gives bone to simulated dog
boneButton.pack()    

def dogSwim():
   messagebox.showinfo("water", "Splash!") #spalshes water message box

swimButton = Button(root, text="It's hot outside, go for a swim!", command = dogSwim) #button that displays splash message box
swimButton.pack()   

root.mainloop()