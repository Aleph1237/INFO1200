# prints beginning message and adds a space
print("Corbin Woods Registration App")
print()

# gathers users first and last name, then birth year.
firstName = str(input("What is your first name? "))
lastName = str(input("What is your last name? "))
birthYear = int(input("What is your birth year? "))

# prints welcome message plus full name of user
print()
print("Welcome " + firstName + ' ' + lastName)          

# prints registration complete message
print("Your registration is complete")

# prints the users temporary password, adding the * to the password is more difficult than necessary.
tempPassword = '*'.join([firstName, str(birthYear)])
print("Your temporary password is:\t" + tempPassword)
