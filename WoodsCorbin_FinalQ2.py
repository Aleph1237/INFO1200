#!/usr/bin/env python3


#3.  Create an If elif elif else statement
# error messages if the user gives bad inputs
if miles_driven <= 0: #if miles is not greater or equal to 0
        print("Miles driven must be greater than zero. Please try again.") #prints error message
elif gallons_used <= 0: #if gallons is not greater or equal to 0
        print("Gallons used must be greater than zero. Please try again.") #error message
elif cost_per_gallon <= 0: #if cost is not greater or equal to 0
        print("Cost per gallon must be greater than zero. Please try again.") #error message
else:
        print(miles_per_gallon) #prints miles per gallon


#4.  Read a .csv or .txt file
with open("dogs.csv", newline="") as file: #opens the csv file
    reader = csv.reader(file) #reads the rile
    for row in reader:
        print(f"{row[0]} ({row[1]})") #prints the file
    

#5. Write to a .csv for a .txt file
with open("dogs.csv", "w", newline="") as file: #opens the dogs.csv file and adds new lines for each new dog
    writer = csv.writer(file) #starts writer
    writer.writerows(dogs) #writes each new dog to the list


#6. For loop that prints all items inside the loop
name = "doggos" #variable with value "doggos"
for letter in name:
    print(letter) #verticaly prints the variable value


#8. Gui with at least one control
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
    woofLabel.pack()  #woof window

woofButton = Button(root, text="Press for Woof", command=woof) #button that makes the program go woof.
woofButton.pack() #woof button

def boneGive():
   messagebox.showinfo("A bone!", "8---8") #displays a bone message

boneButton = Button(root, text="Get a bone!", command = boneGive) #button that gives bone to simulated dog
boneButton.pack()    #bone button

def dogSwim():
   messagebox.showinfo("water", "Splash!") #spalshes water message box

swimButton = Button(root, text="It's hot outside, go for a swim!", command = dogSwim) #button that displays splash message box
swimButton.pack()   #swim button