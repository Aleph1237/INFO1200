#!/usr/bin/env python3

tax = 0.06 #defines tax as .06

def main(): #main function
    print("Sales Tax Calculator\n") #prints welcome message
    total = float(input("Enter total: ")) #gets input from user in the form of an int
    sales_tax = total * tax #math for sales tax
    total_after_tax = (total + sales_tax) #math for total after tax, I removed the round function because it was printing the round function instead of rounding the number, but the answer is the same
    print("Total after tax: ",  total_after_tax) #prints final result
    
if __name__ == "__main__":
    main() #calls main function
