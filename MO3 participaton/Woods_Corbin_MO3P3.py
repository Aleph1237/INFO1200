#!/usr/bin/env python3

print("Corbin Woods's Rectangle App") # prints first welcome message

# display a welcome message
print("The Rectanble Size App")
print()

# get input from the user regarding rectangle
length= float(input("Enter Rectangle Length:\t"))
width = float(input("Enter Regtangle Width:\t"))

# calculate area
area = length * width
area = round(area, 2)

# calculate perimeter
perimeter = 2 * (length + width)
perimeter = round (perimeter, 2)
            
# format and display the results based off inputs
print()
print("Area = " + str(area))
print("Perimeter = " +str(perimeter))
print("Thanks for using this program") # Thanks message


