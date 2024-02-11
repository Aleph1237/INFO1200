#!/usr/bin/env python3

# display a welcome message
print("Welcome to Corbin Woods's Future Value Calculator")
print()

# begin is_valid loop to aid user to enter logical numbers. No one will invest for 3000 years
choice = "y"
while choice.lower() == "y":

    is_valid = False

    while is_valid == False:

    # get input from the user, or display an error message, for monthly investment
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = True
        else: print("Entry must be greater than 0 and less than 1000. Please try again") # error message if user inputs more than 1000 for monthly investment
    is_valid = False

    #get input from the user, or display error message, for yearly interest rate
    while is_valid == False:       
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True
        else: print("Entry must be greater than 0 and less than 15. Please try again") # error messge if user has unrealistic interest rate
    is_valid = False

    # get input from the user, or display an error message, for years of investment
    while is_valid == False:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            is_valid = True
        else: print("Entry must be greater than 0 and less than 50. Please try again.") # error message if user thinks they are immortal
    is_valid = False

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

# exit message if user chooses No option
print("Bye!")
