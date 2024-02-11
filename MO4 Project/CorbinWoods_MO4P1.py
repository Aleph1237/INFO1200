#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 9/22/22
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#welcome message
print("Corbin Woods's Letter Grade Converter")
print()

# Sets the choice variable to y
choice = "y"
letter = "A"

# begins while loop to calculate grades.
while choice.lower() == "y":
    number = int(input("Enter numerical grade: ")) #Asks user to enter a numerical grade.
    
    # Beginning of the if else statement loops to calculate letter grades
    if number >= 94 and number <= 100:
        letter = "A"
    elif number >= 90 and number <= 93:
        letter = "A-"
    elif number >= 87 and number <= 89:
        letter = "B+"
    elif number >= 83 and number <= 86:
        letter = "B"
    elif number >= 80 and number <= 82:
        letter = "B-"
    elif number >= 77 and number <= 79:
        letter = "C+"
    elif number >= 73 and number <= 76:
        letter = "C"
    elif number >= 70 and number <= 72:
        letter = "C-"
    elif number >= 67 and number <= 69:
        letter = "D+"
    elif number >= 63 and number <= 66:
        letter = "D"
    elif number >= 60 and number <= 62:
        letter = "D-"
    elif number >= 0 and number <= 59:
        letter = "E"
# Prints the users grade based on input number      
    print("Letter Grade: " + letter)
    print()
# continues or ends the program, then shows bye if program is ended
    choice = str(input("Continue? (y/n) "))
#exit message 
print("Bye!")
                 
            
