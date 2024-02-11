#!/usr/bin/env python3

#import the csv module so we can modify csv files
import csv

# create a variable for the csv file
FILE_NAME = "trips.csv"

#retreives miles driven
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
# retrieves gallons used
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # declares trips list to hold trips data
    trips = []

    more = "y"
    #while loop to promp for input
    while more.lower() == "y":
        #retreives gallons and miles
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        #retreives mpg by calculating the miles / gallons                         
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        #create a single trip list to hold trip info
        single_trip = [miles_driven, gallons_used, mpg]
        #append the single trip to the trips list
        trips.append(single_trip)
        
        more = input("More entries? (y or n): ")
    
    #write to the csv file
    with open(FILE_NAME, "w", newline="") as output_file:
        #create a writer object to interact with the file
        writer = csv.writer(output_file)
        #write the rtips list to the file
        writer.writerows(trips)
    
    print("Bye!")

#check current module
if __name__ == "__main__":
    main()

