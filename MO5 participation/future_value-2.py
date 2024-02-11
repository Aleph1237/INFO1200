#!/usr/bin/env python3
        
import validate as v
print("Woods's Validated Future Value App")
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value
#begins "main" chunk of code
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user for the variables, and display an error message if they are out of bounds
        monthly_investment = v.get_float("Enter monthly investment:\t",1,1000)
        #checks if entered number is within bounds
        if monthly_investment < 0 and monthly_investment > 1000:
            #error message
            print("Entry must be greater than 0 and less than or equal to 1000")
        #gets input from user
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t",1,15)
        #checks if entered number is within bounds
        if yearly_interest_rate < 0 and yearly_interest_rate >= 15:
            #error message
            print("Entry must be greater than 0 and less than or equal to 15")
        #gets input from user
        years = v.get_int("Enter number of years:\t\t",1,50)
        #checks if entered number is within bounds
        if years < 0 and years >= 50:
            #error message
            print("Entry must be greater than 0 and less than or equal to 50")

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        #prints the future value
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()
# exit message
    print("Bye!")

    #main control statement
if __name__ == "__main__":
    main()

