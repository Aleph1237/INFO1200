#!/usr/bin/env python3
        
#check if input is valid float
def get_number(prompt, low, high):
    while True:
        #validate user input
        try:
            #check if floating point number
            number = float(input(prompt))   
        except ValueError:
            #show error message
            print("Please enter a valid number")
            continue
        if number > low and number <= high:
            #is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")
            
# check if input is valid integer
def get_integer(prompt, low, high):
    while True:
        #validates user input
        try:
            #gets user input and convert to int
            number = int(input(prompt))
        except ValueError:
             #show error message
            print("Please enter a valid number")
            continue
        if number > low and number <= high:
            #is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

# recieve user input and calculate future value
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        #print the future value with spaces
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    # ending message
    print("Bye!")
    
if __name__ == "__main__":
    main()
