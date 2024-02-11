#!/usr/bin/env python3

#import the csv module
import csv


# csv file name
FILE_NAME = "trips.csv"


#write trips to the csv file
def write_trips(trips):
    #open the csv file in write mode
    with open(FILE_NAME, "w", newline="") as output_file:
        #create a write object to write to the file
        writer = csv.writer(output_file)
        #write the trips argument to the csv file
        writer.writerows(trips)


#read from csv file
def read_trips():
    #create an empty list
    trips = []
    #opens the file in read mode
    with open(FILE_NAME, "r", newline="") as input_file:
        #create reader object to read through the file
        reader = csv.reader(input_file)
        #iterate the file and add rows to trips list
        for row in reader:
            trips.append(row)
            #return the trips list
    return trips

#read trips and display them


def list_trips(trips):
    #display the header
    print("Disance\t\tGallons\t\tMPG")
    #iterate through the passed in 2d list
    for i in range(0, len(trips)):
        #assign each single trip to the trip variable
        trip = trips[i]
        #print out each trip value
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
        #print out a blank line
    print()


def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    #2 dimensional list for trips
    trips = read_trips()
    #list out the trips
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        #create a single trip
        single_trip = [miles_driven, gallons_used, mpg]
        #add a single trip to the list
        trips.append(single_trip)
        #write the trips to the csv file
        write_trips(trips)

        #list out the trips
        list_trips(trips)

        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

