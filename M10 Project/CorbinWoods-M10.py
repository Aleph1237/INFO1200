#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/17/22
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#title function
def display_title():
    print("Corbin Woods's Monthly Sales") #welcome message
    print() #extra space

#menu function
def display_menu():
    print("COMMAND MENU") #the command menu
    print()
    #prints out the options in a vertical list
    print("monthly - View Monthly Sales")
    print("yearly  - View yearly sales")
    print("edit    - Edit Sales for a month")
    print("exit    - Exit program")

#main function
def main():
    #calls the title and menu function
    display_title()
    display_menu()
    while True: #while loop to control commands issued by the user
        command = input("Command: ")
        if command == "monthly": #command to see monthly sales
            view_monthly_sales(sales)
        elif command == "yearly": #command to see yearly sales
            view_yearly_sales(sales)
        elif command == "edit": #command to edit sales
            edit(sales)
        elif command == "exit": #command to exit the program
            break
        else:
            print("Not a valid command. Please try again.\n") #if the user enters an invalid command, shows an error message.
    print("Bye!") #exit message

#read sales function
def read_sales():
    sales = [] #makes a blank list
    with open(FILENAME, newline="") as file: #opens the file
        reader = csv.reader(file) #uses the csv reader 
        for row in reader:
            sales.append(row) #adds the data to the list
    return sales

#monthly sales funtion
def view_monthly_sales(sales):
    for row in sales:
        print(f"{row[0]} - {row[1]}") #prints out the monthly sales data from the csv file
        print()

#yearly sales function
def view_yearly_sales(sales):
    total = 0
    for row in sales:
        amount = int(row[1])
        total += amount #prints out the yearly sales data

    # get count
    count = len(sales)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # format and display the result
    print("Yearly total:    ", total)
    print("Monthly average: ", average)        
    print()

# get sales function
def edit_sales(sales): #if loop for collecting user data
    # names variable with list of abreviated month names
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    name = name.title(input) #user input for abbreviated month names
    if name != names: #if loop for if user enters a wrong month name, prints out the error below
        print("Invalid three-letter month") #error message for bad month name
    else:
        return
    index = names.index(name) #index variable to store the index
    amount = int(input("Sales Amount: ")) # amount variable to hold sales amount from user input
    month = [] #empty month list
    month.append(name) #adds the data to the csv from the name variable
    month.append(str(amount)) #adds the user input data from the amount variable
    (sales[index] == month) #ads he month and amount to the sales list at the correct index
    write_sales(sales) #calls the write_sales function
    print("Sales amount for {month[0]} was modified.") #prints the message for a successful modification to the csv file
    print()

#write_sales function
def write_sales(sales):
    with open(FILENAME, "w", newline="") as file: #opens the file
        writer = csv.writer(file) #writes and closes the file
        writer.writerows(sales) #writes the data to the csv file

if __name__ == "__main__":  main()