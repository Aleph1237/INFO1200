#!/usr/bin/env python3

# display a welcome message
print("Corbin Woods's Miles Per Gallon application")
print()

another_trip = "y"
while another_trip == "y":
    # get input from the user for variables, and defines another_trip variable
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter the cost per gallon:  "))
    print()
    
    # error messages if the user gives bad inputs
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        
        print()
    
        # calculate and display miles per gallon, total gas cost, and cost per mile
        total_gas_cost = gallons_used * cost_per_gallon 
        mpg = round((miles_driven / gallons_used), 2)
        cost_per_mile = total_gas_cost / miles_driven
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)

    #asks user if they want to do another trip calculation after a blank line
    print()
    another_trip = input("Get entries for another trip? (y/n)\t")

    # exit message
    print()
print("Bye")



