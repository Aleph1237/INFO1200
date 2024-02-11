#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#prints welcome message
print("Corbin Woods's Change App")
print()

# y variable to determine if program repeats or program ends
choice = "y"

#begins while loop for math, and 
while choice.lower()== "y":
    cents = int(input("Enter number of cents (0-99): "))
    print()

    #calculations to determine how many of each coin there is.
    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5
    pennies = cents // 1
    cents = cents % 1

    #prints number of quarters, dimes, nickels, and pennies. Then adds a space
    print("Quarters: " + str(quarters))
    print("Dimes:    " + str(dimes))
    print("Nickels:  " + str(nickels))
    print("Pennies:  " + str(pennies))
    print()

    # asks user if they want to continue
    choice = str(input("Continue? (y/n)"))

# exit message
print("Bye!")
    
