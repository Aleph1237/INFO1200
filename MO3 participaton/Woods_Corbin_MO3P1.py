#!/usr/bin/env python3

print("Corbin Wood's MPG App") # Display first welcome message

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
# mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)

# total gas cost calculation
total_gas_cost = round(miles_driven / mpg * cost_per_gallon, 2)

# cost per mile calculations
cost_per_mile = round(total_gas_cost / miles_driven, 2)

            
# format and display the results based off inputs
print()
print("Miles Per Gallon:\t" + str(mpg)) 
print("Total Gas Cost:\t\t" + str(total_gas_cost))
print()
print("Cost Per Mile:\t\t" + str(cost_per_mile))
print()
print("Bye") # exit message


