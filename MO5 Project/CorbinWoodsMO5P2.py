#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports CWconverter and other files needed to run program
from types import MethodDescriptorType
import CWconverter as c

# Defines functions
def fm_welcome():
    print("Corbin Woods's Feet / Meters Converter") #prints welcome messge when function is called
def fm_menu():
    print("Conversions Menu:") #prints menu options when menu funcion is called
    print("a. Feet to Meters")
    print("b. Meters to Feet")
def main(): #begins main function
    fm_welcome() #calls welcome function
    more = "y"
    while more.lower() == "y":
        fm_menu() #calls menu funcion
        choice = str(input("Select a conversion(a/b): ")) #user selects a function, which is assigned to variable "choice"
        print()
        if choice == "a": #if choice is "a" then begins math for feet to meters
            feet = float(input("Enter feet: ")) #user enters amount of feet
            meters = c.to_meters(feet) #converts feet to meters
            print(round(meters,2), "meters") #prints meters rounded to 2 decimals
        elif choice =="b": #if choice is "b" then beging math for meters to feet
            meters = float(input("Enter meters: ")) #user enters amount of meters
            feet = c.to_feet(meters) #converts meters to feet
            print(round(feet,2), "feet") #prints feet rounded to 2 decimals
        else:
            print("You did not enter a valid selection") #prints error message if neither A nor B are selected

        #see if user wants to convert again
        more = str(input("Would you like to perform another conversion? (y/n)")) 
        print()

        #if they do not select "y" then ends program
        if more != "y":
            print("Thanks, bye!") #goodbye message

if __name__ == "__main__": main()
