#!/usr/bin/env python3

tax_rate = 0.06 #the sales tax rate


def main():
    print("Sales Tax Calculator\n") #welcome message
    total = float(input("Enter total: "))#gets list price from user
    sales_tax = total * tax_rate    #calculates sales tax based off user input
    total_after_tax = (total + sales_tax) # calculates price plus tax
    print("Total after tax: ", str(total_after_tax)) #prints total price, including tax
    
if __name__ == "__main__":
    main()
