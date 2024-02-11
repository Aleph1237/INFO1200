# Corbin Woods validation file for the Future Value App
# retrieve user input and convert
def get_float(prompt, low, high):
    #begin while loop
    while True:
        #ruser inputs a number
        number = float(input(prompt))
        #check if number is valid
        if number > low and number <= high:
            return number
        #print error messsage, and gives range for desired number
        else:
            print("Entry must be greater than", low,
            "and less than or equal to", high)

#begins the while loop for get_int and retrieves number from user
def get_int(prompt, low, high):
    while True:
        #user inputs number
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        #print error message, and gives range for desired number
        else:
            print("Entry must be greater than", low,
             "and less than or equal to", high)

#begins the while loop while choice is y
choice = "y"
while choice.lower() == "y":
    #gets a float number from user
    valid_number = get_float("Enter number:", 0, 1000)
    #prints the number user entered
    print("Valid number =", valid_number)
    print()
    #gets an integer from the user
    valid_integer = get_int("Enter integer:", 0, 50)
    #prints the number user entered
    print("Valid Integer =", valid_integer)
    print()
    #asks user if they want to repeat
    choice = input("Repeat? (y/n):")
# exit message
print("Bye!")
#main control statement
if __name__ == "__main__" :
    main()



  
